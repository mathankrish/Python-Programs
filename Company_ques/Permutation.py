# # Permutation in a string
#
# from itertools import permutations
#
# string = input()
#
# prem_list = permutations(string)
#
# a =[]
#
# for perm in prem_list:
#
#     perm = ''.join(perm)
#     a.append(perm)
#
#
# print(a)

# Permutation in a string

from itertools import combinations

string = input()
# stri = list(map(str, string))
prem_list = combinations(string, 2)

for perm in list(prem_list):

    perm = ''.join(perm)
    print(perm)





