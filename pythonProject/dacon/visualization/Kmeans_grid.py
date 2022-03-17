from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from konlpy.tag import Okt
from nltk import word_tokenize
import re
import scipy.cluster.hierarchy as shc

data_path = '/Users/junho/Desktop/pycharmProjects/pythonProject/dacon/visualization/data/promise10.csv'
stopword_path = '/Users/junho/Desktop/pycharmProjects/pythonProject/dacon/visualization/data/stopwords_all.txt'

df = pd.read_csv(data_path) # 14 by 10
arr = df.values.tolist()

okt = Okt()

def tokenization(df):
    temp = []
    for arr in df:
        arr.pop(0)
        text = word_tokenize(' '.join(arr))
        temp.append(okt.nouns(str(text)))
    return temp

text = tokenization(arr)

f = open(stopword_path, 'r')
lines = f.readlines()
stopwords = []
for line in lines:
    line = line.replace('\n', '')
    stopwords.append(line)
f.close()


def preprocessing(text):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    storage = []
    for txt in text:
        temp = []
        for t in txt:
            txt = hangul.sub('', str(t))
            tokens = okt.morphs(txt)
            stop = stopwords
            tokens = [token for token in tokens if token not in stop]
            if len(tokens) > 0:
                temp.extend(tokens)
        storage.append(' '.join(temp))

    return storage

clean_text = preprocessing(text)
print(clean_text)

vectorize = CountVectorizer()
x = vectorize.fit_transform(clean_text)
new_df = pd.DataFrame(x.toarray(), columns=vectorize.get_feature_names_out())
kmeans = KMeans(n_clusters=5, n_init = 10, max_iter = 300, random_state = 50).fit(new_df)
pca = PCA(n_components=2)
pc = pca.fit_transform(kmeans.cluster_centers_)



pca = PCA(n_components=2)
pc = pca.fit_transform(new_df)
p_df = pd.DataFrame(data=pc, columns=['x', 'y'])
km = KMeans(init='k-means++', n_clusters=4, n_init=10).fit(pc)

h = 0.01

x_min, x_max = pc[:, 0].min() - 1, pc[:, 0].max() + 1
y_min, y_max = pc[:, 1].min() - 1, pc[:, 1].max() + 1
x_vals, y_vals = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

output = km.predict(np.c_[x_vals.ravel(), y_vals.ravel()])
output = output.reshape(x_vals.shape)

km.cluster_centers_



kmeans = KMeans(n_clusters=2, n_init = 10, max_iter = 300, random_state = 50).fit(new_df)
pca = PCA(n_components=2)
pc = pca.fit_transform(kmeans.cluster_centers_)
# kmeans_cen = KMeans(n_clusters=4, random_state=0).fit(p_df)
print('K-평균 군집 분석 결과')
candidate_num = ['1번','2번','3번','4번','5번','6번','7번','8번','9번','10번','11번','12번','13번','14번']
for i, j in zip(candidate_num,kmeans.labels_):
    print(i, j)

sns.set_style('whitegrid')

fig = plt.figure(figsize=(8, 5))

plt.scatter(p_df.iloc[kmeans.labels_ == 0,0],
            p_df.iloc[kmeans.labels_ == 0,1], s = 10, c = 'red', label = 'clustering1')
plt.scatter(p_df.iloc[kmeans.labels_ == 1,0],
            p_df.iloc[kmeans.labels_ == 1,1], s = 10, c = 'blue', label = 'clustering2')
#plt.scatter(p_df.iloc[kmeans.labels_ == 2,0],
#            p_df.iloc[kmeans.labels_ == 2,1], s = 10, c = 'green', label = 'clustering3')
#plt.scatter(p_df.iloc[kmeans.labels_ == 3,0],
#            p_df.iloc[kmeans.labels_ == 3,1], s = 10, c = 'purple', label = 'clustering4')
#plt.scatter(p_df.iloc[kmeans.labels_ == 4,0],
#            p_df.iloc[kmeans.labels_ == 4,1], s = 10, c = 'orange', label = 'clustering5')
kmeans.labels_
plt.scatter(
    pc[:, 0], pc[:, 1],
    s=250, marker='*',
    c='red', edgecolor='black',
    alpha=0.7,
    label='centroids'
)

plt.legend()
plt.title('Promise 10')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


data = p_df.values
plt.figure(figsize=(10, 5))
plt.title('Dendrogram')
plt.axhline(y=4.75, ls='--', c='r')
dend = shc.dendrogram(shc.linkage(data, method='average'),
                      color_threshold=254,
                      )

