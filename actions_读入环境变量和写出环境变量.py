# -*- coding: utf-8 -*-
import os
from icecream import ic

环境变量文件路径 = os.environ["GITHUB_ENV"]
ic(环境变量文件路径)

def 查看系统所有环境变量():
    for item in os.environ:
        name = item
        value = os.environ[item]
        ic(name, value)

def 设置环境变量(变量名,变量值):
    with open(环境变量文件路径, 'a') as f:
        f.writelines(f"{变量名}={变量值}")

def 读入文件变量文件(变量名,变量值):
    with open(环境变量文件路径, 'r') as f:
        读入文件变量文件 = f.read()
    ic(读入文件变量文件)


os.environ['bbb'] = 'hello' # 这个方式是不行的

查看系统所有环境变量()
exit(0)