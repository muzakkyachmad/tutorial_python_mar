#this is a file from learning on youtube - how to set custom indexes


import pandas as pd


df = pd.read_csv('../stack-overflow-developer-survey-2021/survey_results_public.csv', index_col='ResponseId')
print(df)

dfset1 = pd.set_option('display.max_columns, 5')
dfset2 = pd.set_option('display.max_rows, 5')
head1 = df.head()
print(head1)
print(dfset1)
print(dfset2)


loc = df.loc[1]
print(loc)

people = {
    "first": ["corey", "jane", "john"],
    "last": ["schafer", "doe", "doe"],
    "email": ["corey@gmail.com", "jane@gmail.com", "john@gmail.com"]
}

df1 = pd.DataFrame(people)
#print(df1)

df2 = df1['email'] #this command is to access selected index
#print(df2)

#to set the email as the index
df3 = df1.set_index('email', inplace=True) #inplace=true as the index
df4 = df1
#print(df4)

df5 = df1.index #index
#print(df5)

df6 = df1.reset_index(inplace=True) #to reset the changing of indexing
df7 = df1
#print(df7)



