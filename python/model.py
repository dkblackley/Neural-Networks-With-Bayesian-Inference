"""
File responsible for holding the model, uses efficientnet
"""
import torch
import torch.nn as nn
from torch.nn import functional as TF
from efficientnet_pytorch import EfficientNet


class Classifier(nn.Module):
    """
    Class that holds and runs the efficientnet CNN
    """
    def __init__(self, image_size, output_size, dropout=0.5):
        """
        init function sets the type of efficientnet and any extra layers
        :param dropout: rate for dropout
        """
        super(Classifier, self).__init__()
        self.model = EfficientNet.from_pretrained("efficientnet-b0")
        self.drop_rate = dropout
        self.pool = nn.AdaptiveAvgPool2d(1)
        self.output_size = output_size

        with torch.no_grad():

            temp_input = torch.zeros(1, 3, image_size, image_size)
            encoder_size = self.model.extract_features(temp_input).shape[1]

        # Initialises the classification head for generating predictions.

        self.efficient_net_output = nn.Linear(encoder_size, 512)

        self.hidden_layer1 = nn.Linear(512, 512)
        self.hidden_layer2 = nn.Linear(512, 512)
        self.hidden_layer3 = nn.Linear(512, 512)
        self.hidden_layer4 = nn.Linear(512, 512)

        self.output_layer = nn.Linear(512, output_size)

    def forward(self, input, dropout=False):
        """
        Method for handling a forward pass though the network, applies dropout using nn.functional
        :param input: input batch to be processed
        :param dropout: bool for whether or not dropout should be applied
        :return: processed output
        """
        output = self.model.extract_features(input)
        output = self.pool(output)
        output = output.view(output.shape[0], -1)

        if self.training:
            output = TF.dropout(output, self.drop_rate)
            output = self.efficient_net_output(output)
            output = TF.dropout(output, self.drop_rate)
            output = self.hidden_layer1(output)
            output = TF.dropout(output, self.drop_rate)
            output = self.hidden_layer2(output)
            output = TF.dropout(output, self.drop_rate)
            output = self.hidden_layer3(output)
            output = TF.dropout(output, self.drop_rate)
            output = self.hidden_layer4(output)
            output = TF.dropout(output, self.drop_rate)

        elif dropout:

            output = self.efficient_net_output(output)
            output = self.hidden_layer1(output)
            output = TF.dropout(output, self.drop_rate)
            output = self.hidden_layer2(output)
            output = TF.dropout(output, self.drop_rate)
            output = self.hidden_layer3(output)
            output = TF.dropout(output, self.drop_rate)
            output = self.hidden_layer4(output)
            output = TF.dropout(output, self.drop_rate)

        else:

            output = self.efficient_net_output(output)
            output = self.hidden_layer1(output)
            output = self.hidden_layer2(output)
            output = self.hidden_layer3(output)
            output = self.hidden_layer4(output)

        output = self.output_layer(output)
        return output
