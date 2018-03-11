# id()取得物件的id號碼，其為整數
# type()，得到'type'類別的物件
# print()印出物件的數值
a = 33
print(type(id(a)))
print(type(type(a)))
print(type(print(a)))

a = "33"
print(type(id(a)))
print(type(type(a)))
print(type(print(a)))

# 物件的屬性(attribute)及方法(methon)，透過變數運用小數點符號.存取
a = 0.0
print(a.__str__())
print(a.__bool__())

a = 33
print(a.__str__())
print(a.__bool__())

a = "33"
print(a.__str__())
#print(a.__bool__()) X
print(a.__len__())
