#•	Python Program to Print the Fibonacci sequence

n=int(input("Enter the vale\n"))
a=0
b=1
sums=0
for i in range (n):
    print(sums,end=" ")
    a=b
    b=sums
    sums=a+b
