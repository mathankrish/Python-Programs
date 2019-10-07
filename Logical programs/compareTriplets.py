a = []
b = []

bob = 0
alice = 0

for i in range(3):
    k = input()
    a.append(k)

for j in range(3):
    k1 = input()
    b.append(k1)
print(a)
print(b)

for i1 in range(3):

    if(b[i1] < a[i1]):
        alice = alice + 1

    elif(b[i1] > a[i1]):
        bob = bob + 1

print(alice)
print(bob)

