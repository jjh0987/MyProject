import pandas as pd
import seaborn as sns
import glob
root_path = '/Users/junho/Desktop/data/coin/'
coin_csv_path = sorted(glob.glob(root_path+'price/*'))
btc_path = coin_csv_path[0]


def price_365(path):
    temp = pd.read_csv(path)
    temp = temp.iloc[::-1,:]
    return temp.iloc[:365,:]

def price_graph(df):
    df = df.iloc[::-1,:]
    labels = ['2021-04','2021-06',
              '2021-08','2021-10','2021-12',
              '2022-02','2022-04']
    fig = sns.lineplot(x=df.loc[:,'Date'],y=df.loc[:,'Close'])
    fig.set_xticks(range(-1,len(df),60))
    fig.set_xticklabels(labels)
    fig.set_xlabel('Month')
    fig.set_ylabel('USD')

price_graph(price_365(btc_path))


df = price_365(btc_path)
df = df.reset_index()
df = df.drop('index',axis=1)
df['price'] = (df['Close']-df['Open']>0)

temp = [int(i) for i in df.loc[:,'price']]
df['price'] = temp

label_df = df.loc[:,['Date','price']]
label_df