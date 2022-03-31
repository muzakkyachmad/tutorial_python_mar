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


    def __getitem__(self, i):
        return self.cars[i]


    def __repr__(self):
        return f'<Garage with {len(self)}>'

ford = Garage()
ford.cars.append('fiesta')
ford.cars.append('focus')


print(ford[1]) #to call Garage.__getitem__(ford, 0)


for car in ford:
    print(car)


#exercise magic in python

class Club:
    def __init__(self, name):
        self.name = name
        self.players = []
        

some_club = Club('Arsenal')
my_club.players.append('Rolf')
my_club.players.append('Anne')

my