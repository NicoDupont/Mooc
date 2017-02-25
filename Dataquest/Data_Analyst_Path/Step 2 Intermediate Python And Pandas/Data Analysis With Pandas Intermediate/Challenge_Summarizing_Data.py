"""
02/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Data Analysis With Pandas Intermediate : Challenge: Summarizing Data
"""


"""
1: How Challenges Work
At Dataquest, we're huge believers in learning through doing, and we hope this shows in your learning experience.
While missions focus on introducing concepts, challenges allow you to perform deliberate practice by completing structured problems.
You can read more about deliberate practice here and here.
Challenges will feel similar to missions, but with little instructional material and a greater focus on exercises.

If you have questions or run into issues, head over to the Dataquest forums or our Slack community.
"""


"""
2: Introduction To The Data
The American Community Survey is a U.S. Census Bureau survey that collects data on everything from housing affordability to industry employment rates.
For this challenge, you'll be using the data that the team at FiveThirtyEight derived from the 2010-2012 American Community Surveys.
FiveThirtyEight cleaned the data set and made it available in a Github repository.

Here's a quick overview of the files we'll be working with:

all-ages.csv - Employment data by major for all ages
recent-grads.csv - Employment data by major for recent college graduates only
Here are descriptions for a few of the columns (out of 21 total columns):

Rank - The major's numerical rank, by post-graduation median earnings
Major_code - The major's numerical code
Major - The major's description
Major_category - The major's category
Total - The total number of people who studied the major
Men - The number of men who studied the major
Women - The number of women who studied the major
ShareWomen - The share of women (from 0 to 1) who studied the major
Employed - The number of people who studied the major and obtained a job after graduating
Here are the first few rows and columns in recent-grads.csv.
The data set all-ages.csv has the same structure, but with different values for some of the columns:

Rank	Major_code	Major	Major_category	Total	Sample_size	Men	Women	ShareWomen	Employed
1	2419	PETROLEUM ENGINEERING	Engineering	2339	36	2057	282	0.120564	1976
2	2416	MINING AND MINERAL ENGINEERING	Engineering	756	7	679	77	0.101852	640
3	2415	METALLURGICAL ENGINEERING	Engineering	856	3	725	131	0.153037	648
4	2417	NAVAL ARCHITECTURE AND MARINE ENGINEERING	Engineering	1258	16	1123	135	0.107313	758
5	2405	CHEMICAL ENGINEERING	Engineering	32260	289	21239	11021	0.341631	25694
By completing this challenge, you'll test your comfort level with using pandas to manipulate DataFrames and calculate summary statistics.
First, we'll need to read the data set into pandas.

Instructions
Read all-ages.csv into a DataFrame object, and assign it to all_ages.
Read recent-grads.csv into a DataFrame object, and assign it to recent_grads.
Display the first five rows of all_ages and recent_grads.
"""
import pandas as pd
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")

def pd_head(df,row=5):
    print(df.head(row))
    print("-----------")

pd_head(all_ages)
pd_head(recent_grads)
""" Console Output or Results
Output
   Major_code                                  Major  \
0        1100                    GENERAL AGRICULTURE
1        1101  AGRICULTURE PRODUCTION AND MANAGEMENT
2        1102                 AGRICULTURAL ECONOMICS
3        1103                        ANIMAL SCIENCES
4        1104                           FOOD SCIENCE

                    Major_category   Total  Employed  \
0  Agriculture & Natural Resources  128148     90245
1  Agriculture & Natural Resources   95326     76865
2  Agriculture & Natural Resources   33955     26321
3  Agriculture & Natural Resources  103549     81177
4  Agriculture & Natural Resources   24280     17281

   Employed_full_time_year_round  Unemployed  Unemployment_rate  Median  \
0                          74078        2423           0.026147   50000
1                          64240        2266           0.028636   54000
2                          22810         821           0.030248   63000
3                          64937        3619           0.042679   46000
4                          12722         894           0.049188   62000

   P25th    P75th
0  34000  80000.0
1  36000  80000.0
2  40000  98000.0
3  30000  72000.0
4  38500  90000.0
-----------
   Rank  Major_code                                      Major Major_category  \
0     1        2419                      PETROLEUM ENGINEERING    Engineering
1     2        2416             MINING AND MINERAL ENGINEERING    Engineering
2     3        2415                  METALLURGICAL ENGINEERING    Engineering
3     4        2417  NAVAL ARCHITECTURE AND MARINE ENGINEERING    Engineering
4     5        2405                       CHEMICAL ENGINEERING    Engineering

   Total  Sample_size    Men  Women  ShareWomen  Employed      ...        \
0   2339           36   2057    282    0.120564      1976      ...
1    756            7    679     77    0.101852       640      ...
2    856            3    725    131    0.153037       648      ...
3   1258           16   1123    135    0.107313       758      ...
4  32260          289  21239  11021    0.341631     25694      ...

   Part_time  Full_time_year_round  Unemployed  Unemployment_rate  Median  \
0        270                  1207          37           0.018381  110000
1        170                   388          85           0.117241   75000
2        133                   340          16           0.024096   73000
3        150                   692          40           0.050125   70000
4       5180                 16697        1672           0.061098   65000

   P25th   P75th  College_jobs  Non_college_jobs  Low_wage_jobs
0  95000  125000          1534               364            193
1  55000   90000           350               257             50
2  50000  105000           456               176              0
3  43000   80000           529               102              0
4  50000   75000         18314              4440            972

[5 rows x 21 columns]
-----------
"""



"""
3: Summarizing Major Categories
Both of these data sets group the various majors into categories in the Major_category column.
Let's start by understanding the number of people in each Major_category for both data sets.

To do so, you'll need to:

Return the unique values in Major_category.
Use the Series.unique() method to return the unique values in a column, like this: recent_grads['Major_category'].unique()
For each unique value:
Return all of the rows where Major_category equals that unique value.
Calculate the total number of students those rows represent (using the Total column).
Use the Series.sum() to calculate the sum of the values in a column. recent_grads['Total'].sum() returns the sum of the values in the Total column.
Keep track of the totals by adding the Major_category value and the total number of students to a dictionary.
Instructions
Use the Total column to calculate the number of people who fall under each Major_category in each data set.
Store the result as a separate dictionary for each data set.
The key for the dictionary should be the Major_category, and the value should be the total count.
For the counts from all_ages, store the results as a dictionary named aa_cat_counts.
For the counts from recent_grads, store the results as a dictionary named rg_cat_counts.
Recall that we format a dictionary like this:
{
    "Engineering": 500,
    "Business": 500
    ...
}
"""
# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()

for major in all_ages['Major_category'].unique():
    aa_cat_counts[major] = all_ages['Total'][all_ages['Major_category'] == major].sum()
print(aa_cat_counts)
print("-----------------------")

for major in recent_grads['Major_category'].unique():
    rg_cat_counts[major] = recent_grads['Total'][recent_grads['Major_category'] == major].sum()
print(rg_cat_counts)
print("-----------------------")
""" Console Output or Results
Output
['Agriculture & Natural Resources' 'Biology & Life Science' 'Engineering'
 'Humanities & Liberal Arts' 'Communications & Journalism'
 'Computers & Mathematics' 'Industrial Arts & Consumer Services'
 'Education' 'Law & Public Policy' 'Interdisciplinary' 'Health'
 'Social Science' 'Physical Sciences' 'Psychology & Social Work' 'Arts'
 'Business']
{'Interdisciplinary': 45199,
'Biology & Life Science': 1338186,
'Social Science': 2654125, 'Law & Public Policy': 902926, 'Humanities & Liberal Arts': 3738335, 'Engineering': 3576013, 'Physical Sciences': 1025318, 'Industrial Arts & Consumer Services': 1033798, 'Education': 4700118, 'Psychology & Social Work': 1987278, 'Computers & Mathematics': 1781378, 'Health': 2950859, 'Arts': 1805865, 'Communications & Journalism': 1803822, 'Business': 9858741, 'Agriculture & Natural Resources': 632437}
-----------------------
{'Interdisciplinary': 12296,
'Biology & Life Science': 453862,
'Social Science': 529966, 'Law & Public Policy': 179107, 'Humanities & Liberal Arts': 713468, 'Engineering': 537583, 'Physical Sciences': 185479, 'Industrial Arts & Consumer Services': 229792, 'Education': 559129, 'Communications & Journalism': 392601, 'Computers & Mathematics': 299008, 'Agriculture & Natural Resources': 79981, 'Arts': 357130, 'Psychology & Social Work': 481007, 'Business': 1302376, 'Health': 463230}
-----------------------
"""



"""
4: Low-Wage Job Rates
The press likes to talk about the number of college graduates working low-pay, unskilled jobs because they can't find better ones.
As a data person, you should be skeptical of any broad claims, and analyze relevant data to obtain a more nuanced view.

Let's run some basic calculations to explore that idea further.

Instructions
Use the Low_wage_jobs and Total columns to calculate the proportion of recent college graduates that worked low wage jobs.
Recall that you can use the Series.sum() method to return the sum of the values in a column.
Store the resulting float as low_wage_percent, and display the value with the print()
"""
low_wage_percent = 0.0
print(recent_grads.head(3))
low_wage_percent = (recent_grads["Low_wage_jobs"].sum() / recent_grads["Total"].sum())
print("--------------")
print(low_wage_percent)
""" Console Output or Results
Output
   Rank  Major_code                           Major Major_category  Total  \
0     1        2419           PETROLEUM ENGINEERING    Engineering   2339
1     2        2416  MINING AND MINERAL ENGINEERING    Engineering    756
2     3        2415       METALLURGICAL ENGINEERING    Engineering    856

   Sample_size   Men  Women  ShareWomen  Employed      ...        Part_time  \
0           36  2057    282    0.120564      1976      ...              270
1            7   679     77    0.101852       640      ...              170
2            3   725    131    0.153037       648      ...              133

   Full_time_year_round  Unemployed  Unemployment_rate  Median  P25th   P75th  \
0                  1207          37           0.018381  110000  95000  125000
1                   388          85           0.117241   75000  55000   90000
2                   340          16           0.024096   73000  50000  105000

   College_jobs  Non_college_jobs  Low_wage_jobs
0          1534               364            193
1           350               257             50
2           456               176              0

[3 rows x 21 columns]
--------------
0.0985254607612
"""



"""
5: Comparing Data Sets
It looks like only about 9.85% of graduates took on a low wage job after finishing college.

Both the all_ages and recent_grads data sets have 173 rows, corresponding to the 173 college major codes.
This enables us to do some comparisons between the two data sets, and perform some initial calculations to see how the statistics for recent college graduates compare with those for the entire population.

Next, let's calculate the number of majors where recent graduates did better than the overall population.

Instructions
Use a for loop to iterate over majors.
For each major, use Boolean filtering to find the corresponding row in both DataFrames.
Compare the values for Unemployment_rate to see which DataFrame has a lower value.
Increment rg_lower_count if the value for Unemployment_rate is lower for recent_grads than it is for all_ages.
Display rg_lower_count with the print() function.
"""
# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
print(majors.shape)
print("----------------")
rg_lower_count = 0
for m in majors:
    recent_grads_row = recent_grads[recent_grads['Major'] == m]
    all_ages_row = all_ages[all_ages['Major'] == m]

    rg_unemp_rate = recent_grads_row.iloc[0]['Unemployment_rate']
    aa_unemp_rate = all_ages_row.iloc[0]['Unemployment_rate']

    if rg_unemp_rate < aa_unemp_rate:
        rg_lower_count += 1

print(rg_lower_count)
""" Console Output or Results
Output
(173,)
43
"""



"""
6: Next Steps
It appears that less recent graduates who studied 43 of the 173 majors ended up having lower unemployment rates than the general population.

In the next few missions, we'll dive further into the two key data structures in pandas: Series and DataFrame objects.
"""
