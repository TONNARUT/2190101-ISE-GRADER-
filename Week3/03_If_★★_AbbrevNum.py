a = input()

if len(a) <= 3:
    print(a)
    
elif len(a) == 4:
    print(f"{(round(int(a)/100)/10)}K")
elif len(a) == 5:
    print(f"{(round(int(a)/1000))}K")
elif len(a) == 6:
    print(f"{(round(int(a)/1000))}K")
elif len(a) == 7:
    print(f"{(round(int(a)/100000)/10)}M")
elif len(a) == 8:
    print(f"{(round(int(a)/1000000))}M")
elif len(a) == 9:
    print(f"{(round(int(a)/1000000))}M")
elif len(a) == 10:
    print(f"{(round(int(a)/100000000)/10)}B")
elif len(a) == 11:
    print(f"{(round(int(a)/1000000000))}B")
elif len(a) >= 12:
    print(f"{(round(int(a)/1000000000))}B")