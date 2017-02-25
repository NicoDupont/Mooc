"""
02/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Data Cleaning : Challenge: Cleaning data
"""


"""
1: How Challenges Work
At Dataquest, we're huge believers in learning through doing and we hope this shows in the learning experience of the missions.
While missions focus on introducing concepts, challenges allow you to perform deliberate practice by completing structured problems.
You can read more about deliberate practice here and here. Challenges will feel similar to missions but with little instructional material and a larger focus on exercises.

If you have questions or run into issues, head over to the Dataquest forums or our Slack community.
"""



"""
2: Life And Death Of Avengers
The Avengers are a well-known and widely loved team of superheroes in the Marvel universe that were introduced in the 1960's in the original comic book series.
They've since become popularized again through the recent Disney movies as part of the new Marvel Cinematic Universe.

The team at FiveThirtyEight wanted to dissect the deaths of the Avengers in the comics over the years.
The writers were known to kill off and revive many of the superheroes so they were curious to know what data they could grab from the Marvel Wikia site, a fan-driven community site, to explore further.
To learn how they collected their data, which is available on their Github repo, read the writeup they published on their site.
"""




"""
3: Exploring The Data
While the FiveThirtyEight team has done a wonderful job acquiring this data, the data still has some inconsistencies.
Your mission, if you choose to accept it, is to clean up their dataset so it can be more useful for analysis in Pandas.
Let's read our dataset into Pandas as a DataFrame and preview the first 5 rows to get a better sense of our data.

Instructions
This step is a demo. Play around with code or advance to the next step.
"""
import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)
""" Console Outputs or Results
                                                 URL  \
0      http://marvel.wikia.com/Henry_Pym_(Earth-616)
1  http://marvel.wikia.com/Janet_van_Dyne_(Earth-...
2  http://marvel.wikia.com/Anthony_Stark_(Earth-616)
3  http://marvel.wikia.com/Robert_Bruce_Banner_(E...
4   http://marvel.wikia.com/Thor_Odinson_(Earth-616)

                    Name/Alias  Appearances Current?  Gender  \
0    Henry Jonathan "Hank" Pym         1269      YES    MALE
1               Janet van Dyne         1165      YES  FEMALE
2  Anthony Edward "Tony" Stark         3068      YES    MALE
3          Robert Bruce Banner         2089      YES    MALE
4                 Thor Odinson         2402      YES    MALE

  Probationary Introl Full/Reserve Avengers Intro  Year  Years since joining  \
0                 NaN                      Sep-63  1963                   52
1                 NaN                      Sep-63  1963                   52
2                 NaN                      Sep-63  1963                   52
3                 NaN                      Sep-63  1963                   52
4                 NaN                      Sep-63  1963                   52

  Honorary                        ...                         Return1 Death2  \
0     Full                        ...                              NO    NaN
1     Full                        ...                             YES    NaN
2     Full                        ...                             YES    NaN
3     Full                        ...                             YES    NaN
4     Full                        ...                             YES    YES

  Return2 Death3 Return3 Death4 Return4 Death5 Return5  \
0     NaN    NaN     NaN    NaN     NaN    NaN     NaN
1     NaN    NaN     NaN    NaN     NaN    NaN     NaN
2     NaN    NaN     NaN    NaN     NaN    NaN     NaN
3     NaN    NaN     NaN    NaN     NaN    NaN     NaN
4      NO    NaN     NaN    NaN     NaN    NaN     NaN

                                               Notes
0  Merged with Ultron in Rage of Ultron Vol. 1. A...
1  Dies in Secret Invasion V1:I8. Actually was se...
2  Death: "Later while under the influence of Imm...
3  Dies in Ghosts of the Future arc. However "he ...
4  Dies in Fear Itself brought back because that'...

[5 rows x 21 columns]
"""




"""
4: Filter Out The Bad Years
Since the data was collected from a community site, where most of the contributions came from individual users, there's room for errors to surface in the dataset. 
If you plot a histogram of the values in the Year column, which describes the year each Avenger was introduced, you'll immediately notice some oddities. 
There are quite a few Avengers who look like they were introduced in 1900, which we know is a little fishy. 
The Avengers weren't introduced in the comic series until the 1960's!

This is obviously a mistake in the data and you should remove all Avengers before 1960 from the DataFrame.

Instructions
We only want to keep the Avengers who were introduced after 1960.
Store only the rows describing Avengers added in 1960 or later in true_avengers.
"""
import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

#avengers['Year'].hist()

true_avengers = avengers[avengers["Year"] > 1960]
true_avengers['Year'].hist()
""" Console Outputs or Results
see plot13.png
"""



"""
5: Consolidating Deaths
We are interested in the number of total deaths each character experienced and we'd like a field containing that distilled information. 
Right now, there are 5 fields (Death1 to Death5) that each contain a binary value representing if a superhero experienced that death or not. 
For example, a superhero can experience Death1, then Death2, etc. until they were no longer brought back to life by the writers.

We'd like to coalesce that information into just one field so we can do numerical analysis more easily.

Instructions
Create a new column, Deaths, that contains the number of times each superhero died. 
The possible values for each death field are YES, NO, and NaN for missing data.
Keep all of the original columns (including Death1 to Death5) and update true_avengers with the new Deaths column.

"""
col_death = ["Death1","Death2","Death3","Death4","Death5"]

#for col in col_death:
#    true_avengers[col] = true_avengers[col].fillna("NO")

#print("----------------")
#print(true_avengers[["Death1","Death2","Death3","Death4","Death5"]].head())

def convdeath(str):
    if str == "YES":
        return int(1)
    else:
        return int(0)
    
#for col in col_death:
#    true_avengers[col] = true_avengers[col].apply(convdeath)

#print("----------------")
#print(true_avengers[["Death1","Death2","Death3","Death4","Death5"]].head())

def sumdeath(df):
    res = 0
    for col in col_death:
        if df[col] == 'YES':
            res += 1
    return res

true_avengers["Deaths"] = true_avengers.apply(sumdeath,axis=1)

print("----------------")
print(true_avengers[["Deaths","Death1","Death2","Death3","Death4","Death5"]].head())
""" Console Outputs or Results
Output
----------------
   Deaths Death1 Death2 Death3 Death4 Death5
0       1    YES    NaN    NaN    NaN    NaN
1       1    YES    NaN    NaN    NaN    NaN
2       1    YES    NaN    NaN    NaN    NaN
3       1    YES    NaN    NaN    NaN    NaN
4       2    YES    YES    NaN    NaN    NaN
"""




"""
6: Years Since Joining
For the final task, we want to know if the Years since joining field accurately reflects the Year column. 
If an Avenger was introduced in Year 1960, is the Years since joining value for that Avenger 55?

Instructions
Calculate the number of rows where Years since joining is accurate.
Since this challenge was created in 2015, use that as the reference year.
We want to know for how many rows Years since joining was correctly calculated as Year value subtracted from 2015.
Assign the integer value describing the number of rows with a correct value for Years since joining to joined_accuracy_count.
"""
joined_accuracy_count  = int()

print("----------------")
print(true_avengers.info())
print("----------------")

print(true_avengers[["Year","Years since joining"]].head())

def testyearssincecol(df):
    if 2015 - df["Years since joining"] == df["Year"]:
        return 1
    else:
        return 0

true_avengers["test"] = true_avengers.apply(testyearssincecol,axis=1)

joined_accuracy_count = true_avengers["test"].sum()
print(joined_accuracy_count)
print(true_avengers[["Year","Years since joining","test"]].head())

# more simple ...
joined_accuracy_count  = int()
correct_joined_years = true_avengers[true_avengers['Years since joining'] == (2015 - true_avengers['Year'])]
joined_accuracy_count = len(correct_joined_years)
""" Console Outputs or Results
Output
----------------
<class 'pandas.core.frame.DataFrame'>
Int64Index: 159 entries, 0 to 172
Data columns (total 22 columns):
URL                            159 non-null object
Name/Alias                     149 non-null object
Appearances                    159 non-null int64
Current?                       159 non-null object
Gender                         159 non-null object
Probationary Introl            13 non-null object
Full/Reserve Avengers Intro    159 non-null object
Year                           159 non-null int64
Years since joining            159 non-null int64
Honorary                       159 non-null object
Death1                         159 non-null object
Return1                        68 non-null object
Death2                         16 non-null object
Return2                        16 non-null object
Death3                         2 non-null object
Return3                        2 non-null object
Death4                         1 non-null object
Return4                        1 non-null object
Death5                         1 non-null object
Return5                        1 non-null object
Notes                          74 non-null object
Deaths                         159 non-null int64
dtypes: int64(4), object(18)
memory usage: 28.6+ KB
None
----------------
   Year  Years since joining
0  1963                   52
1  1963                   52
2  1963                   52
3  1963                   52
4  1963                   52
159
   Year  Years since joining  test
0  1963                   52     1
1  1963                   52     1
2  1963                   52     1
3  1963                   52     1
4  1963                   52     1
"""
