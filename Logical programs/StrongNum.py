def strong(num):
    n = num
    sum1 = 0

    while (num):
        i = 1
        fact = 1
        rem = num % 10
        while (i <= rem):
            fact = fact * i
            i = i + 1
        sum1 = sum1 + fact
        num = num // 10

    if (sum1 == n):
        s = "Is a strong number"
        return s
    else:
        s = "Not a strong number"
        return s


a = int(input())
print(strong(a))