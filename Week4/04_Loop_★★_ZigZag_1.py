N = int(input())

store_x = [] 
store_y = [] 

for i in range(N):
    x,y = input().split()
    store_x.append(x)
    store_y.append(y)
for i in range(1,len(store_x), 2): #range(start,stop,step)
    store_x[i],store_y[i] = store_y[i],store_x[i]
command = input()
store_x = [int(x)for x in store_x]
store_y = [int(x)for x in store_y]
if command == 'Zig-Zag':
    print(min(store_x),max(store_y))
elif command == 'Zag-Zig':
    print(min(store_y),max(store_x))
    
#print(store_x)
#print(store_y)