#to call the dictionary

friend_ages = {"rolf": 25, "anne": 37, "charlie": 31, "bob": 22}

for name in friend_ages: #to let the program show the name in the list
    print(name)

for age in friend_ages.values(): #.values used to call the number
    print(age)

for friend, age in friend_ages.items(): #.values used to call the number
    print(f"{name} is {age} years old")


