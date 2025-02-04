u = input()
v = input()

u = eval(u)
v = eval(v)

u = [float(i)for i in u]
v = [float(i)for i in v]

u1 = u[0]
u2 = u[1]
u3 = u[2]

v1 = v[0]
v2 = v[1]
v3 = v[2]

output = [u1+v1,u2+v2,u3+v3]
print(u,'+',v,'=',output)