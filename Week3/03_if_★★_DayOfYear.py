day = input()
month = input()
year = input()
#15/1/2559
day,month,year = int(day),int(month),int(year)

'''
January   31
Februar   28 (29 in a leap year)
March     31
April     30
May       31
June      30
July      31
August    31
September 30
October   31
November  30
December  31
'''
dict1 = [0,31,28,31,30,31,30,31,31,30,31,30,31]
if (year-543) % 400 == 0 or ((year-543) % 4 == 0 and (year-543) % 100 != 0):
    dict1[2] += 1
else:
    if month == 2:
       if day > 28:
          day = 28 
result = 0
for i in range(month):
    result += dict1[i]
#print(result)
#print(dict1)
print(result+day)