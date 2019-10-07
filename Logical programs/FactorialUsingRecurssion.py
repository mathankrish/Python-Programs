# factorial Numbers in a list using reccurssion

def factorial(a1):
    if (a1 == 1):
        return 1
    else:
        return a1 * factorial(a1 - 1)


a = []
a1 = int(input())
for j in range(0, a1):
    k = int(input())
    a.append(k)

for i in range(0, len(a)):
    if (a[i] < 0):
        print("Not Allowed")
    elif (a[i] == 0):
        print("1")
    else:
        print(factorial(a[i]))