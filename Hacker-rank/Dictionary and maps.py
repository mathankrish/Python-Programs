n = int(input().strip())
phonebook = {}
for i in range(n):
    line = input().split()
    # k, v = line.split()
    phonebook[line[0]] = line[1]

while True:
    try:
        number = input()
    except EOFError: # end of line error occurs when more number of inputs are given
        break
    if number in phonebook:
        print("{}={}".format(number, phonebook[number]))
    else:
        print("Not found")