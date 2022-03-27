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


class preprocessing:

    def __init__(self,stopword_path,pdf_path):
        self.stopword_path = stopword_path
        self.pdf_path = pdf_path
        self.pdf_files = [pdfplumber.open(i) for i in pdf_path]

        f = open(self.stopword_path, 'r')
        stop = f.readlines()
        self.stopwords = set(i.rstrip('\n') for i in stop)
        f.close()
        self.clear_sentences,self.top10 = self.make_clear_sentences() # 원본: 역추적용

    def tokenization(self):
        # okt.nouns(pdfplumber.open(pdf_path[0]).pages[0].extract_text())[0] : 호출 순서
        tokenized_word = []
        for pdf in self.pdf_files:
            temp = []
            for page in pdf.pages:
                temp.extend(okt.nouns(page.extract_text()))
            token = []
            for word in temp:
                if word not in self.stopwords:
                    token.append(word)
            tokenized_word.append(token)
        return tokenized_word

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

    # def stopword_re(self):

stopword_path = '../pycharmProjects/pythonProject/dacon/visualization/data/stopwords_all.txt'
pdf_path = sorted(glob.glob('/Users/junho/Downloads/pdf/*'))

pre = preprocessing(stopword_path,pdf_path)
token = pre.tokenization()
len(token[0])

pre.stopwords
pre.pdf_path
pre.top10
pre.clear_sentences

top10 = pre.top10
okt.nouns(top10[0][0])

clear = [pre.pdf[0].pages[0].extract_text().split('\n')]
clear

