#Full pyramid of stars

k=0
rows = int(input("Enter the number of rows"))
for i in range(1,rows+1):
    for space in range(1,(rows-i)+ 1):
        print( end=" ")
    while k!=(2*i - 1):
        print("*",end="")
        k+=1
    k=0        
    print()

