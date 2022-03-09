#using math problem - prime number


for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0: #n divided by x will give us 0
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number")
