import pdfplumber
from konlpy.tag import Okt
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from matplotlib import font_manager, rc
import glob
import re
from gensim.models import Word2Vec
import numpy as np
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
okt = Okt()

class internal_data():
    def __init__(self):
        pass

    def get_candidate_page_data(self,num):
        path = f'/Users/junho/Downloads/pdf/기호_{num} 공약.pdf'
        pdf = pdfplumber.open(path)
        temp = [page.extract_text() for page in pdf.pages]
        return temp

    def tokenization(slef,pdf):
        stopword_path = '/Users/junho/Desktop/pycharmProjects/pythonProject/dacon/visualization/data/stopwords_all.txt'
        temp = []
        f = open(stopword_path, 'r')
        stop = f.readlines()
        f.close()
        stopwords = set(i.rstrip('\n') for i in stop)
        for page in pdf.pages:
            temp.extend(okt.nouns(page.extract_text()))
        token = []
        for word in temp:
            if word not in stopwords:
                token.append(word)
        return token

    # append [[],[]..] for each candidate
    # extend [] for all
    def dict_data(self,num_of_candidate,method):
        candidate_text = []
        for num in range(1,num_of_candidate+1):
            path = f'/Users/junho/Downloads/open/기호_{num} 공약.pdf' # glob 이용 해보기
            pdf = pdfplumber.open(path)
            if method == 'each':
                candidate_text.append(self.tokenization(pdf))
            elif method == 'all':
                candidate_text.extend(self.tokenization(pdf))
        return candidate_text

    # 호출형식 pdf.pages[0].extract_text()
    # type(okt.nouns(pdf.pages[0].extract_text())) : list
    # input : pdfplumber.open(path)
    # 필요사항 : non_data dict -> 파파고

    def word_idx_dict_all(self,num_of_candidate):
        df = pd.DataFrame(data=self.dict_data(num_of_candidate,'all'))
        token_set = df.value_counts()
        word_idx = {token_set.index[i][0]: i+1 for i in range(len(token_set))}
        return word_idx

    def idx_word_dict_all(self,num_of_candidate):
        df = pd.DataFrame(data=self.dict_data(num_of_candidate, 'all'))
        token_set = df.value_counts()  # : series
        word_idx = {i+1: token_set.index[i][0] for i in range(len(token_set))}
        return word_idx

    def idx_word_dict_each(self,num_of_candidate):
        idx_word_each = []
        for i in self.dict_data(num_of_candidate, 'each'):
            temp_df = pd.DataFrame(data=i)
            token_set = temp_df.value_counts()  # 여기 까지 진행시, 빈도수 나열
            temp_word_idx = {i+1: token_set.index[i][0] for i in range(len(token_set))}
            idx_word_each.append(temp_word_idx)
        return idx_word_each

    def word_idx_dict_each(self,num_of_candidate):
        word_idx_each = []
        for i in self.dict_data(num_of_candidate, 'each'):
            temp_df = pd.DataFrame(data=i)
            token_set = temp_df.value_counts()  # 여기 까지 진행시, 빈도수 나열
            temp_word_idx = {token_set.index[i][0]:i+1 for i in range(len(token_set))}
            word_idx_each.append(temp_word_idx)
        return word_idx_each

    def showWordCloud(self,text_counts, person=None):
        tags = text_counts.most_common(100)

        wc = WordCloud(font_path='AppleGothic', background_color='white',
                       max_font_size=60)
        cloud = wc.generate_from_frequencies(dict(tags))

        plt.figure(figsize=(10, 8))
        plt.title(f'{person} keywords', size=20)
        plt.axis('off')
        plt.imshow(cloud)

    def showGraph(self,tags, person=None):
        # font_location = '/Users/junho/Downloads/나눔고딕/NanumGothic.ttf'
        # font_name = font_manager.FontProperties(fname=font_location).get_name()
        rc('font', family='AppleGothic')
        plt.rcParams['axes.unicode_minus'] = False  # 한글화 경우, 마이너스 깨짐 방지.

        plt.figure(figsize=(10, 5))
        plt.xlabel('keyword')
        plt.grid(True)

        Dict_Values = tags.values() # collection/Counter/values
        Dict_Keys = tags

        plt.title(f'{person} keyword top 20', size=20)
        plt.bar(range(len(tags)), Dict_Values, align='center')
        plt.xticks(range(len(tags)), list(Dict_Keys), rotation='70')

    def make_clear_sentences(self,candidate_number, stopword_path, drop_len=5):
        temp = self.get_candidate_page_data(candidate_number)  # input : number of candidate
        clear = [i.split('\n') for i in temp]
        hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
        clear_cen = []
        for candidate in clear:
            for cen in candidate:
                clear_cen.append(hangul.sub('', str(cen)))
        temp = [i.strip() for i in clear_cen]
        cen = []
        for i in temp:
            if len(i) > drop_len:
                cen.append(i)
        f = open(stopword_path, 'r')
        stop = f.readlines()
        f.close()
        stopwords = set(i.rstrip('\n') for i in stop)
        sents = [list(okt.nouns(i)) for i in cen]  # 원본

        sents_clear = []
        for sent in sents:
            temp = []
            for word in sent:
                if word not in stopwords:
                    temp.append(word)
            sents_clear.append(temp)
        return sents_clear

    def show_simirality(self, sents_clear, target_word, num=None):
        model = Word2Vec(sents_clear)
        df = pd.DataFrame(reversed(model.wv.most_similar(target_word)))
        df.set_index(0)

        plt.figure(figsize=(10, 6))
        plt.barh(df[0], df[1])
        plt.xlabel('Similarity')
        plt.ylabel('Words')
        if not num:
            plt.title(f"'{target_word}'의 언어 유사도")
        else:
            plt.title(f"기호{num}번의 '{target_word}' 유사도")

    def vetorize_seq(self,seqs, dim=10000):
        results = np.zeros((len(seqs), dim + 1))
        for i, seq in enumerate(seqs):
            results[i, seq] += 1
            # print()
        return results

    def setting_data(self,list, dim, word_idx):
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
        return self.vetorize_seq(list, dim)

    def preprocessing_ml_data(self,label_con,word_idx,dim):
        # dim = len(word_idx) 3900-
        stopword_path = '/Users/junho/Desktop/pycharmProjects/pythonProject/dacon/visualization/data/stopwords_all.txt'
        train_data = []
        train_label = []
        for i in range(1, label_con + 1):
            temp_data = self.make_clear_sentences(i, stopword_path)
            temp_label = [i - 1] * len(temp_data)
            train_data.extend(temp_data)
            train_label.extend(temp_label)
        train_data = self.setting_data(train_data, dim, word_idx)
        train_label = np.array(train_label)
        return train_data, train_label

    def ml(self,label_con, train_data, train_label):
        # dim = len(word_idx)
        random.set_seed(50)
        # train_data,train_label = cl.preprocessing_ml_data(label_con,word_idx)
        # len(train_data) # line length : num of sentence
        # len(train_data[0]) # dict length : num of word
        model = models.Sequential()
        model.add(layers.Dense(300, activation='relu'))
        model.add(layers.Dense(50, activation='relu'))

        model.add(layers.Dense(label_con, activation='softmax'))

        opt = optimizers.Adam(learning_rate=0.01)
        loss = losses.sparse_categorical_crossentropy
        model.compile(optimizer=opt, loss=loss, metrics=['accuracy'])

        model.fit(train_data, train_label, epochs=15, batch_size=50)
        return model

    def show_similar_candidate(self,target_string,model,dim):
        # print(np.argmax(model.predict(cl.setting_data([okt.nouns(target_string)],dim))))
        target = model.predict(cl.setting_data([okt.nouns(target_string)], dim, word_idx))
        target = target.squeeze()
        # print('키워드 유사 공약 후보')
        idx = []
        acc = []
        for i in range(len(target)):
            if target[i] > 0.10:
                # print(f'기호{i + 1}번, {round(target[i] * 100, 2)}%')
                idx.append(i+1)
                acc.append(round(target[i] * 100, 2))
        return idx,acc

    def tf_idf_score(self):
        sentences = []
        for i in range(1, 15):
            target = self.get_candidate_page_data(i)
            temp = []
            for i in target:
                temp.extend(i.split('\n'))
            hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
            temp = [hangul.sub('', i).strip() for i in temp]
            temp_sen = ''

            for i in temp:
                if len(i) > 5:
                    temp_sen += i
            sentences.append(okt.nouns(temp_sen))

        tf_sentences = []
        for i in sentences:
            temp = ''
            for j in i:
                temp += j + ' '
            tf_sentences.append(temp)

        f = open(path_stopword_all, 'r')
        stop = f.readlines()
        f.close()
        stopwords = set(i.rstrip('\n') for i in stop)
        t_vec = TfidfVectorizer(max_features=3000, stop_words=stopwords)
        tdm = t_vec.fit_transform(tf_sentences)
        t_vec.get_feature_names_out()
        word_count = pd.DataFrame({
            '단어': t_vec.get_feature_names_out(),
            'tf-idf': tdm.sum(axis=0).flat
        })
        #word_count = word_count.set_index('단어')
        #word_count = word_count.sort_values('tf-idf', ascending=False)
        return t_vec,tf_sentences,word_count

    def cluster_map(self,max_features=1000):
        tf_idf, tf_sentences, tf_idf_score = self.tf_idf_score()
        cv = CountVectorizer(max_features=max_features)
        tdm = cv.fit_transform(tf_sentences)
        df = pd.DataFrame(data=tdm.toarray(), columns=cv.get_feature_names_out())
        df.reset_index(inplace=True)
        df['index'] += 1
        df.set_index('index', inplace=True)
        df = df.transpose()

        import seaborn as sns
        sns.clustermap(df.corr(),
                       annot=True,
                       cmap='RdYlBu_r',
                       vmin=-1, vmax=1)

# 전체 후보가 언급한 단어에 대한 시각화 : extend
# 각 후보가 언급한 단어에 대한 시각화 : append
# 2회분량 공약집 내용 변화 시각화 -> 사진 페이지 처리 혹은 다른 pdf 혹은 파일
# 불용어, 복합 명사 처리
path_stopword_all = '/Users/junho/Desktop/pycharmProjects/pythonProject/dacon/visualization/data/stopwords_all.txt'
# using glob
path_stopword_can = '/Users/junho/Desktop/pycharmProjects/pythonProject/dacon/visualization/data/stopwords/stopwords_01.txt'
path_title_csv = '/Users/junho/Desktop/pycharmProjects/pythonProject/dacon/visualization/data/promise10.csv'

cl = internal_data()
cl.make_clear_sentences(14,path_stopword_all)


word_idx = cl.word_idx_dict_all(14)

clean_text = cl.dict_data(14,'all') # 모든 후보,중복 단어
counts = Counter(clean_text)

cl.showWordCloud(counts,'All candidates')

tags_20 = counts.most_common(20)
cl.showGraph(dict(tags_20),'All candidates')

# 기호 1번 샘플
clean_text_each = cl.dict_data(14,'each')
counts_each = [Counter(i) for i in clean_text_each]
len(counts_each)
counts_each[0]['분석']
counts_each[0]

cl.showWordCloud(counts_each[0],'기호1')
cl.showGraph(dict(counts_each[0].most_common(20)),'기호1')


# 유사도 측정
# input : 번호,stopword path,
# drop_len=5 제거길이 (문장 정규표혀,공백 strip 후 빈문장 혹은 '목표','이행방법' 등의 문장 제거를 위한 단위길이)
sents_clear = cl.make_clear_sentences(1,path_stopword_can,drop_len=5)
sents_clear
cl.show_simirality(sents_clear,'일자리','1')


temp_sents_all = [cl.make_clear_sentences(num,path_stopword_all) for num in range(1,15)]
clear_sents_all = []
for i in temp_sents_all:
    clear_sents_all += i

model = Word2Vec(clear_sents_all)
model.wv.most_similar('부동산',topn=15)

df = pd.read_csv(path_title_csv)
df = df.set_index('Unnamed: 0')
df

# word_idx = cl.word_idx_dict_all(14)
# dim = len(word_idx)
# target = cl.dict_data(14,method='each')
# target

'''
# divide data
from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=5)
for train_index,test_index in skf.split(train_data,train_label):
    x_train,y_train = train_data[train_index],train_label[train_index]
    x_test,y_test = train_data[test_index],train_label[test_index]
'''

# ML
tf_idf,tf_sentences,tf_idf_score = cl.tf_idf_score()
tf_idf.get_feature_names()
tdm = tf_idf.fit_transform(tf_sentences)

cl = internal_data()
label_con = 6
dim = 2500
word_idx = cl.word_idx_dict_all(14)
word_idx
# train data : 14pdf 각 문장
tf_idf_score[:50] # 스코어가 높을수록 특정 문서에서 많이 쓰이는 경향이 있음. # 갯수 슬라이싱

'''
train_data, train_label = cl.preprocessing_ml_data(label_con, word_idx,dim=dim)

model = cl.ml(label_con,dim,train_data,train_label)
target_string = input('원하는 키워드를 적어 주세요. 카워드를 기반한 공약집이 추천 됩니다.')
idx,acc = cl.show_similar_candidate(target_string,model,dim)
# ml preprocessing 방식
# 각페이지 붙인 공약집 re 처리후 길이 5이하 제거 -> okt.nouns 이용 후 토크나이징
'''

# corr
tf_sentences
cl.cluster_map() # all contents, counter_vector, max features : 500



# ML
label_con = 6
dim = 2500 # vector dimension
word_idx = cl.word_idx_dict_all(14)

train_data, train_label = cl.preprocessing_ml_data(label_con, word_idx,dim=dim)
model = cl.ml(label_con,train_data,train_label)
len(train_data[0])

def temp():
    target_string = input('원하는 키워드를 적어 주세요. 카워드를 기반한 공약집이 추천 됩니다.')
    key = okt.nouns(target_string)
    idx,acc = cl.show_similar_candidate(target_string,model,dim)
    candidate_dict = {idx[i]:acc[i] for i in range(len(idx))}
    df = pd.read_csv('/Users/junho/Downloads/promise_all.csv') # 14 by 10
    # df = pd.read_csv('/Users/junho/Downloads/promise10.csv') # 14 by 10

    check = set(tf_idf_score.sort_values('tf-idf', ascending=False)[:300].iloc[:,0])
    for i in idx:
        x = 0
        cnt = 0
        print()
        for j in range(1,11):
            if x == 0:
                print(f'기호{i}번, {candidate_dict[i]}%')
                x += 1
            for k in key:
                if k in str(df.iloc[i-1,j]) and k in check:
                    print(f'공약{j}번: {df.iloc[i - 1, j][:15]}..')
                    break

