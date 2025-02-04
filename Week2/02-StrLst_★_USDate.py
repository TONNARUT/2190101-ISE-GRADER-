def us_months(month_number):
    months_dictionary = ("January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December")
    
    month_result = months_dictionary[int(month_number)-1]
    return month_result
    
us_date = input('')
split = us_date.split("/")

day_number = split[0]
month_number = split[1]
year_number = split[2]

result = us_months(month_number)

#print(result,day_number,",",year_number)
print(f"{result} {day_number}, {year_number}")