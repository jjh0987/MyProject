import pdfplumber
from konlpy.tag import Okt
import pandas as pd

path = '/Users/junho/Downloads/open/기호_1 공약.pdf'
pdf = pdfplumber.open(path)
page_len = len(pdf.pages)
first_page = pdf.pages[0]
first_page.extract_text()

okt = Okt()
# input : pdfplumber.open(path)
def tokenization(pdf):
    temp = []
    for page in pdf.pages:
        temp.append(okt.nouns(page.extract_text()))
    return temp

templs = tokenization(pdf)

data = []
non_data = []
for page in templs:
    data += page
    for j in page:
        if len(j) == 1:
            non_data.append(j)
data


df = pd.DataFrame(data=data)
df.value_counts()
non_df = pd.DataFrame(data=non_data)
non_df.value_counts()

df