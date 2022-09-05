import pandas as pd
import numpy as np

from glob import glob
from tqdm import tqdm
from scipy import interpolate

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, GRU, AveragePooling1D, GlobalAveragePooling1D, Dropout, Conv1D
w_list = sorted(glob("C:/Users/User/Downloads/competition_data/water_data/*.csv"))
w_list
r_list = sorted(glob("C:/Users/User/Downloads/competition_data/rf_data/*.csv"))
r_list

# setting train
train_data = []
train_label = []
num = 0

# tp1 = pd.read_csv(w_list[0])
# tp1.columns
# tp2 = pd.read_csv(r_list[0])
# tp2.columns
# pd.merge(tp1,tp2,how='inner',on='ymdhm')

for i in range(10):

    tmp1 = pd.read_csv(w_list[i])
    tmp2 = pd.read_csv(r_list[i])

    tmp = pd.merge(tmp1,tmp2,how='inner',on='ymdhm')

    tmp['rain_mean'] = [tmp.loc[j,['rf_10184100','rf_10184110','rf_10184140']].mean() for j in range(len(tmp))]
    tmp = tmp.replace(" ", np.nan)
    tmp = tmp.interpolate(method='values')
    tmp = tmp.fillna(0)

    for j in tqdm(range(len(tmp) - 432)):
        train_data.append(np.array(tmp.loc[j:j + 431, ['swl','inf','sfw',
                                                       "tototf",

                                                       "fw_1018662", "fw_1018680",
                                                       "fw_1018683", "fw_1019630"]]).astype(float))

        train_label.append(np.array(tmp.loc[j + 432, ["wl_1018662", "wl_1018680",
                                                      "wl_1018683", "wl_1019630"]]).astype(float))

train_data = np.array(train_data)
train_label = np.array(train_label)

tmp['inf'].mean()
# setting test
test_data = []
test_label = []
tmp1 = pd.read_csv(w_list[-1])
tmp2 = pd.read_csv(r_list[-1])
tmp = pd.merge(tmp1,tmp2,how='inner',on='ymdhm')
tmp['rain_mean'] = [tmp.loc[j, ['rf_10184100', 'rf_10184110', 'rf_10184140']].mean() for j in range(len(tmp))]
tmp = tmp.replace(" ", np.nan)
# 이전값을 사용
tmp = tmp.fillna(method='pad')
tmp = tmp.fillna(0)

tmp.loc[:, ["wl_1018662", "wl_1018680", "wl_1018683", "wl_1019630"]] = tmp.loc[:, ["wl_1018662", "wl_1018680", "wl_1018683", "wl_1019630"]]*100

for j in tqdm(range(4032, len(tmp) - 432)):
    test_data.append(np.array(tmp.loc[j:j + 431, ['swl','inf','sfw',
                                                  "tototf",

                                                  "fw_1018662", "fw_1018680",
                                                  "fw_1018683", "fw_1019630"]]).astype(float))

    test_label.append(np.array(tmp.loc[j + 432, ["wl_1018662", "wl_1018680",
                                                 "wl_1018683", "wl_1019630"]]).astype(float))

test_data = np.array(test_data)
test_label = np.array(test_label)



# # setting model
# input_shape = (train_data[0].shape[0], train_data[0].shape[1])
# model = Sequential()
# model.add(AveragePooling1D(input_shape=input_shape))
# model.add(LSTM(256)) # input_shape=input_shape
# # model.add(GRU(32,return_sequences=False)) # input_shape=input_shape
# model.add(Dense(4, activation = 'relu'))
#
# optimizer = tf.optimizers.Adam(0.0005)
# model.compile(optimizer=optimizer,loss='mse', metrics=['mae'])
# model.fit(train_data, train_label, epochs=10, batch_size=128)
#
#
# pred = model.predict(test_data)
#
# pred = pd.DataFrame(pred)
#
# sample_submission = pd.read_csv("/Users/junho/Downloads/competition_data/sample_submission.csv")
#
# sample_submission["wl_1018662"] = pred[0]
# sample_submission["wl_1018680"] = pred[1]
# sample_submission["wl_1018683"] = pred[2]
# sample_submission["wl_1019630"] = pred[3]
# sample_submission.to_csv("/Users/junho/Downloads/competition_data/submission.csv", index = False)
# print(1)