#!/usr/bin/python
#coding:utf-8

import glob
import numpy as np
import h5py
import cv2
from random import shuffle


def list_images_and_lables(images_path, keyword, shuffle_data = True):
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
        if "in" in addrs[i]:
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

    dev_addrs = addrs[int(0.6*len(addrs)):int(0.8*len(addrs))]
    dev_labels = labels[int(0.6*len(addrs)):int(0.8*len(addrs))]

    test_addrs = addrs[int(0.8*len(addrs)):]
    test_labels = labels[int(0.8*len(labels)):]

    return (train_addrs, train_labels, dev_addrs, dev_labels, test_addrs, test_labels)

# diamention: orign = 64  VGGNet16 = 24
def create_hdf5(train_hdf5_path, test_hdf5_path, file_sets, diamention = 224):

    train_addrs, train_labels, dev_addrs, dev_labels, test_addrs, test_labels = file_sets

    train_shape = (len(train_addrs), diamention, diamention, 3)
    dev_shape = (len(dev_addrs), diamention, diamention, 3)
    test_shape = (len(test_addrs), diamention, diamention, 3)

    # trainset
    with h5py.File(train_hdf5_path, 'a') as train_hdf5_file:
        train_hdf5_file.create_dataset("train_set_x", train_shape, np.int8)
        # train_hdf5_file.create_dataset("train_mean", train_shape[1:], np.float32)
        train_hdf5_file.create_dataset("train_set_y", (len(train_addrs),), np.int8)
        train_hdf5_file["train_set_y"][...] = train_labels

    # testset
    with h5py.File(test_hdf5_path, 'a') as test_hdf5_file:
        test_hdf5_file.create_dataset("test_set_x", test_shape, np.int8)
        test_hdf5_file.create_dataset("test_set_y", (len(test_addrs),), np.int8)
        test_hdf5_file["test_set_y"][...] = test_labels
    # devset
    # could someone finish this part? :)


def load_images_info_h5(train_hdf5_path, test_hdf5_path, file_sets, diamention = 224):
    train_addrs, train_labels, dev_addrs, dev_labels, test_addrs, test_labels = file_sets
    train_shape = (len(train_addrs), diamention, diamention, 3)
    # dev_shape = (len(dev_addrs), diamention, diamention, 3)
    test_shape = (len(test_addrs), diamention, diamention, 3)
    # mean = np.zeros(train_shape[1:], np.float32)

    # loop over train addresses
    for i in range(len(train_addrs)):
        # print how many images are saved every 100 images
        if i % 100 == 0 and i > 1:
            print 'Train data: {}/{}'.format(i, len(train_addrs))

        # read an image and resize to (224, 224)
        # cv2 load images as BGR, convert it to RGB
        addr = train_addrs[i]
        img = cv2.imread(addr)
        img = cv2.resize(img, (diamention, diamention), interpolation=cv2.INTER_CUBIC)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # save the image and calculate the mean so far
        with h5py.File(train_hdf5_path, 'a') as train_hdf5_file:
            train_hdf5_file["train_set_x"][i, ...] = img[None]
        # mean += img / float(len(train_labels))
        # hdf5_file["train_mean"][...] = mean

    # loop over validation addresses
    # for i in range(len(dev_addrs)):
    #     # print how many images are saved every 1000 images
    #     if i % 100 == 0 and i > 1:
    #         print 'Dev data: {}/{}'.format(i, len(dev_addrs))
    #
    #     # read an image and resize to (224, 224)
    #     # cv2 load images as BGR, convert it to RGB
    #     addr = dev_addrs[i]
    #     img = cv2.imread(addr)
    #     img = cv2.resize(img, (diamention, diamention), interpolation=cv2.INTER_CUBIC)
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #
    #     # add any image pre-processing here
    #
    #     # save the image
    #     with h5py.File(hdf5_path, 'a') as hdf5_file:
    #         hdf5_file["dev_set_x"][i, ...] = img[None]

    # loop over test addresses
    for i in range(len(test_addrs)):
        # print how many images are saved every 100 images
        if i % 100 == 0 and i > 1:
            print 'Test data: {}/{}'.format(i, len(test_addrs))

        # read an image and resize to (224, 224)
        # cv2 load images as BGR, convert it to RGB
        addr = test_addrs[i]
        img = cv2.imread(addr)
        img = cv2.resize(img, (diamention, diamention), interpolation=cv2.INTER_CUBIC)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # add any image pre-processing here

        # save the image
        with h5py.File(test_hdf5_path, 'a') as test_hdf5_file:
            test_hdf5_file["test_set_x"][i, ...] = img[None]
