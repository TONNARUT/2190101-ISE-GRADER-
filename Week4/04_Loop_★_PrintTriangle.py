a = int(input())

base = (a*2)-1 #15 for 8

space=''
inner_space =' '
for i in range(a-1):
    space+=' '
star ='*'
print(space+star)

for i in range(a-2):
    space = space[:-1]
    print(space+star+(inner_space)+star)
    inner_space += '  '

print(star*base)