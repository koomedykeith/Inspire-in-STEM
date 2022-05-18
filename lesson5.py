# methods
name = "Keith Koome"
name = "Keith Kiara"
user_name="Koomedy Comedian"
age = 15
person = " I am "+ str(name)+" and my age is "+str(age)
print (person)
#the format() method
print("My name is {} and i am {} years old ".format(name,age))
#"f" is the short form of format
#new line (\n) and tab (\t)
print (f"My  \t name is {name} \n I am {age}years old")
print(name)
print (name.lstrip())


#Multiple lines

msg = ''' QRST126XDG MPESA confirmed
     you have received ksh 5000 from 
     Keith Kiara
     18th May 2022
     SAfaricom transparent for you
    '''
print(msg)


city = "Nairobi"
print(city[:5])
print(city[2:])
print(city[-1])


f_name = "keith koome" #small letters
# .upper() convert to uppercase
print(f_name.upper())

s_name = "KEITH KOOME" #capital letters
# .lower() convert to lower case
print(s_name.lower())

#concatination-converting from one type of an integer yo another
#int->float     float (x)
#float ->int      int(x)
#int-> string   str(x)
number = 6
print(str(number))

x = 4 #x is an integer
print(float(x))

y = 3.24
print(int(y))

f_name = "Keith"

s_name ="Koome"
 
full_name = (f_name + s_name)
print(full_name)


#The relace() method replaces a string with another

name = "Keith Koome"

print(name.replace('t','G'))\

#The split Method
msg = "Hello from Keith Koome how are you"
print(msg.split()) 
#calcualating the number of words in the split 
print(len(msg))




