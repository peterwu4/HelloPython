# class Class_Name:
#
# 內建函數 help() 會顯示物件（包括類別）的資訊，
# dir() 則會把物件（包括類別）的所有屬性與方法以串列 (list) 列出
#
# 1. 建構子(constructor) __init__()
#
# 2. __str__(): 方法，回傳實體物件(instance object)的字串表達形式
#
# 3. __doc__: 屬性，三引號字串定義的文字，屬於類別的說明文件
#   """first line
#   senond line"""
class Demo:
    #pass
    def __init__(self, i):
        self.i = i

    def hello(self):
        print("hello", self.i)

print("helo(Demo):")
help(Demo)
print("dir(Demo):")
print(dir(Demo))

d = Demo(1112)
print()
print(type(Demo))
print(type(d))
print()
print(d.i)
d.hello()

a = 22 #1
print()
print(a.__str__())
print(type(a.__str__()))
print(a.__doc__)

a = 22.0 #2
print()
print(a.__str__())
print(type(a.__str__()))
print(a.__doc__)

a = "22" #3
print()
print(a.__str__())
print(type(a.__str__()))
print(a.__doc__)

a = [22] #4
print()
print(a.__str__())
print(type(a.__str__()))
print(a.__doc__)

a = Demo(22) #5
print()
print(a.__str__())
print(type(a.__str__()))
print(a.__doc__)

class Demo2:
    """
Demo2 -
        learning Phthon class..."""

    def __init__(self, i):
        self.i = i

    def __str__(self):
        return (self.i)

a = Demo2(22) #6
print()
print(a.__str__())
print(type(a.__str__()))
print(a.__doc__)

#
# 4.
# 類別屬性(class attribute)
# 實體屬性(instance attribute)
#
# 兩者有何差別呢？
# 通常類別屬性需要用類別名稱來存取，但若兩者的識別字 (identifier) 不同，
# 實體物件 (object) 也可以存取類別屬性。
# 若是類別屬性與實體屬性的識別字相同，實體物件只能存取實體屬性。
#
class Demo3:
    i = 0 #類別屬性
    x = 0

    def __init__(self, i):
        self.i = i #實體屬性
        Demo3.i += 1
        Demo3.x += 1

    def __str__(self):
        return str(self.i)

    def hello(self):
        print("hello", self.i)

print()
print("Demo3:")
print("There are", Demo3.x, "instances.")
a = Demo3(1122)
a.hello()
print("a.x =", a.x)
b = Demo3(3344)
b.hello()
print("b.x =", b.x)
c = Demo3(5566)
c.hello()
print("c.x =", c.x)
d = Demo3(7788)
d.hello()
print("d.x =", d.x)
e = Demo3(9900)
e.hello()
print("e.x =", e.x)
print("After all, there are", Demo3.x, "instances.")
e.x = 100
print(e.x)
print(a.x)
print(c.x)
print(Demo3.x)

#
# 5. static 方法與類別方法
# Python 類別 (class) 的方法 (method) 除了實體方法外，還有 static 方法與類別方法。
#
# static 方法的作用與函數 (function) 相同，也就是說不需要建立實體物件 (instance)
# 就可以使用，然而 static 方法仍是類別的一部分，因此呼叫 (call) 類別方法需連用類別名稱。
#
# 類別方法需要一個特別的參數 (parameter) ，習慣上使用 cls ，這與實體方法的 self 類似，
# 不同的是 cls 用來存取類別的屬性 (attribute) 。
#
class Demo4:
    def __init__(self, i):
        self.i = i

    def __str__(self):
        return str(self.i)

    def hello(self):
        print("hello", self.i)

    def statictest():
        print("this is static method...")

    statictest = staticmethod(statictest)

    def classtest(cls):
        print("this is class method...")
        print("the class name is", cls.__name__)

    classtest = classmethod(classtest)

print()
print("Demo4:")
Demo4.statictest()
Demo4.classtest()
print()
a = Demo4(9527)
a.hello()
a.statictest()
a.classtest()

# 另一種利用修飾符號 @ ，如下例
class Demo5:
    def __init__(self, i):
        self.i = i

    def __str__(self):
        return str(self.i)

    def hello(self):
        print("hello", self.i)

    @staticmethod
    def statictest():
        print("this is static method...")

    @classmethod
    def classtest(cls):
        print("this is class method...")
        print("the class name is", cls.__name__)

print()
print("Demo5:")
Demo5.statictest()
Demo5.classtest()
print()
a = Demo5(9527)
a.hello()
a.statictest()
a.classtest()

#
# 6. 屬性的封裝
#
# 類別的屬性預設是公開的(public)
#
# 在屬性識別字(identifier)加上連續兩個底線符巳 => private
#
class Demo6:
    __x = 0

    def __init__(self, i):
        self.__i = i
        Demo6.__x += 1

    def __str__(self):
        return str(self.__i)

    def hello(self):
        print("hello", self.__i)

    @classmethod
    def getX(cls):
        return cls.__x

print()
print("Demo6: 屬性的封裝")
a = Demo6(9527)
a.hello()
print("Demo6.__x =", Demo6.getX())
#print("Demo6.__x =", Demo6.__x) # 不能直接存取

#
# 7. 繼承(inheritance)
#
# 繼承的格式
# class SubDemo(Demo)
#    pass
#
# ps:  Python所有的類別繼承自 object 這個類別，因此以下寫法
# class Demo:   =     class Demo(object)
#    pass                pass
#
# 類別名稱後的小括弧中註明父類別
#
class Demo7:
    __x = 0

    def __init__(self, i):
        self.__i = i
        Demo7.__x += 1

    def __str__(self):
        return str(self.__i)

    def hello(self):
        print("hello", self.__i)

    @classmethod
    def getX(cls):
        return cls.__x

class SubDemo(Demo7):
    pass


print()
print("Demo7: 繼承")
a = SubDemo(1234)
a.hello()
print(a.getX())
b = SubDemo(5678)
b.hello()
print(b.getX())
c = SubDemo(9012)
c.hello()
print(c.getX())
d = SubDemo(3456)
d.hello()
print(b.getX()) #類別函式call那個物件都一樣
e = SubDemo(7890)
e.hello()
print(c.getX())

#
# 「繼承」是程式語言社群習慣用詞，英文動詞原文為 inherit ，
# 意思泛指從什麼得到什麼，所以生物學中的「遺傳」也是用這個詞。
# 實際上物件導向程式設計的繼承機制相當複雜，然而中文的繼承常用於某物不再，
# 另物將起的意思，譬如我繼承某某的精神，雖然某某不見得已死，可是將來要付出
# 努力的卻是我而非某某，因而這裡的意思中文用「遺傳」比較恰當，
# 子代會從親代遺傳性狀，子代與親代也會並存一段時間，這就沒有某物不再的意含了。
#

#
# isinstance()
# 判斷某一個物件是否為某一個類別所建構的實體 (instance) ，
# 若真則回傳 True ，否則回傳 False 。
#
# issubclass()
# 判斷某一個類別是否為另一個類別的子類別
#
a = Demo7(1234)
a.hello()
b = SubDemo(5678)
b.hello()
print(isinstance(a, Demo7))
print(isinstance(a, SubDemo))
print(isinstance(b, Demo7))
print(isinstance(b, SubDemo))
print(issubclass(SubDemo, Demo7))
print(issubclass(Demo7, SubDemo))

#
# 8. 方法改寫(method override)
#
# 一般來說，沒有設定成私有的屬性及方法都會被繼承，
# 子類別可由父類別公開的方法存取父類別私有的屬性。
#
# 子類別也可依需要改寫 (override) 父類別的方法，
# 這是說子類別需要用到與父類別具有相同名稱的方法，
# 但是子類別需要的功能有所修改、擴充或增加，
# 因此當子類別裡頭定義與父類別相同名稱的方法時，就會改寫父類別的方法。
# 經過改寫，子類別的方法完全屬於子類別所有。
#
class Demo8:
    __x = 0

    def __init__(self, i):
        self.__i = i
        Demo8.__x += 1

    def __str__(self):
        return str(self.__i)

    def hello(self):
        print("hello", self.__str__())

    @classmethod
    def getX(cls):
        return cls.__x

class SubDemo8(Demo8):
    def __init__(self, i, j):
        super().__init__(i)  # 呼叫父類別的方法super()
        self.__j = j

    def __str__(self):
        return super().__str__() + "+" + str(self.__j)

print()
print("Demo8: method override")
a = SubDemo8(12, 34)
a.hello()
print("a.__x =", a.getX())
b = SubDemo8(56, 78)
b.hello()
print("b.__x =", b.getX())
print()
print("a.__x =", a.getX())
print("b.__x =", b.getX())


#
# 9. 多重繼承
#