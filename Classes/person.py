#!/usr/bin/python
####################################################################              
#                  CLASSES     
#              Name : Keith Koome
#              Date : 1 / 6 / 2022
#######################################################################

class person:
    def __init__(self, _name, _age) :
        self.name = _name
        self.age = _age

    def sayHi(self):
        print('Hello,my name is ' + self.name + ' and i am '+ self.age + ' years old')
person1 = person('Keith Koome Kiara',str(19))  
person1.sayHi()


person2 = person('Raila Odinga',str(70))  
person2.sayHi()

person3 = person('Nikita Kerring',str(21))  
person3.sayHi()







class person:
    def __init__(self, _name, _age, _location) :
        self.name = _name
        self.age = _age
        self.location = _location


    def sayHi(self):
        print('Hello,my name is ' + self.name + ' and i am '+ self.age + ' years old' + ' and i live in ' + self.location)
person1 = person('Keith Koome Kiara',str(19),'Kajiado County')  
person1.sayHi()
