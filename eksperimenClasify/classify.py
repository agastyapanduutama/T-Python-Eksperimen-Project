#!/usr/bin/python3
import numpy as np
from PIL import Image as gambar
import os
import sys
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
# import json

pathModel = "/home/pandu/Documents/eksperimen/model/16jun21.h5"
# pathImage = "/opt/lampp/htdocs/backend/upload/images"

model = tf.keras.models.load_model(pathModel)
# model.summary()
input_size = (96, 96)
channel = (3,)
input_shape = input_size + channel
labels = ['1', '2', '3', '4', '5', '6', '7']


def preprocess(img, input_size):
    nimg = img.convert('RGB').resize(input_size, resample=0)
    img_arr = (np.array(nimg))/255
    return img_arr


def reshape(imgs_arr):
    return np.stack(imgs_arr, axis=0)

# frameGet = sys.argv[1]

def predict():
    im = gambar.open("/home/pandu/Documents/eksperimen/image/download.png")
    X = preprocess(im, input_size)
    X = reshape([X])
    y = model.predict(X)
    label = labels[np.argmax(y)]
    akurasi = np.max(y)

    hasil = {
        "keterangan": label,
        "nilaiAkurat": akurasi
    }

    return hasil


print(predict())
