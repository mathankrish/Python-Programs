from functools import reduce
def fact1(number):

    return reduce(lambda x, y : x * y, range(1, number+1))

number = int(input())
print(fact1(number))