import string

def swap_case(s):
    # Swap Case


    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    l1 = []
    for i in s:
        if i in lower:
            l1.append(i.upper())
        elif i in upper:
            l1.append(i.lower())
        else:
            l1.append(i)

    return ''.join(l1)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)