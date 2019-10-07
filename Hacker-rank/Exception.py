n = int(input())

l1 = []

for i in range(n):
    a = input().split(" ")
    l1.append(a)
for j in range(len(l1)):
    try:
        c = int(l1[j][0]) // int(l1[j][1])
    except ZeroDivisionError as z:
        print("Error code:", z)
    except ValueError as v:
        print("Error code:",v)

    else:
        print(c)

