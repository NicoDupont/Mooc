10/2017  
Datacamp - Cleaning Data in Python  

---

Here, you'll learn about the principles of tidy data and more importantly, why you should care about them and how they make subsequent data analysis more efficient. You'll gain first hand experience with reshaping and tidying your data using techniques such as pivoting and melting.  

# Part 2 : Tidying data for analysis  


## Recognizing tidy data

For data to be tidy, it must have:  

 - Each variable as a separate column.
 - Each row as a separate observation.

As a data scientist, you'll encounter data that is represented in a variety of different ways, so it is important to be able to recognize tidy (or untidy) data when you see it.  

In this exercise, two example datasets have been pre-loaded into the DataFrames df1 and df2. Only one of them is tidy. Your job is to explore these further in the IPython Shell and identify the one that is not tidy, and why it is not tidy.  

In the rest of this course, you will frequently be asked to explore the structure of DataFrames in the IPython Shell prior to performing different operations on them. Doing this will not only strengthen your comprehension of the data cleaning concepts covered in this course, but will also help you realize and take advantage of the relationship between working in the Shell and in the script.  

### Instructions :

Possible Answers
 - df2; the rows are not all separate observations.
 - df1; each variable is not a separate column.
 - df2; each variable is not a separate column.
 - df1; the rows are not all separate observations.

=> answer 3

```python
df1.head()
df2.head()
```

### Results :  

  In [1]: df1.head()
  Out[1]:
     Ozone  Solar.R  Wind  Temp  Month  Day
  0   41.0    190.0   7.4    67      5    1
  1   36.0    118.0   8.0    72      5    2
  2   12.0    149.0  12.6    74      5    3
  3   18.0    313.0  11.5    62      5    4
  4    NaN      NaN  14.3    56      5    5

  In [2]: df2.head()
  Out[2]:
     Month  Day variable  value
  0      5    1    Ozone   41.0
  1      5    2    Ozone   36.0
  2      5    3    Ozone   12.0
  3      5    4    Ozone   18.0
  4      5    5    Ozone    NaN

---

## Reshaping your data using melt

Melting data is the process of turning columns of your data into rows of data. Consider the DataFrames from the previous exercise. In the tidy DataFrame, the variables Ozone, Solar.R, Wind, and Temp each had their own column. If, however, you wanted these variables to be in rows instead, you could melt the DataFrame. In doing so, however, you would make the data untidy! This is important to keep in mind: Depending on how your data is represented, you will have to reshape it differently.  

In this exercise, you will practice melting a DataFrame using pd.melt(). There are two parameters you should be aware of: id_vars and value_vars. The id_vars represent the columns of the data you do not want to melt (i.e., keep it in its current shape), while the value_vars represent the columns you do wish to melt into rows. By default, if no value_vars are provided, all columns not set in the id_vars will be melted. This could save a bit of typing, depending on the number of columns that need to be melted.  

The (tidy) DataFrame airquality has been pre-loaded. Your job is to melt its Ozone, Solar.R, Wind, and Temp columns into rows. Later in this chapter, you'll learn how to bring this melted DataFrame back into a tidy form.  

### Instructions :

 - Print the head of airquality.
 - Use pd.melt() to melt the Ozone, Solar.R, Wind, and Temp columns of airquality into rows. Do this by using id_vars to specify the columns you do not wish to melt: 'Month' and 'Day'.
 - Print the head of airquality_melt.

```python
# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame=airquality, id_vars=['Month','Day'])

# Print the head of airquality_melt
print(airquality_melt.head())
```

### Results :  

Well done! This exercise demonstrates that melting a DataFrame is not always appropriate if you want to make it tidy. You may have to perform other transformations depending on how your data is represented.  

  <script.py> output:
         Ozone  Solar.R  Wind  Temp  Month  Day
      0   41.0    190.0   7.4    67      5    1
      1   36.0    118.0   8.0    72      5    2
      2   12.0    149.0  12.6    74      5    3
      3   18.0    313.0  11.5    62      5    4
      4    NaN      NaN  14.3    56      5    5
         Month  Day variable  value
      0      5    1    Ozone   41.0
      1      5    2    Ozone   36.0
      2      5    3    Ozone   12.0
      3      5    4    Ozone   18.0
      4      5    5    Ozone    NaN

---

## Customizing melted data

When melting DataFrames, it would be better to have column names more meaningful than variable and value.  

The default names may work in certain situations, but it's best to always have data that is self explanatory.  

You can rename the variable column by specifying an argument to the var_name parameter, and the value column by specifying an argument to the value_name parameter. You will now practice doing exactly this. The DataFrame airquality has been pre-loaded for you.  

### Instructions :

 - Print the head of airquality.
 - Melt the Ozone, Solar.R, Wind, and Temp columns of airquality into rows, with the default variable column renamed to 'measurement' and the default value column renamed to 'reading'. You can do this by specifying, respectively, the var_name and value_name parameters.
 - Print the head of airquality_melt.

```python
# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame=airquality, id_vars=['Month','Day'], value_vars=['Ozone', 'Solar.R', 'Wind', 'Temp'],
var_name='measurement', value_name='reading')

# Print the head of airquality_melt
print(airquality_melt.head())
```

### Results :  

Great work! The DataFrame is more informative now. In the next video, you'll learn about pivoting, which is the opposite of melting. You'll then be able to convert this DataFrame back into its original, tidy, form!  

  <script.py> output:
         Ozone  Solar.R  Wind  Temp  Month  Day
      0   41.0    190.0   7.4    67      5    1
      1   36.0    118.0   8.0    72      5    2
      2   12.0    149.0  12.6    74      5    3
      3   18.0    313.0  11.5    62      5    4
      4    NaN      NaN  14.3    56      5    5
         Month  Day measurement  reading
      0      5    1       Ozone     41.0
      1      5    2       Ozone     36.0
      2      5    3       Ozone     12.0
      3      5    4       Ozone     18.0
      4      5    5       Ozone      NaN

---

## Pivot data  

Pivoting data is the opposite of melting it. Remember the tidy form that the airquality DataFrame was in before you melted it? You'll now begin pivoting it back into that form using the .pivot_table() method!  

While melting takes a set of columns and turns it into a single column, pivoting will create a new column for each unique value in a specified column.  

.pivot_table() has an index parameter which you can use to specify the columns that you don't want pivoted: It is similar to the id_vars parameter of pd.melt(). Two other parameters that you have to specify are columns (the name of the column you want to pivot), and values (the values to be used when the column is pivoted). The melted DataFrame airquality_melt has been pre-loaded for you.  

### Instructions :

 - Print the head of airquality_melt.
 - Pivot airquality_melt by using .pivot_table() with the rows indexed by 'Month' and 'Day', the columns indexed by 'measurement', and the values populated with 'reading'.
 - Print the head of airquality_pivot.

```python
# Print the head of airquality_melt
print(airquality_melt.head())

# Pivot airquality_melt: airquality_pivot
airquality_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading')

# Print the head of airquality_pivot
print(airquality_pivot.head())
```

### Results :  

	<script.py> output:
		   Month  Day measurement  reading
		0      5    1       Ozone     41.0
		1      5    2       Ozone     36.0
		2      5    3       Ozone     12.0
		3      5    4       Ozone     18.0
		4      5    5       Ozone      NaN
		measurement  Ozone  Solar.R  Temp  Wind
		Month Day                              
		5     1       41.0    190.0  67.0   7.4
			  2       36.0    118.0  72.0   8.0
			  3       12.0    149.0  74.0  12.6
			  4       18.0    313.0  62.0  11.5
			  5        NaN      NaN  56.0  14.

Excellent work! Notice that the pivoted DataFrame does not actually look like the original DataFrame. In the next exercise, you'll turn this pivoted DataFrame back into its original form.  
			  
---

## Resetting the index of a DataFrame  

After pivoting airquality_melt in the previous exercise, you didn't quite get back the original DataFrame.  

What you got back instead was a pandas DataFrame with a hierarchical index (also known as a MultiIndex).  

Hierarchical indexes are covered in depth in Manipulating DataFrames with pandas. In essence, they allow you to group columns or rows by another variable - in this case, by 'Month' as well as 'Day'.  

There's a very simple method you can use to get back the original DataFrame from the pivoted DataFrame: .reset_index(). Dan didn't show you how to use this method in the video, but you're now going to practice using it in this exercise to get back the original DataFrame from airquality_pivot, which has been pre-loaded.  

### Instructions :

 - Print the index of airquality_pivot by accessing its .index attribute. This has been done for you.
 - Reset the index of airquality_pivot using its .reset_index() method.
 - Print the new index of airquality_pivot.
 - Print the head of airquality_pivot.

```python
# Print the index of airquality_pivot
print(airquality_pivot.index)

# Reset the index of airquality_pivot: airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the new index of airquality_pivot
print(airquality_pivot.index)

# Print the head of airquality_pivot
print(airquality_pivot.head())
```

### Results :  

	<script.py> output:
		MultiIndex(levels=[[5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]],
				   labels=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]],
				   names=['Month', 'Day'])
		RangeIndex(start=0, stop=153, step=1)
		measurement  Month  Day  Ozone  Solar.R  Temp  Wind
		0                5    1   41.0    190.0  67.0   7.4
		1                5    2   36.0    118.0  72.0   8.0
		2                5    3   12.0    149.0  74.0  12.6
		3                5    4   18.0    313.0  62.0  11.5
		4                5    5    NaN      NaN  56.0  14.3

Great work! You've now converted the DataFrame back into its original form!  

---

## Pivoting duplicate values  

So far, you've used the .pivot_table() method when there are multiple index values you want to hold constant during a pivot. In the video, Dan showed you how you can also use pivot tables to deal with duplicate values by providing an aggregation function through the aggfunc parameter. Here, you're going to combine both these uses of pivot tables.  

Let's say your data collection method accidentally duplicated your dataset. Such a dataset, in which each row is duplicated, has been pre-loaded as airquality_dup. In addition, the airquality_melt DataFrame from the previous exercise has been pre-loaded. Explore their shapes in the IPython Shell by accessing their .shape attributes to confirm the duplicate rows present in airquality_dup.  

You'll see that by using .pivot_table() and the aggfunc parameter, you can not only reshape your data, but also remove duplicates. Finally, you can then flatten the columns of the pivoted DataFrame using .reset_index().  

NumPy and pandas have been imported as np and pd respectively.  

### Instructions :

 - Pivot airquality_dup by using .pivot_table() with the rows indexed by 'Month' and 'Day', the columns indexed by 'measurement', and the values populated with 'reading'. Use np.mean for the aggregation function.
 - Flatten airquality_pivot by resetting its index.
 - Print the head of airquality_pivot and then the original airquality DataFrame to compare their structure.

```python
# Pivot airquality_dup: airquality_pivot
airquality_dup = airquality_dup.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading', aggfunc=np.mean)

# Reset the index of airquality_pivot
airquality_pivot = airquality_dup.reset_index()

# Print the head of airquality_pivot
print(airquality_pivot.head())

# Print the head of airquality
print(airquality.head())

```

### Results :  

	<script.py> output:
		measurement  Month  Day  Ozone  Solar.R  Temp  Wind
		0                5    1   41.0    190.0  67.0   7.4
		1                5    2   36.0    118.0  72.0   8.0
		2                5    3   12.0    149.0  74.0  12.6
		3                5    4   18.0    313.0  62.0  11.5
		4                5    5    NaN      NaN  56.0  14.3
		   Ozone  Solar.R  Wind  Temp  Month  Day
		0   41.0    190.0   7.4    67      5    1
		1   36.0    118.0   8.0    72      5    2
		2   12.0    149.0  12.6    74      5    3
		3   18.0    313.0  11.5    62      5    4
		4    NaN      NaN  14.3    56      5    5

Fantastic! The default aggregation function used by .pivot_table() is np.mean(). So you could have pivoted the duplicate values in this DataFrame even without explicitly specifying the aggfunc parameter.  
		
---

## Splitting a column with .str  

The dataset you saw in the video, consisting of case counts of tuberculosis by country, year, gender, and age group, has been pre-loaded into a DataFrame as tb.  

In this exercise, you're going to tidy the 'm014' column, which represents males aged 0-14 years of age. In order to parse this value, you need to extract the first letter into a new column for gender, and the rest into a column for age_group. Here, since you can parse values by position, you can take advantage of pandas' vectorized string slicing by using the str attribute of columns of type object.  

Begin by printing the columns of tb in the IPython Shell using its .columns attribute, and take note of the problematic column.  

### Instructions :

 - Melt tb keeping 'country' and 'year' fixed.
 - Create a 'gender' column by slicing the first letter of the variable column of tb_melt.
 - Create an 'age_group' column by slicing the rest of the variable column of tb_melt.
 - Print the head of tb_melt. This has been done for you, so hit 'Submit Answer' to see the results!

```python
# Melt tb: tb_melt
tb_melt = pd.melt(frame=tb, id_vars=['country', 'year'])

print("------")
print(tb_melt.head())
print("------")

# Create the 'gender' column
tb_melt['gender'] = tb_melt.variable.str[0]

# Create the 'age_group' column
tb_melt['age_group'] = tb_melt.variable.str[1:]

# Print the head of tb_melt
print(tb_melt.head())
```

### Results :  

	<script.py> output:
		------
		  country  year variable  value
		0      AD  2000     m014    0.0
		1      AE  2000     m014    2.0
		2      AF  2000     m014   52.0
		3      AG  2000     m014    0.0
		4      AL  2000     m014    2.0
		------
		  country  year variable  value gender age_group
		0      AD  2000     m014    0.0      m       014
		1      AE  2000     m014    2.0      m       014
		2      AF  2000     m014   52.0      m       014
		3      AG  2000     m014    0.0      m       014
		4      AL  2000     m014    2.0      m       014

Superb! Notice the new 'gender' and 'age_group' columns you created. It is vital to be able to split columns as needed so you can access the data that is relevant to your question.    

---

## Splitting a column with .split() and .get()  

Another common way multiple variables are stored in columns is with a delimiter. You'll learn how to deal with such cases in this exercise, using a dataset consisting of Ebola cases and death counts by state and country. It has been pre-loaded into a DataFrame as ebola.  

Print the columns of ebola in the IPython Shell using ebola.columns. Notice that the data has column names such as Cases_Guinea and Deaths_Guinea. Here, the underscore _ serves as a delimiter between the first part (cases or deaths), and the second part (country).  

This time, you cannot directly slice the variable by position as in the previous exercise. You now need to use Python's built-in string method called .split(). By default, this method will split a string into parts separated by a space. However, in this case you want it to split by an underscore. You can do this on Cases_Guinea, for example, using Cases_Guinea.split('_'), which returns the list ['Cases', 'Guinea'].  

The next challenge is to extract the first element of this list and assign it to a type variable, and the second element of the list to a country variable. You can accomplish this by accessing the str attribute of the column and using the .get() method to retrieve the 0 or 1 index, depending on the part you want.  

### Instructions :

 - Melt ebola using 'Date' and 'Day' as the id_vars, 'type_country' as the var_name, and 'counts' as the value_name.
 - Create a column called 'str_split' by splitting the 'type_country' column of ebola_melt on '_'. Note that you will first have to access the str attribute of type_country before you can use .split().
 - Create a column called 'type' by using the .get() method to retrieve index 0 of the 'str_split' column of ebola_melt.
 - Create a column called 'country' by using the .get() method to retrieve index 1 of the 'str_split' column of ebola_melt.
 - Print the head of ebola. This has been done for you, so hit 'Submit Answer' to view the results!

```python
print(ebola.head())
print('----------')
# Melt ebola: ebola_melt
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')

print(ebola_melt.head())
print('----------')

# Create the 'str_split' column
ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')

print(ebola_melt.head())
print('----------')

# Create the 'type' column
ebola_melt['type'] = ebola_melt.str_split.str.get(0)

# Create the 'country' column
ebola_melt['country'] = ebola_melt.str_split.str.get(1)

# Print the head of ebola_melt
print(ebola_melt.head())
```

### Results :  

	<script.py> output:
				 Date  Day  Cases_Guinea  Cases_Liberia  Cases_SierraLeone  \
		0    1/5/2015  289        2776.0            NaN            10030.0   
		1    1/4/2015  288        2775.0            NaN             9780.0   
		2    1/3/2015  287        2769.0         8166.0             9722.0   
		3    1/2/2015  286           NaN         8157.0                NaN   
		4  12/31/2014  284        2730.0         8115.0             9633.0   
		
		   Cases_Nigeria  Cases_Senegal  Cases_UnitedStates  Cases_Spain  Cases_Mali  \
		0            NaN            NaN                 NaN          NaN         NaN   
		1            NaN            NaN                 NaN          NaN         NaN   
		2            NaN            NaN                 NaN          NaN         NaN   
		3            NaN            NaN                 NaN          NaN         NaN   
		4            NaN            NaN                 NaN          NaN         NaN   
		
		   Deaths_Guinea  Deaths_Liberia  Deaths_SierraLeone  Deaths_Nigeria  \
		0         1786.0             NaN              2977.0             NaN   
		1         1781.0             NaN              2943.0             NaN   
		2         1767.0          3496.0              2915.0             NaN   
		3            NaN          3496.0                 NaN             NaN   
		4         1739.0          3471.0              2827.0             NaN   
		
		   Deaths_Senegal  Deaths_UnitedStates  Deaths_Spain  Deaths_Mali  
		0             NaN                  NaN           NaN          NaN  
		1             NaN                  NaN           NaN          NaN  
		2             NaN                  NaN           NaN          NaN  
		3             NaN                  NaN           NaN          NaN  
		4             NaN                  NaN           NaN          NaN  
		----------
				 Date  Day  type_country  counts
		0    1/5/2015  289  Cases_Guinea  2776.0
		1    1/4/2015  288  Cases_Guinea  2775.0
		2    1/3/2015  287  Cases_Guinea  2769.0
		3    1/2/2015  286  Cases_Guinea     NaN
		4  12/31/2014  284  Cases_Guinea  2730.0
		----------
				 Date  Day  type_country  counts        str_split
		0    1/5/2015  289  Cases_Guinea  2776.0  [Cases, Guinea]
		1    1/4/2015  288  Cases_Guinea  2775.0  [Cases, Guinea]
		2    1/3/2015  287  Cases_Guinea  2769.0  [Cases, Guinea]
		3    1/2/2015  286  Cases_Guinea     NaN  [Cases, Guinea]
		4  12/31/2014  284  Cases_Guinea  2730.0  [Cases, Guinea]
		----------
				 Date  Day  type_country  counts        str_split   type country
		0    1/5/2015  289  Cases_Guinea  2776.0  [Cases, Guinea]  Cases  Guinea
		1    1/4/2015  288  Cases_Guinea  2775.0  [Cases, Guinea]  Cases  Guinea
		2    1/3/2015  287  Cases_Guinea  2769.0  [Cases, Guinea]  Cases  Guinea
		3    1/2/2015  286  Cases_Guinea     NaN  [Cases, Guinea]  Cases  Guinea
		4  12/31/2014  284  Cases_Guinea  2730.0  [Cases, Guinea]  Cases  Guinea

Excellent job! It is a lot easier to make sense of the data now!  
You have finished the chapter "Tidying data for analysis"!  		
		
---