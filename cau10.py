num = int(input("Enter your number: "))
sum = 0


for i in range(1,num):
    if num % i == 0:
        sum = sum + i
if sum == num:
        print("Đây là số hoàn hảo")
else: 
        print("Đây không phải là số hoàn hảo")
