#•	Write a program to get the below pattern
#54321
#4321
#321
#21
#1

n = int(input('Enter number: ')) 
for i in range(n): 
	print(''.join(map(str,range(n-i,0,-1)))) 
