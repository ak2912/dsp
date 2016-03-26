import csv
import pandas as pd

url = "https://raw.githubusercontent.com/ak2912/dsp/master/python/faculty.csv"
df = pd.read_csv(url)

list(df.columns.values)
#spaces in tricky places!
df[' degree']

import regex as re  
df[' degree'].replace(regex=True,inplace=True,to_replace=r'[.]',value=r'')
#remove all periods

df[' degree'].value_counts()
#Question 1

df[' title'].value_counts()
#Question 2

email = list(df[' email'])
email
#Question 3


email_split = df[' email'].apply(lambda x: pd.Series(x.split('@')))
email_set= set(email_split[1])
#Question 4
