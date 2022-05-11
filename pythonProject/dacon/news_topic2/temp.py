import pandas as pd
from nltk.corpus import stopwords
st_words = stopwords.words('english')
train_df = pd.read_csv('/Users/junho/Downloads/뉴스그룹분류경진대회/train.csv')
test_df = pd.read_csv('/Users/junho/Downloads/뉴스그룹분류경진대회/test.csv')

train_df.loc[:,'text'] = [str(i).replace('\n','').replace('\t','').replace('\r','').strip() for i in train_df.loc[:,'text']]
test_df.loc[:,'text'] = [str(i).replace('\n','').replace('\t','').replace('\r','').strip() for i in test_df.loc[:,'text']]

import re

train_df.loc[:,'text'] = [re.sub('[0-9-_.=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','',str(i).lower()) for i in train_df.loc[:,'text']]
test_df.loc[:,'text'] = [re.sub('[0-9-_.=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]','',str(i).lower()) for i in test_df.loc[:,'text']]

train_vec = [i for i in train_df.loc[:,'text']]
test_vec = [i for i in test_df.loc[:,'text']]
for i in st_words:
    for j in train_vec:
        if i in j:
            j.replace(i,'')
for i in st_words:
    for j in test_vec:
        if i in j:
            j.replace(i,'')

from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(max_features=20000,min_df=3)
tf.fit(train_vec)

train_vec = tf.transform(train_vec).toarray() # min_df = 5
test_vec = tf.transform(test_vec).toarray()
train_label = train_df.loc[:,'target']

# tf_vec

from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses

model = models.Sequential()

model.add(layers.Dense(500, activation='relu'))
model.add(layers.Dense(50, activation='relu'))

model.add(layers.Dense(20, activation='softmax'))

opt = optimizers.Adam(learning_rate=0.01)
loss = losses.sparse_categorical_crossentropy
model.compile(optimizer=opt, loss=loss, metrics=['accuracy'])

model.fit(train_vec, train_label, epochs=5, batch_size=50)

#
import numpy as np
pred = model.predict(test_vec)
ans = [np.argmax(i) for i in pred]
idx = list(range(len(ans)))
pred = [np.argmax(i) for i in pred]

#
from sklearn.neural_network import MLPClassifier
model = MLPClassifier()
model.fit(train_vec,train_label)
pred = model.predict(test_vec)
idx = list(range(len(pred)))
pred

df = pd.DataFrame()
df['id'] = idx
df['target'] = pred
df = df.set_index('id')
df.to_csv('/Users/junho/Downloads/submission.csv')
print(1)

