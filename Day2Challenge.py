>>> print("30 days 30 hour challenge")
30 days 30 hour challenge
>>> Hours="thirty"
>>> print(Hours)
thirty
>>> Days="Thirty days"
>>> print(Days[0])
T
>>> Challenge="I will win"
>>> print(Challenge[7:10])
win
>>> print(len(Challenge))
10
>>> print(Challenge.lower())
i will win
>>> a="30 Days"
>>> b="30 hours"
>>> c=a+b
>>> print(c)
30 Days30 hours
>>> c=a+" "+b
>>> print(c)
30 Days 30 hours
>>> text="Thirty days and Thirty Hours"
>>> x=text.casefold()
>>> print(x)
thirty days and thirty hours
>>> x=text.capitalize()
>>> print(x)
Thirty days and thirty hours
>>> x=text.find()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x=text.find()
TypeError: find() takes at least 1 argument (0 given)
>>> x=text.find(a)
>>> print(x)
-1
>>> x=text.isalpha()
>>> print(x)
False
>>> x=text.isalnum()
>>> print(x)
False