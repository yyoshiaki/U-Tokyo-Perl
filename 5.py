from Bio import SwissProt
from mod.unimod import Search
import time

file = './samples/uniprot_sprot.dat'

#records = SwissProt.parse(open(file))
#今回は速度アップのためパースしない。

question = input("検索文字列を , で区切って入力。空白なら「NAKAI」と「KENTA」で検索します。")
if question == "":
    list = ["NAKAI","KENTA"]
else:
    list = question.split(',')

t1 = time.time()
header_filter = ["SQ"]

search = Search(file,list,header_filter)
result = search.search()

for i in range(len(list)):
    print("keyword : ", list[i], "\n", result[i], "\n")


t2 = time.time()
print("time : ",t2-t1)