is_learning = True

while is_learning:
    print("You are learning!") #without next line, it will print many times
    is_learning = False #by this line, it will check the is_learning and evaluate as false, so it will not print anymore, just once


is_learning2 = True
while is_learning2:
    print("You're learning!")
    user_input = input("Are you still learning? ")
    is_learning2 = user_input == "Yes!"


#example for making the loop
user_input_ex = input("do you wish to run the program? (yes/no): ")

while user_input_ex == "yes":
    print("we're running it!")
    user_input_ex = input("do you wish to run the program? (yes/no): ")

print("we stopped running")


#################EXERCISE
user_input_ex2 = input("do you want to print? (print/queue): ")

while user_input_ex2 == "print":
    print("hello!")
    user_input_ex2 = input("do you want to print? (print/queue): ")

print("we stopped printing")

# Ask the user to choose one of two options:
# if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
# if they type 'q', our program should terminate.

# Let's begin by asking the user to type either 'p' or 'q':
user_input_sol = input("Enter q or p: ")

# Now we must repeat until they type 'q':
while user_input_sol != "q":
    # Inside our loop, check if they typed 'p'. If they did, print "Hello"
    if user_input_sol == "p":
        print("Hello")
    # Now we must ask the user for their input again—otherwise we would be in an infinite loop!
    user_input_sol = input("Enter q or p: ")