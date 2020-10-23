import torch

x=torch.zeros([6000, 28, 28], dtype=torch.int32)

print(x.reshape(-1,14,32,7).shape)
print(x.reshape(-1,1,1).shape)
print(x.shape)
print(x.reshape(len(x[1]), len(x), len(x[2])).shape)
#print(x.reshape(-1,9).shape)
print(x.reshape(-1).shape)
print(x.reshape(-1,6000).shape)