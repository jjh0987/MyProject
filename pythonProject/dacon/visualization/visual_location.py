
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
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


okt = Okt()
pdf_loc_path = sorted(glob.glob('../pycharmProjects/pythonProject/dacon/visualization/data/pdf_location/*'))
pdf_loc_path

pdf = [pdfplumber.open(file) for file in pdf_loc_path]
pdf[0].pages

# 기호1
import re
temp = []
for i in range(17):
    temp.extend(re.split('지역별 핵심공약', pdf[0].pages[i].extract_text()))

temp = [temp[i] for i in range(1,35,2)]
temp


ans = []
for doc in temp:
    loc = []
    for sen in re.split('[0-1]\d\d\d',doc):
        loc.append(sen.replace('   ', '\n').lstrip('\n'))
    ans.append(loc)
ans[4]

process = []
for i in ans:
    temp = []
    for j in i:
        temp.append(j.split('\n')[0].lstrip().split('•')[0])
    process.append(temp)
process



# 기호2 df
pdf[1].pages[0].extract_text().split('\n')

columns = []
candidate_2 = []
for i in range(len(pdf[2].pages)):
    for j in pdf[2].pages[i].extract_text().split('\n'):
        if len(j) == 2:
            columns.append(j)
        else:
            if j[0] != '■':
                temp = []
            else:
                temp.append(j[2:])
                if len(temp) == 7:
                    candidate_2.append(temp)
len(candidate_2)

df = pd.DataFrame(data=candidate_2)
df = df.transpose()
df.columns = columns
df


# 기호4
