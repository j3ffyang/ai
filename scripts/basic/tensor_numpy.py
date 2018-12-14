import torch
from torch.autograd import Variable
import numpy

tensor = torch.FloatTensor([[1,2], [3,4]])
variable = Variable(tensor, requires_grad=True)

print(tensor)
print(variable)

t_out = torch.mean(tensor * tensor)
v_out = torch.mean(variable * variable)
print(t_out)
print(v_out)

v_out.backward()
print(v_out)
print(variable.grad)

print(variable.data.numpy())