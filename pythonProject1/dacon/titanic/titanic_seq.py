import pandas as pd

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

drop_target = ['PassengerId','Ticket','Name','Ticket','Cabin']
encode_target = ['Sex','Embarked']
titanic_train,titanic_test = load_datasets()


train_set = drop_features(titanic_train,drop_target)
x_train,y_train = devide_train_xy(train_set,'Survived')
x_train = encoder(x_train,encode_target)
x_test = setting_test(titanic_test,drop_target)
x_test = encoder(x_test,encode_target)


