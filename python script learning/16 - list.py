#how to print a list

friends = ["Rolf", "Bob", "Anne"] #to make a list in 1 variable, use [] and put "" to define the list and , to separate it
print(friends[1]) #use [] to make the program choosing the list automatically and the counting is started from 0 as the 1st element of the list

friends_2 = ["Budi", "Bejo"]
print(len(friends_2)) #len stands for the length of the variable and used to count it

#to remove a list in variable
friendlist = [["Budi", 24],
              ["Bejo", 25],
              ["Babi", 40]
              ]
friendlist.remove(["Babi", 40]) #.remove is the command to del the names
print(friendlist)

#to add an elements in the variable
friendship = [["Budi", 24],
              ["Bejo", 25],
              ["Babi", 40]
              ]
friendlist.append(["Bobi", 90]) #use .append to add the elements in the last part of the variable
print(friendship)

