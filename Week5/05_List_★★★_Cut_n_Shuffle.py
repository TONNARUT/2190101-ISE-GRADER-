a = input().split(" ") # card names
b = input() # operations
result = []
list1 = list(b)
#print(a)
#print(list1)

n = len(a)//2 # no of card divied by 2
for i in list1:
    if i == 'C':
        if result == []: # if we start with C
            half1,half2 = a[:n],a[n:]
            result = half2+half1
            #print(result)
            #print("case1.1")
        elif result != []: # if we start with S
            half1,half2 = result[:n],result[n:]
            result = half2+half1
            #print(result)
            #print("case1.2")
    elif i == 'S':
        if result == []: # if we start with S
            half1,half2 = a[:n],a[n:]
            for i in range(n):
                result.append(half1[i])
                result.append(half2[i])                   
            #print(result)
            #print("case2.1")
        elif result != []:# if we start with C
            half1,half2 = result[:n],result[n:]
            result = []
            for i in range(n):
                result.append(half1[i])
                result.append(half2[i])
            #print(result)
            #print("case2.2")
    else:
        pass
#print(result)
print(" ".join(map(str, result)))