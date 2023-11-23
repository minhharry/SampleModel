import torch
from torch import nn

import torchvision
from torchvision import datasets
from torchvision.transforms import ToTensor

import matplotlib.pyplot as plt
import random

print(f"PyTorch version: {torch.__version__}\ntorchvision version: {torchvision.__version__}")


train_data = datasets.FashionMNIST('data', True, ToTensor, download=True)