button = ""
dict1 = ['F','D','D+','C','C+','B','B+','A']
ids = []
grades = []
while button!='q':
    button = input()
    ids.append(button[0:5])
    grades.append(button[6:])
uids = input().split()
ids.pop()
grades.pop()
#print(ids)
#print(grades)
#print(uids)
for i in ids:
    if i in uids:
        index_ids = ids.index(i)
        #print(index_ids)
        if grades[index_ids] in dict1:
            try:
                grades[index_ids] = dict1[dict1.index(grades[index_ids]) + 1]
            except IndexError:
                pass
            #print(grades[index_ids])
#print(grades)

for i in range(len(ids)):
    print(ids[i]+" "+grades[i])