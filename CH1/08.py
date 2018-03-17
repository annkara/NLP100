## 暗号文

def cipher(string):
    """あたえられ文字列の各文字を、以下の仕様で変換する。

    英小文字ならば(219 - 文字コード)の文字に置換する。
    それ以外の文字であれば、そのまま出力する。
    """

    result = ''
    for char in string:
        if char.islower():
            # ord(Char) -> Unicodeのコードポイントを返す。
            # chr(Unicode Point) -> 対応する文字を返す。
            result += chr(219-ord(char))
        else:
            result += char

    return result

if __name__ == '__main__':
    text = 'Azaq12wsx'
    print(cipher(text))
