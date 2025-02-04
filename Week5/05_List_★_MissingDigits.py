a = input()

list1 = []
list2 = ['0','1','2','3','4','5','6','7','8','9']

for char in a:
    list1.append(char)
list1 = list(dict.fromkeys(list1))

try:
    if sorted(map(int,list1)) == [int(item)for item in list2]: print("None")
except ValueError:

    result = list(filter(lambda x: x not in list1, list2))
    res =  list(map(str,result))
    answer = ""
    for i in res:
        answer += i +','
    print(answer.rstrip(","))