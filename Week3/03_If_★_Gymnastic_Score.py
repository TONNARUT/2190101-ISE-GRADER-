a,b,c,d = input().split()

a = float(a)
b = float(b)
c = float(c)
d = float(d)
try:
    max1 = 0
    if a>b:
        if a>c:
            if a>d:
                max1 = a
            elif d>a:
                max1 = d
        elif c>a:
            if c>d:
                max1 = c
            elif d>c:
                max1 = d
    elif b<a:
        if b>c:
            if b>d:
                max1 = b
            elif d>b:
                max1 = d
        elif c>b:
            if c>d:
                max1 = c
            elif d>c:
                max1 = d
            
    print(max1)
except:
    pass