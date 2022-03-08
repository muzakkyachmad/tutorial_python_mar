

numbers = [0, 1, 2, 3, 4]
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * 2)

    print(doubled_numbers)

    doubled_numbers = [number * 2 for number in numbers]

double_numbers = [number * 2 for number in range(5)]
print(double_numbers)



friend_ages = [22, 31, 35, 37]
age_strings = [f"My friends is {age} yo" for age in friend_ages]

print(age_strings)

names = ["Rolf", "Bob", "Jen"]
lower = [name.lower() for name in names]
print(lower)


friend = input("Enter your friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    print(f"{friend} is one of your friends")