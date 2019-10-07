def odd_even_place(names):
    even_list = []
    odd_list = []

    for i in range(len(names)):

        if i % 2 == 0:
           even_list.append(names[i])

        else:
            odd_list.append(names[i])

    out = "".join(even_list) + " " + "".join(odd_list)

    print(out)




times = int(input())
names = []
for i in range(times):
    n = input()
    names.append(n)

for j in range(times):
    odd_even_place(names[j])

