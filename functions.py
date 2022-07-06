#!/usr/bin/python
####################################################################              
#              Functions in Python 
#              Name : Keith Koome
#              Date : 23 / 5 / 2022 and 03 / 6/ 2022
#######################################################################

#defining a function/initializing

def say_hello():
    print("Hello from JKUAT")
    x = 4
    y = 7
    z =x+y
    print(z)
say_hello()

def bark():
    print("Dogs bark woof woof")
def moos():
    print("A cow moos all the time")
def chirps():
    print("A bird chirps in the morning")
def meows():
    print("A cat meows when it is hungry")           
bark()
moos()
chirps()
meows()   

#Function Parameters

#A function to add 2 numbers
def add_numbers(x,y):   # x and y are parameters
    sum_nums = (x+y)
    print("The sum of 2 numbers:",sum_nums)

add_numbers=(40,50)
add_numbers=(100,400)
add_numbers=(1,4)

#Using default parameters#How to change the name or an input

def print_name(name="Keith Koome"):
    print (name)
print_name("Catherine")

#If you add 2 floats/integers together u get an float/integer

#Return from a function#How to add numbers

def get_sum(num1 , num2):
    sum_nums = num1 + num2
    return sum_nums
print(get_sum(7,12))    

#A function to get the square of numbers#How to return a function

def powers(number,power):
    pow_numb = number **power
    return pow_numb
print(powers(6,4))    

#Putting 2 names together
def get_full_name(f_name,s_name):
    full_name = f_name + " " + s_name
    return full_name.title()
print( get_full_name ("Keith","Koome"))

#Returning a dictionary from a function#In dictionaries we use cali brackets{}

def create_full_name(first_name,second_name):
    person = {'first':first_name,'second':second_name}
    return person
student = create_full_name('Keith','Koome')
print(student)

#passing through a list in a function/passing a list through a function
#names is the list
def greet_friends(names):
    for name in names:
        msg = " Hello " + name.title() + "!"
        print (msg)
friends = ['Maggie','Paul','Saul']
greet_friends(friends)        







