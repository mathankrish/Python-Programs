def func(name, num):
    length = len(name)
    l1 = []
    result = []
    for i in num:
        if (int(i) <= length):
            l1.append(i)
    sort_l1 = sorted(l1)

    if len(sort_l1) <= 0:
        result.append("X")
    else:
        result.append(name[int(sort_l1[-1])-1])

    return result

string = list(map(str, input().split(",")))
name = []
num = []
result1 = []
for i in string:
    i = i.split(":")
    name.append(i[0])
    num.append(i[1])

for j in range(len(name)):
    result1.extend(func(name[j], num[j]))

result2 = [str(k) for k in result1]

print(''.join(result2))
