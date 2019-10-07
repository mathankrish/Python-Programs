# PF-Exer-26

def factorial(number):
    sum1 = 0

    temp = number
    while (number):
        i = 1
        f = 1
        r = number % 10
        while (i <= r):
            f = f * i
            i = i + 1
        sum1 = sum1 + f
        number = number // 10
    if (sum1 == temp):
        return sum1


def find_strong_numbers(num_list):
    a1 = []
    for i in range(len(num_list)):
        a1.append(factorial(num_list[i]))

    b = list(filter(lambda x: x != None, a1))
    c = list(filter(lambda x: x != 0, b))
    return c


num_list = [145, 145]
strong_num_list = find_strong_numbers(num_list)
print(strong_num_list)