import math

id = (input(""))

n0 = int(id[0])
n1 = int(id[1])
n2 = int(id[2])
n3 = int(id[3])
n4 = int(id[4])
n5 = int(id[5])
n6 = int(id[6])
n7 = int(id[7])
n8 = int(id[8])
n9 = int(id[9])
n10 = int(id[10])
n11 = int(id[11])

n12 = (11-(13*n0 + 12*n1 + 10*n3 +9*n4 +8*n5+7*n6+6*n7+5*n8+4*n9+3*n10+2*n11)%11)%10


print(f"{n0} {n1}{n2}{n3}{n4} {n5}{n6}{n7}{n8}{n9} {n10}{n11} {n12}")