import os, sys, re, subprocess, shlex
from Bio import SeqIO
import numpy as np

#inputdir = "genomes"
inputdir = sys.argv[1] # define input file
outputdir = sys.argv[2] # define output file


#print(inputdir, outputdir)
for i in os.listdir(inputdir): # begin loop to process fasta files
  if (i.endswith(".fna")):
    inputpath = os.path.join(inputdir, i)
    outputfile = re.sub(".fna", ".faa", i)
    outputpath = os.path.join(outputdir, outputfile)
    #print(inputpath, outputpath)
    cmd = "prodigal -i "+ inputpath + " -a "+ outputpath
    print(cmd)
    cmd2 = shlex.split(cmd)
    #subprocess.call(cmd2, stdout=open("stdout.txt", "w"), stderr=open("stderr.txt", "w"))


for i in os.listdir(outputdir):
  length_dict = {}
  for record in SeqIO.parse(os.path.join(outputdir, i), "fasta"):
    length = len(record.seq)
    #print(record.id, length)
    #length_list.append(length)
    length_dict[record.id] = length
    
  print(length_dict.keys()) 
  #mean = np.mean(length_list)
  #print(i, max(length_list), min(length_list), mean)


