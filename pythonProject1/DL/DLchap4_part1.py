import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
print(tf.__version__)

# loss function
def mean_sqared(y,t):
    return 0.5 * np.sum((y-t)**2)

def cross_entropy(y,t):
    return -np.sum(t*np.log(y+1e-7))

(x_train,t_train), (x_test,t_test) = tf.keras.datasets.mnist.load_data(
    path='mnist.npz'
) # x:그림, t:정답레이블

x_data = np.reshape(x_train,(60000,784)) # default : (60000,28,28)
# 이후 network 에 집어넣어서 활성화함수와 소프트맥스 출력층을 입힌다. 그러면 길이 10짜리 ndarray와
# one hot label 이랑 교차엔트로피 loss function 을 구한다.
# 손실함수를 줄이기 위해 0으로 가는 기울기를 이용한다.

# make one hot array
t_data = np.zeros((60000,10))
for i in range(60000):
    t_data[i][t_train[i]] += 1

batch_size = 10
batch_mask = np.random.choice(60000,batch_size)

x_batch = x_data[batch_mask]
t_batch = t_data[batch_mask]

def cross_entropy_one_hot(y,t):
    if y.ndim == 1:
        t = t.reshape(1,t.size)
        y = y.reshape(1,y.size)
    batch_size = y.shape[0]
    return -np.sum(t*np.log(y+1e-7)) / batch_size

def forward(f,x):
    h = 10e-50
    return (f(x+h)-f(x))/h
# 소수점 밑 8자리 자동반올림 이슈 있음.

def central(f,x):
    h = 1e-4
    return (f(x+h)-f(x-h))/2*h

def func1(x):
    return 0.01*x**2 + 0.1*x
x = np.arange(0,20,0.1)
y = func1(x)
plt.plot(x,y)

central(func1,10)

def func2(x): # x input (a,b)
    return x[0]**2 + x[1]**2

def func2_round_x0(x0):
    return x0**2 + 4**2
central(func2_round_x0,3)
def func2_round_x1(x1):
    return 3**2 + x1**2
central(func2_round_x1,4)

