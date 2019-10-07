a = input()
b = input()

if "".join(sorted([i1 for i1 in b])) in "".join(sorted([i for i in a])):
    print("ssssss")
else:
    print("nooooo")