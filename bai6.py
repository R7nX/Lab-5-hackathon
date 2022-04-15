


for i in range(0,100000): 
    x = i
    temp = 0
    while i > 0:
        temp = temp*10 + i%10
        i = i//10
    # str1 = str(x)
    # str2 = str1[::-1]
    if x == temp:
        print(temp, end = ", ")
    