import csv
import sys, os

infile = sys.argv[1]
outfile = sys.argv[2]

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(ROOT, "neural_npfp"))

with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for l in f:
