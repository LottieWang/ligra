import os
import sys
import subprocess
import re
import pandas as pd
import numpy as np
from Exp_Ecc import graphs


def collect_data(file_in, key_words):
	f = open(file_in,'r')
	res = f.read()
	f.close()
	data_lines = re.findall(f"{key_words}.*", res)
	data = list(map(lambda x: eval(x.split(" ")[-1]), data_lines))
	return data


def collect_average(file_in, key_words, repeat=4):
	f = open(file_in,'r')
	res = f.read()
	f.close()
	data_lines = re.findall(f"{key_words}.*", res)
	data = list(map(lambda x: eval(x.split(" ")[-1]), data_lines))
	data = data[1:]  # Skip the first column which is usually the graph name or similar
	data = np.mean(data)
	return data

def collect_kBFS_1Phase():
	print("Collecting data in kBFS 1Phase")
	LOG_DIR= f"{CURRENT_DIR}/log/kBFS_kBFS-1Phase-Ecc"
	# OUT_FILE=f"{CURRENT_DIR}/../result/exp4.csv"
	data=dict()
	data["Data"]=graphs
	key_words = {
		"CC": "connected components :",
		"Phase1": "Ecc phase 1 :",
		"Total": "total time excluding writing to file :"
	}
	for key, words in key_words.items():
		data[f"{key}"]=[]
		for g in graphs:
			log_file = f"{LOG_DIR}/{g}_64.txt"
			data[f"{key}"].append(collect_average(log_file, words))
	df = pd.DataFrame.from_dict(data)
	print(df.to_csv(index=False))
	# df.to_csv(OUT_FILE, index=False)
def collect_k(test):
	print("Collecting data in different k")
	LOG_DIR= f"{CURRENT_DIR}/log/kBFS_{test}"
	data=dict()
	data["Data"]=graphs
	k = [64, 128, 256, 512, 1024]
	for _k in k:
		data[f"{_k}"]=[]
		for g in graphs:
			log_file = f"{LOG_DIR}/{g}_{_k}.txt"
			data[f"{_k}"].append(collect_average(log_file, "total time excluding writing to file :"))
	df = pd.DataFrame.from_dict(data)
	print(df.to_csv(index=False))
def collect_kBFS_2Phase():
	print("Collecting data in kBFS 2Phase")
	LOG_DIR= f"{CURRENT_DIR}/log/kBFS_kBFS-Ecc"
	# OUT_FILE=f"{CURRENT_DIR}/../result/exp4.csv"
	data=dict()
	data["Data"]=graphs
	key_words = {
		"CC": "connected components :",
		"Phase1": "Ecc phase 1 :",
		"Sort": "sort by decreasing eccentricities :",
		"Phase2": "Ecc phase 2 :",
		"Total": "total time excluding writing to file :"
	}
	for key, words in key_words.items():
		data[f"{key}"]=[]
		for g in graphs:
			log_file = f"{LOG_DIR}/{g}_64.txt"
			data[f"{key}"].append(collect_average(log_file, words))
	df = pd.DataFrame.from_dict(data)
	print(df.to_csv(index=False))
def collect_kBFS_Exact():
	print("Collecting data in kBFS Exact")
	LOG_DIR= f"{CURRENT_DIR}/log/kBFS_kBFS-Exact"
	# OUT_FILE=f"{CURRENT_DIR}/../result/exp4.csv"
	data=dict()
	data["Data"]=graphs
	key_words = {
		"Total": "total time excluding writing to file :"
	}
	for key, words in key_words.items():
		data[f"{key}"]=[]
		for g in graphs:
			log_file = f"{LOG_DIR}/{g}_64.txt"
			if not os.path.exists(log_file):
				data[f"{key}"].append(np.nan)
			else:
					try:
						data[f"{key}"].append(collect_average(log_file, words))
					except:
						data[f"{key}"].append(np.nan)

	df = pd.DataFrame.from_dict(data)
	print(df.to_csv(index=False))
if __name__ == "__main__":
	CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
	test = ["kBFS-1Phase-Ecc", "kBFS-Ecc"]
	for t in test:
		collect_k(t)
	# collect_kBFS_1Phase()
	# collect_kBFS_2Phase()
	# collect_kBFS_Exact()
