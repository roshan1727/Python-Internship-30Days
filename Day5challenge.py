# 1)	Write a program to create a list of n integer values and do the following
>>> List=[1,2,3,45]

# •	Add an item in to the list (using function)
>>> List.append(23)
>>> print(List)
[1, 2, 3, 45, 23]

# •	Delete (using function)
>>> del List
>>> print(List)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(List)
NameError: name 'List' is not defined


# •	Store the largest number from the list to a variable
>>> a=[12,34,56,78,90]
>>> b=max(a)
>>> print(b)
90


# •	Store the Smallest number from the list to a variable
>>> print(min(a))
12

#  2) Create a tuple and print the reverse of the created tuple
>>> tuples=(1,2,34,'roshan')
>>> print("Reverse of the above tupl \n",tuples[::-1])
Reverse of the above tupl 
 ('roshan', 34, 2, 1)


#  3) Create a tuple and convert tuple into list
>>> print(type(tuples))
<class 'tuple'>
>>> print(tuples)
(1, 2, 34, 'roshan')
>>> print(list(tuples))
[1, 2, 34, 'roshan']

>>> List=[1,2,3,45]
>>> List.append(23)
>>> print(List)
[1, 2, 3, 45, 23]
>>> del List
>>> print(List)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(List)
NameError: name 'List' is not defined
>>> a=[12,34,56,78,90]
>>> b=max(a)
>>> print(b)
90
>>> print(min(a))
12
>>> tuples=(1,2,34,'roshan')
>>> print("Reverse of the above tupl \n",tuples[::-1])
Reverse of the above tupl 
 ('roshan', 34, 2, 1)
>>> print(type(tuples))
<class 'tuple'>
>>> print(tuples)
(1, 2, 34, 'roshan')
>>> print(list(tuples))
[1, 2, 34, 'roshan']