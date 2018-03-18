# 各行を3カラム目の数値の順にソート

text = 'hightemp.txt'

with open(text) as f:
    rows = f.readlines()

# sortedメソッドには、ソートで使用するキーを指定できる。
# キーには、lambda、関数、メソッドが使用できる。
# 今回は入力データの3カラム目を利用している。
after_sort = sorted(rows, key=lambda el: float(el.split('\t')[2]))

for row in after_sort:
    print(row, end='')
