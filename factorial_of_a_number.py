

def find_factorial_of_a_number(num):

    if num < 0:
        print("factorial is not present for negative numbers")

    elif num == 0:
        print("factorial for 0 is 1")
    else:
        ans=1
        for i in range(1,num+1):
            ans = ans*i
        print("factorial for {} is {}".format(num, ans))

import math

def find_factorial_of_a_number_rec_fun(num):
    #using recursion
    if num == 1:
        return 1
    else:
        return num * find_factorial_of_a_number_rec_fun(num-1)

def factorial_using_method(num):
    return math.factorial(num)

num = int(input("Enter the number:"))
#find_factorial_of_a_number(num)
print(find_factorial_of_a_number_rec_fun(num))
print(factorial_using_method(num))