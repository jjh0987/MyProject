import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
print(tf.__version__)

# gradient
def gradient(f,x):
    h = 1e-4
    grad = np.zeros_like(x)

    for i in range(len(x)):
        tmp_val = x[i]

        x[i] = tmp_val + h
        fxh1 = f(x)
        x[i] = tmp_val - h
        fxh2 = f(x)

        grad[i] = (fxh1 - fxh2)/(2*h)
        x[i] = tmp_val

    return grad

def func2(x): # x input (a,b)
    return x[0]**2 + x[1]**2

gradient(func2,[3.0,4.0]) # 6,8
gradient(func2,[0.0,2.0]) # 0 4
# 손실함수의 값이 낮아지려면 레이블의 값이 가장높고 나머지는 낮아져야 한다. 손실함수의 값이 가장 낮아지는 방향.
# -> 가중치와 편향이 수정되어야 한다.

def gradient_descent(f,init_x,lr,step_num):
    x = init_x
    for i in range(step_num):
        grad = gradient(f,x)
        x -= lr*grad
    return x

gradient_descent(func2,[-3,4],0.1,100)
# 설계 방법 : W의 편미분값으로 loss function 의 변화를 본다.

def softmax(x):
    # input : np.array
    ek = np.exp(x)
    sum_ek = np.sum(ek)
    return ek/sum_ek

def cross_entropy(y,t):
    return -np.sum(t*np.log(y))

def mean_squared(y,t):
    return 0.5*np.sum((y-t)**2)

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3)

    def predict(self,x):
        return np.dot(x,self.W)

    def loss(self,x,t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy(y,t)

        return loss

net = simpleNet()
net.W
x = np.array([0.6,0.9])
p = net.predict(x)
np.argmax(p) # predict value
t = np.array([0,0,1])
net.loss(x,t)

def func(W):
    return net.loss(x,t)
dW = gradient(func,net.W)

def sigmoid(x):
    return 1/(1+np.exp(-x+1e-6))

def Relu(x):
    return np.maximum(0,x)

def softmax(x):
    # input : np.array
    c = np.max(x)
    ek = np.exp(x-c)
    sum_ek = np.sum(ek)
    return ek/sum_ek

def cross_entropy_error(y,t): # batch loss func
    if y.ndim == 1:
        t = t.reshape(1,t.size)
        y = y.reshape(1,y.size)
    batch_size = y.shape[0]
    return -np.sum(t*np.log(y))/batch_size


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

class TwolayerNet:
    def __init__(self,input_size,output_size,weigt_init_std=0.01):
        self.parms = {}
        self.parms['W1'] = np.random.randn(input_size,output_size)*weigt_init_std
        self.parms['b1'] = np.zeros(output_size)

    def predict(self,x): # x:input
        W1 = self.parms['W1']
        b1 = self.parms['b1']

        a1 = np.dot(x,W1) + b1
        z1 = sigmoid(a1) # err
        y = softmax(z1)
        return y

    def loss(self,x,t): # t:answer label
        y = self.predict(x)
        return cross_entropy_error(y,t)

    def accuracy(self,x,t):
        y = self.predict(x)
        y = np.argmax(y,axis=1)
        t = np.argmax(t,axis=1)
        accuracy = np.sum(y==t)/len(x)
        return accuracy

    def numerical_gradient(self,x,t):
        loss_W = lambda W:self.loss(x,t)
        grad = {}

        grad['W1'] = numerical_gradient(loss_W, self.parms['W1'])
        grad['b1'] = numerical_gradient(loss_W, self.parms['b1'])
        grad['W2'] = numerical_gradient(loss_W, self.parms['W2'])
        grad['b2'] = numerical_gradient(loss_W, self.parms['b2'])

        return  grad

net = TwolayerNet(784,10)

(x_train,t_train), (x_test,t_test) = tf.keras.datasets.mnist.load_data(
    path='mnist.npz'
)
x_data = np.reshape(x_train,(60000,784))
y_data = net.predict(x_data)
t_data = np.zeros((60000,10))
for i in range(60000):
    t_data[i][t_train[i]] += 1

train_loss_list = []

num_of_iter = 10
train_size = x_train.shape[0]
batch_size = 100
lr = 0.01
for i in range(num_of_iter):
    batch_mask = np.random.choice(train_size,batch_size)
    x_batch = x_data[batch_mask] # random 100 input data
    t_batch = t_data[batch_mask]

    loss = net.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    grad = net.numerical_gradient(x_batch,t_batch)

    for key in ('W1','b1','W2','b2'):
        net.parms[key] -= lr * grad[key]

    # RuntimeWarning: overflow encountered in exp ?


grad