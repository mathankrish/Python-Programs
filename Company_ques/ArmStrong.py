# ArmStrong Number

num = int(input())
length = len(str(num))
temp = num
sum_num = 0

while(temp != 0):

    sum_num = sum_num + ((temp % 10)**length)
    temp = temp // 10

if sum_num == num:
    print("ArmStrong num")

else:
    print("Not an ArmStrong")

