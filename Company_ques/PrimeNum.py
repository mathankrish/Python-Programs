# Prime Numbers

import math
def isPrime(number):

    if number <= 1:
        return False

    else:

        for i in range(2, number):
            if number % i == 0:
                return False

        return number


num = int(input())

if isPrime(num) == False:

    print("Enter a valid prime number")
else:
    Prime_num = isPrime(num)
    square_root = math.sqrt(Prime_num)
    print(square_root)