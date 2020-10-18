import torch
import numpy as np

#T = torch.zeros([3, 4])
#print(T)

#print(torch.cuda.is_available())

x0 = np.array([[1,2], [4,5]])
x1 = x0 - 10/(x0 + 1)

print(x1)