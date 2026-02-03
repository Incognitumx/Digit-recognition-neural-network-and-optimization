import torch
import torch.optim as optim
import torch.nn as nn
from torchvision import datasets, transforms
from model import SimpleANN

def train():
    # Data transformation: Convert images to Tensors and normalize
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    
    # Automatically download MNIST dataset to the data folder
    # Fix for MNIST download error
    new_mirror = 'https://ossci-datasets.s3.amazonaws.com/mnist/'
    datasets.MNIST.mirrors = [new_mirror]

    train_dataset = datasets.MNIST('../data', train=True, download=True, transform=transform)
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)

    # Select device (GPU if available, otherwise CPU)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Instantiate the SimpleANN model
    model = SimpleANN().to(device)
    
    # Define optimizer (Adam is a robust choice for most tasks)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    # Define loss function (CrossEntropy is standard for classification)
    criterion = nn.CrossEntropyLoss()

    model.train()
    print("Starting training...")
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        
        # Zero the gradients from the previous step
        optimizer.zero_grad()
        # Forward pass: Compute predicted outputs by passing inputs to the model
        output = model(data)
        # Calculate the loss
        loss = criterion(output, target)
        # Backward pass: Compute gradient of the loss with respect to model parameters
        loss.backward()
        # Perform a single optimization step (parameter update)
        optimizer.step()
        
        if batch_idx % 200 == 0:
            print(f'Batch {batch_idx}: Loss = {loss.item():.4f}')

    # Save the trained model weights
    torch.save(model.state_dict(), "../models/mnist_ann.pth")
    print("Training complete! Model saved in models/mnist_ann.pth")

if __name__ == '__main__':
    train()
