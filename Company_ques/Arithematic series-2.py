# Find the nth term of the series.
# 1,1,2,3,4,9,8,27,16,81,32,243


number_of_term = int(input("Enter the nth term: "))
List = number_of_term * [0]

even_place = 1
odd_place = 1

List[0] = even_place
List[1] = odd_place

for i in range(2, number_of_term):
   if i % 2 == 0:
      even_place *= 2
      List[i] = even_place

   else:
       odd_place *= 3
       List[i] = odd_place

print(List)
print("The {0} element in the series is {1}".format(number_of_term, List[-1]))