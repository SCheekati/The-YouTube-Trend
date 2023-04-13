import requests
import string
from pandas import *
links = read_csv("dataset/output/dataset_mar_23/val.csv")
links = links["thumbnail_link"].tolist()

'''for l in range(0,len(links)):
    img_data = requests.get(links[l]).content
    path = 'CNN/data/validation/'
    file_name = path +"image" + str(l) + ".jpg"
    with open(file_name, 'wb') as handler:
        handler.write(img_data)
'''
