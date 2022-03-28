#example 6.1.1

def add(x,y):

    return x + y

x = 2
y = 5

z = add(x,y)

print(z)


#6.2 functions with multiple retun values

def stat(x):

    totalsum = 0

    #find the sum of all the numbers
    for x in data:
        totalsum = totalsum + x

    #find the mean or average of all the numbers
    N = len(data)
    mean = totalsum / N

    return totalsum,mean

data = [1, 5, 6, 3, 12, 3]

totalsum, mean = stat(data)
print(totalsum, mean)

#6.3 exercises
