# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 09:04:17 2025

@author: Eberechukwu Okonkwo
"""
# num = int(input("Please enter a number: "))
# check = int(input("Please enter another number: "))

# if num % 2 ==0:
#     print (f"{num} is an even number")
    
#     if num % 4 == 0:
#         print(f"{num} is a multiple of 4")

# else:
#     print(f"{num} is an odd number")
  
# if check % num == 0:
#     print(f"{check} is a factor of {num}")
# else:
#     print("Not possible")
    
    
#assignment week 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# less_than_five =[x for x in a if x < 5]
# print("Elements less than five is:", less_than_five)

# new_num = int(input("Please enter a number: "))
# less_than_user_input =[x for x in a if x < new_num]
# print(f"elements less than {new_num}:", less_than_user_input)

#assignment week 4
number = int(input("Please enter a number: "))
for i in range (100):
    divisors = [x for x in (i, number + 1) if number % x == 0]
    # divisors = number % i == 0
    # if number % i == 0:
    #      # new_list =[number for number in i if number % i == 0]
    print(f"divisors of {number}: {divisors}")

# a = [1,1,2,3,5,8,13,21,34,55,89]
# b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
