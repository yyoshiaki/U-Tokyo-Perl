from Bio import SwissProt
import time

"""
Biopython version
2016/06/22
"""

file = './samples/uniprot_sprot.dat'

question = input("検索文字列を , で区切って入力。空白なら「NAKAI」と「KENTA」で検索します。")
if question == "":
    list = ["NAKAI","KENTA"]
else:
    list = question.split(',')

t1 = time.time()

#result_listを初期化
result = [{} for i in range(len(list))]

for record in SwissProt.parse(open(file)):
    for i in range(len(list)):
        if record.sequence.find(list[i]) != -1:
            result[i][record.entry_name] = record.sequence.find(list[i])




for i in range(len(list)):
    print("keyword : ", list[i], "\n", result[i], "\n")


t2 = time.time()
print("time : ",t2-t1)