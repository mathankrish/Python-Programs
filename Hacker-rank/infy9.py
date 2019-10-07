def print_factors(x):
    l2 = []
    l3 = []
    for i in range(1, int(x) + 1):
        if int(x) % int(i) == 0:
            l2.append(i)

    if len(l2) > 1:
        for j in range(0, len(l2)):
            if l2[j] + 1 in l2:
                if ((l2[j]+1) * l2[j] == int(x)):
                    l3.append(x)
    return l3


num = "9305612"
l1 = []
l4 = []
for i in range(0, len(num) + 1):
    for j in range(i + 1, len(num) + 1):
        l1.append(num[i:j])

for k in l1:
    l4.extend(print_factors(k))

p = set(l4)
p1 = []
for m in p:
    if m[0] != "0":
        p1.append(int(m))

print(sorted(p1))

