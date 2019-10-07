times = int(input())
l1 = []
for i in range(times):
    k = input().split()
    if(k[0] == 'insert'):
        l1.insert(int(k[0]), int(k[1]))

    elif(k[0] == 'append'):
        l1.append(int(k[1]))

    elif (k[0] == 'remove'):
        l1.remove(int(k[1]))

    elif (k[0] == 'sort'):
        l1 = sorted(l1)

    elif (k[0] == 'pop'):
        l1.pop()

    elif (k[0] == 'reverse'):
        l1 = l1[::-1]

    elif (k[0] == 'print'):
        print(l1)

