# Lcm of two numbers

def Lcm(a, b):

    if a > b:
        max = a

    else:
        max = b

    while(True):
        if (max % a == 0 and max % b == 0):
            print("Lcm of {0} and {1} is {00}".format(num1, num2, max))
            break
        max += 1

num1 = int(input())
num2 = int(input())

Lcm(num1, num2)