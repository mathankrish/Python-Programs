terms = list(map(int, input().split()))

arr1 = list(map(int, input().split()))

set1 = set(map(int, input().split()))

set2 = set(map(int, input().split()))

hapiness = 0
for i in arr1:
    if i in set1:
        hapiness += 1
    elif i in set2:
        hapiness -= 1

print(hapiness)