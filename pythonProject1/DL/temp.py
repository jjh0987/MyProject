import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
print(tf.__version__)

(x_train,t_train), (x_test,t_test) = tf.keras.datasets.mnist.load_data(
    path='mnist.npz'
)
x_data = np.reshape(x_train,(60000,784))
t_data = np.zeros((60000,10))
for i in range(60000):
    t_data[i][t_train[i]] += 1

def sigmoid(x):
    return 1/(1+np.exp(-x))
def softmax(x):
    # input : np.array
    c = np.max(x)
    ek = np.exp(x-c)
    sum_ek = np.sum(ek)
    return ek/sum_ek
def mean_squared(y,t):
    return 0.5*np.sum((y-t)**2)
def _numerical_gradient_no_batch(f, x):
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)  # x와 형상이 같은 배열을 생성

    for idx in range(x.size):
        tmp_val = x[idx]

        # f(x+h) 계산
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)

        # f(x-h) 계산
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val  # 값 복원

    return grad
def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)

        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)

        return grad

def func(x):
    return np.sum(x**2)
numerical_gradient(func,np.array([[1.,2.],[2.,3.]]))

class TwolayerNet:
    def __init__(self, input_size, hidden_size, output_size, weigt_init_std=0.01):
        self.parmsW1 = np.random.randn(input_size, hidden_size) * weigt_init_std
        self.parmsb1 = np.zeros(hidden_size)
        self.parmsW2 = np.random.randn(hidden_size, output_size) * weigt_init_std
        self.parmsb2 = np.zeros(output_size)

    def predict(self,x): # x:input
        W1,W2 = self.parmsW1,self.parmsW2
        b1,b2 = self.parmsb1,self.parmsb2

        a1 = np.dot(x,W1) + b1
        z1 = sigmoid(a1) # err
        a2 = np.dot(z1,W2) + b2
        y = softmax(a2)
        return y

net = TwolayerNet(784,100,10)

def loss(x,t): # t:answer label
    y = net.predict(x)
    return mean_squared(y,t)


train_loss_list = []
num_of_iter = 1
train_size = x_train.shape[0]
batch_size = 100
lr = 0.01
for i in range(num_of_iter):
    batch_mask = np.random.choice(train_size,batch_size)
    x_batch = x_data[batch_mask] # random 100 input data
    t_batch = t_data[batch_mask]

    loss = loss(x_batch, t_batch)
    train_loss_list.append(loss)

    grad = numerical_gradient(loss,net.parmsW1)