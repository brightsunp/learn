#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2018/12/18'
'''

import os
import numpy as np
# from IPython.display import Image, display
import matplotlib.pyplot as plt
from decode_predictions import decode_predictions
from tensorflow.python.keras.applications import ResNet50
from tensorflow.python.keras.applications.resnet50 import preprocess_input
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array


def read_and_prep_images(img_paths):
    '''read and prepare images'''
    image_size = 224
    imgs = [load_img(img_path, target_size=(image_size, image_size))
            for img_path in img_paths]
    img_array = np.array([img_to_array(img) for img in imgs])
    return preprocess_input(img_array)


def is_hot_dog(predictions):
    '''convert predictions to [True, False, ...]'''
    decoded_preds = decode_predictions(predictions, top=1)
    labels = [d[0][1] for d in decoded_preds]
    return [l=='hotdog' for l in labels]


def calc_accuracy(model, paths_to_hotdog_images, paths_to_other_images):
    '''evaluate model accuracy'''
    pos_preds = model.predict(read_and_prep_images(paths_to_hotdog_images))
    neg_preds = model.predict(read_and_prep_images(paths_to_other_images))
    # Summing list of binary variables gives a count of True values
    correct_count = sum(is_hot_dog(pos_preds)) + (len(neg_preds)-sum(is_hot_dog(neg_preds)))
    total_count = len(pos_preds) + len(neg_preds)
    return correct_count / total_count


image_dir = '../datasets/seefood/train'
hot_dog_paths = [os.path.join(image_dir, 'hot_dog', filename)
                 for filename in ['1000288.jpg', '127117.jpg']]
not_hot_dog_paths = [os.path.join(image_dir, 'not_hot_dog', filename)
                     for filename in ['823536.jpg', '99890.jpg']]
image_paths = hot_dog_paths + not_hot_dog_paths

my_model = ResNet50(weights='../datasets/ResNet-50/resnet50_weights_tf_dim_ordering_tf_kernels.h5')
test_imgs = read_and_prep_images(image_paths)
preds = my_model.predict(test_imgs)
decoded = decode_predictions(preds, top=3)

for i, image_path in enumerate(image_paths):
    plt.imshow(plt.imread(image_path))
    plt.show()
    print(decoded[i])

# calculate accuracy on small dataset as a test
my_model_accuracy = calc_accuracy(my_model, hot_dog_paths, not_hot_dog_paths)
print("Fraction correct in small test set: {}".format(my_model_accuracy))

# similarly:
# from tensorflow.python.keras.applications import VGG16
# vgg16_model = VGG16(weights='../datasets/vgg16/vgg16_weights_tf_dim_ordering_tf_kernels.h5')
# vgg16_accuracy = calc_accuracy(vgg16_model, hot_dog_paths, not_hot_dog_paths)
# print("Fraction correct in small dataset: {}".format(vgg16_accuracy))
