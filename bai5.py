a = int(input("Enter n: "))

# mid = len(a)/2 
# sliceM = slice(0,(mid-1))
# sliceN = slice((mid+1), 4)


# if a[sliceM] == a[sliceN]:
#     print("Đây là số thuận nghịch")
# else: 
#     print("Đây không phải là số thuận nghịch")



str1 = str(a)


str1_rvs = str1[::-1]
print(str1_rvs)
if str1_rvs == str1:
    print("Day la so thuan nghich")
else:
    print("Day k la so thuan nghich")

    

