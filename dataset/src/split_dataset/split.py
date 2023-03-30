
import requests, sys, time, os, argparse, csv
from datetime import date

import random

random.seed(10)

def split(file_name1, file_name2):

    with open(file_name1) as csv_file1, open(file_name2) as csv_file2:
        csv_reader1 = csv.reader(csv_file1, delimiter=',')
        csv_reader2 = csv.reader(csv_file2, delimiter=',')


        trending_list = []
        nontrending_list = []
        mix_list = []

        row_count = 0
        
        for row in csv_reader1:
            if (row_count == 0):
                first_row = row
                row_count += 1
                continue
            
            row_count += 1
            trending_list.append(row)
            mix_list.append(row)
    
        row_count = 0

        for row in csv_reader2:
            if (row_count == 0):
                row_count += 1
                continue
            
            
            row_count += 1
            nontrending_list.append(row)
            mix_list.append(row)


    random.shuffle(mix_list)

    train_num = int(len(mix_list) * 0.8)

    with open("train.csv", "a+", encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(first_row)

        for i in range(train_num):
            csv_writer.writerow(mix_list[i])


    with open("val.csv", "a+", encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(first_row)

        for i in range(train_num, len(mix_list)):
            csv_writer.writerow(mix_list[i])
        

if __name__ == "__main__":

    split("trending_data.csv", "nontrending_data.csv")