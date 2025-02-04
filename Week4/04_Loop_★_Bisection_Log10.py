import math as m
a = input()
a = float(a)
U = a
L = 0
x = (L+U)/2
while abs(a-10**x) > 10**(-10)*max(a,10**x):
    if 10**x>a:
        U = x
    else:
        L = x
    x = (L+U)/2
print(round(x,6))