
#2nd video on the playlist - creating a dataframe

import pandas as pd


#creating a dataframe from a set of dictionary
people = {
    "first": ["corey", "jane", "john"],
    "last": ["schafer", "doe", "doe"],
    "email": ["corey@gmail.com", "jane@gmail.com", "john@gmail.com"]
}

df1 = pd.DataFrame(people)
print(df1)

df2 = pd.DataFrame(people['email'])
print(df2)

df3 = type(df2)
print(df3)

df4 = df1[['last', 'email']] #to access a multiple columns
print(df4)

df5 = df1.columns #to access the columns
print(df5)

df6 = df1.head(1)
print(df6)

#to access a certain data in a row and columns more specific - ok and use this one
df7 = df1.iloc[[0, 1], 2]
print(df7)

df8 = df1.loc[[0, 1], ['email', 'last']]
print(df8)