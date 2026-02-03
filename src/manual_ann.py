# This is my first version of ann.
# No backpropagation, No Loss function, only assigned weight and bias, which are adjusted by programmer manually, after seeing the result.
import torch

def simple_manual_layer(pixel_data):
    # 1. Input: Flatten the 28x28 image to 784 pixels
    x = pixel_data.view(784)
    
    # 2. Weights: Imagine these are the "learned" values (manually set for now)
    # In a real model, these are thousands of decimals. 
    # Here we just create a random "brain" for the neuron.
    weights = torch.randn(10, 784) # 10 neurons, each looking at 784 pixels
    bias = torch.randn(10)         # 10 biases for 10 neurons
    
    # 3. The Core Math: y = wx + b
    # This is the "Full Connection" (Linear Layer)
    raw_score = torch.matmul(weights, x) + bias
    
    # 4. Activation Function: ReLU (Manual)
    # If the score is negative, it becomes 0.
    activated_score = torch.max(torch.tensor(0.0), raw_score)
    
    return activated_score

print("Manual Calculation Result:", simple_manual_layer(torch.randn(28, 28)))
