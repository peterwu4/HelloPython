# built-in function

# 1. abs(x)
print("built-in functions")
print("1. abs(x):")
print(abs(1))
print(abs(-2))
print(abs(3.0))
print(abs(-4.0))
print(abs(True))
print(abs(False))

# 2. all(iterable) : 判斷 iterable 中所有元素是否為迭代器
print()
print("2. all(iterable):")
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

print(all("123")) # 字串
print(all([0, 1])) # 串列
print(all((0, 1))) # 序對
print(all({1:1, 2:2})) # 字典

# 3. any(iterable) ：判斷 iterable 中是否有任一元素為迭代器
print()
print("3. any(iterable):")
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

print(any("123")) # 字串
print(any([0, 1])) # 串列
print(any((0, 1))) # 序對
print(any({1:1, 2:2})) # 字典

# 4. ascii(object)	回傳參數物件的字串表達形式，如果該字串含有非 ASCII 字元，
#                   所有非 ASCII 字元會以 Unicode 跳脫字元的方式呈現
print()
print("4. ascii(object):")
print(ascii("哈囉"))
print(ascii(["你好", "hello"]))
print(ascii((0, 1)))
print(ascii({1:"yes", 2:"好的"}))

# 5. bin(x)	：回傳 x 的二進位形式
print()
print("5. bin(x):")
print(bin(32))
print(bin(128))
print(bin(512))
print(bin(2049))

# 6. bool([x])	：將 x 轉換為布林形式
print()
print("6. bool([x]):")
print(bool(0))
print(bool(1))
print(bool(0.0))
print(bool(0.1))
print(bool(""))
print(bool("0"))
print(bool([]))
print(bool([0]))

# 7. bytearray([source[, encoding[, errors]]])
# 將 source 轉換為 bytearray ，若 source 為字串，需提供 encoding ，也就是字串的編碼格式
print()
print("7. bytearray(source)")
d1 = b"12345"
print(type(d1))
d2 = bytearray(d1)
print(type(d2))
print(d2)
d2[0] = 54
print(d2)
d2[1] = 55
print(d2)
d2[2] = 56
print(d2)
d2[3] = 57
print(d2)
d2[4] = 58
print(d2)

# 8. bytes([source[, encoding[, errors]]])
# 將 source 轉換為 bytes ，若 source 為字串，需提供 encoding ，也就是字串的編碼格式
print()
print("8. bytes(source)")
d1 = "!@#"
print(type(d1))
d2 = bytes(d1, "utf8")
print(type(d2))
print(d2)
for i in d2:
    print(i)

d3 = bytes(d1, "ascii")
print(d3)
for i in d3:
    print(i)

