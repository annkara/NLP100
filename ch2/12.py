## 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
'''確認コマンド
    - cat hightemp.txt | cut -f 1,2
'''

text = "hightemp.txt"
with open(text, 'rt') as in_file:
    col1 = []
    col2 = []
    for row in in_file:
        cols = row.split('\t')
        col1.append(cols[0])
        col2.append(cols[1])

out1 = "col1.txt"
with open(out1, 'wt') as out_file:
    print(*col1, sep='\n', file=out_file)

out2 = "col2.txt"
with open(out2, 'wt') as out_file2:
    print(*col2, sep='\n', file=out_file2)

