# 15. 末尾のN行を出力

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

if row_number <= 0:
    print('0より大きい自然数を指定してください')
    sys.exit()

text = 'hightemp.txt'
with open(text, 'rt') as f:
    lines = f.readlines()
    for line in lines[-row_number:]:
        print(line[:-1])
