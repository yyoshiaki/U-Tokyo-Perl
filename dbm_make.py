import dbm
import sys

#from Bio import SwissProt


file = './samples/uniprot_sprot.dat'
db_file = './samples/cache_uniprot'

current_id = ""
current_line = 0
current_line_num = 0
dic = {}

f = open(file)
print("opening %s ..." % file)

for line in f:

    if line[0:2] == "ID":
        id_fin_pos = line.find("      ")
        current_id = line[5:id_fin_pos]
        current_line_num = 0
        #dic[current_id] = str(current_line)
        sys.stdout.write("\r%s" % current_id)
        sys.stdout.flush()
    if line[0:2] == "//":
        dic[current_id] = str(current_line - current_line_num) + "_" +str(current_line_num)
    current_line += 1
    current_line_num += 1

f.close()
print("complete")
"""
# いくつかの値を設定する
for record in SwissProt.parse(open(file)):
    db[record.entry_name] = record.sequence
"""

print("extracting %s" % db_file)

# データベースを開く、必要なら作成する
db = dbm.open(db_file, 'c')
for k,v in dic.items():
    db[k] = v
    sys.stdout.write("\r%s" % k)
    sys.stdout.flush()
# 終了したらcloseします。


print("writen")
db.close()
print("finished making DB.")
