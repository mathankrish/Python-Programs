# fib_without_recursion

n_term = int(input())
num1 = 0
num2 = 1

if n_term <= 0:
    print("Enter the positive number")

elif n_term == 1:
    print(num1)

elif n_term == 2:
    print(num2)

else:
    print(num1)
    print(num2)

    for i in range(2, n_term):

        c = num1 + num2
        num1 = num2
        num2 = c
        print(c)
