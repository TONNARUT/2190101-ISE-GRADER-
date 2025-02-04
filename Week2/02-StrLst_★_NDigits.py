M = input()
N = input()
try:
    if int(len(M)) < int(N):
        add_zero = int(N)- int(len(M))
        for i in range(add_zero):
            result = "0"+ M
            M = result
        print(M)
    elif int(len(M)) > int(N) or int(len(M)) == int(N):
        print(M)
except ValueError:
    pass
