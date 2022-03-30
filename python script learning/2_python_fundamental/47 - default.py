def add(x, y):
    total = x + y
    return total

print(add(5,10))

#we can set the single value of default on the parameter
def add2(x, y=2):
    return x + y

print(add2(5,)) #the y is not defined because it already has a default value on the def

#sample of default function
print(1, 2, 3, sep=' - ')

def greet1():
    print('hey there rolf')

def hi():
    print('hello')

def greet():
    return 'hello'

x = hi()
y = greet()