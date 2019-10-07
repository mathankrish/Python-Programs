# Palindrome in number

num = int(input("Enter the number"))
count = ""
num = str(num)

num_rev = num[::-1]

print(num)
print(num_rev)

num = int(num)
num_rev = int(num_rev)

if(num == num_rev):

    print("The given number {0} is a palindrome".format(num))

else:

    print("The given number {0} is not a palindrome".format(num))

