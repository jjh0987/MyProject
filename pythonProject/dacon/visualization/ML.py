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

okt = Okt()
class internal_data():
    def __init__(self):
        pass

    def get_candidate_page_data(self,num):
        path = f'/Users/junho/Downloads/open/기호_{num} 공약.pdf'
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
            results[i, seq] = 1
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

    def preprocessing_ml_data(self,label_con,word_idx):
        dim = len(word_idx)
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
# 전체 후보가 언급한 단어에 대한 시각화 : extend
# 각 후보가 언급한 단어에 대한 시각화 : append
# 2회분량 공약집 내용 변화 시각화 -> 사진 페이지 처리 혹은 다른 pdf 혹은 파일
# 불용어, 복합 명사 처리


cl = internal_data()
label_con = 6
word_idx = cl.word_idx_dict_all(14)
dim = len(word_idx)

train_data,train_label = cl.preprocessing_ml_data(label_con,word_idx)
len(train_data) # line length : num of sentence
len(train_data[0]) # dict length : num of word
'''
# divide data
from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=5)
for train_index,test_index in skf.split(train_data,train_label):
    x_train,y_train = train_data[train_index],train_label[train_index]
    x_test,y_test = train_data[test_index],train_label[test_index]
'''

model = models.Sequential()
model.add(layers.Dense(300,activation='relu'))
model.add(layers.Dense(50,activation='relu'))

model.add(layers.Dense(label_con,activation='softmax'))

opt = optimizers.Adam(learning_rate=0.01)
loss = losses.sparse_categorical_crossentropy
model.compile(optimizer=opt,loss=loss,metrics=['accuracy'])

model.fit(train_data,train_label,epochs=15,batch_size=50)

target_string = input('원하는 키워드를 적어 주세요. 카워드에 따라 공약집이 추천 됩니다.')
# print(np.argmax(model.predict(cl.setting_data([okt.nouns(target_string)],dim))))
target = model.predict(cl.setting_data([okt.nouns(target_string)],dim,word_idx))
target = target.squeeze()

print('키워드 유사 공약 후보')
for i in range(len(target)):
    if target[i] > 0.15:
        print(f'기호{i+1}번, {round(target[i]*100,2)}%')
