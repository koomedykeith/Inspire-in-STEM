#first terms of AP---a
#common difference---d
#number of terms-----n

a = int(input("enter first number"))
d = int(input("enter the difference"))
n = int(input("enter the number of terms"))

for i in range(1,n+1):
    n_term = a + (i-1)*d
    print(n_term)

#sum of terms=n/2(2a+(n-1)d)
sum_n = (n_term/2)*(2*a + (n-1)*d)    
print(sum_n)    









