#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/20'
'''

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.applications import ResNet50
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.applications.resnet50 import preprocess_input
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator

# 1. Specify and Compile
num_classes = 2
my_new_model = Sequential()
my_new_model.add(ResNet50(include_top=False, pooling='avg',
                          weights='../datasets/ResNet-50/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5'))
my_new_model.add(Dense(num_classes, activation='softmax'))
# first layer: ResNet50 (already trained)
my_new_model.layers[0].trainable = False
my_new_model.compile(optimizer='sgd',
                     loss='categorical_crossentropy',
                     metrics=['accuracy'])

# 2. Fit the model
image_size = 224
data_generator = ImageDataGenerator(preprocess_input)
train_generator = data_generator.flow_from_directory(
    directory='../datasets/dogs/train',
    target_size=(image_size, image_size),
    batch_size=10,
    class_mode='categorical'
)
val_generator = data_generator.flow_from_directory(
    directory='../datasets/dogs/val',
    target_size=(image_size, image_size),
    class_mode='categorical'
)
fit_stats = my_new_model.fit_generator(train_generator,
                                       steps_per_epoch=3,
                                       validation_data=val_generator,
                                       validation_steps=1)
'''
Output:

Found 220 images belonging to 2 classes.
Found 217 images belonging to 2 classes.
Epoch 1/1

1/3 [=========>....................] - ETA: 9s - loss: 0.9247 - acc: 0.3000
2/3 [===================>..........] - ETA: 3s - loss: 0.8865 - acc: 0.3500
3/3 [==============================] - 16s 5s/step - loss: 0.7288 - acc: 0.5333 - val_loss: 1.1720 - val_acc: 0.5312
'''
