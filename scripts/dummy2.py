import os
import numpy as np
import pandas as pd
from scipy.misc import imread
from sklearn.metrics import accuracy_score
import tensorflow as tf

seed = 128
rng = np.random.RandomState(seed)

root_dir = os.path.abspath('/tmp')
data_dir = os.path.join(root_dir, 'data')
sub_dir = os.path.join(root_dir, 'sub')

os.path.exists(root_dir)
os.path.exists(data_dir)
os.path.exists(sub_dir)
