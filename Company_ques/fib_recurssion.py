# Fibonacci series in recursion method

def fibonacci(num):

    if num <= 1:
        return num

    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


num_of_terms = int(input("Enter the number of terms: "))

if num_of_terms <= 0:
    print("Enter the positive number")

else:
    for i in range(num_of_terms):

        print(fibonacci(i))





