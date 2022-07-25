# -*- coding: utf-8 -*-
import os
from icecream import ic

def 查看系统所有环境变量():
    for item in os.environ:
        name = item
        value = os.environ[item]
        ic(name, value)

查看系统所有环境变量()

环境变量文件路径 = os.environ["GITHUB_ENV"]
ic(环境变量文件路径)

with open(环境变量文件路径, 'r') as f:
    文本内容 = f.read()
ic(文本内容)

# 最后一行追加 123
with open(环境变量文件路径, 'a') as f:
    f.write(f"aaa=123")

os.environ['bbb'] = 'hello'


exit(0)