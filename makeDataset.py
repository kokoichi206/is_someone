# データ作成　保存
import keras
import tensorflow
from keras.utils import np_utils
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.preprocessing.image import array_to_img, img_to_array, load_img
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

import glob

X = []
Y = []

TRUE_DATASET_PATH = "./trimmed/dataset_true/"
FALSE_DATASET_PATH = "./trimmed/dataset_false/"

for picture in glob.glob(TRUE_DATASET_PATH + "*"):
    img = img_to_array(load_img(picture))
    X.append(img)
    Y.append(0)

for picture in glob.glob(FALSE_DATASET_PATH + "*"):
    img = img_to_array(load_img(picture))
    X.append(img)
    Y.append(1)

print(X)
print(Y)
# arrayに変換
X = np.asarray(X)
Y = np.asarray(Y)

# # 中身確認
# print(type(X))
# print(type(Y))

# print(X.size)
# print(Y.size)
print(len(X))
print(len(Y))
# print(X)
# print(Y)


# 画素値を0から1の範囲に変換
X = X.astype('float32')
X = X / 255.0

# クラスの形式を変換
Y = np_utils.to_categorical(Y, 2)

# 学習用データとテストデータ
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=111)
# print(X_train)

# npz形式へ書き出し
np.savez("dataset.npz",X_train=X_train,X_test=X_test,y_train=y_train,y_test=y_test)

