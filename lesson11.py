#Half pyramid of stars
#*
#**
#***
#****
#*****
rows = int(input("enter the number of rows"))

for i in range(rows):
    for j in range(i + 1):
        print("*",end="")
    print("\n")

##################

rows = int(input("Enter the number of rows"))

for i in range(rows):
    for j in range(i + 5):
        print("*",end="")
    print("\n")

