# タブをスペースに置換
'''
    確認用コマンド
    - cat hightemp.txt | tr '\t' ' '
    - cat hightemp.txt | sed s/"\t"/" "/g
'''

text = 'hightemp.txt'

with open(text) as f:
    
    for row in f:
        print(row.replace("\t", " " ), end='')

