a = input()
try:
    b = float(a)
    if b<=100:
        print("18")
    elif 100<b<=250:
        print("22")
    elif 250<b<=500:
        print("28")
    elif 500<b<=1000:
        print("38")
    elif 1000<b<=2000:
        print("58")
    else:
        print("Reject")
except ValueError:
    print("Reject")