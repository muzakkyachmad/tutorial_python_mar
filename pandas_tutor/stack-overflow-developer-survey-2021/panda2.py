
#2nd video on the playlist - creating a dataframe

import pandas as pd

#creating a dataframe from a set of dictionary
people = {
    "first": ["corey", "jane", "john"],
    "last": ["schafer", "doe", "doe"],
    "email": ["corey@gmail.com", "jane@gmail.com", "john@gmail.com"]
}

df1 = pd.DataFrame(people)
#print(df1)

df2 = pd.DataFrame(people['email'])
#print(df2)

df3 = type(df2)
#print(df3)

#df4 = pd.DataFrame[df.count]
#print(df4)

df5 = pd.DataFrame(df['last', 'email']) #whats wrong?
#print(df5)

df6 = pd.DataFrame[df.columns]
print(df6)

