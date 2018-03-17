# 14. 先頭からN行を出力
'''コマンド
    - head -10 hightemp.txt
'''

import sys

# 引数のチェック
if len(sys.argv) > 2:
    print('Usage : python 14.py <Integer>')
    sys.exit()

try:
    row_number = int(sys.argv[1])
except ValueError as e:
    print('整数に変換できません。')
    sys.exit()

text = 'hightemp.txt'
with open(text, 'rt') as f:
    count = 0
    # enumerate()を利用すれば、count変数は不要になる。
    # for i, line in enumerate(f) で、iがcount変数の代わりになる。
    for row in f:
        if count == row_number:
            break
        print(row, end='')
        count+=1
