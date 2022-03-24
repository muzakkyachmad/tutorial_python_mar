
#how to use the function and arguments

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



