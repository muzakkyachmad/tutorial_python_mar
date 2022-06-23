
#this is a tutorial from youtube corey schafer - panda
import pandas as pd

df = pd.read_csv('survey_results_public.csv') #commands to make the data frame and load the data
print(df)

print(df.shape) #to show how many is the rows and columns on the file

print(df.info()) #to give info of the file

#line 12 + 13 is to set the file to be easier to read
print(pd.set_option('display.max_columns', 85))
print(pd.set_option('display.max_rows', 85))

schema_df = pd.read_csv('survey_results_schema.csv') #to load another file named schema
print(schema_df)

print(df.head(10))


