import pandas as pd
from konlpy.tag import Okt
import numpy as np

def load_datasets():
    path_train = '../pycharmProjects/pythonProject/dacon/news_topic/train_data.csv'
    path_test = '../pycharmProjects/pythonProject/dacon/news_topic/test_data.csv'
    path_idx_info = '../pycharmProjects/pythonProject/dacon/news_topic/topic_dict.csv'
    train_set = pd.read_csv(path_train)
    test_set = pd.read_csv(path_test)
    idx_set = pd.read_csv(path_idx_info)

    return train_set,test_set,idx_set

def vetorize_seq(seqs,dim=10000):
    results = np.zeros((len(seqs),dim+1))
    for i,seq in enumerate(seqs):
        results[i,seq] = 1
        # print()
    return results

def submission_DF(pred,len_train,len_test):
    data = []
    idx = len_train
    for i in range(0,len_test):
        temp = []
        temp.append((i)+idx)
        temp.append(pred[i])
        data.append(temp)
    df = pd.DataFrame(data=data,columns=['index','topic_idx'])
    df.set_index('index')
    return df.set_index('index')

def write_csv(path,df):
    df.to_csv(path)

# table is full
# nouns set, all set
train_set,test_set,idx_set = load_datasets()

okt = Okt()
train_set.drop('index',axis=1,inplace=True)


# prior tokenizing
'''
token_list = []
title_set = []
for i in train_set['title']:
    temp = []
    for j in okt.nouns(i):
        token_list.append(j)
        temp.append(j)
    title_set.append(temp)
'''
def tokeniziation(df):
    title_set = []
    for i in df['title']:
        temp = []
        for j in okt.nouns(i):
            temp.append(j)
        title_set.append(temp)
    return title_set

# train_set['title'] = title_set
# train_set

temp = pd.DataFrame(data=token_list)
token_set = pd.DataFrame(data=temp.value_counts())
word_idx = {token_set.index[i][0]:i+1 for i in range(len(token_set))}
word_idx

def setting_data(list,dim):
    for i in list:
        for j in range(len(i)):
            try:
                i[j] = word_idx[i[j]]
            except:
                i[j] = 0

    for i in list:
        for j in range(len(i)):
            if i[j] > dim:
                i[j] = 0
    return vetorize_seq(list,dim)

train_data = setting_data(title_set,8000)
train_label = train_set['topic_idx'].values

test_data = setting_data(tokeniziation(test_set),8000)
test_data
# 얼마나 매칭 안되는게 많은지 체크 해봐야할 사항.

# temp = [[i,j] for i,j in zip(train_data,train_label)]
# df = pd.DataFrame(data=temp)

# divide data
from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=5)
for train_index,test_index in skf.split(train_data,train_label):
    x_train,y_train = train_data[train_index],train_label[train_index]
    x_test,y_test = train_data[test_index],train_label[test_index]

label_con = len(idx_set)

from sklearn.metrics import accuracy_score
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses

model = models.Sequential()
model.add(layers.Dense(500,activation='relu'))
model.add(layers.Dense(100,activation='relu'))

model.add(layers.Dense(label_con,activation='softmax'))

opt = optimizers.RMSprop(learning_rate=0.01)
loss = losses.sparse_categorical_crossentropy
model.compile(optimizer=opt,loss=loss,metrics=['accuracy'])

model.fit(x_train,y_train,epochs=10,batch_size=200)
pred = model.predict(x_test)

# print(model.evaluate(x_test,test_label))
one_hot_pred = np.array([np.argmax(i) for i in pred])
acc = accuracy_score(one_hot_pred,y_test)
print(round(acc,4))




pred = model.predict(test_data)
one_hot_pred = np.array([np.argmax(i) for i in pred])
df = submission_DF(one_hot_pred, len_train=len(train_set), len_test=len(test_set))
path = '../pycharmProjects/pythonProject/dacon/news_topic/submission.csv'
write_csv(path,df)
# 45654 54784
print(1)