from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import gzip
import numpy as np
import os
import requests
import time
from tqdm import tqdm
import urllib
import urllib.request as urlreq


def read_images_nparray(filepaths):
	images = []
	return images


def read_labels(filepath):
	labels = []
	return labels


def read_image_dataset(filenames, work_directory, source_url):
	image_dataset = []
	for fn in filenames:
		images = read_images(fn, work_directory, source_url)
		if images != None:
			for image in images:
				image_dataset.append(image)
	return image_dataset


def read_label_dataset(filenames, work_directory, source_url):
	label_dataset = []
	for fn in filenames:
		labels = read_labels(fn, work_directory, source_url)
		if labels != None:
			for label in labels:
				label_dataset.append(label)
	return label_dataset


def read_dataset(work_directory, source_url):

	TRAIN_IMAGE_FILENAMES = ["train_1.zip", "train_2.zip", "train_3.zip", "train_4.zip"]
	TRAIN_LABEL_FILENAMES = ["trainnames.txt"]

	TEST_IMAGE_FILENAMES = ["test.zip"]
	TEST_LABEL_FILENAMES = ["testnames.txt"]
	
	train_image_dataset = read_image_dataset(TRAIN_IMAGE_FILENAMES, work_directory, source_url)
	train_label_dataset = read_label_dataset(TRAIN_LABEL_FILENAMES, work_directory, source_url)

	test_image_dataset = read_image_dataset(TEST_IMAGE_FILENAMES, work_directory, source_url)
	test_label_dataset = read_label_dataset(TEST_LABEL_FILENAMES, work_directory, source_url)

	return train_image_dataset, train_label_dataset, test_image_dataset, test_label_dataset


if __name__ == "__main__":
	read_dataset("./../../helendataset")

