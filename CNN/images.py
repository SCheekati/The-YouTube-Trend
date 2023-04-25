import requests
import string
from pandas import *
links = read_csv("dataset/output/dataset_mar_23/train.csv")
labels = links["trending"].tolist()
links = links["thumbnail_link"].tolist()


for l in range(0,len(links)):
    img_data = requests.get(links[l]).content
    path = 'CNN/data/trainall/'
    #if labels[l] == 1:
        #path = 'CNN/data/train/trending/'
    #else:
        #path = 'CNN/data/train/nontrending/'
    print(path)
    file_name = path +"image" + str(l) + ".jpg"
    with open(file_name, 'wb') as handler:
        handler.write(img_data)

