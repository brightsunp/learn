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
batch_size = 16

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

# 1. Default: strides = 1
fashion_model = Sequential()
fashion_model.add(Conv2D(16, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(image_size, image_size, 1)))
fashion_model.add(Conv2D(16, (3, 3), activation='relu'))
fashion_model.add(Flatten())
fashion_model.add(Dense(128, activation='relu'))
fashion_model.add(Dense(num_classes, activation='softmax'))

fashion_model.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])
fashion_model.fit(x, y, batch_size=batch_size, epochs=3, validation_split=0.2)
'''
Output:

Train on 48000 samples, validate on 12000 samples
Epoch 1/3
48000/48000 [==============================] - 136s 3ms/step - loss: 0.4042 - acc: 0.8538 - val_loss: 0.3382 - val_acc: 0.8769
Epoch 2/3
48000/48000 [==============================] - 140s 3ms/step - loss: 0.2539 - acc: 0.9065 - val_loss: 0.2556 - val_acc: 0.9115
Epoch 3/3
48000/48000 [==============================] - 142s 3ms/step - loss: 0.1841 - acc: 0.9316 - val_loss: 0.2568 - val_acc: 0.9121
'''

# 2. Set: strides = 2
fashion_model_1 = Sequential()
fashion_model_1.add(Conv2D(16, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(image_size, image_size, 1)))
fashion_model_1.add(Conv2D(16, (3, 3), activation='relu', strides=2))
fashion_model_1.add(Flatten())
fashion_model_1.add(Dense(128, activation='relu'))
fashion_model_1.add(Dense(num_classes, activation='softmax'))

fashion_model_1.compile(optimizer='adam',
                        loss='categorical_crossentropy',
                        metrics=['accuracy'])
fashion_model_1.fit(x, y, batch_size=batch_size, epochs=3, validation_split=0.2)
'''
Output:

Train on 48000 samples, validate on 12000 samples
Epoch 1/3
48000/48000 [==============================] - 48s 1000us/step - loss: 0.4247 - acc: 0.8470 - val_loss: 0.3516 - val_acc: 0.8708
Epoch 2/3
48000/48000 [==============================] - 45s 937us/step - loss: 0.2847 - acc: 0.8945 - val_loss: 0.2994 - val_acc: 0.8964
Epoch 3/3
48000/48000 [==============================] - 51s 1ms/step - loss: 0.2272 - acc: 0.9162 - val_loss: 0.2773 - val_acc: 0.8996
'''
