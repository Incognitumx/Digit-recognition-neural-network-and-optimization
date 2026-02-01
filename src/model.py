import torch.nn as nn
import torch.nn.functional as F

class SimpleANN(nn.Module):
    def __init__(self):
        super(SimpleANN, self).__init__()
        # The input : 28*28=784 
        # 1st layer：784 inputs -> 128 neurons
        self.fc1 = nn.Linear(784, 128)
        # 2nd layer：128 -> 64 
        self.fc2 = nn.Linear(128, 64)
        # output layer：64 -> 10（0-9）
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        # stretch 28*28 to 1D vector
        x = x.view(-1, 784)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return F.log_softmax(x, dim=1)
