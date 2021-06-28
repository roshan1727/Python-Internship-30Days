# Write a Python script to merge two Python dictionaries

>>> a={"Name":"Rakesh","Rollno":18,"age":19}
>>> b={"Name1":"Rose","Rollno":19,"age":20}
>>> print(a.update(b))
None
>>> print(a)
{'Name': 'Rakesh', 'Rollno': 19, 'age': 20, 'Name1': 'Rose'}