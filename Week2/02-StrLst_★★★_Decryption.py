code = input()
code_str = str(code)

a = code_str[3::7]
#print(a)
b = code_str[7::5]
#print(b)
c = int(a)+int(b)+10000
#print(c)
d = str(c)[-4:-1]#-1 is excluded as [start:end]
#print(d)
e = int(str(int(d[0])+int(d[1])+int(d[2]))[-1]) + 1
#print(e)
f = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'][e-1]
#print(f)
print(d+f)