#!/usr/bin/env python
from Bio import SeqIO
from Bio.Seq import Seq

loc = './samples/foxp3.fasta'
handle = open(loc, "rU")
data = list(SeqIO.parse(handle, "fasta"))
handle.close()

# print(data)
i = 0
compseq = []
# SeqIO.parse(...で読み込むとリストのようになる。forで処理したり。

for record in data:
    # print(record.id)
    # print(record.id)
    # print(record.seq)

    # 5'->3'に相補鎖を作る。
    compseq.append(record.seq.reverse_complement())
    # print("Complement:\n", compseq[i])
    i += 1


def display(sequence):
    length = len(sequence)
    num = 0
    for i in range(int(length / 50) + 1):
        for j in range(5):
            print(sequence[i * 50 + j * 10:i * 50 + j * 10 + 10], end=" ")
        print("")


m = 0
for seq in compseq:
    print(data[m].id)
    print("Complement:")
    display(seq)
    m += 1
