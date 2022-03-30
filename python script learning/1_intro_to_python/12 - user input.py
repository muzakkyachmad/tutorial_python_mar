#how to get the user input using input function in string

my_name = "Zakky"
your_name = input("Enter your name: ") #using the input command to ask the user to input the variable

print(f"Hello {your_name}! My name is {my_name}" )

age = input("Enter your age: ")
age_number = int(age) #this line is connecting the input to integer
print(f"You have live for {age_number * 12} months")

age_2 = int(input("Enter your age: "))
months = age_2 * 12
print(f"You have lived for {months} months")

