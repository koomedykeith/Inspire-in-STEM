#A dictionary is a collection of key value pair
#syntax: dictionary = {'key':'value'}
colours= {'colour':'red'}
vehicles={'type':'toyota','plate number':'KCM2330'}
names ={'John','Mary'}
print(type(names))  #we use this type of method to

#Accessing values in a dictionary
print(vehicles['type'])  #you can access the value of an element inside a dictionary using the key

#dictionary person
person= {'name':'Keith Koome','id number':'39905071','phone number':'0712862993','gender':'male'}
#adding a value to the dictionary
person['age']='19'
person['colour']='black'
print(type(person))
print(person)
print(vehicles['type']),vehicles['plate number']

#looking over dictionaries


#Task on dictionaries
mary_fav_food =['Ugali','Nyama','Sukumawiki']
keith_fav_food = ['Rice','pork','stew']

#Dictionary containing the above
fav_food = {
    'mary':mary_fav_food,
    'keith':keith_fav_food
}
for key, value in fav_food.items():
    print(f"{key}:{value}")
print(mary_fav_food)
print(keith_fav_food)


