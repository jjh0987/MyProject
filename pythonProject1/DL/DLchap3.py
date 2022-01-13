# Activate function

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
print(tf.__version__)

def step(x):
    if x>0:
        return 1
    else:
        return 0

def step1(x):
    y = x>0
    return y.astype(np.int)

x = np.arange(-5,5,0.1)
y = step1(x)
plt.plot(x,y)

def sigmoid(x):
    return 1/(1+np.exp(-x))

z = sigmoid(x)
plt.plot(x,z)

def relu(x):
    return np.maximum(0,x)

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
np.dot(A,B) # 행렬곱 , shape이 맞아야한다

x = np.array([1,0.5])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])

A1 = np.dot(x,W1) + B1
Z1 = sigmoid(A1) # 1x3

W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2 = np.array([0.1,0.2])

A2 = np.dot(Z1,W2) + B2
Z2 = sigmoid(A2)

def softmax(x):
    # input : np.array
    c = np.max(x)
    ek = np.exp(x-c)
    sum_ek = np.sum(ek)
    return ek/sum_ek
v = softmax(x)
sum(v) # 함수자체가 평균을내는것이므로 합은 1이 나옴. : 확률로 해석가능.


(x_train,t_train), (x_test,t_test) = tf.keras.datasets.mnist.load_data(
    path='mnist.npz'
) # t 정답레이블

from PIL import Image

img = x_train[0]
label = t_train[0]
def img_show(img):
    number_image = Image.fromarray(img)
    number_image.show()

img_show(img) # 5 image

def predict(x):
    W1 = np.zeros([784,100]) + 0.01
    W2 = np.zeros([100,50]) + 0.001
    W3 = np.zeros([50,10]) + 0.001

    a1 = np.dot(x,W1)
    z1 = sigmoid(a1)

    a2 = np.dot(z1,W2)
    z2 = sigmoid(a2)

    a3 = np.dot(z2,W3)
    y = softmax(a3)

    return y

array = np.empty((100,784))
array = np.append(array,np.zeros(784),axis=0)


acc_cnt = 0
for i in range(len(x_test)):
    y = predict(np.ndarray.flatten(x_train[i]))
    p = np.argmax(y) # (10,1) 에서 가장큰값
    if p == t_test[i]:
        acc_cnt += 1

print(str(float(acc_cnt)/len(x_test)))

# batch 배치모양이 안나옴 넘파이 배열공부

accuracy = 0
batch_size = 100
for i in range(0,len(x_train),batch_size):
    x_batch = array[i:i+batch_size]
    y_batch = predict(x_batch)
    p = np.argmax(y_batch,axis=1)
    accuracy += np.sum(p == t_test[i:i+batch_size])