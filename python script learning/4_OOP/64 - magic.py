class Student:
    def __init__(self, name):
        self.name = name


movies = ['the matrix', 'finding nemo']
print(movies.__class__)
print("hi".__class__)
print(len(movies))



#another example
class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

ford = Garage()
ford.cars.append('fiesta')
ford.cars.append('focus')

print(ford.cars)
