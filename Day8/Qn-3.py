#  Write a Python program to list number of items in a dictionary key and sort the >>> d1={"RARO":[1,2,3,4],"Purni":[2345],"Rose":[98,56,43,22]}
>>> result={R:sorted(d1[R]) for R in sorted(d1)}
>>> print(result)
{'Purni': [2345], 'RARO': [1, 2, 3, 4], 'Rose': [22, 43, 56, 98]}


# list with the help of a function & without the function.

def fun(d1):
    res=dict()
    for key in sorted(d1):
        res[key]=sorted(d1[key])
    return res
    
fun(d1)
