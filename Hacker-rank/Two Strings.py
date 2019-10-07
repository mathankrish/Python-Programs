times = int(input())

l1 = []
for _ in range(times):

    k1 = [input() for _ in range(2)]
    l1.append(k1)

for k in l1:
    k1 = list(set(i for i in k[0] if i in k[1]))
    re_k1 = ["YES" if len(k1) > 0 else "NO"]
    print(*re_k1)