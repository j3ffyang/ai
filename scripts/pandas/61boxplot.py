# https://stackoverflow.com/questions/49544123/keyerror-item-not-in-index-while-trying-to-build-boxplot-with-pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1212)
mydata = pd.DataFrame({'loan_amnt': np.random.randn(50)*100,
                       'tool': ["".join(np.random.choice(['pandas', 'r', 'julia',
                                         'sas', 'stata', 'spss'],1)) for _ in range(50)]})

mydata.boxplot(column='loan_amnt', by='tool')
plt.show()
