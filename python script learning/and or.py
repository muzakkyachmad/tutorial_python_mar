#asking a question and got true or false answer from and or equation

age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age < 150
usually_working = age > 18 or age < 65

print(f"you can learn programming {can_learn_programming}")

#using function bool
print(bool(35))
print(bool(""))

#how the and works

#True and False - word and will look at first value which is true

x = 35 and 0 #and give us the first value if it is false, otherwise it gives you the second value
print(x)

#how the or works - or gives us the first value if it is true, otherwise it gives us the second value

x_2 = 35 and 0
print(x_2)


cmp = 15 > 20 or 17 < 20
print(cmp)

x_3 = True
cmp_2 = x_3 and 18
print(cmp_2)


age = int(input("Enter your age: "))
side_job = True
print(age > 18 and age < 65 or side_job)


