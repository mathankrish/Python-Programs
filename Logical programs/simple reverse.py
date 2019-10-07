def reverse(a):
    b = "".join(reversed(a))
    return b

a = "hello-world"
print(reverse(a))

print(a[::-1])

print(a.split("-"))