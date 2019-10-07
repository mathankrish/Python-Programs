# Arithematic series for 0,0,7,6,14,12,21,18,28 find the 15th term in the series

number_of_term = int(input("Enter the nth term: "))
List = number_of_term * [0]

even_place = 0
odd_place = 0

List[0] = 0
List[1] = 0

for i in range(2, number_of_term):
   if i % 2 == 0:
      even_place += 7
      List[i] = even_place

   else:
       odd_place += 6
       List[i] = odd_place

print(List)
print("The {0} element in the series is {1}".format(number_of_term, List[-1]))