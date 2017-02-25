"""
02/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Data Analysis With Pandas Intermediate : Guided Project: Analyzing Thanksgiving Dinner
"""




"""
1: Introducing Thanksgiving Dinner Data
In this project, you'll be working with Jupyter notebook, and analyzing data on Thanksgiving dinner in the US.
By the end, you'll have a notebook that you can add to your portfolio or build on top of on your own.
If you need help at any point, you can consult our solution notebook here. The dataset came from FiveThirtyEight, and can be found here.
https://github.com/dataquestio/solutions/blob/master/Mission219Solution.ipynb
https://github.com/fivethirtyeight/data/tree/master/thanksgiving-2015
https://www.fivethirtyeight.com/

The dataset is stored in the thanksgiving.csv file. It contains 1058 responses to an online survey about what Americans eat for Thanksgiving dinner.
Each survey respondent was asked questions about what they typically eat for Thanksgiving, along with some demographic questions, like their gender, income, and location. T
his dataset will allow us to discover regional and income-based patterns in what Americans eat for Thanksgiving dinner.

The dataset has 65 columns, and 1058 rows. Most of the column names are questions, and most of the column values are string responses to the questions.
Most of the columns are categorical, as a survey respondent had to select one of a few options.
For example, one of the first column names is What is typically the main dish at your Thanksgiving dinner?. The potential responses are:

Turkey
Other (please specify)
Ham/Pork
Tofurkey
Chicken
Roast beef
I don't know
Turducken
Most of the columns follow the same question/response format as the above.
There are also quite a few NaN values in the columns, which occurred when a survey respondent didn't fill out a question because they didn't want to, or it didn't apply to them.

Here are the first few rows of the dataset:

RespondentID	Do you celebrate Thanksgiving?	What is typically the main dish at your Thanksgiving dinner?	What is typically the main dish at your Thanksgiving dinner? - Other (please specify)	How is the main dish typically cooked?	How is the main dish typically cooked? - Other (please specify)	What kind of stuffing/dressing do you typically have?
What kind of stuffing/dressing do you typically have? - Other (please specify)	What type of cranberry saucedo you typically have?	What type of cranberry saucedo you typically have? - Other (please specify)	...	Have you ever tried to meet up with hometown friends on Thanksgiving night?	Have you ever attended a "Friendsgiving?"	Will you shop any Black Friday sales on Thanksgiving Day?	Do you work in retail?	Will you employer make you work on Black Friday?	How would you describe where you live?	Age	What is your gender?	How much total combined money did all members of your HOUSEHOLD earn last year?	US Region
0	4337954960	Yes	Turkey	NaN	Baked	NaN	Bread-based	NaN	None	NaN	...	Yes	No	No	No	NaN	Suburban	18 - 29	Male	75,000 to 99,999	Middle Atlantic
1	4337951949	Yes	Turkey	NaN	Baked	NaN	Bread-based	NaN	Other (please specify)	Homemade cranberry gelatin ring	...	No	No	Yes	No	NaN	Rural	18 - 29	Female	50,000 to 74,999	East South Central
2	4337935621	Yes	Turkey	NaN	Roasted	NaN	Rice-based	NaN	Homemade	NaN	...	Yes	Yes	Yes	No	NaN	Suburban	18 - 29	Male	0 to 9,999	Mountain
3	4337933040	Yes	Turkey	NaN	Baked	NaN	Bread-based	NaN	Homemade	NaN	...	Yes	No	No	No	NaN	Urban	30 - 44	Male	$200,000 and up	Pacific
4	4337931983	Yes	Tofurkey	NaN	Baked	NaN	Bread-based	NaN	Canned	NaN	...	Yes	No	No	No	NaN	Urban	30 - 44	Male	100,000 to 124,999	Pacific
5 rows × 65 columns

We won't enumerate every single column now, but here are descriptions of some of the most important:

RespondentID -- a unique ID of the respondent to the survey.
Do you celebrate Thanksgiving? -- a Yes/No reponse to the question.
How would you describe where you live? -- responses are Suburban, Urban, and Rural.
Age -- resposes are one of several categories, such as 18-29, and 30-44.
How much total combined money did all members of your HOUSEHOLD earn last year? -- one of several categories, such as $75,000 to $99,999.
In this project, we'll explore the data, and try to find interesting patterns. Our first step is to read in and display the data.

Instructions
Import the pandas package.
Use the pandas.read_csv() function to read the thanksgiving.csv file in.
Make sure to specify the keyword argument encoding="Latin-1", as the CSV file isn't encoded normally.
Assign the result to the variable data.
Display the first few rows of data to see what the columns and rows look like.
In a separate notebook cell, display all of the column names to get a sense of what the data consists of.
You can use the pandas.DataFrame.columns property to display the column names.
"""
# 1: Introducing Thanksgiving Dinner Data
# Import and read data from csv file
import pandas as pd
data = pd.read_csv("thanksgiving.csv",encoding="Latin-1")
print(data.head(3))
 # Columns names from the Data Dataframes
# print(data.columns.tolist())
columns = data.columns.tolist()
for col in columns:
    print(col)
""" Console Output or Results
RespondentID Do you celebrate Thanksgiving?  \
0    4337954960                            Yes
1    4337951949                            Yes
2    4337935621                            Yes

  What is typically the main dish at your Thanksgiving dinner?  \
0                                             Turkey
1                                             Turkey
2                                             Turkey

  What is typically the main dish at your Thanksgiving dinner? - Other (please specify)  \
0                                                NaN
1                                                NaN
2                                                NaN

  How is the main dish typically cooked?  \
0                                  Baked
1                                  Baked
2                                Roasted

  How is the main dish typically cooked? - Other (please specify)  \
0                                                NaN
1                                                NaN
2                                                NaN

  What kind of stuffing/dressing do you typically have?  \
0                                        Bread-based
1                                        Bread-based
2                                         Rice-based

  What kind of stuffing/dressing do you typically have? - Other (please specify)  \
0                                                NaN
1                                                NaN
2                                                NaN

  What type of cranberry saucedo you typically have?  \
0                                               None
1                             Other (please specify)
2                                           Homemade

  What type of cranberry saucedo you typically have? - Other (please specify)  \
0                                                NaN
1                    Homemade cranberry gelatin ring
2                                                NaN

          ...          \
0         ...
1         ...
2         ...

  Have you ever tried to meet up with hometown friends on Thanksgiving night?  \
0                                                Yes
1                                                 No
2                                                Yes

  Have you ever attended a "Friendsgiving?"  \
0                                        No
1                                        No
2                                       Yes

  Will you shop any Black Friday sales on Thanksgiving Day?  \
0                                                 No
1                                                Yes
2                                                Yes

  Do you work in retail? Will you employer make you work on Black Friday?  \
0                     No                                              NaN
1                     No                                              NaN
2                     No                                              NaN

  How would you describe where you live?      Age What is your gender?  \
0                               Suburban  18 - 29                 Male
1                                  Rural  18 - 29               Female
2                               Suburban  18 - 29                 Male

  How much total combined money did all members of your HOUSEHOLD earn last year?  \
0                                 $75,000 to $99,999
1                                 $50,000 to $74,999
2                                       $0 to $9,999

            US Region
0     Middle Atlantic
1  East South Central
2            Mountain

[3 rows x 65 columns]

-----------------------
-----------------------
RespondentID
Do you celebrate Thanksgiving?
What is typically the main dish at your Thanksgiving dinner?
What is typically the main dish at your Thanksgiving dinner? - Other (please specify)
How is the main dish typically cooked?
How is the main dish typically cooked? - Other (please specify)
What kind of stuffing/dressing do you typically have?
What kind of stuffing/dressing do you typically have? - Other (please specify)
What type of cranberry saucedo you typically have?
What type of cranberry saucedo you typically have? - Other (please specify)
Do you typically have gravy?
Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Brussel sprouts
Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Carrots
Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Cauliflower
Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Corn
Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Cornbread
Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Fruit salad
Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Green beans/green bean casserole
Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Macaroni and cheese
Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Mashed potatoes
Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Rolls/biscuits
Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Squash
Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Vegetable salad
Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Yams/sweet potato casserole
Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify)
Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify).1
Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple
Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Buttermilk
Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Cherry
Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Chocolate
Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Coconut cream
Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Key lime
Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Peach
Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan
Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin
Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Sweet Potato
Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - None
Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify)
Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify).1
Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Apple cobbler
Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Blondies
Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Brownies
Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Carrot cake
Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Cheesecake
Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Cookies
Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Fudge
Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Ice cream
Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Peach cobbler
Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - None
Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Other (please specify)
Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Other (please specify).1
Do you typically pray before or after the Thanksgiving meal?
How far will you travel for Thanksgiving?
Will you watch any of the following programs on Thanksgiving? Please select all that apply. - Macy's Parade
What's the age cutoff at your "kids' table" at Thanksgiving?
Have you ever tried to meet up with hometown friends on Thanksgiving night?
Have you ever attended a "Friendsgiving?"
Will you shop any Black Friday sales on Thanksgiving Day?
Do you work in retail?
Will you employer make you work on Black Friday?
How would you describe where you live?
Age
What is your gender?
How much total combined money did all members of your HOUSEHOLD earn last year?
US Region
"""




"""
2: Filtering Out Rows From A DataFrame
Because we want to understand what people ate for Thanksgiving, we'll remove any responses from people who don't celebrate it.
The column Do you celebrate Thanksgiving? contains this information. We only want to keep data for people who answered Yes to this questions.

Instructions
Use the pandas.Series.value_counts() method to display counts of how many times each category occurs in the Do you celebrate Thanksgiving? column.
Filter out any rows in data where the response to Do you celebrate Thanksgiving? is not Yes.
At the end, all of the values in the Do you celebrate Thanksgiving? column of data should be Yes.
"""
# 2: Filtering Out Rows From A DataFrame
# Filter data where : Do you celebrate Thanksgiving? is not Yes
# 2.1 Extract pandas series from the dataframe data :
dyct = data["Do you celebrate Thanksgiving?"]
print(type(dyct))
print("----------------")
print(dyct[0:5])
print("----------------")
print(dyct.value_counts())
print("----------------")
# 2.2 Filter the dataframe data
dyct_yes = data["Do you celebrate Thanksgiving?"] == "Yes"
data = data[dyct_yes]
# verification :
print(data["Do you celebrate Thanksgiving?"].value_counts())
""" Console Output or Results
<class 'pandas.core.series.Series'>
----------------
0    Yes
1    Yes
2    Yes
3    Yes
4    Yes
Name: Do you celebrate Thanksgiving?, dtype: object
----------------
Yes    980
No      78
Name: Do you celebrate Thanksgiving?, dtype: int64
----------------
Yes    980
Name: Do you celebrate Thanksgiving?, dtype: int64
"""




"""
3: Using Value_counts To Explore Main Dishes
Let's explore what main dishes people tend to eat during Thanksgiving dinner.
We can again use the value_counts method to help us with this.

Instructions
Use the pandas.Series.value_counts() method to display counts of how many times each category occurs in the What is typically the main dish at your Thanksgiving dinner? column.
Display the Do you typically have gravy? column for any rows from data where the What is typically the main dish at your Thanksgiving dinner? column equals Tofurkey.
Create a filter that only selects rows from data where What is typically the main dish at your Thanksgiving dinner? equals Tofurkey.
Select the Do you typically have gravy? column, and display it.
"""
# 3: Using Value_counts To Explore Main Dishes
# 3.1: Display counts of each category
print(data["What is typically the main dish at your Thanksgiving dinner?"].value_counts())
# 3.2: Filter row on column : What is typically the main dish at your Thanksgiving dinner?
# equal to : "Tofurkey"
tofurkey = data["What is typically the main dish at your Thanksgiving dinner?"] == "Tofurkey"
print(data["Do you typically have gravy?"][tofurkey])
""" Console Output or Results
Turkey                    859
Other (please specify)     35
Ham/Pork                   29
Tofurkey                   20
Chicken                    12
Roast beef                 11
I don't know                5
Turducken                   3
Name: What is typically the main dish at your Thanksgiving dinner?, dtype: int64
4      Yes
33     Yes
69      No
72      No
77     Yes
145    Yes
175    Yes
218     No
243    Yes
275     No
393    Yes
399    Yes
571    Yes
594    Yes
628     No
774     No
820     No
837    Yes
860     No
953    Yes
Name: Do you typically have gravy?, dtype: object
"""




"""
4: Figuring Out What Pies People Eat
Now that we've looked into the main dishes, let's explore the dessert dishes. Specifically, we'll look at how many people eat Apple, Pecan, or Pumpkin pie during Thanksgiving dinner.
This data is encoded in the following three columns:

Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple
Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin
Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan
In all three columns, the value is either the name of the pie if the person eats it for Thanksgiving dinner, or null otherwise.

We can find out how many people eat one of these three pies for Thanksgiving dinner by figuring out for how many people all three columns are null.

You may recall from an earlier mission that the pandas.isnull() function will return a Boolean Series indicating whether or not each value in a specified DataFrame or Series is null.

We can also use the & operator to combine two Boolean Series into a single one.
If both Series contain True in a position, the result will be True. Otherwise, the result will be False. Here's an example:

see img2.png

If we use the pandas.isnull() function to check where all three columns are null, then use the & operator to join all of the Series, we'll end up with a single Boolean Series.
here that Series contains False, the person ate at least one of the types of pies for Thanksgiving dinner. Where it contains True, they ate none of the types of pies.

Instructions
Generate a Boolean Series indicating where the Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple column is null. Assign to the apple_isnull variable.
Generate a Boolean Series indicating where the Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin column is null. Assign to the pumpkin_isnull variable.
Generate a Boolean Series indicating where the Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan column is null. Assign to the pecan_isnull variable.
Join all three Series using the & operator, and assign the result to ate_pies.
Display the unique values and how many times each occurs in the ate_pies column.
"""
# 4: Figuring Out What Pies People Eat
# 4.1: Boolean series :
col1 = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"
apple_isnull = pd.isnull(data[col1])
print(apple_isnull[0:5])
print("--------------------")
col2 = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"
pumpkin_isnull = pd.isnull(data[col2])
print(pumpkin_isnull[0:5])
print("--------------------")
col3 = "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"
pecan_isnull = pd.isnull(data[col3])
print(pecan_isnull[0:5])
print("--------------------")
# 4.2 Join boolean series
ate_pies = apple_isnull & pumpkin_isnull & pecan_isnull
print(ate_pies[0:5])
print("--------------------")
print(ate_pies.value_counts())
""" Console Output or Results
0    False
1    False
2    False
3     True
4    False
Name: Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple, dtype: bool
--------------------
0     True
1    False
2    False
3    False
4    False
Name: Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin, dtype: bool
--------------------
0     True
1     True
2    False
3    False
4     True
Name: Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan, dtype: bool
--------------------
0    False
1    False
2    False
3    False
4    False
dtype: bool
--------------------
False    876
True     104
dtype: int64
"""





"""
5: Converting Age To Numeric
Let's analyze the Age column in more depth.
In order to analyze the Age column, we'll first need to convert it to numeric values.
This will make it simple to figure out things like the average age of survey respondents.
The Age column contains values that fall into one of a few categories:

18 - 29
30 - 44
45 - 59
60+
null
Because we're missing the exact age value, we won't be able to extract an exact integer value, and we'll instead have to extract the first age value in the strings given.

We can do this by splitting each value on the space character (), then taking the first item in the resulting list.
We'll also have to replace the + character to account for 60+, which follows a different format than the rest.

Instructions
Write a function to convert a single string to an appropriate integer value. This will allow us to convert the values in the Age column to integers.
Use the isnull() function to check if the value is null. If it is, return None.
Split the string on the space character (), and extract the first item of the resulting list.
Replace the + character in the result with an empty string to remove it.
Use int() to convert the result to an integer.
Return the result.
Use the pandas.Series.apply() method to apply the function to each value in the Age column of data.
Assign the result to the int_age column of data.
Call the pandas.Series.describe() method on the int_age column of data, and display the result.
In a separate markdown cell, write up your findings.
Is there anything that we should be aware of about the results or our methodology?
Is this a true depiction of the ages of survey participants?
"""
# 5: Converting Age To Numeric
print("--------------------")
print(data["Age"].value_counts())
print("--------------------")
print(data["Age"].unique().tolist())
print("--------------------")
print(data["Age"].describe())
print("--------------------")
# Function to convert single string to an appropriate integer value
import re
def colagetointeger(str):
    if pd.isnull(str):
        return None
    else:
        splitstr = str.split("-")
        if re.search("..+", splitstr[0]) is not None:
             splitstr[0] = splitstr[0].replace("+", "")
        return int(splitstr[0])

data["int_age"] = data["Age"].apply(colagetointeger)
print("--------------------")
print(data["int_age"].value_counts(dropna=False))
print("--------------------")
print(data["int_age"].describe())
print("--------------------")
print(data["int_age"].unique().tolist())
""" Console Output or Results
--------------------
45 - 59    269
60+        258
30 - 44    235
18 - 29    185
Name: Age, dtype: int64
--------------------
['18 - 29', '30 - 44', '60+', '45 - 59', nan]
--------------------
count         947
unique          4
top       45 - 59
freq          269
Name: Age, dtype: object
--------------------
--------------------
 45.0    269
 60.0    258
 30.0    235
 18.0    185
NaN       33
Name: int_age, dtype: int64
--------------------
count    947.000000
mean      40.089757
std       15.352014
min       18.000000
25%       30.000000
50%       45.000000
75%       60.000000
max       60.000000
Name: int_age, dtype: float64
--------------------
[18.0, 30.0, 60.0, 45.0, nan]
"""




"""
6: Converting Income To Numeric
The How much total combined money did all members of your HOUSEHOLD earn last year? column is very similar to the Age column.
It contains categories, but can be converted to numerical values. Here are the unique values in the column:

Prefer not to answer
$0 to $9,999
$10,000 to $24,999
$25,000 to $49,999
$50,000 to $74,999
$75,000 to $99,999
$100,000 to $124,999
$125,000 to $149,999
$150,000 to $174,999
$175,000 to $199,999
$200,000 and up
null
We can convert these values to numeric by again splitting on the space character ().
We'll then have to account for the string Prefer.
Finally, we'll be able to replace the dollar sign character $ and the comma ,, and return the result.

Instructions
Write a function to convert a single string to an appropriate integer income value.
Use the isnull() function to check if the value is null. If it is, return None.
Split the string on the space character (), and extract the first item of the resulting list.
If the result equals Prefer, return None.
Replace the $ and , characters in the result with empty strings to remove them.
Use int() to convert the result to an integer.
Return the result.
Use the pandas.Series.apply() method to apply the function to each value in the How much total combined money did all members of your HOUSEHOLD earn last year? column of data.
Assign the result to the int_income column of data.
Call the pandas.Series.describe() method on the int_income column of data, and display the result.
In a separate markdown cell, write up your findings.
Is there anything that we should be aware of about the results or our methodology?
Is this a true depiction of the incomes of survey participants?
"""
# 6: Converting Income To Numeric
print(data["How much total combined money did all members of your HOUSEHOLD earn last year?"].value_counts(dropna=False))
print("----------------")

def colincometointeger(income):
    if pd.isnull(income):
        return None
    else:
        splitincome = income.split()[0]
        if splitincome == "Prefer":
            return None
        else:
            splitincome = int(splitincome.replace("$", "").replace(",", ""))
            return splitincome

col = "How much total combined money did all members of your HOUSEHOLD earn last year?"
new_col = "int_income"
data[new_col] = data[col].apply(colincometointeger)
print("--------------------")
print(data[new_col].value_counts(dropna=False))
print("--------------------")
print(data[new_col].describe())
print("--------------------")
print(data[new_col].unique().tolist())
""" Console Output or Results
$25,000 to $49,999      166
$75,000 to $99,999      127
$50,000 to $74,999      127
Prefer not to answer    118
$100,000 to $124,999    109
$200,000 and up          76
$10,000 to $24,999       60
$0 to $9,999             52
$125,000 to $149,999     48
$150,000 to $174,999     38
NaN                      33
$175,000 to $199,999     26
Name: How much total combined money did all members of your HOUSEHOLD earn last year?, dtype: int64
----------------
--------------------
 25000.0     166
NaN          151
 75000.0     127
 50000.0     127
 100000.0    109
 200000.0     76
 10000.0      60
 0.0          52
 125000.0     48
 150000.0     38
 175000.0     26
Name: int_income, dtype: int64
--------------------
count       829.000000
mean      75965.018094
std       59068.636748
min           0.000000
25%       25000.000000
50%       75000.000000
75%      100000.000000
max      200000.000000
Name: int_income, dtype: float64
--------------------
[75000.0, 50000.0, 0.0, 200000.0, 100000.0, 25000.0, nan, 10000.0, 175000.0, 150000.0, 125000.0]
"""




"""
7: Correlating Travel Distance And Income
We can now see how the distance someone travels for Thanksgiving dinner relates to their income level.
It's safe to hypothesize that people earning less money could be younger, and would travel to their parent's houses for Thanksgiving.
People earning more are more likely to have Thanksgiving at their house as a result.

We can test this by filtering data based on int_income, and seeing what the values in the How far will you travel for Thanksgiving?
column are.

Instructions
See how far people earning under 150000 will travel.
Filter data, and only select rows where int_income is less than 150000.
Use indexing to select the How far will you travel for Thanksgiving? column.
Use the value_counts() method to count up how many times each value occurs in the column.
Display the results.
See how far people earning over 150000 will travel.
Filter data, and only select rows where int_income is greater than 150000.
Use indexing to select the How far will you travel for Thanksgiving? column.
Use the value_counts() method to count up how many times each value occurs in the column.
Display the results
Write up your findings in a markdown cell.
"""
# 7: Correlating Travel Distance And Income
filter1 = data["int_income"] < 150000
rowfiltering = data["How far will you travel for Thanksgiving?"][filter1]
print(rowfiltering.value_counts())
print("---------------------")
filter2 = data["int_income"] >= 150000
rowfiltering2 = data["How far will you travel for Thanksgiving?"][filter2]
print(rowfiltering2.value_counts())
""" Console Output or Results
Thanksgiving is happening at my home--I won't travel at all                         281
Thanksgiving is local--it will take place in the town I live in                     203
Thanksgiving is out of town but not too far--it's a drive of a few hours or less    150
Thanksgiving is out of town and far away--I have to drive several hours or fly       55
Name: How far will you travel for Thanksgiving?, dtype: int64
---------------------
Thanksgiving is happening at my home--I won't travel at all                         66
Thanksgiving is local--it will take place in the town I live in                     34
Thanksgiving is out of town but not too far--it's a drive of a few hours or less    25
Thanksgiving is out of town and far away--I have to drive several hours or fly      15
Name: How far will you travel for Thanksgiving?, dtype: int64
"""




"""
8: Linking Friendship And Age
There are two columns which directly pertain to friendship, Have you ever tried to meet up with hometown friends on Thanksgiving night?, and Have you ever attended a "Friendsgiving?.
In the US, a "Friendsgiving" is when instead of traveling home for the holiday, you celebrate it with friends who live in your area.
Both questions seem skewed towards younger people. Let's see if this hypothesis holds up.

In order to see the average ages of people who have done both, we can use a pivot table.
As you may recall from an earlier mission, we can generate a pivot table with the pandas.DataFrame.pivot_table() method.
By calling this method on data, and passing in the right keyword arguments, we can generate a table showing the average ages of people who answered Yes to both questions, answered Yes to one question, and so on.

Instructions
Generate a pivot table showing the average age of respondents for each category of Have you ever tried to meet up with hometown friends on Thanksgiving night? and Have you ever attended a "Friendsgiving?.
Call the pivot_table() method on data.
Pass in "Have you ever tried to meet up with hometown friends on Thanksgiving night?" to the index keyword argument.
Pass in 'Have you ever attended a "Friendsgiving?"' to the columns keyword argument.
Pass in "int_age" to the values keyword argument.
Display the results.
Generate a pivot table showing the average income of respondents for each category of Have you ever tried to meet up with hometown friends on Thanksgiving night? and Have you ever attended a "Friendsgiving?.
Write up a markdown cell with your findings.
"""
# 8: Linking Friendship And Age
import numpy as np
# Average age
# by Have you ever tried to meet up with hometown friends on Thanksgiving night? and Have you ever attended a "Friendsgiving?
print(data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?",
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_age",
    aggfunc=np.mean
))
print("-----------------")
# average income
# by Have you ever tried to meet up with hometown friends on Thanksgiving night? and Have you ever attended a "Friendsgiving?
print(data.pivot_table(
    index="Have you ever tried to meet up with hometown friends on Thanksgiving night?",
    columns='Have you ever attended a "Friendsgiving?"',
    values="int_income",
    aggfunc=np.mean
))
""" Console Output or Results
Have you ever attended a "Friendsgiving?"                  No        Yes
Have you ever tried to meet up with hometown fr...
No                                                  42.283702  37.010526
Yes                                                 41.475410  33.976744
-----------------
Have you ever attended a "Friendsgiving?"                     No           Yes
Have you ever tried to meet up with hometown fr...
No                                                  78914.549654  72894.736842
Yes                                                 78750.000000  66019.736842
"""





"""
9: Next Steps
That's it for the guided steps! We recommend exploring the data more on your own.

Here are some potential next steps:

Figure out the most common dessert people eat.
Figure out the most common complete meal people eat.
Identify how many people work on Thanksgiving.
Find regional patterns in the dinner menus.
Find age, gender, and income based patterns in dinner menus.
We recommend creating a Github repository and placing this project there.
It will help other people, including employers, see your work.
As you start to put multiple projects on Github, you'll have the beginnings of a strong portfolio. 
You're welcome to keep working on the project here, but we recommend downloading it to your computer using the download icon above and working on it there.
"""
