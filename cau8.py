sum = 0

for i in range(2, 101):
        for x in range(2, i):
            if i%x == 0:
                break
        else: 
            sum = sum + i

print(sum)       
