# データ作成　保存
import keras
from keras.utils import np_utils
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.preprocessing.image import array_to_img, img_to_array, load_img
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

import os
import re


def list_pictures(directory, ext='jpg|jpeg|bmp|png|ppm'):
    return [os.path.join(root, f)
            for root, _, files in os.walk(directory) for f in files
            if re.match(r'([\w]+\.(?:' + ext + '))', f.lower())]


# 画像一枚、確認
# temp_img = load_img('./dataset1/F0.jpg', target_size=(64,64))
# temp_img_array  = img_to_array(temp_img)
# print(temp_img_array.shape)

X = []
Y = []

for picture in list_pictures('./dataset_true/'):
    img = img_to_array(load_img(picture, target_size=(64,64)))
    X.append(img)
    Y.append(0)

for picture in list_pictures('./dataset_false/'):
    img = img_to_array(load_img(picture, target_size=(64,64)))
    X.append(img)
    Y.append(1)

print(X)
print(Y)
# arrayに変換
X = np.asarray(X)
Y = np.asarray(Y)

# 中身確認
print(type(X))
print(type(Y))

print(X.size)
print(Y.size)
print(len(X))
print(len(Y))
print(X)
print(Y)


# 画素値を0から1の範囲に変換
X = X.astype('float32')
X = X / 255.0

# クラスの形式を変換
Y = np_utils.to_categorical(Y, 2)

# 学習用データとテストデータ
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=111)
print(X_train)

# npz形式へ書き出し
np.savez("dataset.npz",X_train=X_train,X_test=X_test,y_train=y_train,y_test=y_test)

