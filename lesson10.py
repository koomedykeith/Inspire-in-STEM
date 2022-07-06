#!/usr/bin/python
#Loops
#for loops
from math import factorial

for number in range(0,10):
    if(number % 2==0):
        print(number)

#sum of all numbers btwn 0 and 50
sum = 0 
for number in range(0,50):
    sum = sum + number
print(sum)  #outside the loop

#sum of all even numbers btwn 0 and 20
sum_nums = 0
prod_nums = 1
for number in range(1,20):
    if(number % 2 == 0):     #inside the loop
        sum_nums = sum_nums + number
print(sum_nums)       

#product of all odd numbers btwn 0 and 50

for number in range(0,20):
    if(number % 2 == 1):     #inside the loop   #odd number
        prod_nums = prod_nums * number
print(prod_nums)       


#calculate the factorial of 6(6!)=6*5*4*3*2*1
for number in range(0,6):
    if(factorial == number * (number - 1)):
        print(factorial) 

#numbers btwn 0 to 10
num = 0  #initialize the condition
while num < 10:
    print(num)
    num = num + 1

#even numbers from 0 to 10------using while statements
num = 0  
while num < 10:
    print(num)
    num = num + 2

#even numbers from 
num = 10
while num < 10:
    if(num % 2 == 0):
        print(num)
    num = num + 1        