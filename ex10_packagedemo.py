from ex10_package01.module01 import SubDemo

a = SubDemo(11, 22)
a.hello()
a.bye()
b = SubDemo(56, 78)
b.hello()
b.bye()


# 在 __init__.py 裡提供一個 __all__ 變數，如下
# __all__ = ["module01", "module02", "module03"]
# 當 __all__ 被定義後，寫
from ex10_package01 import *
a = module01.SubDemo(12, 21)
a.hello()
a.bye()



