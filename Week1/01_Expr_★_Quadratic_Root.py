import math
a = float(input(""))
b = float(input(""))
c = float(input(""))

x1 = (-b-math.sqrt(b**2-(4*a*c)))/(2*a)
x2 = (-b+math.sqrt(b**2-(4*a*c)))/(2*a)

print(float(round(x1,3)),float(round(x2,3)))
