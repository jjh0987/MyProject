import pandas as pd

def load_datasets():
    path_train = '../pycharmProjects/pythonProject/dacon/titanic/train.csv'
    path_test = '../pycharmProjects/pythonProject/dacon/titanic/test.csv'
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
    y_train = pd.DataFrame(data=df.loc[:,target],columns=[target])
    x_train = drop_features(df,target)
    x_train = x_train.fillna(x_train['Age'].mean())
    return x_train,y_train

def setting_test(df,target):
    x_test = df.fillna(df['Age'].mean())
    x_test = drop_features(x_test,target)
    return x_test


def submission_DF(pred,len_train,len_test):
    data = []
    idx = len_train
    for i in range(0,len_test):
        temp = []
        temp.append((i+1)+idx)
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
train_set = drop_features(titanic_train,drop_target)
titanic_test.columns

x_train,y_train = devide_train_xy(train_set,'Survived')
x_train = encoder(x_train,encode_target)
x_test = setting_test(titanic_test,drop_target)
x_test = encoder(x_test,encode_target)
idx = 700
x_train_train = x_train.iloc[:idx,:]
x_train_test = x_train.iloc[idx:,:]
y_train_train = y_train.iloc[:idx,:]
y_train_test = y_train.iloc[idx:,:]

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from sklearn.metrics import accuracy_score
from tensorflow.keras import initializers
import numpy as np

model = Sequential()
initializer = initializers.HeNormal()
model.add(Dense(12,activation='relu',kernel_initializer=initializer))

model.add(Dense(5,activation='sigmoid'))
model.add(Dense(1,activation='sigmoid'))

# RMSprop
opt = optimizers.Adam(learning_rate=0.005)
loss = losses.binary_crossentropy
model.compile(optimizer=opt,loss=loss,metrics=['accuracy'])
model.fit(x_train_train,y_train_train,epochs=20,batch_size=20)

# pred = model.predict(x_train_test)

model.evaluate(x_train_test,y_train_test)


one_hot_pred = np.array([np.argmax(i) for i in pred])
acc = accuracy_score(one_hot_pred,y_train_test)
print(round(acc,4))



pred = model.predict(x_test)
one_hot_pred = np.array([np.argmax(i) for i in pred])
one_hot_pred.shape

# print(model.evaluate(x_test,test_label))
# acc = accuracy_score(one_hot_pred,y_train_test)
# print(round(acc,4))

type(one_hot_pred)
one_hot_pred = np.append(one_hot_pred,1)
df = submission_DF(one_hot_pred, len_train=len(titanic_train), len_test=len(titanic_test))

path = '../pycharmProjects/pythonProject/dacon/titanic/submission.csv'
write_csv(path,df)
