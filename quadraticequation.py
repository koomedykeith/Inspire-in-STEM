import math



#!/usr/bin/python
####################################################################              
#              Quadratic equations in Python 
#              Name : Keith Koome
#              Date : 23 / 5 / 2022
#######################################################################

#Method 1
a = int(input("Enter the coefficient of the first term"))
b = int(input("Enter the coefficient of the second term"))
c = int(input("Enter the coefficient of the third term"))

def find_roots(a,b,c):
    y1 = (-b + math.sqrt((b**2) - 4*a*c))/(2*a)
    y2 = (-b - math.sqrt((b**2) - 4*a*c))/(2*a)
    print("The roots of the qadratic equation:",y1,y2)
find_roots(a,b,c)

#Method 2
a = int(input("Enter the coefficient of the first term"))
b = int(input("Enter the coefficient of the second term"))
c = int(input("Enter the coefficient of the third term"))
m = math.sqrt(b**2 - (4*a*c))

def find_roots(a,b,c):
    y_1 = (-b + m)/(2*a)
    y_2 = (-b - m)/(2*a)
    print("The roots of the qadratic equation:",y_1,y_2)
find_roots(a,b,c)











