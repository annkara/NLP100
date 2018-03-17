## n-gram
"""
 n-gramとは
  任意の文字列や文書を連続したn個の文字で分割するテキスト分割方法のこと。
  特にnが1のことをユニグラム、2の場合をバイグラム、3の場合をトライグラム
  と呼ぶ。

"""

def n_gram(n, sequence):
    '''
    引数nに指定された単語n-gramのリストと文字n-gramのリストを返す。
    '''

    # 単語n-gramのリストを生成する
    num   = n
    words = sequence.split()
    start = 0
    end   = len(words)
    word_n_gram = []
    while num <= end:
        word_n_gram.append(words[start:num])
        num += 1
        start +=1

    # 文字n-gramのリストを生成する
    chars = []
    for char in sequence:
        chars.append(char)
    num   = n
    start = 0
    end   = len(chars)
    char_n_gram = []
    while num <= end:
        char_n_gram.append(chars[start:num])
        num += 1
        start += 1

    return (word_n_gram, char_n_gram)

if __name__ == "__main__":
    print(n_gram(2, "I am an NLPer"))
