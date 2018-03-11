# class Class_Name:
#
# 內建函數 help() 會顯示物件（包括類別）的資訊，
# dir() 則會把物件（包括類別）的所有屬性與方法以串列 (list) 列出
#
class Demo:
    # pass
    i = 9527

    def hello(self):
        print("hello")

help(Demo)
print(dir(Demo))

d = Demo()
print()
print(type(Demo))
print(type(d))
print()
print(d.i)
d.hello()