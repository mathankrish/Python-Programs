nums = list(map(int, input().split()))

val1 = list(map(int, input().split()))
val = sorted(val1)
l1 = []
l2 = []
i = 0
while ( i < len(val)):
    for j in range(i + 1, len(val) + 1):
        if sum(val[i:j]) <= nums[1]:
            l1.append(val[i:j])
            l2.append(len(val[i:j]))
    i +=1
# l1 = [val[i:j] for i in range(0, len(val)) for j in range(i + 1, len(val) + 1) ]
# l2 = [len(val[i:j]) for i in range(0, len(val) + 1) for j in range(i + 1, len(val) + 1) if sum(val[i:j]) <= nums[1]]

print(val)
print(l1)
print(l2)
print(len(l1[l2.index(max(l2))]))

