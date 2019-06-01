# expression = operand + operator (運算式為運算元與運算子的組合)
# 運算元可以是：
#	變數(variable)
#	字面常數(literal)
#	物件的定義形式
# 運算式會計算出一個結果，通常會是一個物件(object)，
# Python中的物件由類別(class)定義，一種類別也被稱為一種型態(type)，
# 因盤運算式的結果通常也具有型態。

if True:  # True is a literal(operand)
    print("Hello world!")

print("")
print("1. 算術運算子")
# 1. 算術運算子(arithmetic operator)
# +, -, *, /, **(指數), //(整數除法), %

print("a = 22, b = 33")
a = 22
b = 33

print(a + b)
print(a - b)
print(a * b)
print(a ** b)
print(a / b)
print(a // b)
print(a % b)

print ("a = 22.2, b = 33.3")
a = 22.2
b = 33.3

print(a + b)
print(a - b)
print(a * b)
print(a ** b)
print(a / b)
print(a // b)
print(a % b)

# 字串(string)物件或資料型態(data type)下
# 加法運算子(additive operator)用於字串的連結(concatenation)
# 乘法運算子(multiplicative operator)用於字串的重複
print("a = \"22\", b =\"33\"")
a = "22"
b = "33"

print(a + b + a * 4 + b * 4)
print((a + b) * 5)
print(a * 5 + b * 5)
print(a * 10)

print("")
print("2. 位元運算")
# 2. 位元運算(bit operation)
#	<<	shiht bits left
#	>>	shift bits right
#	&	bitwise AND
#	|	bitwise inclusive OR
#	^	位元互斥或(bitwise exclusive OR) xor
#	~	位元相反(bit inversion) not

print("a = 5, b = 3")
a = 5  # 0000 0000 0000 0101
b = 3  # 0000 0000 0000 0011

print(~a)
# 1111 1111 1111 1010
print(b << 2)
print(b >> 2)
print(a & b)
print(a | b)
print(a ^ b)

print()
print("3. 關係運算子")
# 3. 關係運算子(comparison operator)
#	<
#	>
#	<=
#	>=
#	==
#	!=

print("a = 12, b = 22")
a = 12
b = 22

if a < b:
    print("a < b")

if a <= b:
    print("a <= b")

if a > b:
    print("a > b")

if a >= b:
    print("a >= b")

if a == b:
    print("a == b")

if a != b:
    print("a != b")

print()
print("4. 指派運算子")
# 4. 指派運算子(assignment operator) =
# 和其他運算子(operator)合用，如算術運算子(arithmetic operator)及
# 位元運算子(bitwise operator)
#	=
#	+=
#	-=
#	*=
#	**=
#	/=
#	//=
#	%=
#	&=
#	^=
#	|=
#	<<=
#	>>=

a = 1
print("a=", a)

a += 2
print(a)

a -= 1
print(a)

a *= 22
print(a)

a **= 3
print(a)

a /= 7
print(a)

a //= 5
print(a)

a %= 3
print(a)

print("")
a = 248
print("a=", a)

a &= 7
print(a)

a |= 192
print(a)

a ^= 63
print(a)

a <<= 3
print(a)

a >>= 5
print(a)

print()
print("5. 邏輯運算子")
# 5. 邏輯運算子(logical operator)
#	and
#	or
#	not

a = 12
b = 22

if a > b and a != b:
    print("a > b")
if a < b and a != b:
    print("a < b")

a = 12
b = 0

if a:
    print("a is true")

if b:
    print("b is true")

if not a:
    print("a is false")

if not b:
    print("b is false")

print()
print("6. is operation")
# 6. is - Python的關鍵字之一，用來判斷兩個物件(object)是否相等，
# 也就是判斷由內建函數(function) id()回傳的id號碼是否一樣。

a = 12
b = 12
c = 22

if a is b:
    print("a is b")

if a is c:
    print("a is c")

# is 與 not 連用
if a is not b:
    print("a is not b")

if a is not c:
    print("a is not c")

# 不可變的(immutable)的資料型態，例如字串(string)，
# 	相同內容的字串也會是相同的物件
# 可變的(mutable)的資料型態，例如串列(list)
#	就算有相同的內容，實際上仍會是不同的物件

a = []
b = []

if a is b:
    print("a is b")

if a is not b:
    print("a is not b")

print()
print("7. in operation")
# 7. in 為Python的關鍵字(keywork)之一，用來判複合資料型態
# (compound data type)之中是否有某個元素(element)，也是就在
# 可包含其他物件的物件之中，判斷是否有某個物件。

a = "0123456789"  # string
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # list
print("a=", a)
print("b=", b)

if "5" in a:
    print("'5' in a")

if "a" in a:
    print("'a' in a")

if "5" in b:
    print("'5' in b")

if 5 in b:
    print("5 in b")

if "5" not in a:
    print("'5' not in a")

if "a" not in a:
    print("'a' not in a")

if "5" not in b:
    print("'5' not in b")

if 5 not in b:
    print("5 not in b")

for i in a:
    print(i)

print()
print("8. lambda operation")
# 8. lambda 為Python的關鍵字之一，用以建立無名函數(anonymous function)。

f = lambda x: x ** x
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))

g = lambda x, y: x * y
print(g(1, 6))
print(g(2, 7))
print(g(3, 8))
print(g(4, 9))
print(g(5, 10))


# 函數物件(object)
def lambda_demo(n):
    return lambda x: x ** n + x * 2 + 1


i = 1
f = lambda_demo(2)
while i <= 10:
    print(f(i))
    i += 1

print()
print("9. del operation")
# 9. del 為Python的關鍵字之一，用來刪除物件(object)

a = 1
b = 2
c = 3
d = 4
e = 5

print(a)
print(b)
print(c)
print(d)
print(e)

del a
del b
del c
del d
del e

# print(a) # X 由於已經刪除變數a，因為程式發生錯誤中斷執行。
# print(b)
# print(c)
# print(d)
# print(e)
