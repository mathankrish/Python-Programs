# PerFect Square

import math

number = int(input())

square_root = math.sqrt(number)


if int(square_root + 0.5) ** 2 == number:
    print(int(square_root + 0.5) ** 2)
    print("Perfect")

else:

    print("No")