array_size = int(input())

array_elements = list(map(int, input().split()))

count = 0
for i in range(array_size):
    for j in range(0, array_size-i-1):

        if array_elements[j] > array_elements[j+1]:

            array_elements[j], array_elements[j+1] = array_elements[j+1], array_elements[j]
            count += 1

print("Array is sorted in {} swaps".format(count))
print("First Element: {}".format(array_elements[0]))
print("Last Element: {}".format(array_elements[-1]))