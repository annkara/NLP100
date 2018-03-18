# 19.1カラム目の出現頻度順

import collections

text = 'hightemp.txt'

with open(text) as f:
    col1s = [e.split('\t')[0] for e in f.readlines()]

c = collections.Counter(col1s)

for e in c.most_common():
    print(e[0])
