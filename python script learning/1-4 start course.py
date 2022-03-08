#Course 1-4 - defining a variable and printing it

age = 30 #age = variable | #30 = value
print(age)

friend_age_2 = 23 #use _ as a space between the words of variable
print(friend_age_2)

PHY = 3.14159 #use the uppercase for variable that is fixed



#Course 1-6 - numbers

PI = 3.14
maths_operations = 360 / PI
print(maths_operations)

maths_operation = 1 + 3 * 4 / 2 - 2
print(maths_operation)

float_division = 12 / 3
print(float_division) #floats are numbers with decimal point

integer_division = 12 // 3 # // is used to remove the decimal point
print(integer_division) #integers are whole numbers



#Course 1-7 - the remainder of division
integer_division = 13 // 5
print(integer_division)

remainder = 13 % 5 # % is for modulus calculation
print(remainder)

x = 37
remainder = x % 2
print(remainder)


#Course 1-10 - strings (strings can contain text like characters, symbols, or number)
my_string = 'Hello, world!' #the quotation mark should be consistent to make it works better
print(my_string)

string_with_quotes = "hello, it's me!"
another_with_quotes = 'he said "you are amazing!"' #escaping is putting backslash in front of a character) is used to remove meaning from a character

multiline = """Hello, world!

my name is zakky, nice to meet you!"""
print(multiline) #multiline using 3" is very useful for coding longer text!








#Course 1-11 - using string and f string
age = 34
age_as_str = str (age)
print("you are" + age_as_str)
print(f"You are {age}")

name = "zakky"
greeting = f"how are you {name}?"
print(greeting)

name = "jaki"
final_greeting = "how are you, {}?"
jose_greeting = final_greeting.format(name=name)

print(jose_greeting)


#course 1-12 - getting data from our users
my_name = "zakky"
your_name = input("enter your name: ")

print(f"hello {your_name}, my name is {my_name}")

age = input("enter your age: ")
age_num = int(age)
print(f"you have liveed for {age_num * 12} months.")

#exercise
#question 1

your_name = input('enter your name: ')
print(f'hello {your_name}!')


NAME = input("Enter your name: ")
print(f"Hello, {NAME}")

# Secondly, ask the user for their age and convert it into a number.
# Then, print out how many months that equals to (you'll have to multiply the age by 12).

age = input("enter your age: ")
age_num = int(age)
print(f"you have lived for {age_num * 12} months")



