# Sum of the digits

number = int(input("Enter the number"))

num_str = str(number)

count = 0

for i in num_str:

    i = int(i)
    count += i

print("The sum of the digits are {0}".format(count))