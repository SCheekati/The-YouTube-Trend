
import csv
import numpy as np
import pandas as pd

from sklearn.feature_extraction import FeatureHasher

def hash_cate():

	data = pd.read_csv('val.csv', encoding='utf-8')

	binary = pd.DataFrame()
	for i in range(5):
		binary[f"cate_{i}"] = data["categoryId"].apply(lambda x: x & 1 << i).astype(bool).astype(int)
	
	new_data = pd.concat([data.iloc[:, 0:6], binary, data.iloc[:, 6:]], 
	          axis=1)

	new_data.to_csv('new_val.csv', encoding='utf-8', index=False)


if __name__ == "__main__":

	hash_cate()
