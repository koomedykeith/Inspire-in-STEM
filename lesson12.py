###checking if a number is divisible by 5 or 7###
x = int(input('Enter a number'))
if (int(x%5==0)) and (int(x%7==0)):
    print("The number is divisible by 5 or 7")
else:
    print("The number is not divisible by 5 or 7")
