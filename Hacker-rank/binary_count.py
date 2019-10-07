
def maxConsecutiveOnes(x):

    count = 0


    while (x != 0):

        x = (x & (x << 1))
        print(x << 1)
        print(x & (x << 1))

        count = count + 1

    return count




dec_num = int(input())

print(maxConsecutiveOnes(dec_num))

