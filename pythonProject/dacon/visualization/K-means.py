from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from konlpy.tag import Okt
from nltk import word_tokenize
import re

df = pd.read_csv('/Users/junho/Downloads/promise10.csv') # 14 by 10
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

f = open('/Users/junho/Downloads/stopwords.txt', 'r')
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

#문장 벡터화
vectorize = CountVectorizer()
x = vectorize.fit_transform(clean_text)

######### K-means 분석 ###########
#데이터 프레임 생성 (문장 단어 매트릭스 만들기)
new_df = pd.DataFrame(x.toarray(), columns=vectorize.get_feature_names_out())
# K- means 군집 분석
pca = PCA(n_components=2) # 2차원으로 축소
pc = pca.fit_transform(new_df)
p_df = pd.DataFrame(data=pc, columns=['x', 'y'])
kmeans = KMeans(n_clusters=4, n_init = 10, max_iter = 300, random_state = 50).fit(p_df)
print('K-평균 군집 분석 결과')
candidate_num = ['1번','2번','3번','4번','5번','6번','7번','8번','9번','10번','11번','12번','13번','14번']
for i, j in zip(candidate_num,kmeans.labels_):
    print(i, j)

plt.scatter(p_df.iloc[kmeans.labels_ == 0,0],
            p_df.iloc[kmeans.labels_ == 0,1], s = 10, c = 'red', label = 'clustering1')
plt.scatter(p_df.iloc[kmeans.labels_ == 1,0],
            p_df.iloc[kmeans.labels_ == 1,1], s = 10, c = 'blue', label = 'clustering2')
plt.scatter(p_df.iloc[kmeans.labels_ == 2,0],
            p_df.iloc[kmeans.labels_ == 2,1], s = 10, c = 'green', label = 'clustering3')
plt.scatter(p_df.iloc[kmeans.labels_ == 3,0],
            p_df.iloc[kmeans.labels_ == 3,1], s = 10, c = 'purple', label = 'clustering4')

plt.legend()
plt.title('Promise 10')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



######### k-대푯값 군집 분석 ###########
#인스턴스 생성
# kmedoids_ins = kmedoids.kmedoids(new_df.values,initial_index_medoids=[4,18,36]) # initial_index는 df행 중 대푯값 행 지정
# kmedoids_ins.process()
# clusters = kmedoids_ins.get_clusters()
# print('###########################################')
# print('[K-대푯값 군집 분석 결과]')


# 군집간 정책 교집합
# 후보 추천