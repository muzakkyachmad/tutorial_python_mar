
cars1 = ["ok", "ok", "ok", "faulty", "ok", "ok",]


for status in cars1:
    if status == "faulty":
        print("Found faulty car, skipping...")
        break
    print(f"This car is {status}")
    print("shipping new car to customer")
else:
    print("all cars built good. no faulty cars")