import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
print(tf.__version__)

a = tf.constant(5)
b = tf.constant(2)
c = tf.constant(3)
d = tf.multiply(a,b)
e = tf.add(c,d)
f = tf.subtract(d,e)
g = a*b
sess = tf.Session()
print()
