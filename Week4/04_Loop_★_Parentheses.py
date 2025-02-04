a = input()

if a =="no parentheses ":
    print("no parentheses ")
#a = a.replace( "(" , "[" ).replace( ")" , "]" ).replace("[","(").replace("]",")")
else:
    result = ""
    for i in a:
        if i == "(":
            result += "["
        elif i ==")":
            result += "]"
        elif i == "[":
            result += "("
        elif i == "]":
            result += ")"
        else:
            result += i
    print(result)
