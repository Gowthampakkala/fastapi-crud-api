import torch

tensor = torch.tensor([1,2,3,4])
print(tensor)
matrix = torch.tensor([
               [1,2,3],
               [4,5,6]
])
print(matrix)
print(matrix.shape)
print(torch.randint(1,10,(3,3)))
q= torch.arange(12)
print(q.reshape(3,4))
x = torch.tensor(3.0,requires_grad=True)
y =x*x+5
y.backward()
print(y)
print(x.grad)