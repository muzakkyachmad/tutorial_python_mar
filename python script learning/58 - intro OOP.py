
my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90, 99]
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])

print(average_grade(my_student))


#making the list can useful and operate automatically using class and object
class Student:
    def __init__(self, new_name, new_grade): #this funct is to make the object
        self.name = new_name
        self.grades = new_grade

    def average(self): #this funct is to execute the class
        return sum(self.grades) / len(self.grades)

student_one = Student('Rolf Smith', [70, 88, 90, 99])

print(student_one.name)
print(student_one.grades)
print(student_one.__class__)


print(student_one.average())
print(Student.average(student_one))
