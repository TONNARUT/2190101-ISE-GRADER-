a = input().split()
#a = list(map(int,a))

a = list(dict.fromkeys(a))
a = list(map(int,a))
a = sorted(a,reverse=False)
#print(a)
print(len(a))

if len(a)< 10:
    print(a)
else:
    print(a[0:10])