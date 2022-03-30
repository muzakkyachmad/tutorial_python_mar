#to predict the input of the user and make the program response to it

friend = "rolf"
user_name = input("Enter your name: ")

#if the user input is correct, we can use this
if user_name == friend:
    print("Hello, friend!")

#if the user input is correct, we can use this as well
friends = "boni"
friend_input = input("Enter name: ")
if friend_input == friends:
    print("Hello bro!") #this is the response if the user input is correct

else: #this is the alternative to response f the input is wrong
    print("who the fuck are you?")

#if there are two variables - 1st way

friendss = ["mojo", "joko", "jono"]
family = ["bono", "noob"]

name_user = input("Enter your name: ")

if name_user in friendss:
    print("Hello my friend!")

if name_user in family:
    print("Hello my fam!")

else: #else is used if the input is not correct with the keywords
    print("who are you bitch?")

#2nd way
friend2 = ["mojo", "joko", "jono"]
family2 = ["bono", "noob"]

name_user2 = input("Enter the name: ")

if name_user2 in friend2:
    print("Hello my friend!")
elif name_user2 in family2: #elif is to answer another true statement
        print("Hello my fam!")
else:
    print("who are you dude?")
