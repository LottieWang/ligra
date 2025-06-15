# from graph import GRAPH_DIR
# from graph import TR_DIR
# from graph import graphs
# from graph import largeD_graphs
import os
import subprocess

GRAPH_DIR = f"/data/graphs/bin"
# TR_DIR = f"/data/lwang323/Approx/ground_truth"

graphs = [
"Epinions1_sym",
"Slashdot_sym",
"DBLP_sym",
"com-youtube_sym",
"skitter_sym",
"in_2004_sym",
"soc-LiveJournal1_sym",
"hollywood_2009_sym",
"socfb-uci-uni_sym",
"socfb-konect_sym",
"com-orkut_sym",
"indochina_sym",
"eu-2015-host_sym",
"uk-2002_sym",
"arabic_sym",
"twitter_sym",
"friendster_sym",
"sd_arc_sym"
]

def test_Ecc(test, k, g, CURRENT_DIR, LOG_DIR, ECC_DIR):
	print(f"test on {g}")
	# ground_truth = f"{TR_DIR}/{g}_sym.txt"
	test_file = f"{CURRENT_DIR}/{test}"
	OUT_DIR = f"{LOG_DIR}/kBFS_{test}"
	ANS_DIR = f"{ECC_DIR}/kBFS_{test}"
	os.makedirs(OUT_DIR, exist_ok=True)
	os.makedirs(ANS_DIR, exist_ok=True)
	cmd = f"numactl -i all {test_file} {GRAPH_DIR}/{g}.bin -s -b -out {ANS_DIR}/{g}_{k}.txt >> {OUT_DIR}/{g}_{k}.txt"
	subprocess.call(cmd, shell=True)

def experiment():
	CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
	LOG_DIR= f"{CURRENT_DIR}/log"
	ECC_DIR = "/data/lwang323/MS_BFS/Ecc/Ligra"
	#   LOG_DIR=f"/data/lwang323/MS_BFS/Ecc"
	os.makedirs(LOG_DIR, exist_ok=True)
	os.makedirs(ECC_DIR, exist_ok=True)
	type_names = ["kBFS-1Phase-Ecc","kBFS-Ecc","kBFS-Exact", "RV","TK","LogLog-Ecc", "FM-Ecc", "CLRSTV"]
	# batch_sizes = [64,128,256,512,1024]
	batch_sizes = [64]
	for k in batch_sizes:
		print(f"--------test on batch_size {k}---------")
		for test in type_names:
			print(f"----test on {test}----")	
			for g in graphs:
				test_Ecc(test, k, g, CURRENT_DIR, LOG_DIR, ECC_DIR)

if __name__ == '__main__':
	experiment()
	CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
#   OUT_DIR=f"{CURRENT_DIR}/../result"
#   os.makedirs(OUT_DIR, exist_ok=True)