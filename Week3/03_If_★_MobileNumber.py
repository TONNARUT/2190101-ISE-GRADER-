a = input()
try:
    b = int(a)
    #print(len(str(a)))
    if len(str(a)) == 10:
        if str(a)[0] == '0':
            if str(a)[1] =='6' or str(a)[1] =='8' or str(a)[1] =='9':
                print("Mobile number")
            else:
                #print("case1")
                print("Not a mobile number ")
        else:
            #print("case2")
            print("Not a mobile number ")
    else:
        #print("case3")
        print("Not a mobile number ")
except ValueError:
    #print("case4")
    print("Not a mobile number ")