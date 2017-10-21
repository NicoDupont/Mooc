10/2017  
Datcamp - Merging DataFrames with pandas  

---

# Part 3 : Merging data 

Here, you'll learn all about merging pandas DataFrames. You'll explore different techniques for merging, and learn about left joins, right joins, inner joins, and outer joins, as well as when to use which. You'll also learn about ordered merging, which is useful when you want to merge DataFrames whose columns have natural orderings, like date-time columns.  
 
## Merging company DataFrames   

Suppose your company has operations in several different cities under several different managers. The DataFrames revenue and managers contain partial information related to the company. That is, the rows of the city columns don't quite match in revenue and managers (the Mendocino branch has no revenue yet since it just opened and the manager of Springfield branch recently left the company).  

The DataFrames have been printed in the IPython Shell. If you were to run the command combined = pd.merge(revenue, managers, on='city'), how many rows would combined have?  

### Possible Answers :  

 - 0 rows.
 - 2 rows.
 - 3 rows.
 - 4 rows.

```python
          city  revenue
0       Austin      100
1       Denver       83
2  Springfield        4

        city   manager
0     Austin  Charlers
1     Denver      Joel
2  Mendocino     Brett

In [1]: combined = pd.merge(revenue, managers, on='city')

In [2]: combined;shape
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    combined;shape
NameError: name 'shape' is not defined

In [3]: combined.shape
Out[3]: (2, 3)
```

### Results :  

Correct! Since the default strategy for pd.merge() is an inner join, combined will have 2 rows.  

---

## Merging on a specific column    

This exercise follows on the last one with the DataFrames revenue and managers for your company. You expect your company to grow and, eventually, to operate in cities with the same name on different states. As such, you decide that every branch should have a numerical branch identifier. Thus, you add a branch_id column to both DataFrames. Moreover, new cities have been added to both the revenue and managers DataFrames as well. pandas has been imported as pd and both DataFrames are available in your namespace.  

At present, there should be a 1-to-1 relationship between the city and branch_id fields. In that case, the result of a merge on the city columns ought to give you the same output as a merge on the branch_id columns. Do they? Can you spot an ambiguity in one of the DataFrames?  

### Instructions :  

 - Using pd.merge(), merge the DataFrames revenue and managers on the 'city' column of each. Store the result as merge_by_city.
 - Print the DataFrame merge_by_city. This has been done for you.
 - Merge the DataFrames revenue and managers on the 'branch_id' column of each. Store the result as merge_by_id.
 - Print the DataFrame merge_by_id. This has been done for you, so hit 'Submit Answer' to see the result!

```python
# Merge revenue with managers on 'city': merge_by_city
merge_by_city = pd.merge(revenue,managers,on='city')

# Print merge_by_city
print(merge_by_city)
print('----------------')

# Merge revenue with managers on 'branch_id': merge_by_id
merge_by_id = pd.merge(revenue,managers,on='branch_id')

# Print merge_by_id
print(merge_by_id)
print('----------------')
```

### Results :  

	In [1]: merge_by_city = pd.merge(revenue,managers,on='city')

	In [2]: print(merge_by_city)
	   branch_id_x         city  revenue  branch_id_y   manager
	0           10       Austin      100           10  Charlers
	1           20       Denver       83           20      Joel
	2           30  Springfield        4           31     Sally
	3           47    Mendocino      200           47     Brett
	  File "script.py", line 13
		print('----------------'
							   ^
	SyntaxError: unexpected EOF while parsing

	<script.py> output:
		   branch_id_x         city  revenue  branch_id_y   manager
		0           10       Austin      100           10  Charlers
		1           20       Denver       83           20      Joel
		2           30  Springfield        4           31     Sally
		3           47    Mendocino      200           47     Brett
		----------------
		   branch_id     city_x  revenue     city_y   manager
		0         10     Austin      100     Austin  Charlers
		1         20     Denver       83     Denver      Joel
		2         47  Mendocino      200  Mendocino     Brett
		----------------

Well done! Notice that when you merge on 'city', the resulting DataFrame has a peculiar result: In row 2, the city Springfield has two different branch IDs. This is because there are actually two different cities named Springfield - one in the State of Illinois, and the other in Missouri. The revenue DataFrame has the one from Illinois, and the managers DataFrame has the one from Missouri. Consequently, when you merge on 'branch_id', both of these get dropped from the merged DataFrame.  

---

## Merging on columns with non-matching labels    

You continue working with the revenue & managers DataFrames from before. This time, someone has changed the field name 'city' to 'branch' in the managers table. Now, when you attempt to merge DataFrames, an exception is thrown:  

```python
>>> pd.merge(revenue, managers, on='city')
Traceback (most recent call last):
    ... <text deleted> ...
    pd.merge(revenue, managers, on='city')
    ... <text deleted> ...
KeyError: 'city'
```

Given this, it will take a bit more work for you to join or merge on the city/branch name. You have to specify the left_on and right_on parameters in the call to pd.merge().  

As before, pandas has been pre-imported as pd and the revenue and managers DataFrames are in your namespace. They have been printed in the IPython Shell so you can examine the columns prior to merging.  

Are you able to merge better than in the last exercise? How should the rows with Springfield be handled?  

### Instructions :  

 - Merge the DataFrames revenue and managers into a single DataFrame called combined using the 'city' and 'branch' columns from the appropriate DataFrames.
	- In your call to pd.merge(), you will have to specify the parameters left_on and right_on appropriately.
 - Print the new DataFrame combined.

```python
# Merge revenue & managers on 'city' & 'branch': combined
combined = pd.merge(revenue,managers,left_on='city',right_on='branch')

# Print combined
print(combined)
```

### Results :  

	   branch_id         city  revenue state
	0         10       Austin      100    TX
	1         20       Denver       83    CO
	2         30  Springfield        4    IL
	3         47    Mendocino      200    CA

			branch  branch_id   manager state
	0       Austin         10  Charlers    TX
	1       Denver         20      Joel    CO
	2    Mendocino         47     Brett    CA
	3  Springfield         31     Sally    MO

	<script.py> output:
		   branch_id_x         city  revenue state_x       branch  branch_id_y  \
		0           10       Austin      100      TX       Austin           10   
		1           20       Denver       83      CO       Denver           20   
		2           30  Springfield        4      IL  Springfield           31   
		3           47    Mendocino      200      CA    Mendocino           47   
		
			manager state_y  
		0  Charlers      TX  
		1      Joel      CO  
		2     Sally      MO  
		3     Brett      CA

Great work! It is important to pay attention to how columns are named in different DataFrames.  
		
---

## Merging on multiple columns    

Another strategy to disambiguate cities with identical names is to add information on the states in which the cities are located. To this end, you add a column called state to both DataFrames from the preceding exercises. Again, pandas has been pre-imported as pd and the revenue and managers DataFrames are in your namespace.  

Your goal in this exercise is to use pd.merge() to merge DataFrames using multiple columns (using 'branch_id', 'city', and 'state' in this case).  

Are you able to match all your company's branches correctly?  

### Instructions :  

 - Create a column called 'state' in the DataFrame revenue, consisting of the list ['TX','CO','IL','CA'].
 - Create a column called 'state' in the DataFrame managers, consisting of the list ['TX','CO','CA','MO'].
 - Merge the DataFrames revenue and managers using three columns :'branch_id', 'city', and 'state'. Pass them in as a list to the on paramater of pd.merge().

```python
# Add 'state' column to revenue: revenue['state']
revenue['state'] = ['TX','CO','IL','CA']

# Add 'state' column to managers: managers['state']
managers['state'] = ['TX','CO','CA','MO']

# Merge revenue & managers on 'branch_id', 'city', & 'state': combined
combined = pd.merge(revenue,managers,on=['branch_id','city', 'state'])

# Print combined
print(combined)
```

### Results :  

	<script.py> output:
		   branch_id       city  revenue state   manager
		0         10     Austin      100    TX  Charlers
		1         20     Denver       83    CO      Joel
		2         47  Mendocino      200    CA     Brett

---

## Joining by Index    

The DataFrames revenue and managers are displayed in the IPython Shell. Here, they are indexed by 'branch_id'.  

Choose the function call below that will join the DataFrames on their indexes and return 5 rows with index labels [10, 20, 30, 31, 47]. Explore each of them in the IPython Shell to get a better understanding of their functionality.  

### Possible Answers :  => 3 (1 not possible)   

 - pd.merge(revenue, managers, on='branch_id').
 - pd.merge(managers, revenue, how='left').
 - revenue.join(managers, lsuffix='_rev', rsuffix='_mng', how='outer').
 - managers.join(revenue, lsuffix='_mgn', rsuffix='_rev', how='left').

```python

```

### Results :  

					  city  revenue state
	branch_id                            
	10              Austin      100    TX
	20              Denver       83    CO
	30         Springfield        4    IL
	47           Mendocino      200    CA

					branch   manager state
	branch_id                             
	10              Austin  Charlers    TX
	20              Denver      Joel    CO
	47           Mendocino     Brett    CA
	31         Springfield     Sally    MO

	In [1]: print(pd.merge(managers, revenue, how='left'))
			branch   manager state       city  revenue
	0       Austin  Charlers    TX     Austin    100.0
	1       Denver      Joel    CO     Denver     83.0
	2    Mendocino     Brett    CA  Mendocino    200.0
	3  Springfield     Sally    MO        NaN      NaN

	In [2]: print(revenue.join(managers, lsuffix='_rev', rsuffix='_mng', how='outer'))
					  city  revenue state_rev       branch   manager state_mng
	branch_id                                                                 
	10              Austin    100.0        TX       Austin  Charlers        TX
	20              Denver     83.0        CO       Denver      Joel        CO
	30         Springfield      4.0        IL          NaN       NaN       NaN
	31                 NaN      NaN       NaN  Springfield     Sally        MO
	47           Mendocino    200.0        CA    Mendocino     Brett        CA

	In [3]: print(managers.join(revenue, lsuffix='_mgn', rsuffix='_rev', how='left'))
					branch   manager state_mgn       city  revenue state_rev
	branch_id                                                               
	10              Austin  Charlers        TX     Austin    100.0        TX
	20              Denver      Joel        CO     Denver     83.0        CO
	47           Mendocino     Brett        CA  Mendocino    200.0        CA
	31         Springfield     Sally        MO        NaN      NaN       NaN

	In [4]: print(pd.merge(revenue, managers, on='branch_id'))
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
		print(pd.merge(revenue, managers, on='branch_id'))
	  File "<stdin>", line 58, in merge
		copy=copy, indicator=indicator)
	  File "<stdin>", line 496, in __init__
		self.join_names) = self._get_merge_keys()
	  File "<stdin>", line 747, in _get_merge_keys
		right_keys.append(right[rk]._values)
	  File "<stdin>", line 2059, in __getitem__
		return self._getitem_column(key)
	  File "<stdin>", line 2066, in _getitem_column
		return self._get_item_cache(key)
	  File "<stdin>", line 1386, in _get_item_cache
		values = self._data.get(item)
	  File "<stdin>", line 3541, in get
		loc = self.items.get_loc(item)
	  File "<stdin>", line 2136, in get_loc
		return self._engine.get_loc(self._maybe_cast_indexer(key))
	  File "<stdin>", line 139, in pandas.index.IndexEngine.get_loc (pandas/index.c:4443)
	  File "<stdin>", line 161, in pandas.index.IndexEngine.get_loc (pandas/index.c:4289)
	  File "<stdin>", line 732, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:13733)
	  File "<stdin>", line 740, in pandas.hashtable.PyObjectHashTable.get_item (pandas/hashtable.c:13687)
	KeyError: 'branch_id'

Correct! This function call does indeed return 5 rows with index labels [10, 20, 30, 31, 47]  	
	
---

## Choosing a joining strategy    

Suppose you have two DataFrames: students (with columns 'StudentID', 'LastName', 'FirstName', and 'Major') and midterm_results (with columns 'StudentID', 'Q1', 'Q2', and 'Q3' for their scores on midterm questions).  

You want to combine the DataFrames into a single DataFrame grades, and be able to easily spot which students wrote the midterm and which didn't (their midterm question scores 'Q1', 'Q2', & 'Q3' should be filled with NaN values).  

You also want to drop rows from midterm_results in which the StudentID is not found in students.  

Which of the following strategies gives the desired result?  

### Possible Answers : => 1  

 - A left join: grades = pd.merge(students, midterm_results, how='left').
 - A right join: grades = pd.merge(students, midterm_results, how='right').
 - An inner join: grades = pd.merge(students, midterm_results, how='inner').
 - An outer join: grades = pd.merge(students, midterm_results, how='outer').

```python

```

### Results :  

Correct! A left join is indeed the right strategy here.  

---

## Left & right merging on multiple columns    

You now have, in addition to the revenue and managers DataFrames from prior exercises, a DataFrame sales that summarizes units sold from specific branches (identified by city and state but not branch_id).  

Once again, the managers DataFrame uses the label branch in place of city as in the other two DataFrames. Your task here is to employ left and right merges to preserve data and identify where data is missing.  

By merging revenue and sales with a right merge, you can identify the missing revenue values. Here, you don't need to specify left_on or right_on because the columns to merge on have matching labels.  

By merging sales and managers with a left merge, you can identify the missing manager. Here, the columns to merge on have conflicting labels, so you must specify left_on and right_on. In both cases, you're looking to figure out how to connect the fields in rows containing Springfield.  

pandas has been imported as pd and the three DataFrames revenue, managers, and sales have been pre-loaded. They have been printed for you to explore in the IPython Shell.  

### Instructions :  

 - Execute a right merge using pd.merge() with revenue and sales to yield a new DataFrame revenue_and_sales.
	- Use how='right' and on=['city', 'state'].
 - Print the new DataFrame revenue_and_sales. This has been done for you.
 - Execute a left merge with sales and managers to yield a new DataFrame sales_and_managers.
	- Use how='left', left_on=['city', 'state'], and right_on=['branch', 'state].
 - Print the new DataFrame sales_and_managers. This has been done for you, so hit 'Submit Answer' to see the result!

```python
# Merge revenue and sales: revenue_and_sales
revenue_and_sales = pd.merge(revenue,sales,on=['city', 'state'],how='right')

# Print revenue_and_sales
print(revenue_and_sales)

# Merge sales and managers: sales_and_managers
sales_and_managers = pd.merge(sales,managers,how='left',left_on=['city','state'],right_on=['branch','state'])

# Print sales_and_managers
print(sales_and_managers)
```

### Results :  

	<script.py> output:
		   branch_id         city  revenue state  units
		0       10.0       Austin    100.0    TX      2
		1       20.0       Denver     83.0    CO      4
		2       30.0  Springfield      4.0    IL      1
		3       47.0    Mendocino    200.0    CA      1
		4        NaN  Springfield      NaN    MO      5
				  city state  units       branch  branch_id   manager
		0    Mendocino    CA      1    Mendocino       47.0     Brett
		1       Denver    CO      4       Denver       20.0      Joel
		2       Austin    TX      2       Austin       10.0  Charlers
		3  Springfield    MO      5  Springfield       31.0     Sally
		4  Springfield    IL      1          NaN        NaN       NaN

Well done! This is a good way to retain both entries of Springfield.  		
		
---

## Merging DataFrames with outer join    

This exercise picks up where the previous one left off. The DataFrames revenue, managers, and sales are pre-loaded into your namespace (and, of course, pandas is imported as pd). Moreover, the merged DataFrames revenue_and_sales and sales_and_managers have been pre-computed exactly as you did in the previous exercise.  

The merged DataFrames contain enough information to construct a DataFrame with 5 rows with all known information correctly aligned and each branch listed only once. You will try to merge the merged DataFrames on all matching keys (which computes an inner join by default). You can compare the result to an outer join and also to an outer join with restricted subset of columns as keys.  

### Instructions :  

 - Merge sales_and_managers with revenue_and_sales. Store the result as merge_default.
 - Print merge_default. This has been done for you.
 - Merge sales_and_managers with revenue_and_sales using how='outer'. Store the result as merge_outer.
 - Print merge_outer. This has been done for you.
 - Merge sales_and_managers with revenue_and_sales only on ['city','state'] using an outer join. Store the result as merge_outer_on and hit 'Submit Answer' to see what the merged DataFrames look like!

```python
# Perform the first merge: merge_default
merge_default = pd.merge(sales_and_managers,revenue_and_sales)

# Print merge_default
print(merge_default)
print('-------------------')

# Perform the second merge: merge_outer
merge_outer = pd.merge(sales_and_managers,revenue_and_sales,how='outer')

# Print merge_outer
print(merge_outer)
print('-------------------')

# Perform the third merge: merge_outer_on
merge_outer_on = pd.merge(sales_and_managers,revenue_and_sales,how='outer',on=['city','state'])

# Print merge_outer_on
print(merge_outer_on)
print('-------------------')
```

### Results :  

	<script.py> output:
		    city state  units     branch  branch_id   manager  revenue
	    0  Mendocino    CA      1  Mendocino       47.0     Brett    200.0
	    1     Denver    CO      4     Denver       20.0      Joel     83.0
	    2     Austin    TX      2     Austin       10.0  Charlers    100.0
	    -------------------
		      city state  units       branch  branch_id   manager  revenue
	    0    Mendocino    CA      1    Mendocino       47.0     Brett    200.0
	    1       Denver    CO      4       Denver       20.0      Joel     83.0
	    2       Austin    TX      2       Austin       10.0  Charlers    100.0
	    3  Springfield    MO      5  Springfield       31.0     Sally      NaN
	    4  Springfield    IL      1          NaN        NaN       NaN      NaN
	    5  Springfield    IL      1          NaN       30.0       NaN      4.0
	    6  Springfield    MO      5          NaN        NaN       NaN      NaN
	    -------------------
		      city state  units_x       branch  branch_id_x   manager  \
	    0    Mendocino    CA        1    Mendocino         47.0     Brett   
	    1       Denver    CO        4       Denver         20.0      Joel   
	    2       Austin    TX        2       Austin         10.0  Charlers   
	    3  Springfield    MO        5  Springfield         31.0     Sally   
	    4  Springfield    IL        1          NaN          NaN       NaN   
	    
	       branch_id_y  revenue  units_y  
	    0         47.0    200.0        1  
	    1         20.0     83.0        4  
	    2         10.0    100.0        2  
	    3          NaN      NaN        5  
	    4         30.0      4.0        1  
	    -------------------

Fantastic work! Notice how the default merge drops the Springfield rows, while the default outer merge includes them twice.  

---

## Using merge_ordered()    

This exercise uses pre-loaded DataFrames austin and houston that contain weather data from the cities Austin and Houston respectively. They have been printed in the IPython Shell for you to examine.  

Weather conditions were recorded on separate days and you need to merge these two DataFrames together such that the dates are ordered. To do this, you'll use pd.merge_ordered(). After you're done, note the order of the rows before and after merging.  

### Instructions :  

 - Perform an ordered merge on austin and houston using pd.merge_ordered(). Store the result as tx_weather.
 - Print tx_weather. You should notice that the rows are sorted by the date but it is not possible to tell which observation came from which city.
 - Perform another ordered merge on austin and houston.
	 - This time, specify the keyword arguments on='date' and suffixes=['_aus','_hus'] so that the rows can be distinguished. Store the result as tx_weather_suff.
 - Print tx_weather_suff to examine its contents. This has been done for you.
 - Perform a third ordered merge on austin and houston.
	 - This time, in addition to the on and suffixes parameters, specify the keyword argument fill_method='ffill' to use forward-filling to replace NaN entries with the most recent non-null entry, and hit 'Submit Answer' to examine the contents of the merged DataFrames!

```python
# Perform the first ordered merge: tx_weather
tx_weather = pd.merge_ordered(austin,houston)

# Print tx_weather
print(tx_weather)
print('--------------------')

# Perform the second ordered merge: tx_weather_suff
tx_weather_suff = pd.merge_ordered(austin,houston,on='date',suffixes=['_aus','_hus'])

# Print tx_weather_suff
print(tx_weather_suff)
print('--------------------')

# Perform the third ordered merge: tx_weather_ffill
tx_weather_ffill = pd.merge_ordered(austin,houston,on='date',suffixes=['_aus','_hus'],fill_method='ffill')

# Print tx_weather_ffill
print(tx_weather_ffill)
print('--------------------')
```

### Results :  

	austin
		date ratings
	0 2016-01-01  Cloudy
	1 2016-02-08  Cloudy
	2 2016-01-17   Sunny

	houston
		date ratings
	0 2016-01-04   Rainy
	1 2016-01-01  Cloudy
	2 2016-03-01   Sunny

	<script.py> output:
		    date ratings
	    0 2016-01-01  Cloudy
	    1 2016-01-04   Rainy
	    2 2016-01-17   Sunny
	    3 2016-02-08  Cloudy
	    4 2016-03-01   Sunny
	    --------------------
		    date ratings_aus ratings_hus
	    0 2016-01-01      Cloudy      Cloudy
	    1 2016-01-04         NaN       Rainy
	    2 2016-01-17       Sunny         NaN
	    3 2016-02-08      Cloudy         NaN
	    4 2016-03-01         NaN       Sunny
	    --------------------
		    date ratings_aus ratings_hus
	    0 2016-01-01      Cloudy      Cloudy
	    1 2016-01-04      Cloudy       Rainy
	    2 2016-01-17       Sunny       Rainy
	    3 2016-02-08      Cloudy       Rainy
	    4 2016-03-01      Cloudy       Sunny
	    --------------------
Well done! Notice how after using a fill method, there are no more NaN entries.  

---

## Appending Series with nonunique Indices  

Similar to pd.merge_ordered(), the pd.merge_asof() function will also merge values in order using the on column, but for each row in the left DataFrame, only rows from the right DataFrame whose 'on' column values are less than the left value will be kept.  

This function can be use to align disparate datetime frequencies without having to first resample.  

Here, you'll merge monthly oil prices (US dollars) into a full automobile fuel efficiency dataset. The oil and automobile DataFrames have been pre-loaded as oil and auto. The first 5 rows of each have been printed in the IPython Shell for you to explore.    

These datasets will align such that the first price of the year will be broadcast into the rows of the automobiles DataFrame. This is considered correct since by the start of any given year, most automobiles for that year will have already been manufactured.  

You'll then inspect the merged DataFrame, resample by year and compute the mean 'Price' and 'mpg'. You should be able to see a trend in these two columns, that you can confirm by computing the Pearson correlation between resampled 'Price' and 'mpg'.  

### Instructions :  

 - Merge auto and oil using pd.merge_asof() with left_on='yr' and right_on='Date'. Store the result as merged.
 - Print the tail of merged. This has been done for you.
 - Resample merged using 'A' (annual frequency), and on='Date'. Select [['mpg','Price']] and aggregate the mean. Store the result as yearly.
 - Hit Submit Answer to examine the contents of yearly and yearly.corr(), which shows the Pearson correlation between the resampled 'Price' and 'mpg'.

```python
# Merge auto and oil: merged
merged = pd.merge_asof(auto,oil,left_on='yr',right_on='Date')

# Print the tail of merged
print(merged.tail())
print('------------------')

# Resample merged: yearly
yearly = merged.resample('A',on='Date')[['mpg','Price']].mean()

# Print yearly
print(yearly)
print('------------------')

# print yearly.corr()
print(yearly.corr())
print('------------------')
```

### Results :  

	oil
		Date  Price
	0 1970-01-01   3.35
	1 1970-02-01   3.35
	2 1970-03-01   3.35
	3 1970-04-01   3.35
	4 1970-05-01   3.35

	auto
	    mpg  cyl  displ   hp  weight  accel         yr origin  \
	0  18.0    8  307.0  130    3504   12.0 1970-01-01     US   
	1  15.0    8  350.0  165    3693   11.5 1970-01-01     US   
	2  18.0    8  318.0  150    3436   11.0 1970-01-01     US   
	3  16.0    8  304.0  150    3433   12.0 1970-01-01     US   
	4  17.0    8  302.0  140    3449   10.5 1970-01-01     US   

		                name  
	0  chevrolet chevelle malibu  
	1          buick skylark 320  
	2         plymouth satellite  
	3              amc rebel sst  
	4                ford torino

	<script.py> output:
		  mpg  cyl  displ  hp  weight  accel         yr  origin             name  \
	    387  27.0    4  140.0  86    2790   15.6 1982-01-01      US  ford mustang gl   
	    388  44.0    4   97.0  52    2130   24.6 1982-01-01  Europe        vw pickup   
	    389  32.0    4  135.0  84    2295   11.6 1982-01-01      US    dodge rampage   
	    390  28.0    4  120.0  79    2625   18.6 1982-01-01      US      ford ranger   
	    391  31.0    4  119.0  82    2720   19.4 1982-01-01      US       chevy s-10   
	    
		      Date  Price  
	    387 1982-01-01  33.85  
	    388 1982-01-01  33.85  
	    389 1982-01-01  33.85  
	    390 1982-01-01  33.85  
	    391 1982-01-01  33.85  
	    ------------------
		              mpg  Price
	    Date                        
	    1970-12-31  17.689655   3.35
	    1971-12-31  21.111111   3.56
	    1972-12-31  18.714286   3.56
	    1973-12-31  17.100000   3.56
	    1974-12-31  22.769231  10.11
	    1975-12-31  20.266667  11.16
	    1976-12-31  21.573529  11.16
	    1977-12-31  23.375000  13.90
	    1978-12-31  24.061111  14.85
	    1979-12-31  25.093103  14.85
	    1980-12-31  33.803704  32.50
	    1981-12-31  30.185714  38.00
	    1982-12-31  32.000000  33.85
	    ------------------
		        mpg     Price
	    mpg    1.000000  0.948677
	    Price  0.948677  1.000000
	    ------------------
Great work! It looks like there is a strong correlation between miles per gallon and the price of oil!  

---