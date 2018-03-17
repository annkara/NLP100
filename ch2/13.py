# col1.txtとcol2.txtをマージ
'''確認コマンド
    paste <FILE1> <FILE2>
'''


with open('col1.txt', 'rt') as in_file, \
        open('col2.txt', 'rt') as in_file2:
            rows1 = []
            rows2 = []

            for row1 in in_file:
                # ファイルから読み込むと、改行付きのため
                # rstrip()で削除する。
                rows1.append(row1.rstrip())

            for row2 in in_file2:
                rows2.append(row2.rstrip())

# zip関数使う必要はなかったが、慣れのために使用した。
# 使用しなかったら、一行ずつ読み込みながら出力すれば良い。
for merged_row in zip(rows1, rows2):
    print('\t'.join(merged_row))
