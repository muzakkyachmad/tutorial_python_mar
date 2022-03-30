#studying about string - course 10

#one string
my_string = "Hello, world!"
print(my_string)

string_with_quotes = "Hello, it's me!"
another_wit_quotes = "he said \"you are amazing!\" yesterday" #escaping is putting a backslash in front of the character to remove meaning from a character

#multiline string is for long sentences, example

multiline = """Hello, world!

My name is Zakky. Let's change!
"""
print(multiline)


#add string together
name_1 = "zakky"
greeting = "hello, " + name_1
print(greeting)

age = 27
age_as_str = str(age) #str = string
sentence = "You are " + age_as_str
print(sentence)


#string formatting using f string

age_f_string = 28 #way 1
age_as_str_2 = str(age_f_string) #str = string
word = "You are " + age_as_str_2
print(word)

#way 2 - using f but directly with words
age_f_string_2 = 26
print(f"You are {age_f_string_2}") #the string is not using variable, just format it

#way 3 - using f string but using variables

name_2 = "Zakky" #variable 1
greet = f"how are you, {name_2}" #variable 2
print(greet)


#way 4 - using .format and template

name = "Zuko"
final_greeting = "how are you, {} ?" #template
jose_greeting = final_greeting.format(name)
print(jose_greeting)

name = "Bob"
bob_greeting = final_greeting.format(name) #the combination of string by replacing the name_3
print(bob_greeting)

name = "Jose"
final_greeting_2 = "How are you, {name}?"
jose_greeting_2 = final_greeting_2.format(name="Jose") #replacing the name by determined variable
print(jose_greeting_2)
