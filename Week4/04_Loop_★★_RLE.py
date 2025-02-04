a = input()

count = 1
result = []
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        count+=1
    else:
        result.append(f"{a[i]} {count}")
        count = 1
result.append(f"{a[-1]} {count}")
print(" ".join(result))

    
    
