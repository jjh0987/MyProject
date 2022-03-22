############################# 공약집의 모든 텍스트 크롤링
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

def tokenization(pdf):
    temp_token = [[page.extract_text()] for page in pdf.pages]
    
    return temp_token

def promise10(num_of_candidate):

    candidate_text = []
    candidate = []
    policy = ['공약순위 1', '공약순위 2', '공약순위 3', '공약순위 4', '공약순위 5',
            '공약순위 6', '공약순위 7', '공약순위 8', '공약순위 9', '공약순위 10']
    for number in range(1, num_of_candidate+1):
        path = f'/Users/junho/Downloads/open/기호_{number} 공약.pdf'
        pdf = pdfplumber.open(path)
        temp_1list = sum(tokenization(pdf),[])
        temp_text = ''.join(temp_1list)
        temp_text = ' '.join(temp_text.splitlines())
        text_space = []

        for num in range(1,11):
            if num != 10:
                premise_text = temp_text[temp_text.find(f'공약순위 {num}')+9 :temp_text.find(f'공약순위 {num + 1}', temp_text.find(f'공약순위 {num}'))]
            else:
                premise_text = temp_text[temp_text.find(f'공약순위 {num}')+9 :temp_text.rfind(f'기호 {number}')]

            if '\n' in premise_text:
                premise_text = ' '.join(premise_text.splitlines())

            premise_text = premise_text.strip(f'기호 {number}')

            text_space.append(premise_text)

        candidate_text.append(text_space)
        candidate.append(f'기호_{number}')

    premise10 = pd.DataFrame(candidate_text, index = candidate, columns = policy)

    return premise10


import os
######################################## 공약 제목만 크롤링

def promise10(num_of_candidate):
    if os.path.isfile('self.path'):      ### promise10.csv 파일이 있는지 확인
        print('해당 파일이 이미 존재합니다.')
    else:
        candidate_text = []
        candidate = []
        policy = ['공약순위 1', '공약순위 2', '공약순위 3', '공약순위 4', '공약순위 5',
                '공약순위 6', '공약순위 7', '공약순위 8', '공약순위 9', '공약순위 10']
        for number in range(1, num_of_candidate+1):
            path = f'/Users/junho/Downloads/open/기호_{number} 공약.pdf'
            pdf = pdfplumber.open(path)
            temp_1list = sum(tokenization(pdf),[])
            temp_text = ''.join(temp_1list)
            text_space = []
            
            if number != 12 and number != 14:
                for num in range(1,11):
                    premise_text = temp_text[temp_text.find(f'공약순위 {num}')+9 :temp_text.find('\n목', temp_text.find(f'공약순위 {num}'))]
                    if '\n' in premise_text:
                        premise_text = ''.join(premise_text.splitlines())
                        
                    if f'기호 {number}' in premise_text:
                        premise_text = premise_text[:premise_text.find(f'기호 {number}')]
                    text_space.append(premise_text)
                    
                candidate_text.append(text_space)
            else:
                for num in range(1,11):
                    premise_text = temp_text[temp_text.find(f'공약순위 {num}')+9 :temp_text.find('\n', temp_text.find(f'공약순위 {num}'))]
                    if '\n' in premise_text:
                        premise_text = ''.join(premise_text.splitlines())
                    text_space.append(premise_text)
                candidate_text.append(text_space)
            candidate.append(f'기호_{number}')
            
        premise10 = pd.DataFrame(candidate_text, index = candidate, columns = policy)

        return premise10
content = promise10(14)
content
################################# k-means 전처리

    def preprocessed_promise10(self, text):
        df = pd.read_csv(text) # 14 by 10
        arr = df.values.tolist()

        okt = Okt()

        temp = []
        for txtls in arr:
            txtls.pop(0)
            text = word_tokenize(' '.join(txtls))
            temp.append(okt.nouns(str(text)))

        text = temp

        f = open('stopwords.txt', 'r')
        lines = f.readlines()
        stopwords = []

        for line in lines:
            line = line.replace('\n', '')
            stopwords.append(line)
        f.close()

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

        clean_text = storage

        #문장 벡터화
        vectorize = CountVectorizer()
        x = vectorize.fit_transform(clean_text)

        ######### K-means 분석 ###########
        #데이터 프레임 생성 (문장 단어 매트릭스 만들기)
        new_df = pd.DataFrame(x.toarray(), columns=vectorize.get_feature_names_out())