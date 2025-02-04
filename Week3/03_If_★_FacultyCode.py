a =input()
try:
    b = int(a)
    if 20 <= b <= 40 or b in [51,53,55,58]:
        print("OK")
        exit()
except ValueError:
    b = None
    pass
dict1 = ["The Sirindhorn Thai Language Institute",
"General Education Center",
"Graduate School",
"Faculty of Engineering",
"Faculty of Arts",
"Faculty of Science",
"Faculty of Political Science",
"Faculty of Architecture",
"Faculty of Commerce and Accountancy",
"Faculty of Education",
"Faculty of Communication Arts",
"Faculty of Economics",
"Faculty of Medicine",
"Faculty of Veterinary Science",
"Faculty of Dentistry",
"Faculty of Pharmaceutical Sciences",
"Faculty of Law",
"Faculty of Fine and Applied Arts",
"Faculty of Nursing",
"Faculty of Allied Health Sciences",
"Faculty of Psychology",
"Faculty of Sports Science",
"School of Agricultural",
"College of Population Studies",
"College of Public Health Sciences",
"Language Institute",
"Sasin Graduate Institute of Business",
"Administration of Chulalongkorn University"
]
if str(a) == '01' or str(a) =='02' :
    print("OK")
elif str(a) in dict1:
    print("OK")
else:
    print("Error")