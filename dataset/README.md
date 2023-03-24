# Dataset Preparation
In this section, we describe how we prepare our dataset from scratch. We utilize existing Youtube trending video dataset from Kaggle and also collect Youtube non-trending video data on our own with Youtube API. Next, we conduct dataset cleaning and split the dataset for train and validation set. We show the dataset preparation procedures in below.

## 1. Download Youtube Trending Video Dataset in Kaggle
We download the existing daily update Youtube trending video statistic Kaggle dataset in [here](https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset). This dataset contains all Youtube trending video statistics from 2020 till today across several countries and regions. In this project, we only use the trending data in `US` region

### Data preprocessing
For simplicity, we only use those trending data after `2022-12-15`. We use `src/preprocess/preprocess.py` to collect trending videos published after `2022-12-15` to `2023-03-23`, check the current status of the video (whether it has been removed or not), remove some of unnecessary columns and calculate number of likes/dislikes per day.

## 2. Collect Non-Trending Video Data
Next, we use the [Youtube API V3](https://developers.google.com/youtube/v3) to collect non-trending videos in the same timeframe (after `2022-12-15` till `2023-03-23`). We use `src/non_trending_scraper/scraper.py` to download random video statistics and make sure they are not overlapping with those data we have in step 1 (therefore, they are not trending videos.) To avoid distribution change, we make sure we collect those video categories also shown in trending videos.

## 3. Add Number of Channel Subscribers and Split dataset
In the last step, we download number of channel subscribers with `src/add_channel_sub/add_channel_sub.py`. And, we split the overall dataset (trending + non-trending) into train set and validation set in the ratio of 8:2 using `src/split_dataset/split.py`.

## Dataset Features
There are 4324 examples in train set and 1082 examples in validation set. There are 2703 trending video examples and 2703 non-trending video examples.

