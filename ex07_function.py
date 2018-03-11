# function
#
# def function_name():
#   pass # pass 為關鍵字之一，其為什麼事情都不做的陳述(statement)
#

def fun():
    i = 0
    while i < 6:
        #print(i)
        i += 1

fun()
fun()
fun()

#
# 1. 函數回傳值(function return value)
#
# def function_name():
#   pass
#
#   return something
#
print()
print("0: fun()")
a = fun()
print(a)
print(type(a))

print()
print("1: sum()")
def sum():
    i = 1
    sum = 0
    while i <= 100:
        sum += i
        i += 1
    return sum

a = sum()
print(a)
print(type(a))


# 函數定義中沒有限制 retrun 陳述的數量，可依需要自行設置，如
print()
print("2: other()")
def other():
    if 1:
        return 10
    else:
        return "hello"

a = other()
print(a)
print(type(a))


# 函數定義中也沒有限制回傳值的數量，可在 retrun 陳述中以逗號分隔回傳值，例如
print()
print("3: test()")
def test():
    return 10, "hello"

a, b = test()
print(a)
print(b)
print(type(a))
print(type(b))

#
# 2. 函數參數(function parament)
#
# def function_name(arg1, arg2):
#   pass
#
#   return something
#
# 嚴格的學院區分函數定義時，小括弧中的變數為參數，
# 呼叫函數時實際提供的數值稱為引數 (argument)
#
print()
print("4: function parameter")
def sum(n):
    i = 1
    sum = 0
    while i <= n:
        sum += i
        i += 1
    return sum

print("1 + 2 + ... + 199 + 200 = ", sum(200))
print("1 + 2 + ... + 299 + 300 = ", sum(300))
print("1 + 2 + ... + 399 + 400 = ", sum(400))
print("1 + 2 + ... + 499 + 500 = ", sum(500))
print("1 + 2 + ... + 599 + 600 = ", sum(600))
print("1 + 2 + ... + 699 + 700 = ", sum(700))

print()
def sum(a, b):
    return a + b

print(sum(1, 1))
print(sum(1, 2))
print(sum(2, 3))
print(sum(3, 5))
print(sum(5, 8))
print(sum(8, 13))


# 數學上有個有趣的費博納西數列 (Fibonacci series) ，
# 頭兩個數字為 0 和 1 ，之後的數字為前兩個數字的和。
def fib(n):
    i = 1
    j = 1
    while sum(i, j) < n:
        i, j = j, sum(i, j)

    return j

print()
print("fib(n):")
print(fib(100))
print(fib(200))
print(fib(300))
print(fib(400))
print(fib(700))
print(fib(1000))


#
# 3. 預設參數
#
# 函數 (function) 的參數 (parameter) 可以提供預設值 (default argument) ，
# 也就是可以在參數列 (paramenter list) 直接將參數指派數值 (value) ，形式如下
#
# def function_name(arg1 = default1, arg2 = default2):
#    pass
#
#    return something
#
def hello(name = "John"):
    print("Hello, ", name, "!")

print()
print("default parameter")
hello("Mary")
hello()
hello("9527")
hello("Tony")
hello()
hello("Sherry")

def hello(age, name = "John", day = "Monday"):
    print("Hello, ", name, "!")
    print("Today is", day)
    print("You are", age, "years old.")

hello(12, "Mary", "Sunday")
hello(name = "Bill", age = 33)
hello(day = "Wednesday", age = 23, name = "9527")

#
# 4. 不定個數參數
#
# 函數 (function) 可以有不定個數的參數 (parameter) ，也就是可以在參數列
# (paramenter list) 提供任意長度的參數個數，形式如下
#
#def function_name(*arguments, **keywords):
#    pass
#
#    return something
#
# *arguments 就是參數識別字 (identifier) 前面加上一個星號，與
# **keywords 參數識別字前面加上兩個星號，這是兩種不同的不定參數設定模式。
# 前者 *arguments 會把多的參數當成一組序對 (tuple) ，
# 後者 **keywords 則是會把多的參數當成一組字典 (dictionary) ，
# 因此需額外提供參數名稱當 key 。
#
# *arguments 與 **keywords 可以同時使用，但是任一函數只能有一個 *arguments
# 或 **keywords 。以下程式示範 *arguments
def hello(age, *name):
    for n in name:
        print("Hello,", n, "!")
        print("You are", age, "years old.")

print()
print("4. 不定個數參數：")
hello(13, "John", "Mary", "9527")

# 以下程式示範 **keywords
def hello(**name):
    for n in name:
        print("Hello", n, ", you're", name[n])

hello(one = "John", two = "Mary", three = "9527")

def hello(*name, **age):
    for n in name:
        print("Hello,", n, "!")

    for n in age:
        print("You are", age[n], "years old.")

hello("John", "Mary", "9527", one = 13, two = 25, three = 33)
# ps:感覺*arguments像list{, ,}；**keywords像array[]

#
# 5. 產生器
#
# return: 函數會直接回傳數值(value)
# yield: 可使函數產生數值，而不會結束函數執行，這樣的函數被稱為產生器函數
#        generator function
def fun(n):
    for i in range(2, n):
        yield i

print()
print("5. 產生器：")
for j in fun(7):
    print(j)

def reverse(data):
    for i in range(len(data) - 1, -1, -1): # range(start, end, step)
        yield data[i]

for i in reverse("wonderful"):
    print(i * 33)  # 字串的乘法=字串重覆的次數

def t(data):
    for i in data:
        if i in "aeiou":
            yield 1
        if i not in "aeiou":
            yield 0

s = "perpetual"
d = []

print(s)
for i in t(s):
    d.append(i)
print(d)
print()

#
# 6. 變數範圍
#
# 函數 (function) 內的變數 (variable) 包括參數 (parameter) 都稱為區域變數
# (local variable) ，這意思是說區域變數的使用範圍 (scope) 限於函數的區塊
# (block) 內，一旦離開該區塊範圍，便無法繼續使用原本在區塊內的變數值。
def outer(a):
    def inner(a):
        a += 1
        print("inner a =", a)

    a += 1
    inner(a)
    print("outer a =", a)

a = 12
print()
print("6. 變數範圍：")
print("global a =", a)
outer(a)
print("global a =", a)

# 如果想要在函數區塊中使用範圍外的變數，可使用關鍵字 (keyword) 中的
# global 及 nonlocal 宣告範圍外的變數名稱。

def outer(a):
    def inner():
        # global a
        nonlocal a
        a += 1
        print("inner a =", a)

    a += 1
    inner()
    print("outer a =", a)

a = 12
print()
print("global a =", a)
outer(a)
print("global a =", a)
