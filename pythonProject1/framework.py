import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
print(tf.__version__)
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
# initializer ?
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(200,activation='sigmoid'),
  tf.keras.layers.Dense(200, activation='relu'),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss=[tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                    'sparse_categorical_crossentropy'],
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10)
model.evaluate(x_test,y_test)
model.summary()

'''
model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              optimizer=tf.keras.optimizers.RMSprop(),
              metrics=['accuracy'])
'''
# opt
# SGD
# RMSprop
# Adam
# Adadelta
# Adagrad
# Adamax
# Nadam
# Ftrl

# BinaryCrossentropy class
# CategoricalCrossentropy class
# SparseCategoricalCrossentropy class
# Poisson class
# binary_crossentropy function
# categorical_crossentropy function
# sparse_categorical_crossentropy function
# poisson function
# KLDivergence class
# kl_divergence function

tf.keras.layers.Maximum()([np.arange(5).reshape(5, 1),np.arange(5, 10).reshape(5, 1)])