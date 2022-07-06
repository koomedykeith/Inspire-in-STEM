#!/usr/bin/python
#######################################################################
# for loops with lists
# for loops              
#                  SQUARES
#              Name : Keith Koome
#              Date : 24 / 5 / 2022
#######################################################################
squares = []   #empty list
for number in range (0,10):
    square = number **2
    squares.append(square)

print(squares)

cubes = []
for number in range (0,10):
    cube = number **3
    cubes.append(cube)

print(cubes)

#sum of numbers from one to a hundred(1-100)
sum = 0
for number in range(0,100):
    sum = sum + number
print(sum)

sum = 0
for number in range(0,1000000):
    sum = sum + number
print(sum)

  #If statements
age = 24
age = 18
age = 17
if age >= 18:
    print("You are allowed to drive")
else:
    print("You are too young to drive")