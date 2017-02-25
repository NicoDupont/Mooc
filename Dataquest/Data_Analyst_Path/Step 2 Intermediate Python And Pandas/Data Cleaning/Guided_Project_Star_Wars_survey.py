"""
02/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Data Cleaning : Guided Project Star Wars survey
"""


"""
1: How Guided Projects Work
Welcome to a Guided project! Guided projects help you synthesize concepts learned during the Dataquest missions, and start building a portfolio.
Guided projects provide an in-browser coding experience along with help and hints.
Guided projects bridge the gap between learning using the Dataquest missions, and applying the knowledge on your own computer.

Guided projects help you develop key skills that you'll need to perform data science work in the "real world".
Doing well on these projects is slightly different from doing well in the missions, where there is a "right" answer.
In the guided projects, you'll need to create solutions on your own (although we'll be there to help along the way).

In this project, you'll be working with Jupyter notebook, and analyzing data on the Star Wars movies.
By the end, you'll have a notebook that you can add to your portfolio or build on top of on your own.

As you go through this project, Google, StackOverflow, and the documentation for various packages will help you along the way.
All data scientists make extensive use of these and other resources as they write code.

We'd love to hear your feedback as you go through this project, and we hope it's a great experience!

Instructions
For now, just hit "Next" to get started with the project!
"""



"""
2: Introduction
While waiting for Star Wars: The Force Awakens, the team at FiveThirtyEight was interested in answering some questions about Star Wars fans.
One question that particularly interested the team was: Does the rest of America realize that “The Empire Strikes Back” is clearly the best of the bunch?

The team needed to collect data before they could get started answering this question.
They used SurveyMonkey, an online survey tool, to survey Star Wars fans. They received 835 responses total, which you can find here.

In this project, you'll be cleaning and exploring the dataset in Jupyter. You can find the dataset here if you want to download it.

If you want to look at an example notebook that has all the answers to these steps as you go through, you can find one here.

The following code will read the data into a pandas Dataframe:


import pandas as pd
star_wars = pd.read_csv("star_wars.csv", encoding="ISO-8859-1")
We need to specify an encoding because the dataset has some characters that aren't in the Python default utf-8 encoding.
You can read more about character encodings here.

The data has several columns, including:

RespondentID -- An anonymized ID of the person taking the survey.
Gender -- Gender of the respondent.
Age -- Age of the respondent.
Household Income -- Income of the respondent.
Education -- Education level of the respondent.
Location (Census Region) -- Location of the respondent.
Have you seen any of the 6 films in the Star Wars franchise? -- Yes or No response.
Do you consider yourself to be a fan of the Star Wars film franchise? -- Yes or No response.
There are several other columns, which involve questions about the Star Wars movies.
Some questions involved checkboxes, where someone was asked which of several options they liked, and to check all the ones they did like.
This type of data is hard to represent in columnar format, and you'll be cleaning up the columns extensively in this project.

This dataset needs a lot of cleaning, which makes it a good place to practice the skills you've been learning so far.
The first step you'll take is to remove invalid rows. RespondentID is supposed to be a unique ID for each respondent, but it's blank in some rows.
You'll need to remove any rows with an invalid RespondentID.

Instructions
Read the dataset into a Dataframe
Explore the data by using star_wars.head(10). Look for any strange values in the columns and rows.
Look at the column names with star_wars.columns.
Remove any rows where RespondentID is NaN. You can use the pandas.notnull() function for this.
Only select rows where the RespondentID column is not null.
At the end star_wars should only consist of rows where RespondentID is not NaN.
"""
import pandas as pd
star_wars = pd.read_csv("star_wars.csv", encoding="ISO-8859-1")
star_wars.head(10)
star_wars.columns.tolist()
star_wars = star_wars[pd.notnull(star_wars["RespondentID"])]
star_wars.head(3)




"""
3: Cleaning Up Yes/No Columns
Take a look at the next two columns, which are:


* `Have you seen any of the 6 films in the Star Wars franchise?`
* `Do you consider yourself to be a fan of the Star Wars film franchise?`
You'll see that they are both Yes/No questions.
There's another possible value they can take on, NaN, when a respondent chose not to answer that question.
You can use the value_counts() method on a Series to see all the unique values in a column, and the counts of each value.

Both columns are currently string types -- Yes or No.
In order to make it a bit easier to analyze down the line, convert each column to a Boolean, with only True, False, or NaN.
Booleans are easier to work with because you can select the rows that are True or False without having to do a string comparisons.

You can use the map() method on Series to do this conversion.

If you have a Series that looks like this:


series = ["Yes", "No", NaN, "Yes"]
You can use a dictionary to define a mapping from each value in series to a new value:


yes_no = {
    "Yes": True,
    "No": False
}
Then, you can call the map function to perform the mapping:


series = series.map(yes_no)
series will end up looking like this:


[True, False, NaN, True]
Instructions
Convert the Have you seen any of the 6 films in the Star Wars franchise? column to the Boolean type.
Convert the Do you consider yourself to be a fan of the Star Wars film franchise? column to the Boolean type.
At the end, both columns should have only True, False, or NaN values in them.
"""
# 3: Cleaning Up Yes/No Columns
yes_no = {
    "Yes": True,
    "No": False
}

#star_wars["Have you seen any of the 6 films in the Star Wars franchise?"] = star_wars["Have you seen any of the 6 films in the Star Wars franchise?"].fillna(value="No")
star_wars["Have you seen any of the 6 films in the Star Wars franchise?"] = star_wars["Have you seen any of the 6 films in the Star Wars franchise?"].map(yes_no)

#star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"] = star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"].fillna(value="No")
star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"] = star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"].map(yes_no)

star_wars.head(3)


""" Console Outputs or Results

"""




"""
4: Cleaning Up Checkbox Columns
The next 6 columns represent a checkbox question.
The respondent was asked Which of the following Star Wars films have you seen?
Please select all that apply., and then was able to check off a series of boxes indicating which movies they saw.

The columns that represent this data are:

Which of the following Star Wars films have you seen? Please select all that apply. -- whether or not the respondent saw Star Wars: Episode I The Phantom Menace.
Unnamed: 4 -- whether or not the respondent saw Star Wars: Episode II Attack of the Clones.
Unnamed: 5 -- whether or not the respondent saw Star Wars: Episode III Revenge of the Sith.
Unnamed: 6 -- whether or not the respondent saw Star Wars: Episode IV A New Hope.
Unnamed: 7 -- whether or not the respondent saw Star Wars: Episode V The Empire Strikes Back.
Unnamed: 8 -- whether or not the respondent saw Star Wars: Episode VI Return of the Jedi.
For each of these columns, if the value in a cell is the name of the movie, that means the respondent saw it.
If the value is NaN, the respondent either didn't answer, or didn't see the movie, but we'll assume that they didn't see the movie.

You need to convert each of these columns to a Boolean, then rename the column to have a more clear name.
You can do the Boolean conversion like you did earlier, except you'll need to include the movie title and NaN in the mapping dictionary.

For example, if the column Series looks like this:


["Star Wars: Episode I  The Phantom Menace", NaN, "Star Wars: Episode I  The Phantom Menace"]
You can use a mapping dictionary that looks like this:


{
    "Star Wars: Episode I  The Phantom Menace": True,
    NaN: False
}
After you call the map() method on the Series, the column should only contain True or False values.

After the values are converted with the map method, you can rename the columns to better reflect what the values represent. You can use the rename() method on Dataframes for this.

The rename method works a lot like map. You pass it a dictionary that maps current column names to new ones:


star_wars = star_wars.rename(columns={
    "Which of the following Star Wars films have you seen? Please select all that apply.": "seen_1"
})
The rename method will only rename columns specified in the dictionary, and will not change the names of other columns.
The above code will rename the Which of the following Star Wars films have you seen? Please select all that apply. column to seen_1.

Instructions
For each column above, convert the column to only contain True and False values.
One easy way to select the column names is to do star_wars.columns[3:9] instead of typing them out.
Be very careful with spacing when constructing your mapping dictionary!
In the cells, Star Wars: Episode I The Phantom Menace has two spaces between the end of Episode I and the start of The Phantom, but this is not the case in Star Wars: Episode VI Return of the Jedi.
Make sure to look at the values in the cells to find the appropriate spacing.
Rename each of the columns above to have more clear names.
We recommend using seen_1 to indicate if the respondent saw Star Wars: Episode I The Phantom Menace, seen_2 for Star Wars: Episode II Attack of the Clones, and so on.
At the end, you should have clearly named columns indicating with a True or False if the respondent saw each Star Wars movie from 1-6.
"""
# 4: Cleaning Up Checkbox Columns

film_list = ["Which of the following Star Wars films have you seen? Please select all that apply.","Unnamed: 4","Unnamed: 5","Unnamed: 6","Unnamed: 7","Unnamed: 8"]

#for film in film_list:
#    print(star_wars[film].value_counts())

real_name = {
    "Which of the following Star Wars films have you seen? Please select all that apply.":"See Stw Ep1",
    "Unnamed: 4":"See Stw Ep2",
    "Unnamed: 5":"See Stw Ep3",
    "Unnamed: 6":"See Stw Ep4",
    "Unnamed: 7":"See Stw Ep5",
    "Unnamed: 8":"See Stw Ep6"}

#Star Wars: Episode III  Revenge of the Sith
#Star Wars: Episode III Revenge of the Sith

film_map = {
    "Star Wars: Episode I  The Phantom Menace": True,
    np.nan: False,
    "Star Wars: Episode II  Attack of the Clones": True,
    "Star Wars: Episode III  Revenge of the Sith": True,
    "Star Wars: Episode IV  A New Hope": True,
    "Star Wars: Episode V The Empire Strikes Back": True,
    "Star Wars: Episode VI Return of the Jedi": True
}

for film in film_list:
    #star_wars[film] = star_wars[film].fillna(value="No")
    star_wars[film] = star_wars[film].map(film_map)

star_wars = star_wars.rename(columns=real_name)

# see all star wars
def seeallstw(df):
    nbsee = df["See Stw Ep1"]+df["See Stw Ep2"]+df["See Stw Ep3"]+df["See Stw Ep4"]+df["See Stw Ep5"]+df["See Stw Ep6"]
    if nbsee == 6:
        return True
    else:
        return False

star_wars["See All Stw"] = star_wars.apply(seeallstw,axis=1)
star_wars.head(3)

# verif
test = star_wars[(star_wars["See Stw Ep1"] == True) & (star_wars["See Stw Ep2"] == True) & (star_wars["See Stw Ep3"] == True) & (star_wars["See Stw Ep4"] == True) & (star_wars["See Stw Ep5"] == True) & (star_wars["See Stw Ep6"] == True)]
test.head()
""" Console Outputs or Results

"""



"""
5: Cleaning Up Ranking Columns
The next 6 columns ask the respondent to rank the Star Wars movies in order of least to most favorite.
1 means the film was their most favorite, and 6 means it was their least favorite. Each of the following columns can contain the values 1, 2, 3, 4, 5, 6, or NaN:

Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film. -- How much the respondent liked Star Wars: Episode I The Phantom Menace.
Unnamed: 10 -- How much the respondent liked Star Wars: Episode II Attack of the Clones.
Unnamed: 11 -- How much the respondent liked Star Wars: Episode III Revenge of the Sith.
Unnamed: 12 -- How much the respondent liked Star Wars: Episode IV A New Hope.
Unnamed: 13 -- How much the respondent liked Star Wars: Episode V The Empire Strikes Back.
Unnamed: 14 -- How much the respondent liked Star Wars: Episode VI Return of the Jedi.
You don't need to do a ton of cleanup for these columns. You'll need to convert each column to a numeric type, then rename the columns so you can tell what they're for more easily.

You can do the numeric conversion with the astype() method on Dataframes. In this case, you can use code that looks like this:


star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)
star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)
The code above will convert each column from column 9 up to but not including column 15 to a float type.

Instructions
Convert each column above to a float type.
Instead of typing in each column name, you can select them all with star_wars.columns[9:15].
Rename each of the above columns to a more descriptive name. We suggest ranking_1, ranking_2, and so on.
You can use the rename method from the last screen.
"""
# 5: Cleaning Up Ranking Columns
star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)
star_wars[star_wars.columns[9:15]].columns.tolist()
real_name = {
    "Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.":"ranking_1",
    "Unnamed: 10":"ranking_2",
    "Unnamed: 11":"ranking_3",
    "Unnamed: 12":"ranking_4",
    "Unnamed: 13":"ranking_5",
    "Unnamed: 14":"ranking_6"}
star_wars = star_wars.rename(columns=real_name)
""" Console Outputs or Results
['Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.',
 'Unnamed: 10',
 'Unnamed: 11',
 'Unnamed: 12',
 'Unnamed: 13',
 'Unnamed: 14']
"""


"""
6: Finding The Highest Ranked Movie
Now that you've cleaned up the ranking columns, you can easily find the highest ranked movie.
You can do this by taking the mean of each of the ranking columns.
 The mean() method on Dataframes will enable you to do this.

Instructions
Use the mean method to compute the mean of each of the ranking columns from the last screen.
Make a bar chart of each ranking. You can use a matplotlib bar chart for this.
Make sure to run %matplotlib inline beforehand to show your plots in the notebook.
Create a markdown cell, and write a summary of what you've done up until now, and why you think the movies are ranked like they are.
Remember that a lower ranking is better!
"""
# 6: Finding The Highest Ranked Movie
mean_rank = star_wars[star_wars.columns[9:15]].mean()
mean_rank
%matplotlib inline
mean_rank.plot.bar()
""" Console Outputs or Results
ranking_1    3.732934
ranking_2    4.087321
ranking_3    4.341317
ranking_4    3.272727
ranking_5    2.513158
ranking_6    3.047847
dtype: float64

see plot14.png
"""



"""
7: Finding The Most Seen Movie
You cleaned up the seen columns earlier, and converted the values to the Boolean type.
When you call methods like sum() or mean(), Booleans are treated like integers -- Trueis treated like a 1, and False is treated like a 0.
This makes it easy to figure out how many people have seen each movie -- we just take the sum of the column.

Instructions
Use the sum method to compute the sum of each of the seen columns from a previous screen.
Make a bar chart of each ranking. You can use a matplotlib bar chart for this.
Create a markdown cell, and write about why you think the results look like they do, and how they correlate with the rankings.
"""
#7: Finding The Most Seen Movie
most_see = star_wars[star_wars.columns[3:9]].sum()
most_see
most_see.plot.bar()
""" Console Outputs or Results
See Stw Ep1    673
See Stw Ep2    571
See Stw Ep3    550
See Stw Ep4    607
See Stw Ep5    758
See Stw Ep6    738
dtype: int64

see plot15.png
"""




"""
8: Exploring The Data By Binary Segments
We've seen what the whole survey population thinks are the highest ranked movies, but we can break this down by segments.
There are several columns that segment our data into two groups, including:

Do you consider yourself to be a fan of the Star Wars film franchise? -- True or False.
Do you consider yourself to be a fan of the Star Trek franchise? -- Yes or No.
Gender -- Male or Female.
You can split a Dataframe into two groups based on a binary column by taking two subsets. Here, we'll split on the Gender column:


males = star_wars[star_wars["Gender"] == "Male"]
females = star_wars[star_wars["Gender"] == "Female"]
We can compute statistics like the most seen movie and the highest ranked movie separately for each group.

Instructions
Split the data into 2 groups based on one of the above columns.
Redo the 2 previous analyses (find the most seen movie and finding the highest ranked movie) separately for each group, and then compare results.
Write about any interesting patterns you see in a Markdown cell.
"""
# 8: Exploring The Data By Binary Segments
males = star_wars[star_wars["Gender"] == "Male"]
females = star_wars[star_wars["Gender"] == "Female"]

""" Console Outputs or Results

"""


"""
9: Next Steps
That's it for the guided steps! We highly recommend exploring the data more on your own.

Here are some potential next steps:

Try to segment the data by columns like Education, Location (Census Region), and Which character shot first?, which aren't binary. Are they any interesting patterns?
Clean up columns 15 to 29, which have to do with what characters are viewed favorably and unfavorably.
Which character is the most liked?
Which character is the most disliked?
Which character creates the most controversy? (split between dislikes and likes)
We highly recommend creating a Github repository and placing this project there.
It will help other people, including employers, see your work.
As you start to put multiple projects on Github, you'll have the beginnings of a strong portfolio.

You're welcome to keep working on the project here, but we highly recommend downloading it to your computer using the download icon above and working on it there.

We hope this guided project has been a good experience, and please email us at hello@dataquest.io if you want to share your work!
"""
