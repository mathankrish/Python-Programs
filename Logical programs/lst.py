bob = 0
alice = 0



a=list(map(int, input().split(' ')))
b = list(map(int , input().split(' ')))

for i1 in range(3):

    if(b[i1] < a[i1]):
        alice = alice + 1

    elif(b[i1] > a[i1]):
        bob = bob + 1

print(alice,"\n")
print(bob,"\n")

