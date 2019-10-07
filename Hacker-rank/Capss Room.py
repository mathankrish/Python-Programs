from collections import Counter

n = int(input())
arr = input().split()

c = Counter(arr)

d = dict(c)

for k,v in d.items():
  if v == 1:
    print(k)
