root = '/Users/junho/Desktop/git_repo/pycharmProjects/pythonProject/dacon/jeju'

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
train = pd.read_parquet('/Users/junho/Desktop/git_repo/pycharmProjects/pythonProject/dacon/jeju/train.parquet')
test = pd.read_parquet('/Users/junho/Desktop/git_repo/pycharmProjects/pythonProject/dacon/jeju/test.parquet')
train = train.drop(['road_in_use','vehicle_restricted','height_restricted'],axis=1)
test = test.drop(['road_in_use','vehicle_restricted','height_restricted'],axis=1)

from haversine import haversine, Unit, haversine_vector
start = [(i-90,j) for i,j in zip(train['start_longitude'],train['start_latitude'])]
end = [(i-90,j) for i,j in zip(train['end_longitude'],train['end_latitude'])]
distance = [haversine(i, j, unit=Unit.KILOMETERS) for i,j in zip(start,end)]

# train = train.drop(['start_longitude','end_longitude','start_latitude','end_latitude'],axis=1)
train['distance'] = distance

from haversine import haversine, Unit, haversine_vector
start = [(i-90,j) for i,j in zip(test['start_longitude'],test['start_latitude'])]
end = [(i-90,j) for i,j in zip(test['end_longitude'],test['end_latitude'])]
distance = [haversine(i, j, unit=Unit.KILOMETERS) for i,j in zip(start,end)]

# train = train.drop(['start_longitude','end_longitude','start_latitude','end_latitude'],axis=1)
test['distance'] = distance
#train = train[train['connect_code'] == 0]
#train = train[train['multi_linked'] == 0]
train = train[train['maximum_speed_limit'] != 40]

import glob
rain_path = glob.glob(f'{root}/rain_temp/rn*.csv')
tar = [pd.read_csv(i,header=6,encoding='cp949') for i in rain_path]
ans = pd.DataFrame()
for i in tar:
    ans = pd.concat([ans,i],axis=0)
ans = ans.groupby('날짜').mean()
ans = ans.fillna(0)
ans = ans.reset_index()
ans['날짜'] = ans['날짜'].str.replace('-','')
ans['날짜'] = pd.to_numeric(ans['날짜'])
ans.columns = ['base_date','loc','rain']
ans = ans.drop('loc',axis=1)
train = pd.merge(ans,train)
test = pd.merge(ans,test)

temperature_path = glob.glob(f'{root}/rain_temp/ta*.csv')
tar = [pd.read_csv(i,header=6,encoding='cp949') for i in temperature_path]
ans = pd.DataFrame()
for i in tar:
    ans = pd.concat([ans,i],axis=0)
ans = ans.groupby('날짜').mean()
ans = ans.reset_index()
ans['날짜'] = ans['날짜'].str.replace('-','')
ans['날짜'] = ans['날짜'].str.replace('\t','')
ans['날짜'] = pd.to_numeric(ans['날짜'])

ans.columns = ['base_date','loc','temp','low','high']
ans = ans.drop(['loc','low','high'],axis=1)
train = pd.merge(ans,train)
test = pd.merge(ans,test)

# train['base_date'] = train['base_date'].astype('object')
train['base_date'] = [str(i)[4:6] for i in train['base_date']]
test['base_date'] = [str(i)[4:6] for i in test['base_date']]

from sklearn.preprocessing import LabelEncoder
str_col = ["base_date","base_hour","day_of_week","multi_linked","connect_code"
,"weight_restricted","road_type","start_longitude",'start_turn_restricted','end_turn_restricted'
,"road_name","start_node_name","end_node_name",'end_longitude'] # "maximum_speed_limit"
for i in str_col:
    le = LabelEncoder()
    le=le.fit(train[i])
    train[i]=le.transform(train[i])

    for label in np.unique(test[i]):
        if label not in le.classes_:
            le.classes_ = np.append(le.classes_, label)
    test[i]=le.transform(test[i])

from sklearn.decomposition import PCA
pca = PCA(n_components=1)
target = ['start_turn_restricted','end_turn_restricted',
          'start_latitude','end_latitude','lane_count']
x1 = pca.fit_transform(train.loc[:,target])
x2 = pca.fit_transform(test.loc[:,target])
train['x'] = x1
test['x'] = x2

train = train.drop(target,axis=1)
test = test.drop(target,axis=1)

train = train.sort_values(by='id')
test = test.sort_values(by='id')


import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from catboost import CatBoostRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import VotingRegressor
from sklearn.model_selection import GridSearchCV
import xgboost

def rf_speed(speed, train, test):
    #     train = pd.read_parquet('./train.parquet')
    #     test = pd.read_parquet('./test.parquet')
    #     train = train.drop(['road_in_use','vehicle_restricted','height_restricted'],axis=1)
    #     test = test.drop(['road_in_use','vehicle_restricted','height_restricted'],axis=1)

    train = train.drop(train[(train['distance'] > 0.8) & (train['target'] < 5)].index)
    train = train.drop(train[train['target'] > 120].index)

    train = train[train["maximum_speed_limit"] == speed]
    y_train = train['target']
    X_train = train.drop(['id', 'target'], axis=1)

    test = test[test["maximum_speed_limit"] == speed]
    test_id = test['id']
    test = test.drop(['id'], axis=1)

    prediction_table = pd.DataFrame(test_id)

    X_train, X_test, y_train, y_test = train_test_split(
        X_train, y_train, test_size=0.08, random_state=10
    )

    r1 = RandomForestRegressor(random_state=10, bootstrap=200, oob_score=True)
    r2 = CatBoostRegressor(random_state=10, iterations=5000, verbose=False)
    r3 = ExtraTreesRegressor(random_state=10)
    r4 = xgboost.XGBRegressor(random_state=10)
    vote = VotingRegressor([('r1', r1), ('r2', r2), ('r3', r3), ('r4',r4)])

    parms = {'verbose': [False]}
    grid_cv = GridSearchCV(vote, param_grid=parms, cv=5, n_jobs=-1,
                           scoring='neg_mean_absolute_error')  # ,param_grid=parms
    grid_cv.fit(X_train, y_train)

    pred = grid_cv.predict(X_test)
    mae = mean_absolute_error(pred, y_test)
    print(mae)

    prediction_table['target'] = grid_cv.predict(test)
    prediction_table.to_csv(f'{root}/target{speed}.csv')
    print(f'save {speed}')

for i in [30,50,60,70,80]:
    rf_speed(i,train,test)

ans = pd.concat([pd.read_csv('target30.csv'),pd.read_csv('target50.csv'),
          pd.read_csv('target60.csv'),pd.read_csv('target70.csv'),
          pd.read_csv('target80.csv')]).drop('Unnamed: 0',axis=1)
ans = ans.sort_values('id')
ans = ans.set_index('id')
ans.to_csv('./submit.csv')

#
pd.read_csv(f'{root}/data_info.csv')

# 제주,성산,서귀포,고산

train
ans
# train['start_node_name'].value_counts()
# train['end_node_name'].value_counts()
# train['start_latitude'].head()
# train['distance'].value_counts()
# train.loc[:5,['start_latitude','start_node_name','end_node_name','distance']]