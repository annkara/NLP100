## 07.テンプレートによる文生成

def str_template(x, y, z):
    '''
    x時のyはzというテンプレートに当てはめた文字列を返す。
    '''

    x_, y_, z_ = str(x), str(y), str(z)
    template = '{}時の{}は{}'

    return template.format(x_, y_, z_)

if __name__ == '__main__':
    print(str_template(x=12, y='気温', z=22.4))
