# -*- coding: utf-8 -*-
import os

def 查看系统所有环境变量():
    from icecream import ic
    # 打印系统所有的环境变量
    for item in os.environ:
        name = item
        value = os.environ[item]
        ic(name, value)

查看系统所有环境变量()

环境变量文件路径 = os.environ["GITHUB_ENV"]
with open(环境变量文件路径, 'r') as f:
    文本内容 = f.read()
print(文本内容)

# 最后一行追加 123
with open(环境变量文件路径, 'a') as f:
    f.write(f"aaa=123")


exit(0)