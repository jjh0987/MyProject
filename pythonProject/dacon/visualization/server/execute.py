import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow import random
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from PIL import Image
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from konlpy.tag import Okt
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
from wordcloud import WordCloud
plt.rcParams['axes.unicode_minus'] = False
okt = Okt()

import preprocessing
pre = preprocessing

candidates = ['기호 1번', '기호 2번', '기호 3번', '기호 4번', '기호 5번', '기호 6번', '기호 7번',
              '기호 8번', '기호 9번', '기호 10번', '기호 11번', '기호 12번', '기호 13번', '기호 14번', '전체']
font_location = 'AppleGothic'
font_name = 'AppleGothic'

import streamlit as st
class VisualizeKeywords():
    def __init__(self):
        self.mask_path = pre.mask_path
        self.font_location = font_location
        self.font_name = font_name

        sns.set_style('whitegrid')
        rc('font', family=self.font_name)

    def show_graphs(self, text_counts, sents_clear=None, num=None):
        tags = text_counts.most_common(100)

        mask = np.array(Image.open(pre.mask_path))

        wc = WordCloud(font_path=self.font_location, background_color='white',
                       colormap='twilight_shifted', max_font_size=100, mask=mask)

        cloud = wc.generate_from_frequencies(dict(tags))

        fig = plt.figure(figsize=(25, 13))
        plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.35)

        plt.subplot(2, 2, 1)
        if not num:
            plt.title(f'정책 공약 키워드', size=20)
        else:
            plt.title(f'기호 {num}번의 정책 공약 키워드', size=27)
        plt.axis('off')
        plt.imshow(cloud)

        tags20 = dict(text_counts.most_common(20))

        plt.subplot(2, 2, 2)
        plt.xlabel('주요 단어')
        plt.ylabel('빈도')

        tags20_df = pd.DataFrame(tags20.values(), index=tags20.keys(), columns=['빈도'])

        if not num:
            plt.title(f'정책 공약 키워드 top 20', size=20)
        else:
            plt.title(f'기호 {num}번의 정책 공약 키워드 top 20', size=20)
            plt.suptitle(f'기호 {num}번', size=40, va='bottom')

        sns.set_palette(reversed(sns.color_palette('Purples', 20)), 20)

        ax1 = sns.barplot(x=tags20_df.index, y=tags20_df['빈도'], data=tags20_df)
        for bar in ax1.patches:
            bar.set_width(0.5)

        plt.xticks(rotation='45')

        if sents_clear:
            keys = ['추진', '폐지']
            model = Word2Vec(sents_clear, min_count=4, seed=65)

            for i in range(len(keys)):
                try:
                    df = pd.DataFrame(model.wv.most_similar(keys[i]))
                    df.set_index(0)
                except:
                    print(f"기호 {num}번의 정책 공약에 '{keys[i]}'이/가 존재하지 않습니다.")
                    plt.subplot(2, 2, i + 3)
                    if not num:
                        plt.title(f"단어 유사도: {keys[i]}", size=20)
                    else:
                        plt.title(f"기호 {num}번의 단어 유사도: {keys[i]}", size=20)
                else:
                    plt.subplot(2, 2, i + 3)
                    ax2 = sns.barplot(y=df[0], x=df[1])

                    for bar in ax2.patches:
                        bar.set_height(0.5)

                    plt.xlabel('유사도')
                    plt.ylabel('단어')
                    if not num:
                        plt.title(f"단어 유사도: {keys[i]}", size=20)
                    else:
                        plt.title(f"기호 {num}번의 단어 유사도: {keys[i]}", size=20)

        st.pyplot(fig)

    def stacked_category(self):
        temp = []
        for i in range(4):
            key = {'경제': 0, '복지': 0, '정치': 0, '보건': 0, '환경': 0, '문화': 0,
                   '관광': 0, '노동': 0, '교육': 0, '산업': 0, '안보': 0, '국방': 0,
                   '북한': 0}
            for j in pre.tokens[i]:
                if j in key:
                    key[j] += 1

            temp.append(key)
        df = pd.DataFrame(temp)
        df.index = ['기호1', '기호2', '기호3', '기호4']
        df = df.transpose()

        df_per = df.copy()
        for i in range(len(df_per.index)):
            df_per.loc[df_per.index[i]] /= sum(df_per.loc[df_per.index[i]])

        df_per = round(df_per, 3)

        fig = plt.figure(figsize=(30, 8))
        colors = ['royalblue', 'crimson', 'gold', 'sandybrown']

        ax1 = fig.add_subplot(1, 2, 1)
        df.plot(kind='bar', stacked=True, color=colors, ax=ax1)
        plt.xticks(rotation='45')
        plt.legend(frameon=True, shadow=True)
        plt.title('후보자별 키워드 등장 횟수', fontsize=20)

        ax2 = fig.add_subplot(1, 2, 2)
        df_per.plot(kind='bar', stacked=True, color=colors, ax=ax2)
        plt.xticks(rotation='45')
        plt.title('후보자별 키워드 등장 비율', fontsize=20)
        plt.legend().remove()

        i = 0
        j = 0
        for p in ax2.patches:
            if i >= len(df.index):
                i = 0
                j += 1
            left, bottom, width, height = p.get_bbox().bounds
            if height == 0:
                i += 1
                continue
            ax2.annotate("%d%%" % (df_per[df.columns[j]][i] * 100), xy=(left + width / 2, bottom + height / 2),
                         ha='center', va='center')
            i += 1

        st.pyplot(fig)

    def corr_map(self, max_features=500):  # max features = 1000 등 높은값 에러 이슈 rename하지 않은코드는 정상작동
        cv = CountVectorizer(max_features=max_features)
        tdm = cv.fit_transform(pre.tf_sentences)
        df = pd.DataFrame(data=tdm.toarray(), columns=cv.get_feature_names_out(), index=list(range(1, 15)))
        df = df.transpose()

        sns.clustermap(df.corr(),
                       annot=True,
                       cmap='RdYlBu_r',
                       vmin=-1, vmax=1,
                       figsize=(12, 10))


class SearchPromise():
    def __init__(self):
        self.df = pre.promise140
        self.word_dict = self.word_vectorized()
        self.df_reshaped_vector = self.promise_vectorized()

    def dict_promise(self):
        dict_df = {value: self.df['기호'][idx] for idx, value in zip(self.df.index, self.df['정책 공약'].values)}

        return dict_df

    def word_vectorized(self):
        tokens = []
        for text in self.df['정책 공약_tokens'].values.tolist():
            token = [word for word in text.split()]
            tokens.append(token)

        model = Word2Vec(tokens, min_count=1, window=3, workers=3, seed=1)

        word_dict = {}
        for vocab in model.wv.index_to_key:
            word_dict[vocab] = model.wv[vocab]

        return word_dict

    def promise_vectorized(self):
        dict_vector = {}
        df_reshaped_vector = self.df.copy()
        for idx in df_reshaped_vector.index:
            list_vector = []
            for word in self.df['정책 공약_tokens'][idx].split():
                if word in self.word_dict.keys():
                    list_vector.append(self.word_dict[word])
            dict_vector[df_reshaped_vector['정책 공약'][idx]] = np.sum(list_vector, axis=0).tolist()

        df_reshaped_vector['vector'] = df_reshaped_vector['정책 공약'].map(dict_vector)

        return df_reshaped_vector

    def user_input_to_vector(self, user_input):
        tokenized_input = okt.nouns(user_input)

        list_vector = []

        for word in tokenized_input:
            if word in self.word_dict.keys():
                list_vector.append(self.word_dict[word])
        if len(list_vector) != 0:
            user_vector = (np.sum(list_vector, axis=0) / len(list_vector)).tolist()
        else:
            user_vector = 0

        return user_vector

    def find_similar_promise(self, user_input):
        user_vector = self.user_input_to_vector(user_input)
        if user_vector == 0:
            result = '없음'
        else:
            similarity = {}

            for idx in self.df_reshaped_vector.index:
                sim = cosine_similarity(np.array(user_vector).reshape(1, -1),
                                        np.array([float(i) if i != '.' else float('0.0') for i in
                                                  str(self.df_reshaped_vector.loc[idx, 'vector'])[1:-1].split(
                                                      ', ')]).reshape(1, -1))
                similarity[self.df_reshaped_vector['정책 공약'][idx]] = float(sim)
            similarity = {key: value for key, value in
                          sorted(similarity.items(), key=lambda item: item[1], reverse=True)}
            rating = [str(key) for key, value in sorted(similarity.items(), key=lambda item: item[1], reverse=True)]
            top = rating[:3]
            result = {}

            for i in top:
                result[i] = str(abs(round(similarity[i] * 100, 2))) + '%'

        return result

    def show_similar_promise(self, user_input):
        result = self.find_similar_promise(user_input)
        dict_df = self.dict_promise()
        if result == '없음':
            st.write('관심사를 다시 입력해주세요.')
        else:
            for i in result.keys():
                st.write(f'[{dict_df[i]}] {i} : {result[i]}')


from tensorflow import random


class ML():
    def __init__(self):
        # self.clear_sentences,self.top10 = self.make_clear_sentences()
        pass

    def vetorize_seq(self, seqs, dim=10000):
        results = np.zeros((len(seqs), dim))
        for i, seq in enumerate(seqs):
            try:
                results[i, seq] += 1
            except:
                pass
            # print()
        return results

    def setting_data(self, list, dim, word_idx):
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

    def preprocessing_ml_data(self, label_con, word_idx, dim):
        # dim = len(word_idx) 3900-
        train_data = []
        train_label = []
        for i in range(1, label_con + 1):
            temp_data = pre.lines_token[i - 1]
            temp_label = [i - 1] * len(temp_data)
            train_data.extend(temp_data)
            train_label.extend(temp_label)
        train_data = self.setting_data(train_data, dim, word_idx)
        train_label = np.array(train_label)
        return train_data, train_label

    def ml(self, label_con, train_data, train_label):

        random.set_seed(50)

        model = models.Sequential()
        model.add(layers.Dense(300, activation='relu'))
        model.add(layers.Dense(50, activation='relu'))

        model.add(layers.Dense(label_con, activation='softmax'))

        opt = optimizers.Adam(learning_rate=0.01)
        loss = losses.sparse_categorical_crossentropy
        model.compile(optimizer=opt, loss=loss, metrics=['accuracy'])

        model.fit(train_data, train_label, epochs=5, batch_size=50)  #
        return model

    def show_similar_candidate(self, target_string, model, dim):
        target = model.predict(self.setting_data([okt.nouns(target_string)], dim, pre.word_idx))
        target = target.squeeze()
        idx = []
        acc = []
        for i in range(len(target)):
            if target[i] > 0.10:
                idx.append(i + 1)
                acc.append(round(target[i] * 100, 2))
        return idx, acc

    def tf_idf_score(self):

        tf_sentences = pre.tf_sentences
        stopwords = pre.stopwords
        t_vec = TfidfVectorizer(max_features=3000, stop_words=stopwords)
        tdm = t_vec.fit_transform(tf_sentences)
        t_vec.get_feature_names_out()
        tf_rank = pd.DataFrame({
            '단어': t_vec.get_feature_names_out(),
            'tf-idf': tdm.sum(axis=0).flat
        })

        return tf_rank.sort_values(by='tf-idf', ascending=False)

    def pred(self,target_string):
        key = okt.nouns(target_string)
        idx, acc = mlc.show_similar_candidate(target_string, model, dim)
        candidate_dict = {idx[i]: acc[i] for i in range(len(idx))}

        for i in key:
            if i not in pre.word_idx.keys():
                key.pop(key.index(i))
        temp = []
        if not key:
            return ['적용된 키워드가 없으므로 다시 검색해 주세요.']
        else:
            # print(f'적용된 키워드: {key}')
            for i in idx:
                x = 0
                cnt = 0
                print()
                for j in range(1, 11):
                    if x == 0:
                        temp.append(f'기호{i}번, {candidate_dict[i]}%')
                        x += 1
            return temp
mlc = ML()
label_con = 4
dim = 1500 # vector dimension
word_idx = pre.word_idx

train_data, train_label = mlc.preprocessing_ml_data(label_con, word_idx,dim=dim)
X_train, X_val, y_train, y_val = train_test_split(train_data,train_label, test_size=0.2,shuffle=True)
model = mlc.ml(label_con,train_data,train_label) # 모델이 리턴됨.
