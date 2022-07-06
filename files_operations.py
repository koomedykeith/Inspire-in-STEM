f = open("lesson.txt")
#f = open("lesson1.txt",'x')   

#Reading a file
print(f.read())
f.close

#opening a file
with open("lesson1.txt",'w') as f:
   f.write("This is my mother\n")
   f.write("I am from Kinoo\n\n")
   f.write("Nawacha pombe till further notice\n")

#Read line by line
f = open("lesson.txt")
print(f.readline())



