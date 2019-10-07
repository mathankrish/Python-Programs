# Average of two numbers

def Avg(num1, num2):

    Total = num1 + num2
    average = Total / 2

    return average


num1 = int(input())
num2 = int(input())

print("The average of {0} and {1} is {00} ".format(num1, num2, Avg(num1, num2)))