#!/usr/bin/python
#coding:utf-8

from utils import *

train_hdf5_path = '../train_dataset.h5'
test_hdf5_path = '../test_dataset.h5'

images_path = './images/*.jpg'
keyword = 'cat'

file_sets = list_images_and_lables(images_path, keyword)
create_hdf5(train_hdf5_path, test_hdf5_path, file_sets)
load_images_info_h5(train_hdf5_path, test_hdf5_path, file_sets)
