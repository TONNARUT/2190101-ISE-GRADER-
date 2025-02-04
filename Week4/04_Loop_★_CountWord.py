word = input()
sentence = input()
count = 0
sentence = sentence.replace('"','').replace('.',' ').replace('(','').replace(')','').replace("'","").replace('...','')
for i in sentence.split():
    if word == i:
        count += 1
#print(sentence.split())
print(count)