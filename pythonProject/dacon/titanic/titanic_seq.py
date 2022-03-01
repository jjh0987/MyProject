import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


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
    return x_train,y_train

def setting_test(df,target):
    x_test = drop_features(df,target)
    x_test = x_test.fillna(x_test['Fare'].mean())
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


# x_train = x_train.fillna(df['Age'].mean())

drop_target = ['PassengerId','Ticket','Name','Cabin','Age']
encode_target = ['Sex','Embarked']
titanic_train,titanic_test = load_datasets()

titanic_train.info()
titanic_test.info()

train_set = drop_features(titanic_train,drop_target)

x_train,y_train = devide_train_xy(train_set,'Survived')
x_train = encoder(x_train,encode_target)
x_test = setting_test(titanic_test,drop_target)
x_test = encoder(x_test,encode_target)

x_train.info()
x_test.info()

x_train,y_train = devide_train_xy(train_set,'Survived')
x_train = encoder(x_train,encode_target)
x_test = setting_test(titanic_test,drop_target)
x_test = encoder(x_test,encode_target)
idx = 800
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
model.add(Dense(8,activation='relu',kernel_initializer=initializer))

model.add(Dense(4,activation='sigmoid'))
model.add(Dense(1,activation='sigmoid'))

# RMSprop
opt = optimizers.RMSprop(learning_rate=0.005)
loss = losses.binary_crossentropy
model.compile(optimizer=opt,loss=loss,metrics=['accuracy'])
model.fit(x_train_train,y_train_train,epochs=40,batch_size=30)

# pred = model.predict(x_train_test)

model.evaluate(x_train_test,y_train_test)


# one_hot_pred = np.array([np.argmax(i) for i in pred])
# acc = accuracy_score(one_hot_pred,y_train_test)
# print(round(acc,4))



pred = model.predict(x_test)
one_hot_pred = []
for i in pred:
    if i > 0.55:
        one_hot_pred.append(1)
    else:
        one_hot_pred.append(0)

# print(model.evaluate(x_test,test_label))
# acc = accuracy_score(one_hot_pred,y_train_test)
# print(round(acc,4))

type(one_hot_pred)
df = submission_DF(one_hot_pred, len_train=len(titanic_train), len_test=len(titanic_test))

path = '../pycharmProjects/pythonProject/dacon/titanic/submission.csv'
write_csv(path,df)
