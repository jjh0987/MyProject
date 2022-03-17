import pdfplumber
from konlpy.tag import Okt,Komoran
import pandas as pd

import re
okt = Okt()


def tokenization(pdf):
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
def dict_data(num_of_candidate, method, stopword_path):
    candidate_text = []

    for num in range(1, num_of_candidate + 1):
        path = f'/Users/junho/Downloads/open/기호_{num} 공약.pdf'  # glob 이용 으로 은닉
        pdf = pdfplumber.open(path)
        if method == 'append':
            candidate_text.append(tokenization(pdf))
        elif method == 'extend':
            candidate_text.extend(tokenization(pdf))
    return candidate_text

# 호출형식 pdf.pages[0].extract_text()
# type(okt.nouns(pdf.pages[0].extract_text())) : list
# input : pdfplumber.open(path)


# 필요사항 : non_data dict


def idx_word_dict_all(num_of_candidate):
    df = pd.DataFrame(data=dict_data(num_of_candidate, 'extend'))
    token_set = df.value_counts() # : series
    word_idx = {i+1:token_set.index[i][0] for i in range(len(token_set))}
    return word_idx



# 전체 후보가 언급한 단어에 대한 시각화 : extend
# 각 후보가 언급한 단어에 대한 시각화 : append
word_idx = idx_word_dict_all(14)


import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from matplotlib import font_manager, rc

clean_text_reshaped = dict_data(14,'extend') # 모든 후보
len(clean_text_reshaped)
counts = Counter(clean_text_reshaped)
len(counts)
counts


def showWordCloud(text_counts, person=None):
    tags = text_counts.most_common(100)

    wc = WordCloud(font_path='/Users/junho/Downloads/나눔고딕/NanumGothic.ttf', background_color='white', max_font_size=60)
    cloud = wc.generate_from_frequencies(dict(tags))

    plt.figure(figsize=(10, 8))
    plt.title(f'{person} keywords', size=20)
    plt.axis('off')
    plt.imshow(cloud)


showWordCloud(counts)


def showGraph(tags, person=None):
    #font_location = '/Users/junho/Downloads/나눔고딕/NanumGothic.ttf'
    #font_name = font_manager.FontProperties(fname=font_location).get_name()
    rc('font', family='AppleGothic')
    plt.rcParams['axes.unicode_minus'] = False  # 한글화 경우, 마이너스 깨짐 방지.

    plt.figure(figsize=(10, 5))
    plt.xlabel('keyword')
    plt.grid(True)

    Dict_Values = tags.values()
    Dict_Keys = tags

    plt.title(f'{person} keyword top 20', size=20)
    plt.bar(range(len(tags)), Dict_Values, align='center')
    plt.xticks(range(len(tags)), list(Dict_Keys), rotation='70')


tags_20 = counts.most_common(20)
showGraph(dict(tags_20))

# 키워드별 예산 추정치
# 불용어, 복합명사 - 나연
# 공약,정책 labeling - 선종
# 후보자 이름 유사도 - 준호

# project : 제목으로만 보는 언론사 분류기
# 크롤링을 통해 언론사 data,레이블 작성
# 언론사 성향 분석

from gensim.models import word2vec


komoran = Komoran(userdic='/Users/junho/Downloads/uesr-dict.txt')

def tokenization(file):
    temp = []
    text = f.read()
    temp.append(komoran.nouns(text))
    return temp

f = open('/Users/junho/Downloads/stopwords(1).txt', 'r')
lines = f.readlines()
stopwords = []
for line in lines:
    line = line.replace('\n', '')
    stopwords.append(line)
f.close()

stopwords

def preprocessing(text):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    text = hangul.sub('', str(text))
    tokens = komoran.morphs(text)

    stop = stopwords
    tokens = [token for token in tokens if token not in stop]

    return tokens

def get_candidate_page_data(num):
    path = f'/Users/junho/Downloads/open/기호_{num} 공약.pdf'
    pdf = pdfplumber.open(path)
    temp = [page.extract_text() for page in pdf.pages]
    return temp
temp = get_candidate_page_data(1)
token = preprocessing(temp)

def make_clear_sentences(candidate_number,stopword_path,drop_len=5):
    temp = get_candidate_page_data(candidate_number)  # input : number of candidate
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

temp = get_candidate_page_data(1) # input : number of candidate

clear = [i.split('\n') for i in temp]
clear
clear[0][10]

hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
clear_cen = []
for candidate in clear:
    for cen in candidate:
        clear_cen.append(hangul.sub('', str(cen)))
clear_cen
temp = [i.strip() for i in clear_cen]

cen = []
for i in temp:
    if len(i) > 5:
        cen.append(i)
cen
'''
f = open('/Users/junho/Downloads/공약_2022/기호_01 공약.txt','r')
lines = f.readlines()
f.close()
sen = [i.rstrip('\n') for i in lines]

sents = [list(okt.nouns(i)) for i in sen] # 붙인 텍스트 이용
'''

f = open('/Users/junho/Downloads/stopwords.txt','r')
stop = f.readlines()
f.close()
stopwords = set(i.rstrip('\n') for i in stop)
sents = [list(okt.nouns(i)) for i in cen] # 원본

sents_clear = []
for sent in sents:
    temp = []
    for word in sent:
        if word not in stopwords:
            temp.append(word)
    sents_clear.append(temp)

sents_clear = make_clear_sentences(1,'/Users/junho/Desktop/stopwords.txt',drop_len=4)
from gensim.models import Word2Vec
model = Word2Vec(sents_clear)
model.wv.most_similar('청년')


# 원본 + 후보 2명 stopword
# 전체원본 + 전체 stopword
path = '/Users/junho/Desktop/pycharmProjects/pythonProject/dacon/visualization/data/promise10.csv'
df = pd.read_csv(path)
# label = [경제,안보,환경,복지,교육,보건,주거]
df = df.rename(columns=df.columns)
df = df.set_index('Unnamed: 0')



