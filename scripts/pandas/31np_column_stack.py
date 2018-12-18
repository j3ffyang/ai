import numpy as np

costs = np.column_stack(([2, 2, 3, 1],
                         [7, 7, 6, 4]))
mean_costs = np.mean(costs[:, 1])
print(mean_costs)
