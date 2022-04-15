
a = int(input("Input a side of a triangle: "))
b = int(input("Input a side of a triangle: "))
c = int(input("Input a side of a triangle: "))

if (a + b) > c and (a+c) > b and (b+c) > a:
    print("It can form a triangle")
else: 
    print("It can not form a triangle")