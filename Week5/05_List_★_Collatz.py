n = int(input())
list1 = [n]
while n != 1:
    if n%2 == 0:
        n=n/2
        n = int(n)
        list1.append(n)
    else:
        n = 3*n+1
        n = int(n)
        list1.append(n)

if len(list1) <=15:
    pass
elif len(list1) > 15:
    list1 = list1[-15:]
result = '->'.join(map(str,list1))

print(result)

