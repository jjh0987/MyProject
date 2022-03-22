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
        self.pdf = [pdfplumber.open(i) for i in pdf_path]

        f = open(self.stopword_path, 'r')
        stop = f.readlines()
        self.stopwords = set(i.rstrip('\n') for i in stop)
        f.close()

    def tokenization(self):
        # okt.nouns(pdfplumber.open(pdf_path[0]).pages[0].extract_text())[0] : 호출 순서
        tokenized_word = []
        for pdf in self.pdf:
            temp = []
            for page in pdf.pages:
                temp.extend(okt.nouns(page.extract_text()))
            tokenized_word.append(temp)
            token = []
            for word in temp:
                if word not in self.stopwords:
                    token.append(word)
        return tokenized_word

stopword_path = '../pycharmProjects/pythonProject/dacon/visualization/data/stopwords_all.txt'
pdf_path = sorted(glob.glob('/Users/junho/Downloads/open/*'))

okt.nouns(pdfplumber.open(pdf_path[0]).pages[0].ti)

pre = preprocessing(stopword_path,pdf_path)
token = pre.tokenization()

pre.tokenization()
pre.stopwords
pre.pdf_path
pre.pdf


def make_clear_sentences(self, candidate_number, stopword_path, drop_len=5):
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

