import csv
import pandas as pd

url = "https://raw.githubusercontent.com/ak2912/dsp/master/python/faculty.csv"
df = pd.read_csv(url)

reverse = lambda x: pd.Series([i for i in reversed(x.split(' '))])
reverse_name = df['name'].apply(reverse)
#The first column now has the last name

df['last name'] = reverse_name[0]

#let's clean the "title" column
df[' title'] = df[' title'].map(lambda x: str(x)[:-17])

from collections import defaultdict
faculty_dict=defaultdict(list)
for i,j,k,l in zip(df['last name'],df[' degree'],df[' title'],df[' email']):
    faculty_dict[i].append(j)
    faculty_dict[i].append(k)
    faculty_dict[i].append(l)

from itertools import islice
def take(n, iterable):
    return list(islice(iterable, n))

q6 = take(3, faculty_dict.iteritems())
##Question 6


name = df['name'].apply(lambda x: pd.Series(x.split(' ')))
df['first name'] = name[0]
#two of the names are initials.  may need to fix

del df['name']

professor_dict = df.set_index(['first name','last name']).T.to_dict('list')

q7 = take(3, professor_dict.iteritems())
##Question 7, using the previously defined function in Q6


new_professor_dict = df.set_index(['last name','first name']).T.to_dict('list')

q8 = take(3, new_professor_dict.iteritems())

##Question 8
