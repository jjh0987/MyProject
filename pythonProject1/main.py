import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
hello = tf.constant('hello')
print(hello.numpy())
tf.__version__

def babo(x,y=1,z=0):
    return x+y+z
babo(1,1,1)

x = np.arange(0,6,0.1)
y = np.sin(x)
plt.plot(x,y)