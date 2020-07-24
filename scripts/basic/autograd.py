from torch.autograd import Variable
import torch

x = Variable(torch.ones(2), requires_grad=True)
y = 4*x*x
z = y.norm()

print(z)
