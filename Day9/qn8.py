
#8)Solve Trigonometry problem using math function write a program to solve using math function

import math
def trigo(n,m):
    if n=='sin':
        print( math.sin(m))
    elif n=='cos':
        print(math.cos(m))
    elif n=='cosin':
        print(math.cosine(m))
    elif n=='tan':
        print(math.tan(m))
    elif n=='sec':
        print(math.sec(m))
    elif n=='cosec':
        print(math.cosec(m))

trigo('tan',45)

