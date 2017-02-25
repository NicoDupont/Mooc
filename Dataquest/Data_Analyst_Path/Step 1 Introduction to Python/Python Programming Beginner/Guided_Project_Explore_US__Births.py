""" 01/2017
Dataquest : Data Analyst Path
Step 1: Introduction To Python
SubStep : Python Programming: Beginner : Guided Project: Explore U.S. Births
"""


"""
"""




"""
1: Introduction To The Dataset
In the last guided project, we explored the Jupyter notebook environment and worked with a dataset on births in the U.S. In this guided project, we'll continue working with the same dataset, compiled by FiveThirtyEight. When you're finished, you can compare your work to the reference solution.

The dataset contains the following columns:

year: Year (1994 to 2003).
month: Month (1 to 12).
date_of_month: Day number of the month (1 to 31).
day_of_week: Day of week (1 to 7).
births: Number of births that day.
First things first, let's read in the CSV file and explore it.

Instructions
Read the CSV file "US_births_1994-2003_CDC_NCHS.csv" into a string.
Split the string on the newline character ("\n").
Display the first 10 values in the resulting list.

"""

""" notebook
Dataquest : Guided Project: Explore U.S. Births
Step1
In [4]:

births_file = open("US_births_1994-2003_CDC_NCHS.csv","r").read().split("\n")
print(births_file[0:10])
['year,month,date_of_month,day_of_week,births', '1994,1,1,6,8096', '1994,1,2,7,7772', '1994,1,3,1,10142', '1994,1,4,2,11248', '1994,1,5,3,11053', '1994,1,6,4,11406', '1994,1,7,5,11251', '1994,1,8,6,8653', '1994,1,9,7,7910']
"""



"""
2: Converting Data Into A List Of Lists
While a list of strings helps us get a general picture of the dataset, we need to convert it to a more structured format to be able to analyze it. Specifically, we need to convert the dataset into a list of lists where each nested list contains integer values (not strings). We also need to remove the header row.

Here's what we want the data to look like:


[
  [1994, 1, 1, 6, 8096],
  [1994, 1, 2, 7, 7772],
  [1994, 1, 3, 1, 10142],
  [1994, 1, 4, 2, 11248],
  [1994, 1, 5, 3, 11053],
...
]
Instructions
Create a function named read_csv() that:
Takes a single, required argument, a string representing the file name of the CSV file.
Reads the file into a string, splits the string on the newline character ("\n"), and removes the header row. Assign this list to string_list and create an empty list named final_list.
Uses a for loop to:
Iterate over string_list,
Create an empty list named int_fields,
Splits each row on the comma delimiter (,) and assigns the resulting list to string_fields,
Converts each value in string_fields to an integer and appends to int_fields,
Appends int_fields to final_list.
Returns final_list.
Use the read_csv() function to read in the file "US_births_1994-2003_CDC_NCHS.csv" and assign the result to cdc_list.
Display the first 10 rows of cdc_list to confirm it's a list of lists, containing only integer values, and no header row.
"""

""" notebook
Step2
In [8]:

def read_csv(file):
    final_list = []
    split_file = open(file,"r").read().split("\n")
    string_list = split_file[1:len(split_file)]
    for row in string_list:
        int_fields = []
        string_fields = row.split(',')
        for i in range(len(string_fields)):
            string_fields[i] = int(string_fields[i])
        int_fields = string_fields
        final_list.append(int_fields)
    return final_list
​
cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_list[0:10]
Out[8]:
[[1994, 1, 1, 6, 8096],
 [1994, 1, 2, 7, 7772],
 [1994, 1, 3, 1, 10142],
 [1994, 1, 4, 2, 11248],
 [1994, 1, 5, 3, 11053],
 [1994, 1, 6, 4, 11406],
 [1994, 1, 7, 5, 11251],
 [1994, 1, 8, 6, 8653],
 [1994, 1, 9, 7, 7910],
 [1994, 1, 10, 1, 10498]]
"""





"""
3: Calculating Number Of Births Each Month
Now that the data is in a more usable format, we can start to analyze it. Let's calculate the total number of births that occured in each month, across all of the years in the dataset. We'll create a dictionary where each key is a unique month and each value is the number of births that happened in that month, across all years:


{
   1: 3232517,
   2: 3018140,
   3: 3322069,
   4: 3185314,
   5: 3350907,
   6: 3296530,
   7: 3498783,
   8: 3525858,
   9: 3439698,
   10: 3378814,
   11: 3171647,
   12: 3301860
}
Instructions
Create a function named month_births() that:
Takes a single, required argument, a list of lists.
Creates an empty dictionary, births_per_month, to store the monthly totals.
Uses a for loop to:
Iterate over the list of lists,
Extract the value in the month and births columns,
If the month value already exists as a key in births_per_month, the births value is added to the existing value,
If the month value doesn't exist as a key in births_per_month, it's created and the associated value is the births value.
After the loop, return the births_per_month dictionary.
Use the month_births() function to calculate the monthly totals for the dataset and assign the result to cdc_month_births. Display the dictionary.
"""

""" notebook
step3
In [10]:

def month_births(list_of_lists):
    births_per_month = {}
    for list in list_of_lists:
        # print(list[3])
        if list[1] not in births_per_month:
            births_per_month[list[1]] = list[4]
        else:
            births_per_month[list[1]] = births_per_month[list[1]] + list[4]
    return births_per_month
cdc_month_births = month_births(cdc_list)
print(cdc_month_births)

{1: 3232517, 2: 3018140, 3: 3322069, 4: 3185314, 5: 3350907, 6: 3296530, 7: 3498783, 8: 3525858, 9: 3439698, 10: 3378814, 11: 3171647, 12: 3301860}
"""


"""
4: Calculating Number Of Births Each Day Of Week
Let's now create a function that calculates the total number of births for each unique day of the week. Here's what we want the dictionary to look like:


{
  1: 5789166,
  2: 6446196,
  3: 6322855,
  4: 6288429,
  5: 6233657,
  6: 4562111,
  7: 4079723
}
Instructions
Create a function named dow_births() that takes a single, required argument (a list of lists) and returns a dictionary containing the total number of births for each unique value of the day_of_week column.
Use the dow_births() function to return the day-of-week totals for the dataset and assign the result to cdc_day_births. Display the dictionary.
"""

""" notebook
Step4
In [11]:

def dow_births(list_of_lists):
    births_per_day_of_week = {}
    for list in list_of_lists:
        # print(list[3])
        if list[3] not in births_per_day_of_week:
            births_per_day_of_week[list[3]] = list[4]
        else:
            births_per_day_of_week[list[3]] = births_per_day_of_week[list[3]] + list[4]
    return births_per_day_of_week
cdc_day_births = dow_births(cdc_list)
print(cdc_day_births)

{1: 5789166, 2: 6446196, 3: 6322855, 4: 6288429, 5: 6233657, 6: 4562111, 7: 4079723}
"""



"""
5: Creating A More General Function
You may have noticed that there was a lot of similarity between the two functions you just wrote. While we can also create separate functions to calculate the totals for the year and date_of_month columns, it's better to create a single function that works for any column and specify the column we want as a parameter each time we call the function.

Instructions
Create a function named calc_counts() that:
Takes two, required parameters:
data: a list of lists
column: the column number we want to calculate the totals for
Populates and returns a dictionary containing the total number of births for each unique value in the column at position column.
Use the calc_counts() function to:
Return the yearly totals for the dataset and assign the result to cdc_year_births.
Return the monthly totals for the dataset and assign the result to cdc_month_births.
Return the day-of-month totals for the dataset and assign the result to cdc_dom_births.
Return the day-of-week totals for the dataset and assign the result to cdc_dow_births.
"""

""" notebook
step5
In [14]:

def calc_counts(list_of_lists,column):
    births_count = {}
    for list in list_of_lists:
        # print(list[3])
        if list[column] not in births_count:
            births_count[list[column]] = list[4]
        else:
            births_count[list[column]] = births_count[list[column]] + list[4]
    return births_count
cdc_year_births = calc_counts(cdc_list,0)
cdc_month_births = calc_counts(cdc_list,1)
cdc_dom_births = calc_counts(cdc_list,2)
cdc_dow_births = calc_counts(cdc_list,3)
print("------------------")
print("Births per years :")
print(cdc_year_births)
print("------------------")
print("Births per month :")
print(cdc_month_births)
print("------------------")
print("Births per day-of-month :")
print(cdc_dom_births)
print("------------------")
print("Births per day-of-week :")
print(cdc_dow_births)
------------------
Births per years :
{2000: 4058814, 2001: 4025933, 2002: 4021726, 2003: 4089950, 1994: 3952767, 1995: 3899589, 1996: 3891494, 1997: 3880894, 1998: 3941553, 1999: 3959417}
------------------
Births per month :
{1: 3232517, 2: 3018140, 3: 3322069, 4: 3185314, 5: 3350907, 6: 3296530, 7: 3498783, 8: 3525858, 9: 3439698, 10: 3378814, 11: 3171647, 12: 3301860}
------------------
Births per day-of-month :
{1: 1276557, 2: 1288739, 3: 1304499, 4: 1288154, 5: 1299953, 6: 1304474, 7: 1310459, 8: 1312297, 9: 1303292, 10: 1320764, 11: 1314361, 12: 1318437, 13: 1277684, 14: 1320153, 15: 1319171, 16: 1315192, 17: 1324953, 18: 1326855, 19: 1318727, 20: 1324821, 21: 1322897, 22: 1317381, 23: 1293290, 24: 1288083, 25: 1272116, 26: 1284796, 27: 1294395, 28: 1307685, 29: 1223161, 30: 1202095, 31: 746696}
------------------
Births per day-of-week :
{1: 5789166, 2: 6446196, 3: 6322855, 4: 6288429, 5: 6233657, 6: 4562111, 7: 4079723}
"""



"""
6: Next Steps
That's it for the guided steps. Here are some suggestions for next steps:

Write a function that can calculate the min and max values for any dictionary that's passed in.
Write a function that extracts the same values across years and calculates the differences between consecutive values to show if number of births is increasing or decreasing.
For example, how did the number of births on Saturday change each year between 1994 and 2003?
Find a way to combine the CDC data with the SSA data, which you can find here. Specifically, brainstorm ways to deal with the overlapping time periods in the datasets.
"""

""" notebook

"""
