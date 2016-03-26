#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

"""""
import csv

  def read_data(data):
   # COMPLETE THIS FUNCTION

  def get_min_score_difference(self, parsed_data):
    # COMPLETE THIS FUNCTION

  def get_team(self, index_value, parsed_data):
    # COMPLETE THIS FUNCTION
    
""""""
#My code

import pandas as pd

url = "https://raw.githubusercontent.com/ak2912/dsp/master/python/football.csv"
df = pd.read_csv(url)

df['Goals Difference'] = df['Goals'].sub(df['Goals Allowed'])
df['Raw Goals Difference'] = df['Goals Difference'].abs()

df['Raw Goals Difference'].argmin()

df.loc[7, 'Team']
df.loc[7, 'Goals Difference']


def Q8(url):
    df = pd.read_csv(url)
    df['Goals Difference'] = df['Goals'].sub(df['Goals Allowed'])
    print "Team Name: " + df.loc[7, 'Team']
    print "Goal Differential: " + str(df.loc[7, 'Goals Difference'])

#Run the Q8 function with the correct URL for the correct answer.  Output is-

"""""
Team Name: Aston_Villa
Goal Differential: -1
"""""
