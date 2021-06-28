# Write a program to sort the value from descending to ascending in list and 
# convert it in to a set.

>>> List=[22,33,44,1,2,3,4]
>>> sorted(List)
[1, 2, 3, 4, 22, 33, 44]
>>> List[::-1]
[4, 3, 2, 1, 44, 33, 22]
>>> print(set(List))
{33, 2, 1, 3, 4, 44, 22}