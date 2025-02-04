s = 0; n = 0
while True:
    t = input()
    if t == "q":
        break
    s += float(t)
    n += 1
try:
    x = s/n
    print(round(x,2))
except:
    print("No Data")