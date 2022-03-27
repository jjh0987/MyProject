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
[i.split('•')for i in pdf[0].pages[0].extract_text().split('00')]


pdf[0].pages[0].extract_text().split('\n')
pdf[1].pages[0].extract_text().split('\n')


