# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

S = str(input())
T = [list(g) for k, g in groupby(S)]

l1 = []
for i in T:
    p = len(i), int(i[0])
    l1.append(tuple(p))
print(*l1)
