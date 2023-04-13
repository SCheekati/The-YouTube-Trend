import torch
import numpy as np
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from skimage.io import imread
import requests
import string
import urllib.request
import urllib.error
from pandas import *

training_csv = read_csv("dataset/output/dataset_mar_23/train.csv")
links = training_csv["thumbnail_link"].tolist()
labels = training_csv["trending"].tolist()

training_set = []
training_labels = []
for l in range(0,len(links)):
   print(links[l])
   try:
      image = imread(links[l], as_gray=True)
      image /= 255.0
      image = image.astype('float32')
      training_set.append(image)
      training_labels.append(labels[l])
   except urllib.error.HTTPError as err:
      print("image not found")
   


train_x = np.array(training_set)
print(train_x.shape)

