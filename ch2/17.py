# 1列目の文字列の異なり
'''コマンド
    cat hightemp.txt | cut -f 1 | sort | uniq
'''
text = 'hightemp.txt'

with open(text) as f:
    col1s = set([e.split('\t')[0] for e in f.readlines()])

for e in col1s:
    print(e)
