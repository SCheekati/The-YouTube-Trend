
import csv
import numpy as np
from sklearn.decomposition import PCA
from sklearn import svm
from sklearn import metrics

from scipy.stats import boxcox

import matplotlib.pyplot as plt

from scipy import stats



def svm_model():

	train_list = []
	val_list = []

	with open('new_train.csv', encoding='utf-8') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')

		for row in csv_reader:
			train_list.append(row)

	with open('new_val.csv', encoding='utf-8') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')

		for row in csv_reader:
			val_list.append(row)

	train_numpy = np.array(train_list)[1:, :]
	val_numpy = np.array(val_list)[1:, :]

	general_train_np = train_numpy[:, [6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 19]].astype(float)
	train_y_np = train_numpy[:, -1].astype(int)

	general_train_np[:, 7:10] = general_train_np[:, 7:10] / general_train_np[:, [6]]
	#general_train_np[:, 5], fitted_lambda1 = boxcox(general_train_np[:, 5], lmbda=None)
	#general_train_np[:, 6], fitted_lambda2 = boxcox(general_train_np[:, 6], lmbda=None)
	general_train_np = (general_train_np - np.mean(general_train_np, axis=0)) / np.std(general_train_np, axis=0)

	general_val_np = val_numpy[:, [6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 19]].astype(float)
	val_y_np = val_numpy[:, -1].astype(int)

	general_val_np[:, 7:10] = general_val_np[:, 7:10] / general_val_np[:, [6]]
	#general_val_np[:, 5] = stats.boxcox(general_val_np[:, 5], fitted_lambda1)[0]
	#general_val_np[:, 6] = stats.boxcox(general_val_np[:, 6], fitted_lambda2)[0]
	general_val_np = (general_val_np - np.mean(general_val_np, axis=0)) / np.std(general_val_np, axis=0)

	clf = svm.SVC(kernel='rbf')
	clf.fit(general_train_np, train_y_np)

	val_y_pred = clf.predict(general_val_np)

	print("Accuracy:",metrics.accuracy_score(val_y_np, val_y_pred))
	
	



if __name__ == "__main__":

	svm_model()