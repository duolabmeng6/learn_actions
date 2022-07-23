# -*- coding: utf-8 -*-
from icecream import ic
# 打印系统所有的环境变量
import os
for item in os.environ:
    变量名 = item
    变量值 = os.environ[item]
    ic(变量名, 变量值)

exit()
