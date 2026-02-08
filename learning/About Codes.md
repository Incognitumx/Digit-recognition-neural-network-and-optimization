### Learning from new functions new logics new strat
1. PyTorch Flex: The **randn** dimensions:

I noticed torch.randn() can take a different number of arguments.

One argument (n): Creates a Vector. This is used for Bias because each neuron is a single entity with one threshold.

Two arguments (rows, cols): Creates a Matrix. This is used for Weights to map every input to every output.

**Concept**: In AI, we call these dimensions Ranks. A 1D tensor is Rank 1, a 2D tensor is Rank 2. The more numbers I put in randn(), the more complex the "shape" of the brain becomes!
