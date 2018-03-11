# 控制結構(control structure)有三種，分別是
# 1. 循序(sequence)、
# 2. 選擇(selection)、
#	if
#	if-else
#	if-elif
#	if-elif-else

a = "h"
b = "k"

if a == b:
    print("Welcome to my world!")
else:
    print("How do you do?")

if a == "a":
    print("Yes!")
else:
    if a == b:
        print("No!")
    else:
        print("What?")

if a == "a":
    print("Yes!")
elif a == b:
    print("No!")
else:
    print("What?")

# 3. 重複(repetition)
#	1. 控制變數初始設定
#	2. 迴圈結束條件測試
#	3. 調整控制變數的值
#
# for loop:
#
a = "abcdefghijklmnopqrstuvwxyz"
i = 0

for x in a:
    print(x, end=" ")
    i += 1

    if i % 10 == 0:
        print()

print()
# print()函數，預設的參數 end，指定印出X之後的結尾符號，
# 如沒指定，就會印出新行。

# nested loop
# 九九乘法表
for x in range(10):
    for y in range(10):
        print(x * y, end=" ")
    print()

# range()為內建函數，會自動產生一個從0～n-1的串列(list)

# 用break, continue 關鍵字來輸出九九乘法表
print()
for x in range(10):
    if x == 0:
        continue
    elif x == 8:
        break

    for y in range(10):
        if y == 0:
            continue
        print(x * y, end=" ")
    print()

#
# while loop:
#
print()
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1

print("1 + 2 + 3 + ... + 98 + 99 + 100 =", sum)

# nested loop
# 用while loop輸出九九乘法表
print()
i = 1
j = 1
while i <= 9:
    while j <= 9:
        print(i * j, end=" ")
        j += 1
    i += 1
    j = 1
    print()

#
print()
i = 1
j = 1
while i <= 9:
    if i == 8:
        break

    while j <= 9:
        if j == 4:
            j += 1
            continue

        print(i * j, end=" ")
        j += 1

    i += 1
    j = 1
    print()


