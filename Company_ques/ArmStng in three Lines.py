# ArmStrong Number in three Lines


num = int(input())

string_num = list(map(int, str(num)))

ArmStrng = list(map(lambda x: x ** len(str(num)), string_num))

if sum(ArmStrng) == num:
    print("{0} is an Armstrong number".format(num))

else:
    print("{0} is not an Armstrong number".format(num))
