# 1.	Create a function getting two integer inputs from user. & print the following:

# Addition of two numbers is +value

# Subtraction of two numbers is +value

# Division of two numbers is +value

# Multiplication of two numbers is +value

# Here the value represents math function associated
def fun(a,b):
	print("Addition of two number is ",a+b)
	print("Subtraction of two number is ",abs(a-b))
	print("Division of two number is ",a//b)
	print("Multiplication of two number is ",a*b)
a=int(input())
b=int(input())
fun(a,b)
