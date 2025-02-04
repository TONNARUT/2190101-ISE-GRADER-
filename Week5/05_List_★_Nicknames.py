full_names = ["Robert", "William", "James", "John", "Margaret", "Edward", "Sarah", "Andrew", "Anthony", "Deborah"]
nicknames = ["Dick", "Bill", "Jim", "Jack", "Peggy", "Ed", "Sally", "Andy", "Tony", "Debbie"]

for i in range(int(input())):
    name = input()
    if name in full_names:
        print(nicknames[full_names.index(name)])
    elif name in nicknames:
        print(full_names[nicknames.index(name)])
    else:
        print("Not found")