# PyTorch Quick Model Example

This script demonstrates a tiny neural network in PyTorch.

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Example data
X = torch.tensor([[0.0], [1.0], [2.0], [3.0]], dtype=torch.float32)
y = torch.tensor([[0.0], [1.0], [2.0], [3.0]], dtype=torch.float32)

# Simple model
model = nn.Sequential(
    nn.Linear(1, 10),
    nn.ReLU(),
    nn.Linear(10, 1)
)

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

for epoch in range(200):
    optimizer.zero_grad()
    preds = model(X)
    loss = criterion(preds, y)
    loss.backward()
    optimizer.step()

    if epoch % 50 == 0:
        print(f"Epoch {epoch}: loss = {loss.item():.6f}")

print("Final prediction:", model(torch.tensor([[4.0]], dtype=torch.float32)).item())
```

## Tasks
- switch to a binary classification problem
- add validation logic
- try a deeper network
- visualize the training loss
