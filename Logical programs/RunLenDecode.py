# Run Length Decoding
def decode(message):
    ret_str = ""
    if (message != ""):
        for i in range(0, len(message), 2):
            num = int(message[i])
            ch = message[i + 1]
            ret_str = ret_str + ch * num

    return ret_str


x = input("Enter the string ")
y = decode(x)
print(y)
