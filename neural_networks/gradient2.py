'''
Реализуйте расчет градиента для функции f(w) = prod(ln(ln(x + 7))) в точке w = [[5, 10], [1, 2]]w =[[5,10],[1,2]]
'''

import torch
x = torch.tensor(
    [[5., 10],
     [1.,  2.]], requires_grad=True)

#######
device = torch.device('cuda:0' 
                      if torch.cuda.is_available() 
                      else 'cpu')
x = x.to(device)
#######

function = torch.log(torch.log(x + 7)).prod()

function.backward()

print(x.grad, '<- gradient')