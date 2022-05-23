from email.errors import MissingHeaderBodySeparatorDefect

plate_number = ['KBX1122','KCA2021','KDD6572']
motorcycle =['suzuki','yamaha','honda']
print(motorcycle)#accessing list items using index
print(plate_number)
#print(motorcycle)....changing element ina list
print(motorcycle[0])
motorcycle[1]='Toyota'
print(motorcycle)
print(motorcycle[1])
##adding a string
print("I love "+str(motorcycle[1]))


#adding elements in a list
motorcycle.append('Prado mitsubishi')
print(motorcycle)

#removing an item from a list-use the index to access each item

print(plate_number[1])
print("My number plate is "+str(plate_number))

#deleting an item from a list
del motorcycle[0]
print(motorcycle)

#pop-printing the last index only
popped_motorcycle =motorcycle.pop()
print(popped_motorcycle)

#My name is Keith Koome and I own a motorcycle plate number
name = "Keith Koome"
motorcycle_owner = "My  name is Keith Koome and i own a "+str(motorcycle[0])+str(plate_number[2])

print(motorcycle_owner)

motorcycle_owner = "Keith Koome"
print(f"My name is {motorcycle_owner} and i own a {motorcycle[0]} plate_number {plate_number[2]}")

#removing anitem from a list
motorcycle.remove('suziki')



fruits = ["Banana","Mango","Apple","Lime"]
print(fruits[0])
print(fruits[-1])
print(fruits)
