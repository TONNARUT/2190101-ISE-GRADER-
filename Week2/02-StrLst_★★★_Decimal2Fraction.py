import math as m
from math import gcd

decimal = input()

test = decimal.split(',')
#print(test)
upper_bound = int(test[0]+test[1]+test[2]) - int(test[0]+test[1])
#print(upper_bound)
lower_bound = 10 ** len((test[1])+(test[2])) - 10 ** len(test[1])
#print(lower_bound)

gcd = m.gcd(upper_bound,lower_bound)
#print(gcd)

print(int(upper_bound//gcd),"/",int(lower_bound//gcd))