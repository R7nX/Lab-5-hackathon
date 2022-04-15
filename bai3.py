a = int(input("Input your number: "))

temp = 0

while a > 0:
    temp = temp + a%10
    a = a//10
print(f"Sum of all digit is{temp}")