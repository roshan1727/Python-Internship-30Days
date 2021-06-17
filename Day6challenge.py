# Exercise:
# 1) Write a Python script to merge two Python dictionaries
>>> a={"name1":"RaRo","age1":19,"gender1":"male"}
>>> print(type(a))
<class 'dict'>
>>> b={"name2":"Purni","age2":21,"gender2":"female"}
>>> print(type(b))
<class 'dict'>
# 2) Write a Python program to remove a key from a dictionary
>>> a.update(b)
>>> print(a)
{'name1': 'RaRo', 'age1': 19, 'gender1': 'male', 'name2': 'Purni', 'age2': 21, 'gender2': 'female'}
>>> del a["age1"]
>>> print(a)
{'name1': 'RaRo', 'gender1': 'male', 'name2': 'Purni', 'age2': 21, 'gender2': 'female'}
>>> keys=['rose','cake',19,'frdship']
>>> values=['flower','food','age','type']
# 3) Write a Python program to map two lists into a dictionary
>>> random_dictonary=dict(zip(keys,values))
>>> print(random_dictonary)
{'rose': 'flower', 'cake': 'food', 19: 'age', 'frdship': 'type'}
>>> num1={1,2,3,4,5,6,7,8,9}
>>> print(type(num1))
<class 'set'>
>>> num2={"raro",1,2,34,56,765,"rakesh"}
>>> print(type(num2))
<class 'set'>
# 5) Write a Python program to remove the intersection of a 2nd set from the 1st set
>>> num1.difference_update(num2)
>>> print(num1)
{3, 4, 5, 6, 7, 8, 9}
# 4) Write a Python program to find the length of a set
>>> print(len(num1))
7