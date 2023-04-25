import os
import sys
from pathlib import Path

import torch
from torch.utils import data

import numpy as np
import imageio.v3 as iio

class YTDataset(data.Dataset):

	def __init__(self, root, split='train', is_transform=True, augmentations=None, is_norm=False):
		self.root = root
		self.split = split
		self.is_transform = is_transform
		self.augmentations = augmentations
		self.is_norm = is_norm

		self.root_path = self.root / 'data_list'

		self.mean = np.array([0.485, 0.456, 0.406])
		self.std = np.array([0.229, 0.224, 0.225])

		#get data path
		self.data_list_file = self.root_path / (split + '_list.txt')

		self.data_list = []
		
		with self.data_list_file.open(mode='r') as f:
			for line in f:
				self.data_list.append(line.rstrip('\n'))

	def __len__(self):
		return len(self.data_list)


	def __getitem__(self, index):
		
		data_split_list = self.data_list[index].split(' ')

		img_id = data_split_list[0]
		label = np.array([int(data_split_list[1])])

		img_tensor = iio.imread(self.root / (self.split + '_image') / (img_id + '.png'))
		
		if self.is_norm:	

			img_tensor = (img_tensor - self.mean) / self.std

		img_tensor = np.moveaxis(img_tensor, -1, 0)
		# img_tensor = img_tensor[np.newaxis, :, :, :]
		# label = label[np.newaxis, :]

		return img_tensor, label, img_id