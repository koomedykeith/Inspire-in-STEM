#Getting the factorials of numbers
from math import factorial

number = input("enter the number")
factorial = 1
#if u want to compare a number with zero u use (==)

if (int(number)) < 0:
    print("factorial of negative number does not exist")
elif number == 0:
    print("factorial of 0 = 1")
else:
    for i in range(1,int(number)+1):
        factorial = factorial*i
print("factorial of number is:",factorial)

#without putting int everywhere
number = int(input("enter the number"))

if (number) < 0:
    print("factorial of negative number does not exist")
elif number == 0:
    print("factorial of 0 = 1")
else:
    for i in range(1,number+1):
        factorial = factorial*i
print("factorial of number is:",factorial)














