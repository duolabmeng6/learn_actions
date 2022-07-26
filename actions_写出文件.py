
def 写到文件(文件名, 欲写入文件的数据):
    变量类型 = type(欲写入文件的数据)
    if (变量类型 == dict or 变量类型 == list):
        # 解析为json文本
        欲写入文件的数据 = json.dumps(欲写入文件的数据)
    if (type(欲写入文件的数据) == str):
        欲写入文件的数据 = bytes(欲写入文件的数据, encoding="utf-8")

    with open(文件名, 'wb') as f:
        f.write(欲写入文件的数据)
    return True


def 读入文件(文件名):
    with open(文件名, 'rb') as f:
        return f.read(-1)


写到文件("content.txt","我叫哆啦b梦 大家好收费功能 add 121233 付款功能123")
