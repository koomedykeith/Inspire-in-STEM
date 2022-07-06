#A palindrome is anumber or letter that remains the same even if the numbers or letters are inverted

number=int(input("Enter any number :"))
#store a copy of this number
temp=number
#calculate reverse of this number
reverse_num=0
while(number>0):
    #extract last digit of this number
    digit=number%10
    #append this digit in reveresed number
    reverse_num=reverse_num*10+digit
    #floor divide the number leave out the last digit from number
    number=number//10
#compare reverse to original number
if(temp==reverse_num):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
#Using While-loop strings
def check_palindrome(string):
    length = len(string)
    first = 0
    last = length -1 
    status = 1
    while(first<last):
           if(string[first]==string[last]):
               first=first+1
               last=last-1
           else:
               status = 0
               break
    return int(status)  
string = input("Enter the string: ")
print("Method 1")
status= check_palindrome(string)
if(status):
    print("It is a palindrome ")
else:
    print("Sorry! Try again")