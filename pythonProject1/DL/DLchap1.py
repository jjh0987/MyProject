import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
hello = tf.constant('hello')
print(hello.numpy())
tf.__version__

class Man:
    def __init__(self,name):
        self.name = name
        print('initialized')

    def hello(self):
        print('hello',self.name)

    def bye(self):
        print('bye',self.name)
M = Man('david')
M.hello()
# 넘파이는 기본적으로 각요소별위치 값에 연산이됨.

X = np.array([[51,52],[14,19],[0,4]])
X = X.flatten()
X[np.array([0,2,4])]
X > 15 # bool타입 정답레이블
X[X>15] # 정답 위치값이 나옴

x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1,label = "y = sin(x)")
plt.plot(x,y2,linestyle = '--',label = "y = cos(x)")
plt.legend()