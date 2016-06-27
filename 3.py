#!/usr/bin/env python
"""
2016/06/15作成
翻訳配列の＊は開始コドン？？

 BiopythonWarning: Partial codon, len(sequence) not a multiple of three.
  Explicitly trim the sequence or add trailing N before translation.
  This may become an error in future.
  BiopythonWarning)
だそう。。。？
"""
from Bio import SeqIO
from Bio.Seq import Seq
import sys

#fasta read
loc = './samples/foxp3.fasta'
handle = open(loc, "rU")
data = list(SeqIO.parse(handle, "fasta"))
handle.close()

#2.pyから移植
def display(sequence):
    length = len(sequence)
    num = 0
    for i in range(int(length/50)+1):
        for j in range (5):
            print(sequence[i*50+j*10:i*50+j*10+10],end=" ")
        print("")

for record in data:
    if len(sys.argv) == 1:
        forward = record.seq
        display(forward.translate())

    elif sys.argv[1] == "-3":
        #3フレーム
        forward = record.seq
        print("0 frame shifted")
        display(forward.translate())
        print("\n1 frame shifted")
        display(forward[1:].translate())
        print("\n2 frame shifted")
        display(forward[2:].translate())

    elif sys.argv[1] == "-6":
        #6フレーム
        forward = record.seq
        back = record.seq.reverse_complement()
        print("0 frame shifted")
        display(forward.translate())
        print("\n1 frame shifted")
        display(forward[1:].translate())
        print("\n2 frame shifted")
        display(forward[2:].translate())

        print("reversed 0 frame shifted")
        display(back.translate())
        print("\nreversed 1 frame shifted")
        display(back[1:].translate())
        print("\nreversed 2 frame shifted")
        display(back[2:].translate())