#!/usr/bin/python
#coding:utf-8

import math
import glob
import numpy as np
import h5py
import cv2
from random import shuffle

def list_images_and_lables(images_path, keyword='in', shuffle_data = True):
    """
    List images location and lables in the same dimensions.

    Arguments:
    images_path -- data path, the directory where saved image data.
    keyword -- image filter.
    shuffle_data -- whether shuffle data.

    Returns:
    (addrs, labels, ...) -- tuple of train/dev/test sets and lables.
    """

    # read addresses and labels from the 'train' folder
    addrs = glob.glob(images_path)

    # you can determine how many image types here
    # labels = [1 if keyword in addr else 0 for addr in addrs]  # 1 = keyword,0 = non-keyword
    labels = []
    for i in range(len(addrs)):
        # fix me! use constants or parameters here! I will fix it later
        if keyword in addrs[i]:
            labels.append(0)
        else:
            labels.append(1)
    # to shuffle data
    if shuffle_data:
        c = list(zip(addrs, labels))
        shuffle(c)
        addrs, labels = zip(*c)

    # Divide the hata into 60% train, 20% validation, and 20% test
    train_addrs = addrs[0:int(0.8*len(addrs))]
    train_labels = labels[0:int(0.8*len(labels))]

    test_addrs = addrs[int(0.8*len(addrs)):]
    test_labels = labels[int(0.8*len(labels)):]

    return (train_addrs, train_labels, test_addrs, test_labels)


def load_dataset(train_set, test_set):
    """
    load train set and test set for the tensorflow session, both of these sets are h5 format.

    Arguments:
    train_set -- train set file path, such as "datasets/train_set.h5"
    test_set -- test set file path, such as "datasets/test_set.h5"

    Returns:
    train_set_x_orig --
    train_set_y_orig --
    test_set_x_orig --
    test_set_y_orig --
    classes --
    """
    print (train_set, test_set)
    train_dataset = h5py.File(train_set, "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:]) # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:]) # your train set labels


    test_dataset = h5py.File(test_set, "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:]) # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:]) # your test set labels

    # classes = np.array(test_dataset["list_classes"][:]) # the list of classes

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig


def convert_to_one_hot(Y, C):
    Y = np.eye(C)[Y.reshape(-1)].T
    return Y
