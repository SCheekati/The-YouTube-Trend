
import requests, sys, time, os, argparse, csv
from datetime import date

def date_diff(date1, date2):

    date1_split = date1.split('-')
    date2_split = date2.split('-')

    d1 = date(int(date1_split[0]), int(date1_split[1]), int(date1_split[2]))
    d2 = date(int(date2_split[0]), int(date2_split[1]), int(date2_split[2]))
    delta = d2 - d1

    return delta.days + 1

def get_dislikes_rating(video_id):

    request_url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"

    proxies = { 
              "http"  : "http://XXXX:XXXX@pr.oxylabs.io:7777", 
              "https" : "http://XXXX:XXXX@pr.oxylabs.io:7777"
            }

    request = requests.get(request_url, proxies=proxies)

    return request.json()["dislikes"], request.json()["rating"]

def setup(api_path):
    with open(api_path, 'r') as file:
        api_key = file.readline()

    return api_key

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def crop_rows(file_name, api_key):

    id_set = set()

    with open(file_name) as csv_file, open("US_youtube_trending_data_trim.csv", "a+", encoding='utf-8') as f:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_writer = csv.writer(f)

        row_count = 0
        output_count = 0
        for row in csv_reader:
            
            if (row_count == 0 or row_count > 173591):
                print(output_count)

                if (row[0] not in id_set):
                    
                    if (not isEnglish(row[1])):
                        pass
                    else:
                        if (row_count == 0):
                            
                            row.append('trending')

                            row[14] = 'rating'
                            row.pop(13)

                            row[8] = 'views per day'
                            row[9] = 'likes per day'
                            row[10] = 'dislikes per day'
                            row[11] = 'comments per day'

                            csv_writer.writerow(row)
                            row_count += 1
                            continue

                        else:
                            # check video status
                            request_url = f"https://www.googleapis.com/youtube/v3/videos?part=status&id={row[0]}&key={api_key}"
                            request = requests.get(request_url)
                            if (len(request.json()["items"]) == 0):
                                pass
                            else:
                                if (output_count == -1):
                                    id_set.add(row[0])
                                    output_count += 1
                                else:
                                    # modify publish time
                                    publish_time = row[2]
                                    row[2] = publish_time[:-10]

                                    # modify trending date
                                    trending_date = row[6]
                                    row[6] = trending_date[:-10]

                                    # modify thumbnail
                                    thumbnail_link = row[12]
                                    thumbnail_link = thumbnail_link.replace('default.jpg', 'hqdefault.jpg')
                                    row[12] = thumbnail_link

                                    # calculate likes per day
                                    days = date_diff(row[2], row[6])
                                    row[9] = round(int(row[9]) / days, 3)

                                    # calculate dislikes and rating
                                    current_days = date_diff(row[2], str(date.today()))
                                    dislikes = None
                                    rating = None
                                    while (dislikes == None):
                                        try:
                                            dislikes, rating = get_dislikes_rating(row[0])
                                        except:
                                            print("retry")

                                    row[10] = round(dislikes / current_days, 3)
                                    row[14] = round(rating, 3)

                                    # calculate comments per day
                                    row[11] = round(int(row[11]) / days, 3)

                                    # calculate views per day
                                    row[8] = round(int(row[8]) / days, 3)

                                    row.append('1')

                                    row.pop(13)

                                    csv_writer.writerow(row)
                                    id_set.add(row[0])
                                    output_count += 1

            row_count += 1

        print(row_count)
        print(output_count)
        

if __name__ == "__main__":
    api_key = setup("api_key.txt")

    crop_rows("US_youtube_trending_data.csv", api_key)


