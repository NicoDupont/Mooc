"""
02/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Data Analysis With Pandas Intermediate : Working with Missing Data
"""


"""
1: Introduction
In this mission, we'll clean and analyze data on passenger survival from the Titanic. Each row contains information for a specific Titanic passenger.

Here are the first few rows of the dataset:

pclass	survived	name	sex	age	sibsp	parch	ticket	fare	cabin	embarked	boat	body	home.dest
0	1	1	"Allen, Miss. Elisabeth Walton"	female	29.0000	0	0	24160	211.3375	B5	S	2		"St Louis, MO"
1	1	1	"Allison, Master. Hudson Trevor"	male	0.9167	1	2	113781	151.5500	C22 C26	S	11		"Montreal, PQ / Chesterville, ON"
2	1	0	"Allison, Miss. Helen Loraine"	female	2	1	2	113781	151.5500	C22 C26	S			"Montreal, PQ / Chesterville, ON"
3	1	0	"Allison, Mr. Hudson Joshua Creighton"	male	30.0000	1	2	113781	151.5500	C22 C26	S		135	"Montreal, PQ / Chesterville, ON"
4	1	0	"Allison, Mrs. Hudson J C (Bessie Waldo Daniels)"	female	25	1	2	113781	151.5500	C22 C26	S			Montreal, PQ / Chesterville, ON
Lets take a closer look at a few of the key columns:

pclass -- The passenger's cabin class from 1 to 3 where 1 was the highest class
survived -- 1 if the passenger survived, and 0 if they did not.
sex -- The passenger's gender
age -- The passenger's age
fare -- The amount the passenger paid for their ticket
embarked -- Either C, Q, or S, to indicate which port the passenger boarded the ship from.
Many of the columns, such as age and sex, have missing values.

Because missing values can cause errors in numerical functions, we'll need to deal with them before we can analyze the data. For instance, finding the mean of a column with a missing value will fail because it's impossible to average a missing value. Addressing missing values will let us perform calculations on the entire data set.

Lets import the data set into pandas. You may notice at the start of the code, we import pandas differently from how we have previously.


import pandas as pd
This gives the pandas library the alias pd, so that instead of typing pandas every time we want to use a function, we can instead type pd, for example pd.read_csv().

Instructions
Read the file titanic_survival.csv into a dataframe called titanic_survival.
"""
import pandas as pd
titanic_survival = pd.read_csv("titanic_survival.csv")
print(titanic_survival.head(3))
""" Console Output or Results
Output
   pclass  survived                            name     sex      age  sibsp  \
0     1.0       1.0   Allen, Miss. Elisabeth Walton  female  29.0000    0.0
1     1.0       1.0  Allison, Master. Hudson Trevor    male   0.9167    1.0
2     1.0       0.0    Allison, Miss. Helen Loraine  female   2.0000    1.0

   parch  ticket      fare    cabin embarked boat  body  \
0    0.0   24160  211.3375       B5        S    2   NaN
1    2.0  113781  151.5500  C22 C26        S   11   NaN
2    2.0  113781  151.5500  C22 C26        S  NaN   NaN

                         home.dest
0                     St Louis, MO
1  Montreal, PQ / Chesterville, ON
2  Montreal, PQ / Chesterville, ON
"""




"""
2: Finding The Missing Data
Missing data can take a few different forms:

In Python, the None keyword and type indicates no value.
The Pandas library uses NaN, which stands for "not a number", to indicate a missing value.
In general terms, both NaN and None can be called null values.

If we want to see which values are NaN, we can use the pandas.isnull() function which takes a pandas series and returns a series of True and False values, the same way that NumPy did when we compared arrays.


sex = titanic_survival["sex"]
sex_is_null = pandas.isnull(sex)
We can use this resultant series to select only the rows that have null values.


sex_null_true = sex[sex_is_null]
We'll use this structure to look at the the null values for the "age" column.

Instructions
Count how many values in the "age" column have null values:
Use pandas.isnull() on age variable to create a Series of True and False values.
Use the resulting series to select only the elements in age that are null, and assign the result to age_null_true
Assign the length of age_null_true to age_null_count.
Print age_null_count to see how many null values are in the "age" column.
"""
age = titanic_survival["age"]
print(age.loc[10:20])
age_null_true = age[pd.isnull(age)]
age_null_count = len(age_null_true)
print("-----------")
print(age_null_count )
""" Console Output or Results
Output
10    47.0
11    18.0
12    24.0
13    26.0
14    80.0
15     NaN
16    24.0
17    50.0
18    32.0
19    36.0
20    37.0
Name: age, dtype: float64
-----------
264
"""




"""
3: Whats The Big Deal With Missing Data?
So, we know that quite a few values are missing from the "age" column, and other columns are missing data too. 
But why is this a problem?

Lets look at a typical approach to calculate the average for the "age" column:


mean_age = sum(titanic_survival["age"]) / len(titanic_survival["age"])
The result of this is that mean_age would be nan. 
This is because any calculations we do with a null value also result in a null value. 
This makes sense when you think about it -- how can you add a null value to a known value?

Instead, we have to filter out the missing values before we calculate the mean.

Instructions
Use age_is_null to create a vector that only contains values from the "age" column that aren't NaN.
Calculate the mean of the new vector, and assign the result to correct_mean_age.
"""
age_is_null = pd.isnull(titanic_survival["age"])
correct_mean_age = sum(titanic_survival["age"][age_is_null == False]) / len(titanic_survival["age"][age_is_null == False])
print("-----------")
print(correct_mean_age)
""" Console Output or Results
Output
-----------
29.8811345124
"""




"""
4: Easier Ways To Do Math
Luckily, missing data is so common that many pandas methods automatically filter for it. 
For example, if we use use the Series.mean() method to calculate the mean of a column, missing values will not be included in the calculation.

To calculate the mean age that we did earlier, we can replace all of our code with one line


correct_mean_age = titanic_survival["age"].mean()
Using the built in method is much easier, but it's import to understand what is happening behind the scenes.

Instructions
Assign the mean of the "fare" column to correct_mean_fare.
"""
correct_mean_age = titanic_survival["age"].mean()
correct_mean_fare = titanic_survival["fare"].mean()
""" Console Output or Results

"""





"""
5: Calculating Summary Statistics
Let's calculate more summary statistics for the data.
 The pclass column indicates the cabin class for each passenger, which was either first class (1), second class (2), or third class (3). 
 You'll use the list passenger_classes, which contains these values, in the following exercise.

Instructions
Use a for loop to iterate over passenger_classes. Within the for loop:
Select just the rows in titanic_survival where the pclass value is equivalent to the current iterator value (class).
Select just the fare column for the current subset of rows.
Use the Series.mean method to calculate the mean of this subset.
Add the mean of the class to the fares_by_class dictionary with class as the key.
Once the loop completes, the dictionary fares_by_class should have 1, 2, and 3 as keys, with the average fares as the corresponding values.
"""
# my Solution :
passenger_classes = [1, 2, 3]
fares_by_class = {}
for pclasse in passenger_classes:
    vector = titanic_survival["pclass"] == pclasse
    p = titanic_survival["fare"][vector].mean()
    fares_by_class[pclasse] = p

print(fares_by_class)

#Dataquest Solution :
passenger_classes = [1, 2, 3]
fares_by_class = {}
for this_class in passenger_classes:
    pclass_rows = titanic_survival[titanic_survival["pclass"] == this_class]
    pclass_fares = pclass_rows["fare"]
    fare_for_class = pclass_fares.mean()
    fares_by_class[this_class] = fare_for_class
""" Console Output or Results
Output
{1: 87.508991640866881, 2: 21.179196389891697, 3: 13.302888700564973}
"""




"""
6: Making Pivot Tables
Pivot tables provide an easy way to subset by one column and then apply a calculation like a sum or a mean. 
The concept of Pivot tables was popularized with the introduction of the 'PivotTable' feature in Microsoft Excel in the mid 1990's.

Pivot tables first group and then apply a calculation. In the previous screen, we actually made a pivot table manually by grouping by the column "pclass" and then calculating the mean of the "fare" column for each class.

Luckily, the Dataframe.pivot_table() method instead, which simplifies the kind of work we did on the last screen. 
To produce the same data, we could use one line.


passenger_survival = titanic_survival.pivot_table(index="pclass", values="fare", aggfunc=np.mean)
The first parameter of the method, index tells the method which column to group by. The second parameter values is the column that we want to apply the calculation to, and aggfunc specifies the calculation we want to perform. 
The default for the aggfunc parameter is actually the mean, so if we're calculating this we can omit this parameter.

Instructions
Use the DataFrame.pivot_table() method to calculate the mean age for each passenger class ("pclass").
Assign the result to passenger_age.
Display the passenger_age pivot table using the print() function.
"""
passenger_survival = titanic_survival.pivot_table(index="pclass", values="survived")
passenger_age = titanic_survival.pivot_table(index="pclass", values="age")
print(passenger_age)
""" Console Output or Results
Output
pclass
1.0    39.159918
2.0    29.506705
3.0    24.816367
Name: age, dtype: float64
"""




"""
7: More Complex Pivot Tables
We can use the DataFrame.pivot_table() method to perform even more advanced tasks. 
If we pass a list of column names to the values parameter instead of a single value, we can perform calculations on multiple columns at once.

We can also specify a custom calculation to be made. 
For instance, if we pass np.sum() to the aggfunc parameter it will total the values in each column.

Instructions
Make a pivot table that calculates the total fares collected ("fare") and total number of survivors ("survived") for each embarkation port ("embarked").
Assign the result to port_stats.
Display port_stats using the print() function.
"""
import numpy as np
port_stats = titanic_survival.pivot_table(index="embarked",values=["fare","survived"],aggfunc=np.sum)
print(port_stats)
""" Console Output or Results
Output
                fare  survived
embarked                      
C         16830.7922     150.0
Q          1526.3085      44.0
S         25033.3862     304.0
"""




"""
8: Drop Missing Values
We learned how to remove the missing values in a vector of data, but how about in a matrix?

We can use the DataFrame.dropna() method on pandas DataFrames to do this. 
The method will drop any rows that contain missing values.

The dropna() method takes an axis parameter, which indicates whether you would like to drop rows or columns.
Specifying axis=0 or axis='index' will drop any rows that have null values, while specifying axis=1 or axis='columns' will drop any columns that have null values. 
We will use 0 and 1 since they're more commonly used, but you can use either.

The code below will drop all rows in titanic_survival that have null values.


drop_na_rows = titanic_survival.dropna(axis=0)
There is also a parameter that allows you to specify a list of columns or rows to look at when using dropna(). 
You will need to use this in the next exercise - take a look at the documentation to work out the name of this parameter and how it works.

Instructions
Drop all columns in titanic_survival that have missing values and assign the result to drop_na_columns.
Drop all rows in titanic_survival where the columns "age" or "sex" have missing and values assign the result to new_titanic_survival.
"""
drop_na_rows = titanic_survival.dropna(axis=0)
drop_na_columns = titanic_survival.dropna(axis='columns') #or axis=1
new_titanic_survival = titanic_survival.dropna(subset=["age","sex"],axis=0)
""" Console Output or Results

"""




"""
9: Using Iloc To Access Rows By Position
In previous missions, we have used row labels to select data in pandas using Dataframe.loc[]. 
These work just like column labels, and can be values like numbers, characters, and strings.

Sometimes your dataset will have row labels that are not numbers, or that are not in order. 
We have sorted the new_titanic_survival dataframe by the "age" column from highest to lowest. 
Here is a preview of the a few of the columns for the first five rows of the data, or the five oldest passengers onboard.

pclass	survived	name	sex	age
14	1.0	1.0	Barkworth, Mr. Algernon Henry Wilson	male	80.0
61	1.0	1.0	Cavendish, Mrs. Tyrell William (Julia Florence...	female	76.0
1235	3.0	0.0	Svensson, Mr. Johan	male	74.0
135	1.0	0.0	Goldschmidt, Mr. George B	male	71.0
9	1.0	0.0	Artagaveytia, Mr. Ramon	male	71.0
You can see that the row labels for the first 5 rows are 14, 61, 1235, 135 and 9. 
If we wanted to select the first five rows, we can use DataFrame.iloc[] method to select by position. 
The easy way to remember which is which is to remember that iloc[] stands for integer location, because you use integers and not labels to select the data.

The following code will select the first 5 rows as shown above:


first_five_rows = new_titanic_survival.iloc[0:5]
Instructions
Assign the first ten rows from new_titanic_survival to first_ten_rows.
Assign the fifth row from new_titanic_survival to row_position_fifth.
Assign the row with index label 25 from new_titanic_survivalto row_index_25.
"""
# We have already sorted new_titanic_survival by age
first_five_rows = new_titanic_survival.iloc[0:5]
first_ten_rows = new_titanic_survival.iloc[0:10]
row_position_fifth = new_titanic_survival.iloc[4]
row_index_25 = new_titanic_survival.loc[25]
""" Console Output or Results

"""





"""
10: Using Column Indexes
We can also index columns using both the loc[] and iloc[] methods. 
With .loc[], we specify the column label strings as we have in the earlier exercises in this missions. 
With iloc[], we simply use the integer number of the column, starting from the left-most column which is 0. 
Similar to indexing with NumPy arrays, you separate the row and columns with a comma, and can use a colon to specify a range or as a wildcard.


first_row_first_column = new_titanic_survival.iloc[0,0]
all_rows_first_three_columns = new_titanic_survival.iloc[:,0:3]
row_index_83_age = new_titanic_survival.loc[83,"age"]
row_index_1000_pclass = new_titanic_survival.loc[766,"pclass"]
Instructions
Assign the value at row index label 1100, column index label "age" from new_titanic_survival to row_index_1100_age.
Assign the value at row index label 25, column index label "survived" from new_titanic_survival to row_index_25_survived.
Assign the first 5 rows and first three columns from new_titanic_survival to five_rows_three_cols.
"""
first_row_first_column = new_titanic_survival.iloc[0,0]
all_rows_first_three_columns = new_titanic_survival.iloc[:,0:3]
row__index_83_age = new_titanic_survival.loc[83,"age"]
row_index_1000_pclass = new_titanic_survival.loc[766,"pclass"]
print("--------------------")
row_index_1100_age = new_titanic_survival.loc[1100,"age"]
print(row_index_1100_age)
print("--------------------")
row_index_25_survived = new_titanic_survival.loc[25,"survived"]
print(row_index_25_survived)
print("--------------------")
five_rows_three_cols = new_titanic_survival.iloc[0:5,0:3]
print(five_rows_three_cols)
print("--------------------")
""" Console Output or Results
Output
--------------------
29.0
--------------------
0.0
--------------------
      pclass  survived                                               name
14       1.0       1.0               Barkworth, Mr. Algernon Henry Wilson
61       1.0       1.0  Cavendish, Mrs. Tyrell William (Julia Florence...
1235     3.0       0.0                                Svensson, Mr. Johan
135      1.0       0.0                          Goldschmidt, Mr. George B
9        1.0       0.0                            Artagaveytia, Mr. Ramon
--------------------
"""




"""
11: Reindexing Rows
After we sorted new_titanic_survival by age, the row indexes were no longer sequential. 
Each row retained its original index from titanic_survival.

Sometimes it's useful to reindex, starting from 0. 
We can use the DataFrame.reset_index() method to do this. 
By default, the method retains the old index by adding an extra column to the dataframe with the old index values.

In this exercise, we don't want to retain the index. 
Check the documentation to see what parameter you need to add so that we don't retain the old index.

Instructions
Reindex the new_titanic_survival dataframe so the row indexes start from 0, and the old index is dropped.
Assign the final result to titanic_reindexed.
Print the first 5 rows and the first 3 columns of titanic_reindexed.
"""
titanic_reindexed = new_titanic_survival.reset_index(drop=True)

print(titanic_reindexed.iloc[0:5,0:3])
print("--------------------")
""" Console Output or Results
Output
   pclass  survived                                               name
0     1.0       1.0               Barkworth, Mr. Algernon Henry Wilson
1     1.0       1.0  Cavendish, Mrs. Tyrell William (Julia Florence...
2     3.0       0.0                                Svensson, Mr. Johan
3     1.0       0.0                          Goldschmidt, Mr. George B
4     1.0       0.0                            Artagaveytia, Mr. Ramon
--------------------
"""




"""
12: Apply Functions Over A DataFrame
To perform a complex calculation across pandas objects, we'll need to learn about the DataFrame.apply() method. 
By default, DataFrame.apply() will iterate through each column in a DataFrame, and perform on each function. 
When we create our function, we give it one parameter, apply() method passes each column to the parameter as a pandas series.

The result from the function will be combined with all of the other results, and placed into a new series. 
The function results will have the same position as the column or row we generated them from. Let's look at a simple example:


# This function returns the hundredth item from a series
def hundredth_row(column):
    # Extract the hundredth item
    hundredth_item = column.iloc[99]
    return hundredth_item
​
# Return the hundredth item from each column
hundredth_row = titanic_survival.apply(hundredth_row)
Instructions
Write a function that counts the number of null elements in a Series.
Use the DataFrame.apply() method along with your function to run across all the columns in titanic_survival.
Assign the result to column_null_count.
"""
def hundredth_row(column):
    hundredth_item = column.iloc[99]
    return hundredth_item

hundredth_row = titanic_survival.apply(hundredth_row)

def null_count(column):
    return len(column[pd.isnull(column)])

column_null_count = titanic_survival.apply(null_count)
print(column_null_count)
""" Console Output or Results
Output
pclass          1
survived        1
name            1
sex             1
age           264
sibsp           1
parch           1
ticket          1
fare            2
cabin        1015
embarked        3
boat          824
body         1189
home.dest     565
dtype: int64
"""




"""
13: Applying A Function To A Row
By passing in the axis=1 argument, we can use the DataFrame.apply() method to iterate over rows instead of columns.

We can use this to calculate some summary information about the ages of the passengers on the Titanic. 
You will need to use an if/elif/else statement in your function. 
The elif statement just means else if. Below is an example of how these statements work.


def which_class(row):
    pclass = row['pclass']
    if pd.isnull(pclass):
        return "Unknown"
    elif pclass == 1:
        return "First Class"
    elif pclass == 2:
        return "Second Class"
    else pclass == 3:
        return "Third Class"
​
classes = titanic_survivors.apply(which_class, axis=1)
When the function is called, each test runs until one of the if, elif or else statements is met.

Instructions
Create a function that returns the string "minor" if someone is under 18, "adult" if they are equal to or over 18, and "unknown" if their age is null.
Then, use the function along with .apply() to find the correct label for everyone in the titanic_survival dataframe.
Assign the result to age_labels.
You can use pd.isnull to check if a value is null or not.
"""
def is_minor(row):
    if row["age"] < 18:
        return True
    else:
        return False

minors = titanic_survival.apply(is_minor, axis=1)
print(minors[0:5])
print("------------------")

def minor(row):
    if pd.isnull(row["age"]):
        return "unknown"
    elif row["age"] < 18:
        return "minor"
    else:
        return "adult"

age_labels = titanic_survival.apply(minor, axis=1)
print(age_labels[0:5])
""" Console Output or Results
0    False
1     True
2     True
3    False
4    False
dtype: bool
------------------
0    adult
1    minor
2    minor
3    adult
4    adult
dtype: object
"""




"""
14: Calculating Survival Percentage By Age Group
Now that we have age labels for everyone, let's make a pivot table to find the probability of survival for each age group.

We have added an "age_labels" column to the dataframe containing the age_labels variable from the previous step.

Instructions
Create a pivot table that calculates the mean survival chance("survived") for each age group ("age_labels") of the dataframe titanic_survival.
Assign the resulting Series object to age_group_survival.
"""
import numpy as np
age_group_survival = titanic_survival.pivot_table(index="age_labels",values="survived",aggfunc=np.mean)
print(type(age_group_survival))
print(age_group_survival)
""" Console Output or Results
Output
<class 'pandas.core.series.Series'>
age_labels
adult      0.387892
minor      0.525974
unknown    0.277567
Name: survived, dtype: float64
"""





"""
15: Next Steps
In this mission, we learned several strategies for identifying missing data, using integer based selection, and performing calculations to perform analysis in pandas dataframes.

The next mission is a challenge, where we'll practice some of the pandas concepts we've learned so far.
"""