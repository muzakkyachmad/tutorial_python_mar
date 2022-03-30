


my_student = {
     'name': 'rolf',
     'grades': [67, 90, 95, 100]
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])

print(average_grade(my_student))


class Student: #class will define what is the object stands for
    def __init__(self, new_name, new_grades): #donderfunction is  __init__
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('rolf', [70, 88, 90, 99])
student_two = Student('jose', [50, 60, 99, 100])


print(student_one.__class__)


#63

class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

print(Movie('The Matrix', 1994).name) #to print only name from the class

matrix = Movie('The Matrix', 1994)

print(matrix.name)
print(matrix.year)






