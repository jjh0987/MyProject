import pandas as pd
path = '/Users/junho/Desktop/data/Bitcoin_tweets.csv'
df = pd.read_csv(path)
df.columns
df.sort_values(by='date')
df.info()
df.describe()
df.drop(['user_created','user_location','user_followers','user_friends',
         'user_favourites','user_verified','source','is_retweet'],axis=1,inplace=True)

import nltk
nltk.word_tokenize('i can not')
