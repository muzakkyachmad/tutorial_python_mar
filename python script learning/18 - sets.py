#sets is another collection like list and tuples which contain multiple values inside them
#sets dont hold orders and dont contain duplicate elements

art_friends = {"budi", "bili"}
science_friends = {"kiki", "loli"}

art_friends.add("jeni")
print(art_friends)

art_friends.add("jean")
print(art_friends)

art_friends.remove("bili")
print(art_friends)

#advance set operations

art_friends_2 = {"rolf", "anne", "jen"}
science_friends_2 = {"jen", "charlie"}

art_but_not_science = art_friends_2.difference(science_friends_2) #.difference is used for sorting which element is out of the context
science_but_not_art = science_friends_2.difference(art_friends_2)



print(art_but_not_science)
print(science_but_not_art)

not_in_both = art_friends_2.symmetric_difference(science_friends_2) #.symmetric_difference is used for sorting which element is included in both variable
print(not_in_both)

#to figure out which element that included in two or more variable, use .intersection

study_both = art_friends_2.intersection(science_friends_2) #.symmetric_difference is used for sorting which element is included in both variable
print(study_both)

#to include all of the elements in the sets

not_in_both = art_friends_2.symmetric_difference(science_friends_2) #.symmetric_difference is used for sorting which element is included in both variable
print(not_in_both)

#quiz nearby friends - chap 1 - 19 ?

nearby_people = {'rolf', 'jen', 'anna'}
user_friends = set()

friend = input("Enter your friend name to see if he is nearby: ")
user_friends.add(friend)
print(user_friends.intersection(nearby_people))


