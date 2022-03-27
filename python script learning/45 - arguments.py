
#how to use the function and arguments

car1 = {
    "make": "Ford",
    "model": "Fiesta",
    "mileage": 23000,
    "fuel consumed": 460
}

mpg1 = car1["mileage"] / car1["fuel consumed"]
name = f"{car1['make']}{car1['model']}"
print(f"{name} does {mpg1} miles per gallon")

#######
def calculate_mpg2():
    car2 = {
    "make": "Ford",
    "model": "Fiesta",
    "mileage": 23000,
    "fuel consumed": 460
}
    mpg2 = car2["mileage"] / car2["fuel consumed"]
    name = f"{car2['make']}{car2['model']}"
    print(f"{name} does {mpg2} miles per gallon")

calculate_mpg2()


# changing the car2 data to have more data


cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel consumed": 350},
    {"make": "mazda", "model": "MX-5", "mileage": 49000, "fuel consumed": 900},
    {"make": "mini", "model": "Cooper", "mileage": 31000, "fuel consumed": 235},
 ]

#argument is a value that the user passes in to the function
#parameter is variable that accepts a value inside the function

def calculate_mpg(car):

    mpg = car["mileage"] / car["fuel consumed"]
    name = f"{car['make']}{car['model']}"
    print(f"{name} does {mpg} miles per gallon")

for car in cars:
    calculate_mpg(car)















