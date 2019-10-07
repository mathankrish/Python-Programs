# Odd or Even

def odd_or_even(num):
    if num % 2 == 0:
        print("The given number {0} is even".format(num))
    else:
        print("The given number {0} is odd".format(num))


number = int(input("Enter the number: "))
odd_or_even(number)