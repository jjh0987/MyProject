import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def load_datasets():
    path_train = '../pycharmProjects/pythonProject1/dacon/titanic/train.csv'
    path_test = '../pycharmProjects/pythonProject1/dacon/titanic/test.csv'
    titanic_train = pd.read_csv(path_train)
    titanic_test = pd.read_csv(path_test)
    return titanic_train,titanic_test

from sklearn import preprocessing
def encoder(df,features):
    # features = ['Sex','Cabin','Embarked']
    encode = preprocessing.LabelEncoder()
    for feature in features:
        encode.fit(df[feature])
        df[feature] = encode.transform(df[feature])
    return df

def drop_features(data,features):
    return data.drop(features,axis=1)

def devide_train_xy(df,target):
    df.dropna(inplace=True)
    y_train = pd.DataFrame(data=df.loc[:,target],columns=[target])
    x_train = drop_features(df,target)
    x_train.reset_index(drop=True,inplace=True)
    y_train.reset_index(drop=True,inplace=True)
    return x_train,y_train

def setting_test(df,target):
    x_test = df.fillna(df['Age'].mean())
    x_test = drop_features(x_test,target)
    return x_test


def submission_DF(pred,len_train,len_test):
    data = []
    idx = len_train
    for i in range(1,len_test+1):
        temp = []
        temp.append(i+idx)
        temp.append(pred[i])
        data.append(temp)
    df = pd.DataFrame(data=data,columns=['PassengerId','Survived'])
    df.set_index('PassengerId')
    return df.set_index('PassengerId')

def write_csv(path,df):
    df.to_csv(path)

drop_target = ['PassengerId','Ticket','Name','Cabin','Embarked','Parch']
encode_target = ['Sex']
titanic_train,titanic_test = load_datasets()

titanic_train.info()

train_set = drop_features(titanic_train,drop_target)
x_train,y_train = devide_train_xy(train_set,'Survived')
x_train = encoder(x_train,encode_target)
x_test = setting_test(titanic_test,drop_target)
x_test = encoder(x_test,encode_target)

x_test.info()


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
dt_clf = DecisionTreeClassifier(random_state=156)
parm = {'max_depth':list(range(1,20)),
        'min_samples_split':list(range(1,10)),
        'min_samples_leaf':list(range(1,10))}

grid_cv = GridSearchCV(dt_clf,param_grid=parm,scoring='accuracy',cv=3,verbose=1)
# verbose : show fitting condition
grid_cv.fit(x_train,y_train)
print(grid_cv.best_params_)
print(round(grid_cv.best_score_,4))

data = x_train.copy()
label = y_train.copy()

X_train,X_test,Y_train,Y_test = train_test_split(
    data,label,test_size=0.3,random_state=156
)
best_estimator = grid_cv.best_estimator_
best_estimator.fit(X_train,Y_train)
pred = best_estimator.predict(X_test)
acc = accuracy_score(pred,Y_test)
acc


pred = best_estimator.predict(x_test)
pred = np.append(pred,0)
df = submission_DF(pred, len_train=len(titanic_train), len_test=len(titanic_test))
path = '../pycharmProjects/pythonProject1/dacon/titanic/submission.csv'
write_csv(path,df)


##############



from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression # 앙상블 조합용
from sklearn.neighbors import KNeighborsClassifier # 앙상블 조합용

data = x_train.copy()
label = y_train.copy()
X_train,X_test,Y_train,Y_test = train_test_split(
    data,label,test_size=0.3,random_state=156
)

lr_clf = LogisticRegression()
knn_clf = KNeighborsClassifier(n_neighbors=8)
vo_clf = VotingClassifier(estimators=[('LR',lr_clf),('KNN',knn_clf)],voting='soft')
vo_clf.fit(X_train,y_train)

pred = vo_clf.predict(X_test)
print(round(accuracy_score(pred,Y_test),4))
pred = vo_clf.predict(x_test)

pred = np.append(pred,0)
df = submission_DF(pred, len_train=len(titanic_train), len_test=len(titanic_test))
path = '../pycharmProjects/pythonProject1/dacon/titanic/submission.csv'
write_csv(path,df)



######################
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV

data = x_train.copy()
label = y_train.copy()
X_train,X_test,Y_train,Y_test = train_test_split(
    data,label,test_size=0.3,random_state=156
)
gb_clf = GradientBoostingClassifier(random_state=0)
gb_clf.fit(X_train,Y_train)
pred = gb_clf.predict(X_test)
acc = accuracy_score(pred,Y_test)
print(acc)


parms = {'n_estimators':[30,50],
         'learning_rate':[0.05,0.1],
         'max_depth': list(range(1, 5)),
         'min_samples_split': list(range(1, 5)),
         'min_samples_leaf': list(range(1, 5))}
grid_cv =GridSearchCV(gb_clf,param_grid=parms,cv=5,verbose=1)
grid_cv.fit(X_train,Y_train)
best = grid_cv.best_estimator_


pred = best.predict(X_test)
pred
acc = accuracy_score(pred,Y_test)
acc


pred = best.predict(x_test)
pred = np.append(pred,0)
df = submission_DF(pred, len_train=len(titanic_train), len_test=len(titanic_test))
path = '../pycharmProjects/pythonProject1/dacon/titanic/submission.csv'
write_csv(path,df)


#############################

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


data = x_train.copy()
label = y_train.copy()
X_train,X_test,Y_train,Y_test = train_test_split(
    data,label,test_size=0.3,random_state=156
)

model = Sequential()
initializer = tf.keras.initializers.HeNormal()
model.add(Dense(50,input_dim=len(x_test),activation='sigmoid',kernel_initializer=initializer))

model.add(Dense(25,activation='relu'))
model.add(Dense(10,activation='sigmoid'))
model.add(Dense(5,activation='sigmoid'))

model.add(Dense(1,activation='sigmoid'))

opt = tf.keras.optimizers.Adam(lr=0.01)
model.compile(loss='binary_crossentropy',optimizer=opt,metrics='accuracy')
model.fit(X_train,Y_train,epochs=200,batch_size=15)
