num = 2

x = ["{} x {} = {}".format(num, i, num*i) for i in range(1, 11)]

for i in range(10):
    print(x[i])