# module
# 一個 .py 檔案就是一個模組(module)，例如以下程式

class Demo:
    __x = 0

    def __init__(self, i):
        self.__i = i
        Demo.__x += 1

    def __str__(self):
        return str(self.__i)

    def hello(self):
        print("hello " + self.__str__())

    @classmethod
    def getX(cls):
        return cls.__x

class Other:
    def __init__(self, k):
        self.k = k

    def __str__(self):
        return str(self.k)

    def hello(self):
        print("hello, world")

    def bye(self):
        print("Good-bye!", self.__str__())

class SubDemo(Demo, Other):
    def __init__(self, i, j):
        super().__init__(i)
        self.__j = j

    def __str__(self):
        return super().__str__() + "+" + str(self.__j)

if __name__ == "__main__": # 如此，當被import時下面的程式碼就不會被執行
#if 1:
    print("module:")
    a = SubDemo(12, 34)
    a.hello()
    a.bye()
    b = SubDemo(56, 78)
    b.hello()
    b.bye()
