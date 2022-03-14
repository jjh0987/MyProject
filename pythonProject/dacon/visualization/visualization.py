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

okt = Okt()
class internal_data():
    def __init__(self):
        pass

    def get_candidate_page_data(self,num):
        path = f'/Users/junho/Downloads/open/기호_{num} 공약.pdf'
        pdf = pdfplumber.open(path)
        temp = [page.extract_text() for page in pdf.pages]
        return temp

    def tokenization(self,pdf):
        temp = []
        for page in pdf.pages:
            temp.extend(okt.nouns(page.extract_text()))
        return temp

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

    def show_simirality(self,sents_clear,target_word):
        model = Word2Vec(sents_clear)
        df = pd.DataFrame(reversed(model.wv.most_similar(target_word)))
        df.set_index(0)

        plt.figure(figsize=(10,6))
        plt.barh(df[0], df[1])
        plt.xlabel('Similarity')
        plt.ylabel('Words')
        plt.title("'청년'의 언어 유사도")
# 전체 후보가 언급한 단어에 대한 시각화 : extend
# 각 후보가 언급한 단어에 대한 시각화 : append
# 2회분량 공약집 내용 변화 시각화 -> 사진 페이지 처리 혹은 다른 pdf 혹은 파일
# 불용어, 복합 명사 처리


cl = internal_data()

show_each = cl.dict_data(14,'each')
show_all = cl.dict_data(14,'all')

word_idx = cl.word_idx_dict_all(14)
word_idx

clean_text = cl.dict_data(14,'all') # 모든 후보,중복 단어
counts = Counter(clean_text)
cl.showWordCloud(counts)

tags_20 = counts.most_common(20)
cl.showGraph(dict(tags_20))


# 기호 1번 샘플
clean_text_each = cl.dict_data(14,'each')
counts_each = [Counter(i) for i in clean_text_each]
counts_each

cl.showWordCloud(counts_each[0],'기호1')
cl.showGraph(dict(counts_each[0].most_common(20)),'기호1')


# 유사도 측정
# input : 번호,stopword path,
# drop_len=5 제거길이 (문장 정규표혀,공백 strip 후 빈문장 혹은 '목표','이행방법' 등의 문장 제거를 위한 단위길이)
sents_clear = cl.make_clear_sentences(2,'/Users/junho/Desktop/stopwords.txt',drop_len=5)
cl.show_simirality(sents_clear,'일자리')

