## Typoglycemia
'''
    Typoglycemiaとは

    単語の頭と末尾をそのままに、内部の文字を入れ替えた文章のこと。
'''

import random

def typoglycemia(text):
    """与えられたテキストからTypoglycemiaな文章を返す。

    ただし、長さが4以下の単語は並び替えない。

    """
    separeted = text.split()
    result = []
    for word in separeted:
        if len(word) <= 4:
            result.append(word)
            continue

        initial = word[0]
        end = word[len(word)-1]
        mid = list(word[1:len(word)-1])
        random.shuffle(mid)
        result.append(initial + ''.join(mid) + end)

    return result

if __name__ == '__main__':

    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

    print(' '.join(typoglycemia(text)))
