#!/usr/bin/env python

"""
2016/06/15
python で書き直してみた。
標準偏差は練習としてnumpyで求めたがちょっと大げさな気もする。
"""
import numpy as np

s = 0
c = 0
ls = []

while True:
    inp = input('input int. or if you want to exit, command "exit".\n')
    #input()は文字列で格納される。

    if inp.isdigit():
        c += 1
        s += int(inp)
        ls.append(int(inp))
    elif inp == 'exit':
        print("sum = ", s)
        print("ave = ",s/c)
        print("SD = ",np.std(ls))

        exit()
    print ("sum = ",s)
    print("count = ",c)
    print(ls)