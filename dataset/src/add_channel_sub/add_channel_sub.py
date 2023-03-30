
import requests, sys, time, os, argparse, csv
from datetime import date

def setup(api_path):
    with open(api_path, 'r') as file:
        api_key = file.readline()

    return api_key


def add_sub(file_name, api_key):


    with open(file_name) as csv_file, open("US_youtube_trending_data_sub.csv", "a+", encoding='utf-8') as f:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_writer = csv.writer(f)

        row_count = 0
        output_count = 0
        for row in csv_reader:

            if (row_count == 0):

                row.insert(6, 'num_sub')

            if (row_count != 0):

                channelID = row[3]

                request_url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channelID}&key={api_key}"
                request = requests.get(request_url)
                #print(request.json())
                #print(request.json()['items'][0]['statistics']['subscriberCount'])
                try:
                    sub_count = request.json()['items'][0]['statistics']['subscriberCount']
                except:
                    print('no sub')
                    sub_count = -1
                row.insert(6, sub_count)

            csv_writer.writerow(row)
            output_count += 1
            row_count += 1
              
        print(row_count)
        print(output_count)
        

if __name__ == "__main__":
    api_key = setup("api_key.txt")

    add_sub("US_youtube_trending_data_trim.csv", api_key)


