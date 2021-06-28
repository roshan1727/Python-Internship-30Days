#Amstrong Number

n=int(input('enter the value :'))
sums=0
temp=n
while temp>0:
    c=temp%10
    sums+=c**3
    temp//=10
if sums==temp:
    print("The given Value is an Amstrong number")
else:
 print("The given Value is not an Amstrong number")
