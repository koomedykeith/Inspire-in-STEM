#!/usr/bin/python
####################################################################              
#              Dictionaries 
#              Nmae : Keith Koome
#              Date : 23 / 5 / 2022
#######################################################################



#Initializing dictionaries
#key value pair
student = {"Name" : "Keith", "age" : 19,"gender" : "male"}

print(student["Name"])
print(student["age"])
print(student["gender"])

student["ID.No"] = "39905071"
student["Hobby"] = "Dancing"
student["Team"] = "Chelsea"
print(student)

#position coordinates
student['x_position'] = 45
student['y_position'] = 4
print(student["x_position"])


#staring with emoty dictionary

student = {}

#add pairs
student["shoe size"] = '9'
student["favorite_meal"] = "Chapo"
student["home_city"] = "Kinoo"
print(student)

#modifying values in a dictionary
student["Name"] = "John"
print(student["Name"])


#removing key value pairs

del student["home_city"]
print(student)

