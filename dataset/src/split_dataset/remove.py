
import requests, sys, time, os, argparse, csv
from datetime import date


def rm(file_name1, file_name2):

    id_set = set()

    with open(file_name1) as csv_file, open("trending_data.csv", "a+", encoding='utf-8') as f:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_writer = csv.writer(f)

        row_count = 0

        for row in csv_reader:
            if (row_count == 975 or row_count == 2134):
                pass
            else:
                csv_writer.writerow(row)

            row_count += 1

    with open(file_name2) as csv_file, open("nontrending_data.csv", "a+", encoding='utf-8') as f:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_writer = csv.writer(f)

        row_count = 0

        for row in csv_reader:
            if (row_count == 975 or row_count == 2134):
                pass
            else:
                csv_writer.writerow(row)

            row_count += 1



        
if __name__ == "__main__":
    #api_key = setup("api_key.txt")

    rm("US_youtube_trending_data_sub.csv", "US_youtube_nontrending_data_sub.csv")


