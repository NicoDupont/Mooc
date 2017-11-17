10/2017  
Datcamp - Merging DataFrames with pandas  

---

# Part 2 : Concatenating data 

Having learned how to import multiple DataFrames and share information using Indexes, in this chapter you'll learn how to perform database-style operations to combine DataFrames. In particular, you'll learn about appending and concatenating DataFrames while working with a variety of real-world datasets.  
 
## Appending Series with nonunique Indices  

The Series bronze and silver, which have been printed in the IPython Shell, represent the 5 countries that won the most bronze and silver Olympic medals respectively between 1896 & 2008. The Indexes of both Series are called Country and the values are the corresponding number of medals won.  

If you were to run the command combined = bronze.append(silver), how many rows would combined have? And how many rows would combined.loc['United States'] return? Find out for yourself by running these commands in the IPython Shell.  

### Possible Answers :  => 2  

 - 1 combined has 5 rows and combined.loc['United States'] is empty (0 rows).
 - 2 combined has 10 rows and combined.loc['United States'] has 2 rows.
 - 3 combined has 6 rows and combined.loc['United States'] has 1 row.
 - 4 combined has 5 rows and combined.loc['United States'] has 2 rows. 

```python
bronze
Country
United States     1052.0
Soviet Union       584.0
United Kingdom     505.0
France             475.0
Germany            454.0
Name: Total, dtype: float64

silver
Country
United States     1195.0
Soviet Union       627.0
United Kingdom     591.0
France             461.0
Italy              394.0
Name: Total, dtype: float64

In [1]: combined = bronze.append(silver)

In [2]: combined;shape
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    combined;shape
NameError: name 'shape' is not defined

In [3]: combined.shape
Out[3]: (10,)

In [4]: combined.loc['United States']
Out[4]: 
Country
United States    1052.0
United States    1195.0
Name: Total, dtype: float64
```

### Results :  

Correct! The combined Series has 10 rows and combined.loc['United States'] has two rows, since the index value 'United States' occurs in both series bronze and silver.  

---


## Appending pandas Series  

In this exercise, you'll load sales data from the months January, February, and March into DataFrames. Then, you'll extract Series with the 'Units' column from each and append them together with method chaining using .append().  

To check that the stacking worked, you'll print slices from these Series, and finally, you'll add the result to figure out the total units sold in the first quarter.  

### Instructions :

 - Read the files 'sales-jan-2015.csv', 'sales-feb-2015.csv' and 'sales-mar-2015.csv' into the DataFrames jan, feb, and mar respectively.
 - Use parse_dates=True and index_col='Date'.
 - Extract the 'Units' column of jan, feb, and mar to create the Series jan_units, feb_units, and mar_units respectively.
 - Construct the Series quarter1 by appending feb_units to jan_units and then appending mar_units to the result. Use chained calls to the .append() method to do this.
 - Verify that quarter1 has the individual Series stacked vertically. To do this:
 - Print the slice containing rows from jan 27, 2015 to feb 2, 2015.
 - Print the slice containing rows from feb 26, 2015 to mar 7, 2015.
 - Compute and print the total number of units sold from the Series quarter1. This has been done for you, so hit 'Submit Answer' to see the result!

```python
# Import pandas
import pandas as pd

# Load 'sales-jan-2015.csv' into a DataFrame: jan
jan = pd.read_csv('sales-jan-2015.csv',parse_dates=True,index_col='Date')

# Load 'sales-feb-2015.csv' into a DataFrame: feb
feb = pd.read_csv('sales-feb-2015.csv',parse_dates=True,index_col='Date')

# Load 'sales-mar-2015.csv' into a DataFrame: mar
mar = pd.read_csv('sales-mar-2015.csv',parse_dates=True,index_col='Date')

# Extract the 'Units' column from jan: jan_units
jan_units = jan['Units']

# Extract the 'Units' column from feb: feb_units
feb_units = feb['Units']

# Extract the 'Units' column from mar: mar_units
mar_units = mar['Units']

# Append feb_units and then mar_units to jan_units: quarter1
quarter1 = jan_units.append(feb_units).append(mar_units)

# Print the first slice from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])

# Print the second slice from quarter1
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])

# Compute & print total sales in quarter1
print(quarter1.sum())
```

### Results :  

	<script.py> output:
		Date
		2015-01-27 07:11:55    18
		2015-02-02 08:33:01     3
		2015-02-02 20:54:49     9
		Name: Units, dtype: int64
		Date
		2015-02-26 08:57:45     4
		2015-02-26 08:58:51     1
		2015-03-06 10:11:45    17
		2015-03-06 02:03:56    17
		Name: Units, dtype: int64
		642

Well done! As you can see, appending pandas Series is very straightforward!  

---


## Concatenating pandas Series along row axis  

Having learned how to append Series, you'll now learn how to achieve the same result by concatenating Series instead. You'll continue to work with the sales data you've seen previously. This time, the DataFrames jan, feb, and mar have been pre-loaded.  

Your job is to use pd.concat() with a list of Series to achieve the same result that you would get by chaining calls to .append().  

You may be wondering about the difference between pd.concat() and pandas' .append() method. One way to think of the difference is that .append() is a specific case of a concatenation, while pd.concat() gives you more flexibility, as you'll see in later exercises.  

### Instructions :

 - Create an empty list called units. This has been done for you.
 - Use a for loop to iterate over [jan, feb, mar]:
 - In each iteration of the loop, append the 'Units' column of each DataFrame to units.
 - Concatenate the Series contained in the list units into a longer Series called quarter1 using pd.concat().
 - Specify the keyword argument axis='rows' to stack the Series vertically.
 - Verify that quarter1 has the individual Series stacked vertically by printing slices. This has been done for you, so hit 'Submit Answer' to see the result!

```python
# Initialize empty list: units
units = []

# Build the list of Series
for month in [jan, feb, mar]:
    units.append(month.Units)

# Concatenate the list: quarter1
quarter1 = pd.concat(units,axis='rows')

# Print slices from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])
```

### Results :  

	<script.py> output:
		Date
		2015-01-27 07:11:55    18
		2015-02-02 08:33:01     3
		2015-02-02 20:54:49     9
		Name: Units, dtype: int64
		Date
		2015-02-26 08:57:45     4
		2015-02-26 08:58:51     1
		2015-03-06 10:11:45    17
		2015-03-06 02:03:56    17
		Name: Units, dtype: int64

Great work! As in this exercise, you can achieve the same results as appending by concatenating along the row axis.  		
		
---


## Appending DataFrames with ignore_index  

In this exercise, you'll use the Baby Names Dataset (from data.gov) again. This time, both DataFrames names_1981 and names_1881 are loaded without specifying an Index column (so the default Indexes for both are RangeIndexes).  

You'll use the DataFrame .append() method to make a DataFrame combined_names. To distinguish rows from the original two DataFrames, you'll add a 'year' column to each with the year (1881 or 1981 in this case). In addition, you'll specify ignore_index=True so that the index values are not used along the concatenation axis. The resulting axis will instead be labeled 0, 1, ..., n-1, which is useful if you are concatenating objects where the concatenation axis does not have meaningful indexing information.  

### Instructions :

 - Create a 'year' column in the DataFrames names_1881 and names_1981, with values of 1881 and 1981 respectively. Recall that assigning a scalar value to a DataFrame column broadcasts that value throughout.
 - Create a new DataFrame called combined_names by appending the rows of names_1981 underneath the rows of names_1881. Specify the keyword argument ignore_index=True to make a new RangeIndex of unique integers for each row.
 - Print the shapes of all three DataFrames. This has been done for you.
 - Extract all rows from combined_names that have the name 'Morgan'. To do this, use the .loc[] accessor with an appropriate filter. The relevant column of combined_names here is 'name'.

```python
# Add 'year' column to names_1881 and names_1981
names_1881['year'] = 1881
names_1981['year'] = 1981
print(names_1881.head())

# Append names_1981 after names_1881 with ignore_index=True: combined_names
# combined_names = pd.concat([names_1881,names_1981],ignore_index=True)
combined_names = names_1881.append(names_1981,ignore_index=True)

# Print shapes of names_1981, names_1881, and combined_names
print(names_1981.shape)
print('-------------')
print(names_1881.shape)
print('-------------')
print(combined_names.shape)
print('-------------')
print(combined_names.head())
print('-------------')

# Print all rows that contain the name 'Morgan'
print(combined_names.loc[combined_names['name'] == 'Morgan'])
```

### Results :  

	<script.py> output:
				name gender  count  year
		0       Mary      F   6919  1881
		1       Anna      F   2698  1881
		2       Emma      F   2034  1881
		3  Elizabeth      F   1852  1881
		4   Margaret      F   1658  1881
		(19455, 4)
		-------------
		(1935, 4)
		-------------
		(21390, 4)
		-------------
				name gender  count  year
		0       Mary      F   6919  1881
		1       Anna      F   2698  1881
		2       Emma      F   2034  1881
		3  Elizabeth      F   1852  1881
		4   Margaret      F   1658  1881
		-------------
				 name gender  count  year
		1283   Morgan      M     23  1881
		2096   Morgan      F   1769  1981
		14390  Morgan      M    766  1981

---


## Concatenating pandas DataFrames along column axis  

The function pd.concat() can concatenate DataFrames horizontally as well as vertically (vertical is the default). To make the DataFrames stack horizontally, you have to specify the keyword argument axis=1 or axis='columns'.  

In this exercise, you'll use weather data with maximum and mean daily temperatures sampled at different rates (quarterly versus monthly). You'll concatenate the rows of both and see that, where rows are missing in the coarser DataFrame, null values are inserted in the concatenated DataFrame. This corresponds to an outer join (which you will explore in more detail in later exercises).  

The files 'quarterly_max_temp.csv' and 'monthly_mean_temp.csv' have been pre-loaded into the DataFrames weather_max and weather_mean respectively, and pandas has been imported as pd.  

### Instructions :

 - Create a new DataFrame called weather by concatenating the DataFrames weather_max and weather_mean horizontally.
	- Pass the DataFrames to pd.concat() as a list and specify the keyword argument axis=1 to stack them horizontally.
 - Print the new DataFrame weather.

```python
# Concatenate weather_max and weather_mean horizontally: weather
weather = pd.concat([weather_max,weather_mean],axis=1)

# Print weather
print(weather)
```

### Results :  

	<script.py> output:
			 Max TemperatureF  Mean TemperatureF
		Apr              89.0          53.100000
		Aug               NaN          70.000000
		Dec               NaN          34.935484
		Feb               NaN          28.714286
		Jan              68.0          32.354839
		Jul              91.0          72.870968
		Jun               NaN          70.133333
		Mar               NaN          35.000000
		May               NaN          62.612903
		Nov               NaN          39.800000
		Oct              84.0          55.451613
		Sep               NaN          63.766667
		
Well done! This is where you start to see the advantages of concatenating over appending.  
		
---


## Reading multiple files to build a DataFrame  

It is often convenient to build a large DataFrame by parsing many files as DataFrames and concatenating them all at once. You'll do this here with three files, but, in principle, this approach can be used to combine data from dozens or hundreds of files.  

Here, you'll work with DataFrames compiled from The Guardian's Olympic medal dataset.  

pandas has been imported as pd and two lists have been pre-loaded: An empty list called medals, and medal_types, which contains the strings 'bronze', 'silver', and 'gold'.  

### Instructions :

 - Iterate over medal_types in the for loop.
 - Inside the for loop:
	 - Create file_name using string interpolation with the loop variable medal. This has been done for you. The expression "%s_top5.csv" % medal evaluates as a string with the value of medal replacing %s in the format string.
	 - Create the list of column names called columns. This has been done for you.
	 - Read file_name into a DataFrame called medal_df. Specify the keyword arguments header=0, index_col='Country', and names=columns to get the correct row and column Indexes.
	 - Append medal_df to medals using the list .append() method.
 - Concatenate the list of DataFrames medals horizontally (using axis='columns') to create a single DataFrame called medals. Print it in its entirety.

```python
for medal in medal_types:

    # Create the file name: file_name
    file_name = "%s_top5.csv" % medal
    
    # Create list of column names: columns
    columns = ['Country', medal]
    
    # Read file_name into a DataFrame: df
    medal_df = pd.read_csv(file_name,header=0,index_col='Country',names=columns)
    print(medal_df.head(6))
    print('---------------')
    # Append medal_df to medals
    medals.append(medal_df)

# Concatenate medals horizontally: medals
medals = pd.concat(medals,axis='columns')

# Print medals
print(medals)
```

### Results :  

	<script.py> output:
						bronze
		Country               
		United States   1052.0
		Soviet Union     584.0
		United Kingdom   505.0
		France           475.0
		Germany          454.0
		---------------
						silver
		Country               
		United States   1195.0
		Soviet Union     627.0
		United Kingdom   591.0
		France           461.0
		Italy            394.0
		---------------
						  gold
		Country               
		United States   2088.0
		Soviet Union     838.0
		United Kingdom   498.0
		Italy            460.0
		Germany          407.0
		---------------
						bronze  silver    gold
		France           475.0   461.0     NaN
		Germany          454.0     NaN   407.0
		Italy              NaN   394.0   460.0
		Soviet Union     584.0   627.0   838.0
		United Kingdom   505.0   591.0   498.0
		United States   1052.0  1195.0  2088.0

Fantastic! Being able to build DataFrames from multiple files like this can be incredibly useful.  		
		
---

## Concatenating vertically to get MultiIndexed rows  

When stacking a sequence of DataFrames vertically, it is sometimes desirable to construct a MultiIndex to indicate the DataFrame from which each row originated. This can be done by specifying the keys parameter in the call to pd.concat(), which generates a hierarchical index with the labels from keys as the outermost index label. So you don't have to rename the columns of each DataFrame as you load it. Instead, only the Index column needs to be specified.  

Here, you'll continue working with DataFrames compiled from The Guardian's Olympic medal dataset. Once again, pandas has been imported as pd and two lists have been pre-loaded: An empty list called medals, and medal_types, which contains the strings 'bronze', 'silver', and 'gold'.  

### Instructions :

 - Within the for loop:
	 - Read file_name into a DataFrame called medal_df. Specify the index to be 'Country'.
	 - Append medal_df to medals.
 - Concatenate the list of DataFrames medals into a single DataFrame called medals. Be sure to use the keyword argument keys=['bronze', 'silver', 'gold'] to create a vertically stacked DataFrame with a MultiIndex.
 - Print the new DataFrame medals. This has been done for you, so hit 'Submit Answer' to see the result! 

```python
for medal in medal_types:

    file_name = "%s_top5.csv" % medal
    
    # Read file_name into a DataFrame: medal_df
    medal_df = pd.read_csv(file_name,index_col='Country')
    
    # Append medal_df to medals
    medals.append(medal_df)
    
# Concatenate medals: medals
medals = pd.concat(medals,keys=['bronze', 'silver', 'gold'])

# Print medals in entirety
print(medals)
```

### Results :  

	<script.py> output:
								Total
			   Country               
		bronze United States   1052.0
			   Soviet Union     584.0
			   United Kingdom   505.0
			   France           475.0
			   Germany          454.0
		silver United States   1195.0
			   Soviet Union     627.0
			   United Kingdom   591.0
			   France           461.0
			   Italy            394.0
		gold   United States   2088.0
			   Soviet Union     838.0
			   United Kingdom   498.0
			   Italy            460.0
			   Germany          407.0

---


## Slicing MultiIndexed DataFrames  

This exercise picks up where the last ended (again using The Guardian's Olympic medal dataset).  

You are provided with the MultiIndexed DataFrame as produced at the end of the preceding exercise. Your task is to sort the DataFrame and to use the pd.IndexSlice to extract specific slices. Check out this exercise from Manipulating DataFrames with pandas to refresh your memory on how to deal with MultiIndexed DataFrames.  

pandas has been imported for you as pd and the DataFrame medals is already in your namespace.  

### Instructions :

 - Create a new DataFrame medals_sorted with the entries of medals sorted. Use .sort_index(level=0) to ensure the Index is sorted suitably.
 - Print the number of bronze medals won by Germany and all of the silver medal data. This has been done for you.
 - Create an alias for pd.IndexSlice called idx. A slicer pd.IndexSlice is required when slicing on the inner level of a MultiIndex.
 - Slice all the data on medals won by the United Kingdom. To do this, use the .loc[] accessor with idx[:,'United Kingdom'], :.

```python
# Sort the entries of medals: medals_sorted
medals_sorted = medals.sort_index(level=0)

# Print the number of Bronze medals won by Germany
print(medals_sorted.loc[('bronze','Germany')])

# Print data about silver medals
print(medals_sorted.loc['silver'])

# Create alias for pd.IndexSlice: idx
idx = pd.IndexSlice

# Print all the data on medals won by the United Kingdom
print(medals_sorted.loc[idx[:,'United Kingdom'], :])
```

### Results :  

	<script.py> output:
		Total    454.0
		Name: (bronze, Germany), dtype: float64
						 Total
		Country               
		France           461.0
		Italy            394.0
		Soviet Union     627.0
		United Kingdom   591.0
		United States   1195.0
							   Total
			   Country              
		bronze United Kingdom  505.0
		silver United Kingdom  591.0
		gold   United Kingdom  498.0

Great work! It looks like only the United States and the Soviet Union have won more Silver medals than the United Kingdom.  
		
---


## Concatenating horizontally to get MultiIndexed columns  

It is also possible to construct a DataFrame with hierarchically indexed columns. For this exercise, you'll start with pandas imported and a list of three DataFrames called dataframes. All three DataFrames contain 'Company', 'Product', and 'Units' columns with a 'Date' column as the index pertaining to sales transactions during the month of February, 2015. The first DataFrame describes Hardware transactions, the second describes Software transactions, and the third, Service transactions.  

Your task is to concatenate the DataFrames horizontally and to create a MultiIndex on the columns. From there, you can summarize the resulting DataFrame and slice some information from it.  

### Instructions :

 - Construct a new DataFrame february with MultiIndexed columns by concatenating the list dataframes.
 - Use axis=1 to stack the DataFrames horizontally and the keyword argument keys=['Hardware', 'Software', 'Service'] to construct a hierarchical Index from each DataFrame.
 - Print summary information from the new DataFrame february using the .info() method. This has been done for you.
 - Create an alias called idx for pd.IndexSlice.
 - Extract a slice called slice_2_8 from february (using .loc[] & idx) that comprises rows between Feb. 2, 2015 to Feb. 8, 2015 from columns under 'Company'.
 - Print the slice_2_8. This has been done for you, so hit 'Submit Answer' to see the sliced data! 

```python
# Concatenate dataframes: february
february = pd.concat(dataframes,axis=1,keys=['Hardware', 'Software', 'Service'])

# Print february.info()
print(february.info())
print('----------------')
print(february.head())
print('----------------')

# Assign pd.IndexSlice: idx
idx = pd.IndexSlice

# Create the slice: slice_2_8
slice_2_8 = february.loc['Feb. 2, 2015':'Feb. 8, 2015', idx[:, 'Company']]

# Print slice_2_8
print(slice_2_8)

```

### Results :  

	<script.py> output:
		<class 'pandas.core.frame.DataFrame'>
		DatetimeIndex: 20 entries, 2015-02-02 08:33:01 to 2015-02-26 08:58:51
		Data columns (total 9 columns):
		(Hardware, Company)    5 non-null object
		(Hardware, Product)    5 non-null object
		(Hardware, Units)      5 non-null float64
		(Software, Company)    9 non-null object
		(Software, Product)    9 non-null object
		(Software, Units)      9 non-null float64
		(Service, Company)     6 non-null object
		(Service, Product)     6 non-null object
		(Service, Units)       6 non-null float64
		dtypes: float64(3), object(6)
		memory usage: 1.6+ KB
		None
		----------------
									Hardware                   Software            \
									 Company   Product Units    Company   Product   
		Date                                                                        
		2015-02-02 08:33:01              NaN       NaN   NaN      Hooli  Software   
		2015-02-02 20:54:49        Mediacore  Hardware   9.0        NaN       NaN   
		2015-02-03 14:14:18              NaN       NaN   NaN    Initech  Software   
		2015-02-04 15:36:29              NaN       NaN   NaN  Streeplex  Software   
		2015-02-04 21:52:45  Acme Coporation  Hardware  14.0        NaN       NaN   
		
								  Service                
							Units Company Product Units  
		Date                                             
		2015-02-02 08:33:01   3.0     NaN     NaN   NaN  
		2015-02-02 20:54:49   NaN     NaN     NaN   NaN  
		2015-02-03 14:14:18  13.0     NaN     NaN   NaN  
		2015-02-04 15:36:29  13.0     NaN     NaN   NaN  
		2015-02-04 21:52:45   NaN     NaN     NaN   NaN  
		----------------
									Hardware         Software Service
									 Company          Company Company
		Date                                                         
		2015-02-02 08:33:01              NaN            Hooli     NaN
		2015-02-02 20:54:49        Mediacore              NaN     NaN
		2015-02-03 14:14:18              NaN          Initech     NaN
		2015-02-04 15:36:29              NaN        Streeplex     NaN
		2015-02-04 21:52:45  Acme Coporation              NaN     NaN
		2015-02-05 01:53:06              NaN  Acme Coporation     NaN
		2015-02-05 22:05:03              NaN              NaN   Hooli
		2015-02-07 22:58:10  Acme Coporation              NaN     NaN

		
Excellent work! Working with MultiIndexes and MultiIndexed columns can seem tricky at first, but with practice, it will become second nature.  
		
---


## Concatenating DataFrames from a dict  

You're now going to revisit the sales data you worked with earlier in the chapter. Three DataFrames jan, feb, and mar have been pre-loaded for you. Your task is to aggregate the sum of all sales over the 'Company' column into a single DataFrame. You'll do this by constructing a dictionary of these DataFrames and then concatenating them.  

### Instructions :

 - Create a list called month_list consisting of the tuples ('january', jan), ('february', feb), and ('march', mar).
 - Create an empty dictionary called month_dict.
 - Inside the for loop:
	- Group month_data by 'Company' and use .sum() to aggregate.
 - Construct a new DataFrame called sales by concatenating the DataFrames stored in month_dict.
 - Create an alias for pd.IndexSlice and print all sales by 'Mediacore'. This has been done for you, so hit 'Submit Answer' to see the result! 

```python
# Make the list of tuples: month_list
month_list = [('january', jan),('february', feb),('march', mar)]

# Create an empty dictionary: month_dict
month_dict = {}

for month_name, month_data in month_list:

    # Group month_data: month_dict[month_name]
    month_dict[month_name] = month_data.groupby('Company').sum()

# Concatenate data in month_dict: sales
sales = pd.concat(month_dict)

# Print sales
print(sales)

# Print all sales by Mediacore
idx = pd.IndexSlice
print(sales.loc[idx[:, 'Mediacore'], :])
```

### Results :  

	<script.py> output:
								  Units
				 Company               
		february Acme Coporation     34
				 Hooli               30
				 Initech             30
				 Mediacore           45
				 Streeplex           37
		january  Acme Coporation     76
				 Hooli               70
				 Initech             37
				 Mediacore           15
				 Streeplex           50
		march    Acme Coporation      5
				 Hooli               37
				 Initech             68
				 Mediacore           68
				 Streeplex           40
							Units
				 Company         
		february Mediacore     45
		january  Mediacore     15
		march    Mediacore     68

Well done! Now that you've mastered of the basics of concatenating your data, it's time to learn about different types of joins!  

---


## Concatenating DataFrames with inner join  

Here, you'll continue working with DataFrames compiled from The Guardian's Olympic medal dataset.  

The DataFrames bronze, silver, and gold have been pre-loaded for you.  

Your task is to compute an inner join.  

### Instructions :

 - Construct a list of DataFrames called medal_list with entries bronze, silver, and gold.
 - Concatenate medal_list horizontally with an inner join to create medals.
	 - Use the keyword argument keys=['bronze', 'silver', 'gold'] to yield suitable hierarchical indexing.
	 - Use axis=1 to get horizontal concatenation.
	 - Use join='inner' to keep only rows that share common index labels.
 - Print the new DataFrame medals. 

```python
# Create the list of DataFrames: medal_list
medal_list = [bronze,silver,gold]

# Concatenate medal_list horizontally using an inner join: medals
medals = pd.concat(medal_list,axis=1,join='inner',keys=['bronze', 'silver', 'gold'])

# Print medals
print(medals)

```

### Results :  

	<script.py> output:
						bronze  silver    gold
						 Total   Total   Total
		Country                               
		United States   1052.0  1195.0  2088.0
		Soviet Union     584.0   627.0   838.0
		United Kingdom   505.0   591.0   498.0

Well done! France, Italy, and Germany got dropped as part of the join since they are not present in each of bronze, silver, and gold. Therefore, the final DataFrame has only the United States, Soviet Union, and United Kingdom.  
		
---


## Resampling & concatenating DataFrames with inner join  

In this exercise, you'll compare the historical 10-year GDP (Gross Domestic Product) growth in the US and in China. The data for the US starts in 1947 and is recorded quarterly; by contrast, the data for China starts in 1966 and is recorded annually.  

You'll need to use a combination of resampling and an inner join to align the index labels. You'll need an appropriate offset alias for resampling, and the method .resample() must be chained with some kind of aggregation method (.pct_change() and .last() in this case).  

pandas has been imported as pd, and the DataFrames china and us have been pre-loaded, with the output of china.head() and us.head() printed in the IPython Shell.  

### Instructions :

 - Make a new DataFrame china_annual by resampling the DataFrame china with .resample('A') (i.e., with annual frequency) and chaining two method calls:
 - Chain .pct_change(10) as an aggregation method to compute the percentage change with an offset of ten years.
 - Chain .dropna() to eliminate rows containing null values.
 - Make a new DataFrame us_annual by resampling the DataFrame us exactly as you resampled china.
 - Concatenate china_annual and us_annual to construct a DataFrame called gdp. Use join='inner' to perform an inner join and use axis=1 to concatenate horizontally.
 - Print the result of resampling gdp every decade (i.e., using .resample('10A')) and aggregating with the method .last(). This has been done for you, so hit 'Submit Answer' to see the result!

```python
# Resample and tidy china: china_annual
china_annual = china.resample('A').pct_change(10).dropna()

# Resample and tidy us: us_annual
us_annual = us.resample('A').pct_change(10).dropna()

# Concatenate china_annual and us_annual: gdp
gdp = pd.concat([china_annual,us_annual],axis=1,join='inner')

# Resample gdp and print
print(gdp.resample('10A').last())
```

### Results :  

					China
	Year                 
	1961-01-01  49.557050
	1962-01-01  46.685179
	1963-01-01  50.097303
	1964-01-01  59.062255
	1965-01-01  69.709153
				   US
	Year             
	1947-04-01  246.3
	1947-07-01  250.1
	1947-10-01  260.3
	1948-01-01  266.2
	1948-04-01  272.9

	<script.py> output:
					   China        US
		Year                          
		1971-12-31  0.988860  1.073188
		1981-12-31  0.972048  1.749631
		1991-12-31  0.962528  0.922811
		2001-12-31  2.492511  0.720398
		2011-12-31  4.623958  0.460947
		2021-12-31  3.789936  0.377506

Great work! It looks like the 10 year GDP growth of China has been higher than the US since the 1990s.  

---