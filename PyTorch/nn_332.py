# С помощью класса Sequential создайте модель нейронной сети с двумя последовательными
#  свёрточными слоями и функцией активации relu между ними.
# На вход модели будет поступать цветное изображение (три цветовых канала).
# На выходе с первого свёрточного слоя должно быть 64 канала, ядра 3х3.
# На выходе со второго свёрточного слоя должно быть 64 канала, ядра 3х3.
# Результат запишите в переменную model.


import torch
from torch import nn

model = nn.Sequential(
    nn.Conv2d(3, 64, (3, 3)),
    nn.ReLU(),
    nn.Conv2d(64, 64, (3, 3)),
)
