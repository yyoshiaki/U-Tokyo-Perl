# coding=utf-8
import dbm
import sys
#import linecache

file = './samples/uniprot_sprot.dat'
db = dbm.open('./samples/cache_uniprot', 'r')

f = open(file, 'r')

ls = sys.argv[1]

line_pos = {}

"""
リストで取得するなら
for entry in ls:
    line_pos[entry] = db.get(entry)
db.close()
"""
line_pos[ls] = db.get(ls)
db.close()

print (line_pos)
# sort
"""
line_pos = sorted(line_pos.items(), key=lambda x: x[1])
print (line_pos)
"""

reading_line = 0

for k, v in line_pos.items():
    print(k)
    reading_line, line_num = v.split(b"_")
    reading_line = int(reading_line)
    line_num = int(line_num)
    print(reading_line," : ",line_num)
    #this_line = linecache.getline(file, reading_line+2)
    i = 0
    for line in f:
        if i >= reading_line and i <= reading_line + line_num:
            print(line, end = "")
        i += 1
