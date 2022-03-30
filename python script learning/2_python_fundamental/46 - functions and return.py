

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
    return mpg


def car_name(car):
    name = f"{car['make']}{car['model']}"
    return name


def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)

    print(f"{name} does {mpg} miles per gallon")


for car in cars:
    print_car_info(car)


####another example on math operations
def divide(x, y):
    if y == 0:
        return "You tried to divide by zero!"
    else:
        return x / y

print(divide(10, 2))
print(divide(6, 0))
