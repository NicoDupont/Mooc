"""
02/2017
Dataquest : Data Analyst Path
Step 1: Introduction To Python
SubStep : Python Programming Intermediate : Guided Project: Exploring Gun Deaths in the US
see notebook : Guided_Project_Exploring_Gun_Deaths_in_the_US.ipynb
"""


"""
1: Introducing US Gun Deaths Data
In this project, you'll be working with Jupyter notebook, and analyzing data on gun deaths in the US.
By the end, you'll have a notebook that you can add to your portfolio or build on top of on your own.
If you need help at any point, you can consult our solution notebook here.

The dataset came from FiveThirtyEight, and can be found here. The dataset is stored in the guns.csv file.
It contains information on gun deaths in the US from 2012 to 2014. Each row in the dataset represents a single fatality.
The columns contain demographic and other information about the victim. Here are the first few rows of the dataset:

year	month	intent	police	sex	age	race	hispanic	place	education
0	1	2012	1	Suicide	0	M	34.0	Asian/Pacific Islander	100	Home	4.0
1	2	2012	1	Suicide	0	F	21.0	White	100	Street	3.0
2	3	2012	1	Suicide	0	M	60.0	White	100	Other specified	4.0
3	4	2012	2	Suicide	0	M	64.0	White	100	Home	4.0
4	5	2012	2	Suicide	0	M	31.0	White	100	Other specified	2.0
As you can see above, the first row of the data is a header row, which tells you what kind of data is in each column of the CSV file.
Each row contains information about the fatality, and the victim. Here's an explanation of each column:

-- this is an identifier column, which contains the row number.
It's common in CSV files to include a unique identifier for each row, but we can ignore it in this analysis.
year -- the year in which the fatality occurred.
month -- the month in which the fatality occurred.
intent -- the intent of the perpetrator of the crime. This can be Suicide, Accidental, NA, Homicide, or Undetermined.
police -- whether a police officer was involved with the shooting. Either 0 (false) or 1 (true).
sex -- the gender of the victim. Either M or F.
age -- the age of the victim.
race -- the race of the victim. Either Asian/Pacific Islander, Native American/Native Alaskan, Black, Hispanic, or White.
hispanic -- a code indicating the Hispanic origin of the victim.
place -- where the shooting occurred. Has several categories, which you're encouraged to explore on your own.
education -- educational status of the victim. Can be one of the following:
1 -- Less than High School
2 -- Graduated from High School or equivalent
3 -- Some College
4 -- At least graduated from College
5 -- Not available
In this project, we'll explore the dataset, and try to find patterns in the demographics of the victims. Our first step is to read the data in and take a look at it.

Instructions
Read the dataset in as a list using the csv module.
Import the csv module.
Open the file using the open() function.
Use the csv.reader() function to load the opened file.
Call list() on the result to get a list of all the data in the file.
Assign the result to the variable data.
Display the first 5 rows of data to verify everything.
"""
# 1.Introducing US Gun Deaths Data
import csv
data = list(csv.reader(open("guns.csv")))
print(data[0:5])
""" Console Output or Results
[['', 'year', 'month', 'intent', 'police', 'sex', 'age', 'race', 'hispanic', 'place', 'education'], ['1', '2012', '01', 'Suicide', '0', 'M', '34', 'Asian/Pacific Islander', '100', 'Home', '4'], ['2', '2012', '01', 'Suicide', '0', 'F', '21', 'White', '100', 'Street', '3'], ['3', '2012', '01', 'Suicide', '0', 'M', '60', 'White', '100', 'Other specified', '4'], ['4', '2012', '02', 'Suicide', '0', 'M', '64', 'White', '100', 'Home', '4']]
"""




"""
2: Removing Headers From A List Of Lists
In the last screen, we read our data into the list of lists data.
Each inner list in data represents a single row.
Each item in the inner lists represents a single column for that row.
Here's how the first 5 rows should have looked:


[
    ['', 'year', 'month', 'intent', 'police', 'sex', 'age', 'race', 'hispanic', 'place', 'education'],
    ['1', '2012', '01', 'Suicide', '0', 'M', '34', 'Asian/Pacific Islander', '100', 'Home', '4'],
    ['2', '2012', '01', 'Suicide', '0', 'F', '21', 'White', '100', 'Street', '3'],
    ['3', '2012', '01', 'Suicide', '0', 'M', '60', 'White', '100', 'Other specified', '4'],
    ['4', '2012', '02', 'Suicide', '0', 'M', '64', 'White', '100', 'Home', '4']
]
You hopefully noticed that the first item in the data list is a header row.
In order to analyze the data properly, we'll have to remove the header row, which contains the names of each column.
We can remove this using list slicing. You can read more about lists here.

Instructions
Extract the first row of data, and assign it to the variable headers.
Remove the first row from data.
Display headers.
Display the first 5 rows of data to verify that you removed the header row properly.
"""
# 2. Removing Headers From A List Of Lists
headers = data[0]
data = data[1:len(data)]
print(headers)
print("----------")
print(data[0:5])
""" Console Output or Results
['', 'year', 'month', 'intent', 'police', 'sex', 'age', 'race', 'hispanic', 'place', 'education']
----------
[['1', '2012', '01', 'Suicide', '0', 'M', '34', 'Asian/Pacific Islander', '100', 'Home', '4'], ['2', '2012', '01', 'Suicide', '0', 'F', '21', 'White', '100', 'Street', '3'], ['3', '2012', '01', 'Suicide', '0', 'M', '60', 'White', '100', 'Other specified', '4'], ['4', '2012', '02', 'Suicide', '0', 'M', '64', 'White', '100', 'Home', '4'], ['5', '2012', '02', 'Suicide', '0', 'M', '31', 'White', '100', 'Other specified', '2']]
"""




"""
3: Counting Gun Deaths By Year
The year column contains information on the year in which gun deaths occurred.
We can use this column to calculate how many gun deaths happened in each year.

We can perform this operation by creating a dictionary, then keeping count in the dictionary of how many times each element occurs in the year column.

Instructions
Use a list comprehension to extract the year column from data.
Because the year column is the second column in the data, you'll need to get the element at index 1 in each row.
Assign the result to the variable years.
Create an empty dictionary called year_counts.
Loop through each element in years.
If the element isn't a key in year_counts, create it, and set the value to 1.
If the element is a key in year_counts, increment the value by one.
Display year_counts to see how many gun deaths occur in each year.
"""
# 3.Counting Gun Deaths By Year
years = [ row[1] for row in data ]
year_counts = {}
for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1
print(years[0:5])
print("------------")
print(year_counts)
""" Console Output or Results
['2012', '2012', '2012', '2012', '2012']
------------
{'2014': 33598, '2013': 33635, '2012': 33562}
"""




"""
4: Exploring Gun Deaths By Month And Year
It looks like gun deaths didn't change much by year from 2012 to 2014. Let's see if gun deaths in the US change by month and year.
In order to do this, we'll have to create a datetime.datetime object using the year and month columns. We'll then be about to count up gun deaths by date, like we did by year in the last screen.

As you may recall from an earlier mission, you can create a datetime object by specifying the year, month, and day keyword arguments:


date = datetime(year=2016, month=12, day=1)
We can use the month and year column of data to create a datetime.
We'll specify a fixed day because we're missing that column in our data.

If we create a datetime.datetime object for each row, we can then count up how many gun deaths occurred in each month and year using a similar procedure to what we did in the last screen.

Instructions
Use a list comprehension to create a datetime.datetime object for each row. Assign the result to dates.
The year column in the second element in each row.
The month column is the third element in each row.
Make sure to convert year and month to integers using int().
Pass year, month, and day=1 into the datetime.datetime() function.
Display the first 5 rows in dates to verify everything worked.
Count up how many times each unique date occurs in dates. Assign the result to date_counts.
This follows a similar procedure to what we did in the last screen with year_counts.
Display date_counts.
"""
# 4.Exploring Gun Deaths By Month And Year
from datetime import datetime
date = [ datetime(year=int(row[1]), month=int(row[2]), day=1).strftime("%B, %Y") for row in data ]
print(date[0:5])
print("------------")
date_counts = {}
for dat in date:
    if dat in date_counts:
        date_counts[dat] += 1
    else:
        date_counts[dat] = 1
print(date_counts)
""" Console Output or Results
['January, 2012', 'January, 2012', 'January, 2012', 'February, 2012', 'February, 2012']
------------
{'March, 2013': 2861, 'March, 2014': 2683, 'September, 2014': 2913, 'April, 2014': 2861, 'July, 2013': 3078, 'November, 2014': 2755, 'June, 2012': 2825, 'August, 2014': 2969, 'August, 2012': 2953, 'October, 2014': 2864, 'May, 2014': 2863, 'December, 2013': 2764, 'May, 2012': 2998, 'February, 2012': 2356, 'April, 2013': 2797, 'December, 2012': 2790, 'October, 2012': 2732, 'June, 2013': 2919, 'September, 2013': 2741, 'January, 2013': 2863, 'November, 2012': 2728, 'February, 2013': 2374, 'July, 2014': 2883, 'September, 2012': 2851, 'January, 2012': 2757, 'December, 2014': 2856, 'October, 2013': 2807, 'February, 2014': 2360, 'April, 2012': 2794, 'November, 2013': 2757, 'June, 2014': 2930, 'May, 2013': 2805, 'January, 2014': 2650, 'August, 2013': 2858, 'March, 2012': 2742, 'July, 2012': 3025}
"""




"""
5: Exploring Gun Deaths By Race And Sex
The sex and race columns contain potentially interesting information on how gun deaths in the US vary by gender and race.
Exploring both of these columns can be done with a similar dictionary counting technique to what we did earlier.

Instructions
Count up how many times each item in the sex column occurs.
Assign the result to sex_counts.
Count up how many times each item in the race column occurs.
Assign the result to race_counts.
Display race_counts and sex_counts to verify your work, and see if you can spot any patterns.
Write a markdown cell detailing what you've learned so far, and what you think might need further examination.
"""
# 5.Exploring Gun Deaths By Race And Sex
print("------------")
sex_counts = {}
for sex in data:
    if sex[5] in sex_counts:
        sex_counts[sex[5]] += 1
    else:
        sex_counts[sex[5]] = 1
print(sex_counts)
print("------------")
race_counts = {}
for race in data:
    if race[7] in race_counts:
        race_counts[race[7]] += 1
    else:
        race_counts[race[7]] = 1
print(race_counts)
""" Console Output or Results
------------
{'F': 14448, 'M': 86348}
------------
{'Asian/Pacific Islander': 1325, 'Black': 23295, 'White': 66236, 'Native American/Native Alaskan': 916, 'Hispanic': 9021}
"""




"""
6: Reading In A Second Dataset
We explored gun deaths by race in the past screen. However, our analysis only gives us the total number of gun deaths by race in the US.
Unless we know the proportion of each race in the US, we won't be able to meaningfully compare those numbers.
What we really want to get is a rate of gun deaths per 100000 people of each race.
In order to do this, we'll need to read in data about what percentage of the US population falls into each racial category.
Luckily, we can import some census data to help us out.

The data contains information on the total population of the US, as well as the total population of each racial group in the US.
The data is stored in the census.csv file, and only consists of two rows:

Id	Year	Id.1	Sex	Id.2	Hispanic Origin	Id.3	Id2	Geography	Total	Race Alone - White	Race Alone - Hispanic	Race Alone - Black or African American	Race Alone - American Indian and Alaska Native	Race Alone - Asian	Race Alone - Native Hawaiian and Other Pacific Islander	Two or More Races
0	cen42010	April 1, 2010 Census	totsex	Both Sexes	tothisp	Total	0100000US	NaN	United States	308745538	197318956	44618105	40250635	3739506	15159516	674625	6984195
As you can see, the first row is a header row, and the second row consists of population counts. We'll need to read this file in using the csv.reader() function.

Instructions
Read in census.csv, and convert to a list of lists. Assign the result to the census variable.
Display census to verify your work.
"""
# 6.Reading In A Second Dataset
census = list(csv.reader(open("census.csv")))
print(census[0:5])
""" Console Output or Results
[['Id', 'Year', 'Id', 'Sex', 'Id', 'Hispanic Origin', 'Id', 'Id2', 'Geography', 'Total', 'Race Alone - White', 'Race Alone - Hispanic', 'Race Alone - Black or African American', 'Race Alone - American Indian and Alaska Native', 'Race Alone - Asian', 'Race Alone - Native Hawaiian and Other Pacific Islander', 'Two or More Races'], ['cen42010', 'April 1, 2010 Census', 'totsex', 'Both Sexes', 'tothisp', 'Total', '0100000US', '', 'United States', '308745538', '197318956', '44618105', '40250635', '3739506', '15159516', '674625', '6984195']]
"""




"""
7: Computing Rates Of Gun Deaths Per Race
Earlier, we computed the number of gun deaths per race, and created a dictionary, race_counts, that looked like this:


{
     'Asian/Pacific Islander': 1326,
     'Black': 23296,
     'Hispanic': 9022,
     'Native American/Native Alaskan': 917,
     'White': 66237
}
In order to get from the raw counts of gun deaths by race to a rate of gun deaths per 100000 people in each race, we'll need to divide the total number of gun deaths by the population of each race. From the census dataset, we know that the number of people in the White racial category is 197318956. We'd divide 66237 by 197318956:


white_gun_death_rate = 66237 / 197318956
This gives us the percentage chance that a given person in the White census race category would have been killed by a gun in the US from 2012 to 2014. If you do this computation, you'll see that the rate is a very small number, 0.0003356849303419181. It's for this reason that it's typical to express crime statistics as the "rate per 100000". This tells you the number of people in a given group out of every 100000 that were killed by guns in the US. To get this, we just multiply by 100000:


rate_per_hundredk = 0.0003356849303419181 * 100000
This gives us 33.56, which we can interpret as "33.56 out of every 100000 people in the White census race category in the US were killed by guns between 2012 and 2014".

We'll need to calculate these same rates for each racial category. The only stumbling block is that the racial categories are named slightly differently in census and in data. We'll need to manually construct a dictionary that allows us to map between them, and perform the division.

Here's a list of the race name in data, and the corresponding race name in census:

Asian/Pacific Islander -- Race Alone - Asian plus Race Alone - Native Hawaiian and Other Pacific Islander.
Black -- Race Alone - Black or African American.
Hispanic -- Race Alone - Hispanic
Native American/Native Alaskan -- Race Alone - American Indian and Alaska Native
White -- Race Alone - White
We'll need to create a dictionary that has each race name from data as a key, and has the population count for the races from census as the values.

Instructions
Manually create a dictionary, mapping that maps each key from race_counts to the population count of the race from census.
The keys in the dictionary should be Asian/Pacific Islander, Black, Native American/Native Alaskan, Hispanic, and White.
In the case of Asian/Pacific Islander, you'll need to add the counts from census for Race Alone - Asian, and Race Alone - Native Hawaiian and Other Pacific Islander.
Create an empty dictionary, race_per_hundredk.
Loop through each key in race_counts.
Divide the value associated with the key in race_counts by the value associated with the key in mapping.
Multiply by 100000.
Assign the result to the same key in race_per_hundredk.
When you're done, race_per_hundredk should contain the rate of gun deaths per 100000 people for each racial category.
Print race_per_hundredk to verify your work.
"""
AsianPacificIslander = 15159516+674625
mapping = {
    "Asian/Pacific Islander":AsianPacificIslander,
    "Black":40250635,
    "Native American/Native Alaskan":3739506,
    "Hispanic":44618105,
    "White":197318956
}
print(mapping)
print("------------")
race_per_hundredk = {}
for key,value in race_counts.items():
    race_per_hundredk[key] = (value / mapping[key]) * 100000
print(race_per_hundredk)
""" Console Output or Results
{'Asian/Pacific Islander': 15834141, 'Black': 40250635, 'White': 197318956, 'Native American/Native Alaskan': 3739506, 'Hispanic': 44618105}
------------
{
'Asian/Pacific Islander': 8.374309664161762,
'Black': 57.8773477735196,
'White': 33.56849303419181,
'Native American/Native Alaskan': 24.521955573811088,
'Hispanic': 20.220491210910907}
"""




"""
8: Filtering By Intent
We can filter our results, and restrict them to the Homicide intent.
This will tell us what the gun-related murder rate per 100000 people in each racial category is.
In order to do this, we'll need to redo our work in generating race_counts, but only count rows where the intent was Homicide.

We can do this by first extracting the intent column, then using the enumerate() function to loop through each index and value in the race column.
If the value in the same position in intents is Homicide, we'll count the value in the race column.

Finally, we'll use the mapping dictionary to convert from raw counts to rates.

Instructions
Extract the intent column using a list comprehension. The intent column is the fourth column in data.
Assign the result to intents.
Extract the race column using a list comprehension. The race column is the eighth column in data.
Assign the result to races.
Create an empty dictionary called homicide_race_per_hundredk
Use the enumerate() function to loop through each item in races. The position should be assigned to the loop variable i, and the value to the loop variable race.
Check the value at position i in intents.
If the value at position i in intents is Homicide:
If the key race doesn't exist in homicide_race_per_hundredk, create it.
Add 1 to the value associated with race in homicide_race_per_hundredk.
When you're done, homicide_race_per_hundredk should have one key for each of the racial categories in data.
The associated value should be the number of gun deaths by homicide for that race.
Perform the same procedure we did in the last screen using mapping on homicide_race_per_hundredk to get from raw numbers to rates per 100000.
Display homicide_race_per_hundredk to verify your work.
Write up your findings in a markdown cell.
Write up any next steps you want to pursue with the data in a markdown cell.
"""
# 8.Filtering By Intent
intents = [ row[3] for row in data ]
print(intents[0:5])
print("--------------")

races = [ row[7] for row in data ]
print(races[0:5])
print("--------------")

homicide_race_per_hundredk = {}
for i,race in enumerate(races,1):
    #print(i)
    if intents[i-1] == "Homicide":
        if race in homicide_race_per_hundredk:
            homicide_race_per_hundredk[race] += 1
        else:
            homicide_race_per_hundredk[race] = 1
print(homicide_race_per_hundredk)
print("--------------")

race_counts = {}
for race in data:
    if race[3] == "Homicide":
        if race[7] in race_counts:
            race_counts[race[7]] += 1
        else:
            race_counts[race[7]] = 1
print(race_counts)
print("--------------")

AsianPacificIslander = 15159516+674625
mapping = {
    "Asian/Pacific Islander":AsianPacificIslander,
    "Black":40250635,
    "Native American/Native Alaskan":3739506,
    "Hispanic":44618105,
    "White":197318956
}
print(mapping)
print("------------")

for key,value in homicide_race_per_hundredk.items():
    homicide_race_per_hundredk[key] = (value / mapping[key]) * 100000
print(homicide_race_per_hundredk)
""" Console Output or Results
['Suicide', 'Suicide', 'Suicide', 'Suicide', 'Suicide']
--------------
['Asian/Pacific Islander', 'White', 'White', 'White', 'White']
--------------
{'Asian/Pacific Islander': 559, 'Black': 19510, 'White': 9147, 'Native American/Native Alaskan': 326, 'Hispanic': 5634}
--------------
{'Asian/Pacific Islander': 559, 'Black': 19510, 'White': 9147, 'Native American/Native Alaskan': 326, 'Hispanic': 5634}
--------------
{'Asian/Pacific Islander': 15834141, 'Black': 40250635, 'White': 197318956, 'Native American/Native Alaskan': 3739506, 'Hispanic': 44618105}
------------
{'Asian/Pacific Islander': 3.530346230970155, 'Black': 48.471284987180944, 'White': 4.6356417981453335, 'Native American/Native Alaskan': 8.717729026240365, 'Hispanic': 12.627161104219914}
"""




"""
9: Next Steps
That's it for the guided steps! We recommend exploring the data more on your own.

Here are some potential next steps:

Figure out the link, if any, between month and homicide rate.
Explore the homicide rate by gender.
Explore the rates of other intents, like Accidental, by gender and race.
Find out if gun death rates correlate to location and education.
We recommend creating a Github repository and placing this project there. It will help other people, including employers, see your work.
As you start to put multiple projects on Github, you'll have the beginnings of a strong portfolio.
You're welcome to keep working on the project here, but we recommend downloading it to your computer using the download icon above and working on it there.
"""
