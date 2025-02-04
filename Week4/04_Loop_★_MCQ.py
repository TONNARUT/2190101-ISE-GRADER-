a = input() #target
b = input() #guess
count = 0

if len(a)==len(b):
    for i in range(len(b)):
        if a[i] == b[i]:
            count+=1
    print(count)
        
elif len(a)!=len(b):
    print("Incomplete answer")