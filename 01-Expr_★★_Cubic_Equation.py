import math

a, b, c, d = map(float, input("").split())
inner_inner_global=(((2*(b**3))-(9*a*b*c)+27*a*a*d)**2)-(4*((b**2)-(3*a*c))**3)

try:
    def first_root(a,b,c,d):
        global inner_inner_global
        inner_upper=(1/2)*((2*(b**3))-(9*a*b*c)+(27*d*(a**2))+math.sqrt(inner_inner_global))
        sol1=(-1/(3*a))*(inner_upper**(1/3))
        return sol1

    def second_root(a,b,c,d):
        global inner_inner_global
        inner_lower=(1/2)*((2*(b**3))-(9*a*b*c)+(27*d*(a**2))-math.sqrt(inner_inner_global))
        sol2=(-1/(3*a))*(inner_lower**(1/3))
        return sol2

    def main():
        sol1=first_root(a,b,c,d)
        sol2=second_root(a,b,c,d)
        result=round(sol1+sol2-(b/(3*a)),3)
        print(result)
        #print(type(result))
    if __name__=="__main__":
        main()
except:
    print("")


#inner_inner_global = (((2*(b**3)) - (9*a*b*c) + 27*a*a*d)**2) - (4*((b**2)-(3*a*c)))**3
#inner_upper = (1/2) * ((2*(b**3)) - (9*a*b*c) + (27*d*(a**2)) + math.sqrt(inner_inner_global))
#upper_x = (-b/(3*a)) - ((1/(3*a))*(inner_upper**(1/3)))


#inner_lower = (1/2) * ((2*(b**3)) - (9*a*b*c) - (27*d*(a**2)) + math.sqrt(inner_inner_global))
#lower_x = (-1/(3*a)) * ((inner_lower)**(1/3))

#print(inner_upper-inner_lower)