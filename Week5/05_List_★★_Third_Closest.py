import math
n = int(input())
list1 = [] #coordinates
list2 = [] #distance
list3 = []
for i in range(n):
    x = input().strip()  #  Remove \r and \n from the input
    list1.append(x)

#print(list1)

for i in list1:
    x, y = i.split(" ")
    x, y =float(x),float(y)
    #print(x,y)
    distance = math.sqrt(y**2+x**2)
    list2.append(distance)
print(list2)

list3 = sorted(list2)
for i in range(3):
    least3rd = list3[2]
#print(least3rd)
#print(list2)
index = list2.index(least3rd)
#print(index)
    
x,y = list1[index].split(" ")
print(f"#{index+1}: ({x}, {y})")