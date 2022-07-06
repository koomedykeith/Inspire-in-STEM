#!/usr/bin/python
####################################################################              
#              Geometric Progression 
#              Name : Keith Koome
#              Date : 23 / 5 / 2022 and 03 / 6/ 2022
#######################################################################

a = int(input("Enter the first term : "))
r = float(input("Enter the common ratio : "))
n = int(input("Enter the number : "))

for i in range (1,n+1):
    n_term = a*r**(n-1)
print(n_term)

for float in range (1,n+1):
    if r > 1 :
        sum_nums = (a -(r **(n-1) - 1))/(r - 1)
    elif r < 1 :
        sum_nums = (a -(1 -(r ** (n - 1)))) / (1-r)   
print(sum_nums)        









