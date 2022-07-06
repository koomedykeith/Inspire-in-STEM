#write a program that gets user input anad adds ksh.10000 to her account if she is btwn 25-30yrs

age = input("What is your age?")
gender = input("What gender are you :male/female?")

acc_bal = 0

if (int(age) > 25) and (int(age) < 30):
    acc_bal = acc_bal + 10000
    print("Confirmed you have received ksh.10000")
else:
    print("Sorry,you are not elligible for this service")

#write a program to withdraw ksh.25,000 if the acc_balance is btwn ksh 100,000 to 200,000
# 25% if acc balance btwn 500,000 and 1,000,000
#Above 1,000,000 deduct 400,000

acc_bal = (int(input("What is your account balance?")))

if (int(acc_bal) > 1000000 and int(acc_bal) < 200000):
    acc_bal = int(acc_bal) - 25000
    print("We have deducted ksh 25000 from your account to pay taxes.\n Your new account balance is " + str(acc_bal))

elif (int(acc_bal)>500000 and int(acc_bal)<1000000):
          acc_balance = float(acc_bal) - (0.3*float(acc_bal))
          print("We have deducted 30% of your account balance to pay for outstanding government debts.\nYour new account balance is " + str(acc_balance))

elif (int(acc_bal)>1000000):
        acc_balance = int(acc_bal) - 15000
        print("We have removed 15000 from your account balance.\n Your new account balance is " + str(acc_balance))
else :
    print("You do not merit the threshold for government taxes.\nNo deductions done.")

