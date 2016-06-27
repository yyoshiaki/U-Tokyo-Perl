#!/usr/bin/env python
"""
#.gzの扱いの例。
import gzip
with gzip.open('./samples/gbpri1.seq.gz', 'rt') as f:
    file_content = f.read()
    f.close()
    #print(file_content[:10000])
"""

from Bio import SeqIO
import gzip
import numpy as np
import math

#開くファイル。
seqfile = ["./samples/gbpri1.seq.gz",
           "./samples/gbpri2.seq.gz",
           "./samples/gbpri9.seq.gz"]

for file in seqfile:
    print ("file : ",file)
    list_seq = []
    i=0
    short_sequences = [] # Setup an empty list
    for record in SeqIO.parse(gzip.open(file, "rt"), "genbank"):
        list_seq.append([record.id,record.description,len(record.seq),])


    print("number of Entry",len(list_seq))
    #平均、標準偏差、最大最小の格納されている番号を調べるためにlistを崩す。
    list_len = []
    for seq in list_seq:
        list_len.append(seq[2])

    print("sum : ", np.sum(list_len))
    print("average : ", np.average(list_len))
    print("SD : ", np.std(list_len))
    print("Max : \n",list_seq[list_len.index(max(list_len))])
    print("Min : \n",list_seq[list_len.index(min(list_len))])

    print("\n")

    #以下分布図
    num_u500 = 0
    num_u1000 = 0
    num_u1500 = 0
    num_u2000 = 0
    num_u2500 = 0
    num_upper = 0
    for length in list_len:
        if length < 500:
            num_u500 += 1
        elif length < 1000:
            num_u1000 += 1
        elif length < 1500:
            num_u1500 += 1
        elif length < 2000:
            num_u2000 += 1
        elif length < 2500:
            num_u2500 += 1
        else:
            num_upper += 1

    def log_plot(num):
        if num == 0:
            return "  "
        else:
            plot = "*"*int(math.log10(num)*5) + "  "
            return plot

    u500 = log_plot(num_u500)
    u1000 = log_plot(num_u1000)
    u1500 = log_plot(num_u1500)
    u2000 = log_plot(num_u2000)
    u2500 = log_plot(num_u2500)
    upper = log_plot(num_upper)

    print("frequency  1    10   100  1000 10000\n",
          "length    ++----+----+----+----+\n",
          "    0-500 |",u500,num_u500,"\n",
          " 501-1000 |",u1000,num_u1000,"\n",
          "1001-1500 |",u1500,num_u1500,"\n",
          "1501-2000 |",u2000, num_u2000,"\n",
          "2001-2500 |", u2500, num_u2500,"\n",
          "2501-     |", upper, num_upper, "\n"
)