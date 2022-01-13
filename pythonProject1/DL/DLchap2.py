# Socket

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
print(tf.__version__)

# 0 0 0 1
def AND(x1,x2):
    w1,w2,theta = 0.5,0.5,0.7
    tmp = x1*w1+x2*w2
    if tmp <= theta:
        return 0
    else:
        return 1

print(AND(0,0),
AND(0,1),
AND(1,0),
AND(1,1))

# 1 1 1 0
def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# 0 1 1 1
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# 0 1 1 0
def XOR(x1,x2):
    temp1 = NAND(x1,x2)
    temp2 = OR(x1,x2)
    return AND(temp1,temp2)

