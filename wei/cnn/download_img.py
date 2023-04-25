import requests
import string
import pandas as pd
import os

links = pd.read_csv("../new_val.csv")

img_id = links["video_id"].tolist()
labels = links["trending"].tolist()
links = links["thumbnail_link"].tolist()

count = 0
with open('val_list.txt', 'w') as f:

    for l in range(len(links)):
        res = requests.get(links[l])
        if res.status_code != 200:
            print('no image')
            continue
        img_data = res.content
        
        path = 'val_image/'
        file_name = path + img_id[l] + ".png"
        with open(file_name, 'wb') as handler:
            handler.write(img_data)

        f.write(img_id[l] + ' ' + str(labels[l]) + '\n')
        count += 1

print(count)
