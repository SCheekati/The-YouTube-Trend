from cnn import ConvNeuralNet
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

batch_size = 64
num_classes = 10
learning_rate = 0.001
#num_epochs = 20

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#def train(model, num_epochs):
   # for i in range(1, num_epochs + 1):

