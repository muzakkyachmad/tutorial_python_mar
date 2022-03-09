cars1 = ["ok", "ok", "ok", "faulty", "ok", "ok", ]

for status1 in cars1:
    print(f"This car is {status1}")

cars2 = ["ok", "ok", "ok", "faulty", "ok", "ok", ]

for status2 in cars2:
    if status2 == "faulty":
        print("Stopping the production line!")
        break  # break is used to stop the loop
        print(f"This car is {status2}")

cars3 = ["ok", "ok", "ok", "faulty", "ok", "ok",]

for status in cars3:
    if status == "faulty":
        print("Found faulty car, skipping...")
        continue #continue is used to continue the whole loop
    print(f"This car is {status}")
    print("shipping new car to customer")


