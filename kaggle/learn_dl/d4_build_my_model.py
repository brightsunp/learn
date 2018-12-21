#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/21'
'''

import numpy as np
from tensorflow import keras
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Flatten, Conv2D

image_size = 28
num_classes = 10

def prep_data(raw):
    y = raw[:, 0]
    out_y = keras.utils.to_categorical(y, num_classes)
    image_nums = raw.shape[0]
    x = raw[:, 1:]
    out_x = x.reshape(image_nums, image_size, image_size, 1)
    out_x /= 255
    return out_x, out_y

fashion_file = '../datasets/fashion/fashion-mnist_train.csv'
fashion_data = np.loadtxt(fashion_file, skiprows=1, delimiter=',')
x, y = prep_data(fashion_data)

# 1. Specify and Compile
fashion_model = Sequential()
# first layer
fashion_model.add(Conv2D(
    filters=12,
    activation='relu',
    kernel_size=3,
    input_shape=(image_size, image_size, 1)
))
# remaining layers
fashion_model.add(Conv2D(20, activation='relu', kernel_size=3))
fashion_model.add(Conv2D(20, activation='relu', kernel_size=3))
fashion_model.add(Flatten())
fashion_model.add(Dense(100, activation='relu'))
fashion_model.add(Dense(num_classes, activation='softmax'))
# compile
fashion_model.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

# 2. Fit the model
fashion_model.fit(x, y, batch_size=100, epochs=4, validation_split=0.2)
'''
Output:

Train on 48000 samples, validate on 12000 samples
Epoch 1/4
48000/48000 [==============================] - 94s 2ms/step - loss: 0.4695 - acc: 0.8294 - val_loss: 0.3664 - val_acc: 0.8697
Epoch 2/4
48000/48000 [==============================] - 98s 2ms/step - loss: 0.2984 - acc: 0.8929 - val_loss: 0.2898 - val_acc: 0.8959
Epoch 3/4
48000/48000 [==============================] - 96s 2ms/step - loss: 0.2436 - acc: 0.9099 - val_loss: 0.2667 - val_acc: 0.9056
Epoch 4/4
48000/48000 [==============================] - 83s 2ms/step - loss: 0.2042 - acc: 0.9249 - val_loss: 0.2565 - val_acc: 0.9088
'''
