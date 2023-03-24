
import requests, sys, time, os, argparse, csv
from datetime import date
import random


def crop_rows(file_name1, file_name2):

    cate = set()

    with open(file_name1) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        row_count = 0

        for row in csv_reader:

            if (row_count == 0):
                pass
            else:
                cate.add(row[5])

            row_count += 1

    rows = []

    with open(file_name2) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        row_count = 0

        for row in csv_reader:

            if (row_count == 0):
                first_row = row
            elif row[5] in cate:
                rows.append(row)

            row_count += 1

    random.shuffle(rows)

    with open("US_youtube_nontrending_data_trim.csv", "a+", encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(first_row)

        for i in range(2705):
            csv_writer.writerow(rows[i])


if __name__ == "__main__":

    crop_rows("US_youtube_trending_data_trim.csv", "US_youtube_nontrending_data.csv")


