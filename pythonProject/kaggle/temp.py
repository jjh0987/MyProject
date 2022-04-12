import pandas as pd
import seaborn as sns

tweets_path = '/Users/junho/Desktop/data/Bitcoin_tweets.csv'
cut = 200000
temp = pd.read_csv(tweets_path)
temp.sort_values(by='date',inplace=True)
temp.iloc[:200000,:].to_csv('/Users/junho/Downloads/cut.csv')
print(1)

def feature_extract():
    df = pd.read_csv(tweets_path)
    # df.columns
    df.sort_values(by='date')
    # df.info()
    # df.describe()
    df.drop(['user_created','user_location','user_followers','user_friends',
             'user_favourites','user_verified','source','is_retweet'],axis=1,inplace=True)

    return df

def hashtags_df():
    df = feature_extract()
    hashtags = df.loc[:cut,'hashtags']

    hashtags_stack = []
    for i in hashtags:
        try:
            hashtags_stack.extend(eval(i))
        except:
            pass

    hashtags_stack_lower = [i.lower() for i in hashtags_stack]

    from collections import Counter
    counts = Counter(hashtags_stack_lower)

    hashtags_df = pd.DataFrame(data=[counts.values(),counts.keys()]).transpose()
    hashtags_df.sort_values(by=0,ascending=False,inplace=True)

    return hashtags_df


df = feature_extract()
hashtags_df = hashtags_df()
sns.barplot(x=hashtags_df.iloc[:20,0],y=hashtags_df.iloc[:20,1])


hashtags_word_idx = {hashtags_df.iloc[i,1]:hashtags_df.iloc[i,0] for i in range(len(hashtags_df))}
hashtags_word_idx

date_df = pd.DataFrame(df.loc[::-1,'date'])
temp = []
for i in date_df.iloc[:cut,0]:
    temp.append(str(i).split()[0])
date_df = pd.DataFrame(temp)
date_df.describe()
date_df.value_counts() # 데이터 밀림