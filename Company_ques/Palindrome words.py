# Palindrome words

string = input("Enter the string: ")

rev_string = string[::-1]

if(string == rev_string):

    print("The given string {0} is a palindrome".format(string))

else:
    print("The given string {0} is not a palindrome".format(string))