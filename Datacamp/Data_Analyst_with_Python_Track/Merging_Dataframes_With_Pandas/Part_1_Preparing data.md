10/2017  
Datcamp - Preparing data   

---

Course Description  
As a Data Scientist, you'll often find that the data you need is not in a single file. It may be spread across a number of text files, spreadsheets, or databases. You want to be able to import the data of interest as a collection of DataFrames and figure out how to combine them to answer your central questions. This course is all about the act of combining, or merging, DataFrames, an essential part of any working Data Scientist's toolbox. You'll hone your pandas skills by learning how to organize, reshape, and aggregate multiple data sets to answer your specific questions.   
 
# Part 1 : Preparing data    


## Reading DataFrames from multiple files

When data is spread among several files, you usually invoke pandas' read_csv() (or a similar data import function) multiple times to load the data into several DataFrames.

The data files for this example have been derived from a list of Olympic medals awarded between 1896 & 2008 compiled by the Guardian.

The column labels of each DataFrame are NOC, Country, & Total where NOC is a three-letter code for the name of the country and Total is the number of medals of that type won (bronze, silver, or gold).

### Instructions :

- Import pandas as pd.
- Read the file 'Bronze.csv' into a DataFrame called bronze.
- Read the file 'Silver.csv' into a DataFrame called silver.
- Read the file 'Gold.csv' into a DataFrame called gold.
- Print the first 5 rows of the DataFrame gold. This has been done for you, so hit 'Submit Answer' to see the results.

```python
# Import pandas
import pandas as pd

# Read 'Bronze.csv' into a DataFrame: bronze
bronze = pd.read_csv('Bronze.csv')

# Read 'Silver.csv' into a DataFrame: silver
silver = pd.read_csv('Silver.csv')

# Read 'Gold.csv' into a DataFrame: gold
gold = pd.read_csv('Gold.csv')

# Print the first five rows of gold
print(gold.head())
```

### Results :  

	<script.py> output:
	       NOC         Country   Total
	    0  USA   United States  2088.0
	    1  URS    Soviet Union   838.0
	    2  GBR  United Kingdom   498.0
	    3  FRA          France   378.0
	    4  GER         Germany   407.0

---


## Reading DataFrames from multiple files in a loop

As you saw in the video, loading data from multiple files into DataFrames is more efficient in a loop or a list comprehension.  

Notice that this approach is not restricted to working with CSV files. That is, even if your data comes in other formats, as long as pandas has a suitable data import function, you can apply a loop or comprehension to generate a list of DataFrames imported from the source files.  

Here, you'll continue working with The Guardian's Olympic medal dataset.  

### Instructions :

- Create a list of file names called filenames with three strings 'Gold.csv', 'Silver.csv', & 'Bronze.csv'. This has been done for you.
- Use a for loop to create another list called dataframes containing the three DataFrames loaded from filenames:
	- Iterate over filenames.
	- Read each CSV file in filenames into a DataFrame and append it to dataframes by using pd.read_csv() inside a call to .append().
- Print the first 5 rows of the first DataFrame of the list dataframes. This has been done for you, so hit 'Submit Answer' to see the results.


```python
# Import pandas
import pandas as pd

# Create the list of file names: filenames
filenames = ['Gold.csv', 'Silver.csv', 'Bronze.csv']

# Create the list of three DataFrames: dataframes
dataframes = []
for filename in filenames:
    dataframes.append(pd.read_csv(filename))

# Print top 5 rows of 1st DataFrame in dataframes
print(dataframes[0].head())
```

### Results :  

	<script.py> output:
		   NOC         Country   Total
		0  USA   United States  2088.0
		1  URS    Soviet Union   838.0
		2  GBR  United Kingdom   498.0
		3  FRA          France   378.0
		4  GER         Germany   407.0

Great work! When you are dealing with multiple csv files like this, it is more efficient to read them into DataFrames using a loop.  

---

## Combining DataFrames from multiple data files  

In this exercise, you'll combine the three DataFrames from earlier exercises - gold, silver, & bronze - into a single DataFrame called medals. The approach you'll use here is clumsy. Later on in the course, you'll see various powerful methods that are frequently used in practice for concatenating or merging DataFrames.  

Remember, the column labels of each DataFrame are NOC, Country, and Total, where NOC is a three-letter code for the name of the country and Total is the number of medals of that type won.  

### Instructions :

 - Construct a copy of the DataFrame gold called medals using the .copy() method.
 - Create a list called new_labels with entries 'NOC', 'Country', & 'Gold'. This is the same as the column labels from gold with the column label 'Total' replaced by 'Gold'.
 - Rename the columns of medals by assigning new_labels to medals.columns.
 - Create new columns 'Silver' and 'Bronze' in medals using silver['Total'] & bronze['Total'].
 - Print the top 5 rows of the final DataFrame medals. This has been done for you, so hit 'Submit Answer' to see the result!

```python
# Import pandas
import pandas as pd

# Make a copy of gold: medals
medals = gold.copy()

# Create list of new column labels: new_labels
new_labels = ['NOC', 'Country', 'Gold']

# Rename the columns of medals using new_labels
medals.columns = new_labels

# Add columns 'Silver' & 'Bronze' to medals
medals['Silver'] = silver['Total']
medals['Bronze'] = bronze['Total']

print(silver.head())
print('-------------')
print(bronze.head())
print('-------------')
# Print the head of medals
print(medals.head())
```

### Results :  

	<script.py> output:
		   NOC         Country   Total
		0  USA   United States  1195.0
		1  URS    Soviet Union   627.0
		2  GBR  United Kingdom   591.0
		3  FRA          France   461.0
		4  GER         Germany   350.0
		-------------
		   NOC         Country   Total
		0  USA   United States  1052.0
		1  URS    Soviet Union   584.0
		2  GBR  United Kingdom   505.0
		3  FRA          France   475.0
		4  GER         Germany   454.0
		-------------
		   NOC         Country    Gold  Silver  Bronze
		0  USA   United States  2088.0  1195.0  1052.0
		1  URS    Soviet Union   838.0   627.0   584.0
		2  GBR  United Kingdom   498.0   591.0   505.0
		3  FRA          France   378.0   461.0   475.0
		4  GER         Germany   407.0   350.0   454.0

---

## Sorting DataFrame with the Index & columns  

It is often useful to rearrange the sequence of the rows of a DataFrame by sorting. You don't have to implement these yourself; the principal methods for doing this are .sort_index() and .sort_values().  

In this exercise, you'll use these methods with a DataFrame of temperature values indexed by month names. You'll sort the rows alphabetically using the Index and numerically using a column. Notice, for this data, the original ordering is probably most useful and intuitive: the purpose here is for you to understand what the sorting methods do.  

### Instructions :

 - Read 'monthly_max_temp.csv' into a DataFrame called weather1 with 'Month' as the index.
 - Sort the index of weather1 in alphabetical order using the .sort_index() method and store the result in weather2.
 - Sort the index of weather1 in reverse alphabetical order by specifying the additional keyword argument ascending=False inside .sort_index().
 - Use the .sort_values() method to sort weather1 in increasing numerical order according to the values of the column 'Max TemperatureF'.

```python
# Import pandas
import pandas as pd

# Read 'monthly_max_temp.csv' into a DataFrame: weather1
weather1 = pd.read_csv('monthly_max_temp.csv',index_col='Month')

# Print the head of weather1
print(weather1.head())
print('------------')
# Sort the index of weather1 in alphabetical order: weather2
weather2 = weather1.sort_index()

# Print the head of weather2
print(weather2.head())
print('------------')
# Sort the index of weather1 in reverse alphabetical order: weather3
weather3 = weather1.sort_index(ascending=False)

# Print the head of weather3
print(weather3.head())
print('------------')
# Sort weather1 numerically using the values of 'Max TemperatureF': weather4
weather4 = weather1.sort_values('Max TemperatureF')

# Print the head of weather4
print(weather4.head())
print('------------')
```

### Results :  

	<script.py> output:
			   Max TemperatureF
		Month                  
		Jan                  68
		Feb                  60
		Mar                  68
		Apr                  84
		May                  88
		------------
			   Max TemperatureF
		Month                  
		Apr                  84
		Aug                  86
		Dec                  68
		Feb                  60
		Jan                  68
		------------
			   Max TemperatureF
		Month                  
		Sep                  90
		Oct                  84
		Nov                  72
		May                  88
		Mar                  68
		------------
			   Max TemperatureF
		Month                  
		Feb                  60
		Jan                  68
		Mar                  68
		Dec                  68
		Nov                  72
		------------
			   Max TemperatureF
		Month                  
		Feb                  60
		Jan                  68
		Mar                  68
		Dec                  68
		Nov                  72

Good job! Being able to sort DataFrames is an important skill. When your DataFrames are sorted, it becomes easier to see how you can combine them.  		
		
---


## Reindexing DataFrame from a list  

Sorting methods are not the only way to change DataFrame Indexes. There is also the .reindex() method.  

In this exercise, you'll reindex a DataFrame of quarterly-sampled mean temperature values to contain monthly samples (this is an example of upsampling or increasing the rate of samples, which you may recall from the pandas Foundations course).  

The original data has the first month's abbreviation of the quarter (three-month interval) on the Index, namely Apr, Jan, Jul, and Sep. This data has been loaded into a DataFrame called weather1 and has been printed in its entirety in the IPython Shell. Notice it has only four rows (corresponding to the first month of each quarter) and that the rows are not sorted chronologically.  

You'll initially use a list of all twelve month abbreviations and subsequently apply the .ffill() method to forward-fill the null entries when upsampling. This list of month abbreviations has been pre-loaded as year.  

### Instructions :

 - Reorder the rows of weather1 using the .reindex() method with the list year as the argument, which contains the abbreviations for each month.
 - Reorder the rows of weather1 just as you did above, this time chaining the .ffill() method to replace the null values with the last preceding non-null value.

```python
# Import pandas
import pandas as pd

# Print weather1
print(weather1)
print('--------')

# Print the list year
print(year)
print('--------')

# Reindex weather1 using the list year: weather2
weather2 = weather1.reindex(year)

# Print weather2
print(weather2)
print('--------')

# Reindex weather1 using the list year with forward-fill: weather3
weather3 = weather1.reindex(year).ffill()

# Print weather3
print(weather3)
print('--------')
```

### Results :  

	<script.py> output:
			   Mean TemperatureF
		Month                   
		Apr            61.956044
		Jan            32.133333
		Jul            68.934783
		Oct            43.434783
		--------
		['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
		--------
			   Mean TemperatureF
		Month                   
		Jan            32.133333
		Feb                  NaN
		Mar                  NaN
		Apr            61.956044
		May                  NaN
		Jun                  NaN
		Jul            68.934783
		Aug                  NaN
		Sep                  NaN
		Oct            43.434783
		Nov                  NaN
		Dec                  NaN
		--------
			   Mean TemperatureF
		Month                   
		Jan            32.133333
		Feb            32.133333
		Mar            32.133333
		Apr            61.956044
		May            61.956044
		Jun            61.956044
		Jul            68.934783
		Aug            68.934783
		Sep            68.934783
		Oct            43.434783
		Nov            43.434783
		Dec            43.434783
		--------

Great work! Notice that values corresponding to months missing from weather1 are filled with NaN values in weather2. This does not happen in weather3, since you used forward-fill.  

---


## Reindexing using another DataFrame Index  

Another common technique is to reindex a DataFrame using the Index of another DataFrame. The DataFrame .reindex() method can accept the Index of a DataFrame or Series as input. You can access the Index of a DataFrame with its .index attribute.  

The Baby Names Dataset from data.gov summarizes counts of names (with genders) from births registered in the US since 1881. In this exercise, you will start with two baby-names DataFrames names_1981 and names_1881 loaded for you.  

The DataFrames names_1981 and names_1881 both have a MultiIndex with levels name and gender giving unique labels to counts in each row. If you're interested in seeing how the MultiIndexes were set up, names_1981 and names_1881 were read in using the following commands:  

```python
names_1981 = pd.read_csv('names1981.csv', header=None, names=['name','gender','count'], index_col=(0,1))
names_1881 = pd.read_csv('names1881.csv', header=None, names=['name','gender','count'], index_col=(0,1))
```

As you can see by looking at their shapes, which have been printed in the IPython Shell, the DataFrame corresponding to 1981 births is much larger, reflecting the greater diversity of names in 1981 as compared to 1881.  

Your job here is to use the DataFrame .reindex() and .dropna() methods to make a DataFrame common_names counting names from 1881 that were still popular in 1981.  

### Instructions :

 - Create a new DataFrame common_names by reindexing names_1981 using the Index of the DataFrame names_1881 of older names.
 - Print the shape of the new common_names DataFrame. This has been done for you. It should be the same as that of names_1881.
 - Drop the rows of common_names that have null counts using the .dropna() method. These rows correspond to names that fell out of fashion between 1881 & 1981.
 - Print the shape of the reassigned common_names DataFrame. This has been done for you, so hit 'Submit Answer' to see the result!

```python
# Import pandas
import pandas as pd

# Reindex names_1981 with index of names_1881: common_names
common_names = names_1981.reindex(names_1881.index)

# Print shape of common_names
print(common_names.shape)

# Drop rows with null counts: common_names
common_names = common_names.dropna()

# Print shape of new common_names
print(common_names.shape)
```

### Results : 

	Shape of names_1981 DataFrame: (19455, 1)
	Shape of names_1881 DataFrame: (1935, 1)

	<script.py> output:
		(1935, 1)
		(1587, 1) 

Excellent work! It looks like 348 names fell out of fashion between 1881 and 1981!  

---


## Loading and viewing your data

### Instructions :


```python
```

### Results :  

---


## Loading and viewing your data

### Instructions :


```python
```

### Results :  

---

## Loading and viewing your data

### Instructions :


```python
```

### Results :  

---

## Loading and viewing your data

### Instructions :


```python
```

### Results :  

---