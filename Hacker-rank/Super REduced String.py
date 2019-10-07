s = input()
distinctList = []
countList = []
for c in s:
    if c not in distinctList:
        distinctList.append(c)
print(distinctList)
for d in distinctList:
    count = s.count(d)
    countList.append(count)
print(countList)
#print(countList)
key = countList[0]
flags = 0
for count in countList:
    if(key != count):
        flags+=1
print(flags)
if(flags > 1):
    print("NO")
else:
    print("YES")