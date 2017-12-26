from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import gzip
import numpy as np
import os
import urllib
import urllib.request as urlreq
from tqdm import tqdm
import requests

def _download_file(filepath, urlreq):
	# request file	
	length = int(urlreq.headers.get('content-length', 0))
	print("Requested file url: {} length: {} local path: {}".format(urlreq, length, filepath))
	# write file
	with open(filepath, "wb") as file:		
		for data in tqdm(urlreq.iter_content(32*1024), total=length, unit='B', unit_scale=True):
			file.write(data)
	print('Successfully downloaded', filepath, length, 'bytes.')
	return filepath

def download_file(filename, work_directory, source_url):
	if not os.path.exists(work_directory):
		os.makedirs(work_directory)
	filepath = os.path.join(work_directory, filename)
	url = urllib.parse.urljoin(source_url, filename)		
	urlreq = requests.get(url, stream=True)
	if not os.path.exists(filepath):
		return _download_file(filepath, urlreq)
	else:
		url_length = int(urlreq.headers.get('content-length', 0))
		statinfo = os.stat(filepath)
		if (statinfo.st_size != url_length):
			_download_file(filepath, urlreq)
	return filepath


def read_images(filename, work_directory, source_url):
	images = []
	filepath = download_file(filename, work_directory, source_url)
	return images


def read_labels(filename, work_directory, source_url):
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


def read_dataset(work_directory, source_url="http://www.ifp.illinois.edu/~vuongle2/helen/data/"):

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

