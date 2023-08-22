import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class Gradient_Net(nn.Module):
  def __init__(self, batch_size = 1):
    super(Gradient_Net, self).__init__()
    kernel_x = [[-1., 0., 1.], [-2., 0., 2.], [-1., 0., 1.]]
    kernel_x = torch.FloatTensor(kernel_x).unsqueeze(0).to(device)

    kernel_y = [[-1., -2., -1.], [0., 0., 0.], [1., 2., 1.]]
    kernel_y = torch.FloatTensor(kernel_y).unsqueeze(0).to(device)

    kernel_x = kernel_x.expand(batch_size, kernel_x.shape[0], kernel_x.shape[1], kernel_x.shape[2])
    kernel_y = kernel_y.expand(batch_size, kernel_y.shape[0], kernel_y.shape[1], kernel_x.shape[2])

    self.weight_x = nn.Parameter(data=kernel_x, requires_grad=False)
    self.weight_y = nn.Parameter(data=kernel_y, requires_grad=False)


  def forward(self, x):
    # x = self.norm_layer(x)
    grad_x = F.conv2d(x, self.weight_x)
    grad_y = F.conv2d(x, self.weight_y)
    gradient = torch.abs(grad_x) + torch.abs(grad_y)
    return gradient


def gradient(x, batch_size):
    gradient_model = Gradient_Net(batch_size=batch_size).to(device)
    g = gradient_model(x)
    return g

