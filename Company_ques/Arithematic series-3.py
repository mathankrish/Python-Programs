# Find the nth term of the series 0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8

n = int(input("Enter the nth term: "))
List = n * [0]

even_place = 0
odd_place = 0

List[0] = 0
List[1] = 0

for i in range(2,n):

    if i % 2 == 0:
        even_place += 2
        List[i] = even_place

    else:
        odd_place = int(List[i-1] / 2)
        List[i] = odd_place

print(List)
print("The {0} element in the series is {1}".format(n, List[-1]))