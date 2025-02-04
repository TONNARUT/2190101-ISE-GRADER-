x = input().split()

x = [int(i) for i in x]
n = len(x)
peak = 0
for i in range(n):
    if i == 0:
        pass
    elif i == n-1:
        pass
    else:
        if x[i]>x[i+1] and x[i]>x[i-1]:
            peak += 1
            #print("case3")
        else:
            pass
print(peak)