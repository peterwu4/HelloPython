# data type: integer, float-pointing number, complex number, expression(運算式)
# conversion:

a = 1
b = 2.1
c = 3 + 4j
d = 5 + 6.2j
e = 7.3 + 8.4j
f = 7.3 - 8.4j

print(a + b, a + c, a + d, a + e)
print(b + c, b + d, b + e)
print(c + d, c + e)
print(e + f)


print()
# 內建函式： int(), float(), complex()

a = 1
b = 2
c = 3.1
d = 3.6

print(int(a + c), int (a + d))
print(float(a + b))
print(complex(a + b))


print()
# complex number: attribute(屬性): real, imag

a = 3 + 5j
print("a =", a)

b = 3 - 5j
print("b =", b)

c = a * b
if c.imag == 0:
	c = c.real
print("c =", c)


