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
from nltk import word_tokenize
okt = Okt()


class PreprocessData():
    def __init__(self, stopwords_path, pdf_path):
        self.stopwords_path = stopwords_path
        self.pdf_path = pdf_path
        self.pdf_files = [pdfplumber.open(file) for file in pdf_path]

        f = open(stopwords_path, 'r')
        sw = f.readlines()
        f.close()
        self.stopwords = set(word.rstrip('\n') for word in sw)

        self.tokens = self.tokenization()
        all_tokens = sum(self.tokens, [])
        word_counts = dict(Counter(all_tokens))
        self.word_counts_sorted = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        self.word_idx = {self.word_counts_sorted[i][0]: i + 1 for i in range(len(self.word_counts_sorted))}

        (lines_token, top10, top10_token) = self.tokenized_lines()

        self.lines_token = lines_token
        self.top10 = top10
        self.top10_token = top10_token
        self.tf_sentences = self.tf_sentences()

    def tokenization(self):
        tokens = []
        hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
        for pdf in self.pdf_files:
            temp = []
            for page in pdf.pages:
                page_text = page.extract_text()
                hangul_text = hangul.sub('', page_text)
                hangul_tokens = okt.nouns(hangul_text)
                for hangul_token in hangul_tokens:
                    if hangul_token not in self.stopwords:
                        temp.append(hangul_token)
            tokens.append(temp)

        return tokens

    def tokenized_lines(self, drop_len=5):
        lines_token = []
        top10 = []
        top10_token = []
        hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')

        for number, pdf in enumerate(self.pdf_files):
            # top 10
            temp_text = [page.extract_text() for page in pdf.pages]
            temp_text = ''.join(temp_text)
            text_space = []
            temp_token = []
            if number != 11 and number != 13:
                for num in range(1, 11):
                    premise_text = temp_text[temp_text.find(f'공약순위 {num}') + 9:temp_text.find('\n목', temp_text.find(
                        f'공약순위 {num}'))]
                    if '\n' in premise_text:
                        premise_text = ''.join(premise_text.splitlines())
                    if f'기호 {number + 1}' in premise_text:
                        premise_text = premise_text[:premise_text.find(f'기호 {number + 1}')]
                    text_space.append(premise_text)
                    hangul_line = hangul.sub('', premise_text)
                    tokens = [token for token in okt.nouns(hangul_line) if token not in self.stopwords]
                    if len(tokens) > 0:
                        temp_token.extend(tokens)
            else:
                for num in range(1, 11):
                    premise_text = temp_text[temp_text.find(f'공약순위 {num}') + 9:temp_text.find('\n', temp_text.find(
                        f'공약순위 {num}'))]
                    if '\n' in premise_text:
                        premise_text = ''.join(premise_text.splitlines())
                    text_space.append(premise_text)
                    hangul_line = hangul.sub('', premise_text)
                    tokens = [token for token in okt.nouns(hangul_line) if token not in self.stopwords]
                    if len(tokens) > 0:
                        temp_token.extend(tokens)
            top10.append(text_space)
            top10_token.append(' '.join(temp_token))

            # lines_token
            temp_lines = []
            for page in pdf.pages:
                page_lines = page.extract_text().split('\n')
                for line in page_lines:
                    hangul_lines = hangul.sub('', str(line).strip())
                    if len(str(hangul_lines)) > drop_len:
                        tokens = [token for token in okt.nouns(hangul_lines) if token not in self.stopwords]
                        if len(tokens) > 0:
                            temp_lines.append(tokens)
            lines_token.append(temp_lines)

        return lines_token, top10, top10_token

    def tf_sentences(self):
        tf_sentences = []
        for tokens in self.tokens:
            temp = ''
            for word in tokens:
                temp += word + ' '
            tf_sentences.append(temp)
        return tf_sentences


stopword_path = '../pycharmProjects/pythonProject/dacon/visualization/data/stopwords_all.txt'
pdf_path = sorted(glob.glob('/Users/junho/Downloads/pdf/*'))

'''
pre = PreprocessData(stopword_path, pdf_path)
pre.pdf_path
pre.top10
pre.stopwords
pre.lines_token[-1]
pre.word_idx
pre.word_counts_sorted
pre.tokens
pre.tf_sentences
pre.top10_token
pre.lines_token
'''
# ml
class ml(PreprocessData):
    def __init__(self,stopwords_path, pdf_path):
        super().__init__(stopwords_path, pdf_path)
        self.clear_sentences,self.top10 = self.make_clear_sentences() # 원본: 역추적용

    def make_clear_sentences(self, drop_len=5):
        clear_sentences = []
        top10 = []
        for pdf in self.pdf_files:
            temp_sen = []
            temp_top = []
            for page in pdf.pages:
                hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
                clear_sen = [hangul.sub('', str(i)).rstrip() for i in page.extract_text().split('\n')]

                for sen in clear_sen:
                    if len(sen) > drop_len:
                        temp_sen.append(sen.replace('공약순위',''))
                    if '공약순위' in sen:
                        temp_top.append(sen.replace('공약순위','').lstrip())
            clear_sentences.append(temp_sen)
            top10.append(temp_top)
        return clear_sentences,top10

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
            temp_data = self.lines_token[i - 1]
            temp_label = [i - 1] * len(temp_data)
            train_data.extend(temp_data)
            train_label.extend(temp_label)
        train_data = self.setting_data(train_data, dim, word_idx)
        train_label = np.array(train_label)
        return train_data, train_label

    def ml(self,label_con, train_data, train_label): #
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

        model.fit(train_data, train_label, epochs=10, batch_size=50) #
        return model

    def show_similar_candidate(self,target_string,model,dim):
        # print(np.argmax(model.predict(cl.setting_data([okt.nouns(target_string)],dim))))
        target = model.predict(self.setting_data([okt.nouns(target_string)], dim, self.word_idx))
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

        tf_sentences = self.tf_sentences
        stopwords = self.stopwords
        t_vec = TfidfVectorizer(max_features=3000, stop_words=stopwords)
        tdm = t_vec.fit_transform(tf_sentences)
        t_vec.get_feature_names_out()
        tf_rank = pd.DataFrame({
            '단어': t_vec.get_feature_names_out(),
            'tf-idf': tdm.sum(axis=0).flat
        })
        #word_count = word_count.set_index('단어')
        #word_count = word_count.sort_values('tf-idf', ascending=False)
        return tf_rank

    def pred(self):
        target_string = input('원하는 키워드를 적어 주세요. 카워드를 기반한 공약집이 추천 됩니다.')
        key = okt.nouns(target_string)
        idx, acc = mlc.show_similar_candidate(target_string, model, dim)
        candidate_dict = {idx[i]: acc[i] for i in range(len(idx))}
        # df = pd.DataFrame(data=self.top10)
        # df = df.transpose()
        # df = pd.read_csv('/Users/junho/Downloads/promise_all.csv') # 14 by 10
        # df = pd.read_csv('/Users/junho/Downloads/promise10.csv') # 14 by 10

        print(f'적용된 키워드: {key}')
        # check = set(tf_rank.sort_values('tf-idf', ascending=False)[:300].iloc[:,0])
        for i in idx:
            x = 0
            cnt = 0
            print()
            for j in range(1, 11):
                if x == 0:
                    print(f'기호{i}번, {candidate_dict[i]}%')
                    x += 1
                '''
                for k in key:
                    if k in str(df.iloc[i-1,j]) and k in check:
                        print(f'공약{j}번: {df.iloc[i - 1, j]}, [사용된 키워드 {k}]')
                        break
                '''


pre = PreprocessData(stopword_path, pdf_path)
label_con = 10
dim = 3000 # vector dimension
word_idx = pre.word_idx

# ML
mlc = ml(stopword_path,pdf_path)
from sklearn.model_selection import train_test_split


train_data, train_label = mlc.preprocessing_ml_data(label_con, word_idx,dim=dim)
# X_train, X_val, y_train, y_val = train_test_split(train_data,train_label, test_size=0.20,shuffle=True)
model = mlc.ml(label_con,train_data,train_label)

# mlc.show_similar_candidate('경제',model,dim)

tf_rank = mlc.tf_idf_score().sort_values('tf-idf',ascending=False)
tf_rank[:100]

mlc.pred()

'''
from sklearn.metrics import accuracy_score
pred = model.predict(X_val)
pred = [np.argmax(i) for i in pred]
accuracy_score(pred,y_val) # 0.58
'''
#
from gensim.models.doc2vec import Doc2Vec,TaggedDocument
from nltk.tokenize import word_tokenize
pre = PreprocessData(stopword_path, pdf_path)
mlc = ml(stopword_path,pdf_path)

temp = []
for i in mlc.clear_sentences:
    for j in i:
        temp.append(j)

taged = []
for idx,sen in enumerate(temp):
    taged.append(TaggedDocument(words=word_tokenize(sen),tags=[str(i)]))

doc2vec = Doc2Vec(alpha=0.001)
doc2vec.build_vocab(taged)
doc2vec.train(
    corpus_iterable=taged,
    epochs=5,
    total_examples=doc2vec.corpus_count
)




#
from gensim.models.word2vec import Word2Vec
temp = []
for i in pre.lines_token:
    for j in i:
        temp.append(j)
w2v = Word2Vec(pre.lines_token[0]) # 카운트 3 이하 제거
w2v.wv.most_similar('복지')
w2v = Word2Vec(temp)
w2v.wv.most_similar('복지')
w2v.corpus_total_words

w2v.wv.vectors.shape # 단어, 벡터 (1061,100)
w2v.wv['복지']
w2v.wv.key_to_index
len(w2v.wv.index_to_key)

from gensim.models.doc2vec import Doc2Vec
d2v = Doc2Vec(mlc.clear_sentences)
mlc.clear_sentences
