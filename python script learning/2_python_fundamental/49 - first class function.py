

avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

students = [
    {"name": "rolf", "grades": (67, 90, 95, 100)},
    {"name": "bob", "grades": (56, 78, 80, 90)},
    {"name": "jen", "grades": (99, 90, 95, 99)},
    {"name": "anne", "grades": (100, 100, 95, 100)},
]
for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', 'top': ")

    if operation == "average":
        print(avg(grades))
    elif operation == "total":
        print(total(grades))
    elif operation == 'top':
        print(top(grades))
