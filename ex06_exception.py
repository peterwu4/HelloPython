# exception
#
# 1. try-except
#
a = 22
b = 33

print("section 1:")
try:
    if a < b:
        print(n)
except:
    print("except")

print("after exception 1...")

print("")
print("section 2:")
try:
    if a > b:
        print(n)
except:
    print("except")
else:
    print("else except")  # 這裡因為 a > b 為假，所以例外不會發生，因此程式執行 else 的部份。

print("after exception 2...")

print("")
print("section 3:")
try:
    if a < b:
        print(n)
except:
    print("except")
else:
    print("else except")
finally:
    print("finally") # 若加入另一個關鍵字 finally ，無論例外有沒有發生都會執行 finally 後的程式區塊。

print("after exception 3...")

#
# 2. raise
#
# 例外 (except) 除了會由直譯器 (interpreter) 自動發生外，
# 我們也可以自己在程式中利用 raise 陳述 (raise statement) 引起例外。
# raise 為關鍵字 (keyword) 之一，用來引起例外。

print("")
print("section 4: raise")
try:
    raise NameError
except NameError:
    print("something wrong")

print("after exception 4...")
