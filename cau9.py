# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# a = i + 1
# b = a + a
# c = b + a
# d = c + b


from re import A


sum = 0
a = 0
b = 1

for i in range(0,10):
    sum = sum + a
    next = a + b
    a = b
    b = next

print(sum)



"""
Nháp: 
sum = 0
next = 1
a = 1
b = 1

sum = 1
next = 2
a = 1
b = 2

sum = 2
next = 3



"""