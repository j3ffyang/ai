from torch.autograd import Variable
import torch

x = Variable(torch.ones(2, 2) * 2, requires_grad = True)
z = 2 * (x * x) + 5 * x
z.backward(torch.ones(2, 2))

# print(z)
print(x)
print(x.grad)

