#!/usr/bin/python
####################################################################              
#           TUPLES-Similar to lists but is immutable(unchangeable)
#              Name : Keith Koome
#              Date : 31 / 5 / 2022
#######################################################################

#list
fruits = ['mango','grapes','orange','lemon']
#Replace 'Orange with apple'
fruits[2] = 'apple'
print(fruits)


# mutable(can be edited)   # immutable(cannot be edited)
# lists[]                  # tuples()
# dictionaries{}


# this is a list that is immutable. It can not be edited. It is called a tuple.
new_fruits = ("guava","apples","banana","peaches")
print(new_fruits)

cars = ("audi","bmw","nissan","toyota")
print(cars)
cars = ("nissan","bmw","nissan","toyota") #in order to change the value of a tuple you have to rewrite the tuple
print(cars)

favFoods = ("chips","ndengu","fish","avocado")
for favFood in favFoods:
    print(favFood)






