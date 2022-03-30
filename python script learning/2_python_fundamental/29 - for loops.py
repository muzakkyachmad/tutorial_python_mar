#using for loops to print the name of the elements
friends = ["rolf", "jen", "anne"]

for friend in friends: #friend will be the determiner loop in the elements
    print(friend)

#using for loops to print the string on the print line to make it printed 10x
elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in elements:
    print("Hello bro!")

#using for loops to print the string on the print line to make it printed 10x
for index in range(10):
    print("Hello world")

#using for loops to sort number
for index_number in range (2, 20): #it will start from 2 to 20
    print(index_number)

#using for loops to sort number base on multiple
for index_number_3 in range (2, 20, 3): #3 will be the indicator of multiple
    print(index_number_3)


#exercise with dictionary

students = [
    {"name": "rolf", "grade": 90},
    {"name": "bob", "grade": 78},
    {"name": "jen", "grade": 100},
    {"name": "anne", "grade": 80},
]

for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}!")


