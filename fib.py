
from math import sqrt

def fib(n):
    print("n={}".format(n))
    res = int(round(
             ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
         ))
    print("res = {}".format(res))
    return res + 1
