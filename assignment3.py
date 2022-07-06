#write a program to withdraw ksh.25,000 if the acc_balance is btwn ksh 100,000 to 500,000
# 10% if acc balance btwn 500,000 and 1,000,000
#Above 1,000,000 deduct 150,000

amount = input("What is your salary?")

if(int(amount) > 100000 and int(amount) < 500000):
    amount = amount - 25000
    print(" We have deducted ksh 25000")
elif (int(amount) > 500000 and int(amount) < 1000000):
    amount = amount - (int(0.1*amount))
    print("We have deducted 10% from your account")
elif int(amount) > 1000000:
    amount = amount - 150000
    print("We have deducted ksh 150000")

