n  = int(input())

list1 = []
list2 = []
list3 = []

for i in range(n):
    a = int(input())
    list1.append(a)
#print(list1)
list1 = list1[::-1]

list2 = input().split(' ')
#print(list2)
if list2 == ['']:
    list2 = []
list2 = list2[::-1]
button = 0
while button != -1:
    button = int(input())
    list3.append(button)
list3.pop()
list3 = list3[::-1]
combined_list = list3+list2+list1
x = (combined_list[::2])
y = ((combined_list[1::2])[::-1])
#print(combined_list)
#print(x)
print(list(map(int,x+y)))