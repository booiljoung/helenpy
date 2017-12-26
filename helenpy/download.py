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


def _download_file(urlreq, filepath, url):
	# request file	
	remote_length = int(urlreq.headers.get('content-length', 0))
	# write file
	with open(filepath, "wb") as file:
		for data in tqdm(urlreq.iter_content(1024*1024), total=remote_length, unit='B', unit_scale=True, leave=False):
			file.write(data)
			time.sleep(0.1)
	return filepath


def download_file(filename, work_directory, source_url):
	if not os.path.exists(work_directory):
		os.makedirs(work_directory)
	filepath = os.path.join(work_directory, filename)
	url = urllib.parse.urljoin(source_url, filename)		
	urlreq = requests.get(url, stream=True)
	remote_length = int(urlreq.headers.get('content-length', 0))
	print("Requested file url: {} length: {} local path: {}".format(url, remote_length, filepath))
	if not os.path.exists(filepath):
		return _download_file(urlreq, filepath, url)
	else:
		statinfo = os.stat(filepath)
		if (statinfo.st_size != remote_length):
			return _download_file(urlreq, filepath, url)
		else:
			print("filename: {} exist. length: {}".format(filename, remote_length))
	return filepath


def download_dataset(work_directory, source_url="http://www.ifp.illinois.edu/~vuongle2/helen/data/"):
    files0 = {
        "train": {
            "image": ["train_1.zip", "train_2.zip", "train_3.zip", "train_4.zip"],
            "label": ["trainnames.txt"]
        },
        "test": {
            "image": ["test.zip"],
            "label": ["testnames.txt"]
        }
    }

    files1 = {}

    for partname in files0.keys():
        parts0 = files0[partname]
        parts1 = {}
        for typename in parts0:
            filenames0 = parts0[typename]
            pathnames1 = []
            for filename0 in filenames0:
                pathname1 = download_file(filename0, work_directory, source_url)
                pathnames1.append(pathname1)
            parts1[typename] = pathname1
        files1[partname] = parts1
    return files1


if __name__ == "__main__":
    filenames = download_dataset("./../../helendataset")
    print(filenames)
