import torch
import torchvision
import torch.optim as optimizer
from torchvision import transforms
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt

import dataLoading
import dataPlotting


composed = transforms.Compose([dataLoading.reScale(1024),
                               dataLoading.randomCrop(800)],
                              dataLoading.randomRotation(90))













"""

dataPlot = dataPlotting.dataPlotting()
scale = dataLoading.reScale(1024)
crop = dataLoading.randomCrop((700, 1000))
composed = transforms.Compose([dataLoading.reScale(1024),
                               dataLoading.randomCrop(800)])

train_data = dataLoading.dataSet("Training_meta_data/ISIC_2019_Training_Metadata.csv", "Training_meta_data/ISIC_2019_Training_GroundTruth.csv")

item = train_data.__getitem__(24)

# Apply each of the above transforms on sample.
fig = plt.figure()

for i, tsfrm in enumerate([scale, crop, composed]):
    transformed_sample = tsfrm(item)
    dataPlot.show_data(transformed_sample)

plt.show()


dataPlot.show_data(item)

"""


