10/2017  
Datacamp - Cleaning Data in Python  

---

The ability to transform and combine your data is a crucial skill in data science, because your data may not always come in one monolithic file or table for you to load. A large dataset may be broken into separate datasets to facilitate easier storage and sharing. Or if you are dealing with time series data, for example, you may have a new dataset for each day. No matter the reason, it is important to be able to combine datasets so you can either clean a single dataset, or clean each dataset separately and then combine them later so you can run your analysis on a single dataset. In this chapter, you'll learn all about combining data.  

# Part 3 : Combining data for analysis  


## Combining rows of data  

The dataset you'll be working with here relates to NYC Uber data. The original dataset has all the originating Uber pickup locations by time and latitude and longitude. For didactic purposes, you'll be working with a very small portion of the actual data.  

Three DataFrames have been pre-loaded: uber1, which contains data for April 2014, uber2, which contains data for May 2014, and uber3, which contains data for June 2014. Your job in this exercise is to concatenate these DataFrames together such that the resulting DataFrame has the data for all three months.  

Begin by exploring the structure of these three DataFrames in the IPython Shell using methods such as .head().  

### Instructions :

 - Concatenate uber1, uber2, and uber3 together using pd.concat(). You'll have to pass the DataFrames in as a list.
 - Print the shape and then the head of the concatenated DataFrame, row_concat.

```python
# Concatenate uber1, uber2, and uber3: row_concat
row_concat = pd.concat([uber1,uber2,uber3])

# Print the shape of row_concat
print(row_concat.shape)

# Print the head of row_concat
print(row_concat.head())
```

### Results :  

	<script.py> output:
		(297, 4)
				  Date/Time      Lat      Lon    Base
		0  4/1/2014 0:11:00  40.7690 -73.9549  B02512
		1  4/1/2014 0:17:00  40.7267 -74.0345  B02512
		2  4/1/2014 0:21:00  40.7316 -73.9873  B02512
		3  4/1/2014 0:28:00  40.7588 -73.9776  B02512
		4  4/1/2014 0:33:00  40.7594 -73.9722  B02512

Great work! You have successfully concatenated the three uber DataFrames! Notice that the head of row_concat is the same as the head of uber1, while the tail of row_concat is the same as the tail of uber3.  
		
---

## Combining columns of data

Think of column-wise concatenation of data as stitching data together from the sides instead of the top and bottom. To perform this action, you use the same pd.concat() function, but this time with the keyword argument axis=1. The default, axis=0, is for a row-wise concatenation.  

You'll return to the Ebola dataset you worked with briefly in the last chapter. It has been pre-loaded into a DataFrame called ebola_melt. In this DataFrame, the status and country of a patient is contained in a single column. This column has been parsed into a new DataFrame, status_country, where there are separate columns for status and country.  

Explore the ebola_melt and status_country DataFrames in the IPython Shell. Your job is to concatenate them column-wise in order to obtain a final, clean DataFrame.  

### Instructions :

 - Concatenate ebola_melt and status_country column-wise into a single DataFrame called ebola_tidy. Be sure to specify axis=1 and to pass the two DataFrames in as a list.
 - Print the shape and then the head of the concatenated DataFrame, ebola_tidy.

```python
print(status_country.shape)
print(status_country.head())
print("----------")
print(ebola_melt.shape)
print(ebola_melt.head())
print("----------")

# Concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt,status_country],axis=1)

# Print the shape of ebola_tidy
print(ebola_tidy.shape)

# Print the head of ebola_tidy
print(ebola_tidy.head())
```

### Results :  

	<script.py> output:
		(1952, 2)
		  status country
		0  Cases  Guinea
		1  Cases  Guinea
		2  Cases  Guinea
		3  Cases  Guinea
		4  Cases  Guinea
		----------
		(1952, 4)
				 Date  Day status_country  counts
		0    1/5/2015  289   Cases_Guinea  2776.0
		1    1/4/2015  288   Cases_Guinea  2775.0
		2    1/3/2015  287   Cases_Guinea  2769.0
		3    1/2/2015  286   Cases_Guinea     NaN
		4  12/31/2014  284   Cases_Guinea  2730.0
		----------
		(1952, 6)
				 Date  Day status_country  counts status country
		0    1/5/2015  289   Cases_Guinea  2776.0  Cases  Guinea
		1    1/4/2015  288   Cases_Guinea  2775.0  Cases  Guinea
		2    1/3/2015  287   Cases_Guinea  2769.0  Cases  Guinea
		3    1/2/2015  286   Cases_Guinea     NaN  Cases  Guinea
		4  12/31/2014  284   Cases_Guinea  2730.0  Cases  Guinea

Fantastic! The concatenated DataFrame has 6 columns, as it should. Notice how the status and country columns have been concatenated column-wise.  

---

## Finding files that match a pattern  

You're now going to practice using the glob module to find all csv files in the workspace. In the next exercise, you'll programmatically load them into DataFrames.  

As Dan showed you in the video, the glob module has a function called glob that takes a pattern and returns a list of the files in the working directory that match that pattern.  

For example, if you know the pattern is part_ single digit number .csv, you can write the pattern as 'part_?.csv' (which would match part_1.csv, part_2.csv, part_3.csv, etc.)  

Similarly, you can find all .csv files with '*.csv', or all parts with 'part_*'. The ? wildcard represents any 1 character, and the * wildcard represents any number of characters.  

### Instructions :

 - Import the glob module along with pandas (as its usual alias pd).
 - Write a pattern to match all .csv files.
 - Save all files that match the pattern using the glob() function within the glob module. That is, by using glob.glob().
 - Print the list of file names. This has been done for you.
 - Read the second file in csv_files (i.e., index 1) into a DataFrame called csv2.
 - Hit 'Submit Answer' to print the head of csv2. Does it look familiar?

```python
# Import necessary modules
import glob
import pandas as pd

# Write the pattern: pattern
pattern = '*.csv'

# Save all file matches: csv_files
csv_files = glob.glob(pattern)

# Print the file names
print(csv_files)

# Load the second file into a DataFrame: csv2
csv2 = pd.read_csv(csv_files[1])

# Print the head of csv2
print(csv2.head())
```

### Results :  

	<script.py> output:
		['uber-raw-data-2014_06.csv', 'uber-raw-data-2014_04.csv', 'uber-raw-data-2014_05.csv']
				  Date/Time      Lat      Lon    Base
		0  4/1/2014 0:11:00  40.7690 -73.9549  B02512
		1  4/1/2014 0:17:00  40.7267 -74.0345  B02512
		2  4/1/2014 0:21:00  40.7316 -73.9873  B02512
		3  4/1/2014 0:28:00  40.7588 -73.9776  B02512
		4  4/1/2014 0:33:00  40.7594 -73.9722  B02512

Excellent work! The next step is to iterate through this list of filenames, load it into a DataFrame, and add it to a list of DataFrames you can then concatenate together.  

---

## Iterating and concatenating all matches  

Now that you have a list of filenames to load, you can load all the files into a list of DataFrames that can then be concatenated.  

You'll start with an empty list called frames. Your job is to use a for loop to iterate through each of the filenames, read each filename into a DataFrame, and then append it to the frames list.  

You can then concatenate this list of DataFrames using pd.concat(). Go for it!  

### Instructions :

 - Write a for loop to iterate though csv_files:
 - In each iteration of the loop, read csv into a DataFrame called df.
  - After creating df, append it to the list frames using the .append() method.
  - Concatenate frames into a single DataFrame called uber.
 - Hit 'Submit Answer' to see the head and shape of the concatenated DataFrame!

```python
# Create an empty list: frames
frames = []

#  Iterate over csv_files
for csv in csv_files:

    #  Read csv into a DataFrame: df
    df = pd.read_csv(csv)
    
    # Append df to frames
    frames.append(df)

# Concatenate frames into a single DataFrame: uber
uber = pd.concat(frames)

# Print the shape of uber
print(uber.shape)

# Print the head of uber
print(uber.head())
```

### Results :  

	<script.py> output:
		(297, 4)
				  Date/Time      Lat      Lon    Base
		0  6/1/2014 0:00:00  40.7293 -73.9920  B02512
		1  6/1/2014 0:01:00  40.7131 -74.0097  B02512
		2  6/1/2014 0:04:00  40.3461 -74.6610  B02512
		3  6/1/2014 0:04:00  40.7555 -73.9833  B02512
		4  6/1/2014 0:07:00  40.6880 -74.1831  B02512

Fantastic work! You can now programmatically combine datasets that are broken up into many smaller parts. You'll find many datasets in the wild will be stored this way, particularly data that is collected incrementally.  

---

## 1-to-1 data merge  

Merging data allows you to combine disparate datasets into a single dataset to do more complex analysis.  

Here, you'll be using survey data that contains readings that William Dyer, Frank Pabodie, and Valentina Roerich took in the late 1920 and 1930 while they were on an expedition towards Antarctica. The dataset was taken from a sqlite database from the Software Carpentry SQL lesson.  

Two DataFrames have been pre-loaded: site and visited. Explore them in the IPython Shell and take note of their structure and column names. Your task is to perform a 1-to-1 merge of these two DataFrames using the 'name' column of site and the 'site' column of visited.  

### Instructions :

 - Merge the site and visited DataFrames on the 'name' column of site and 'site' column of visited.
 - Print the merged DataFrame o2o.

```python
# Merge the DataFrames: o2o
o2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Print o2o
print(o2o)
```

### Results :  

	<script.py> output:
			name    lat    long  ident   site       dated
		0   DR-1 -49.85 -128.57    619   DR-1  1927-02-08
		1   DR-3 -47.15 -126.72    734   DR-3  1939-01-07
		2  MSK-4 -48.87 -123.40    837  MSK-4  1932-01-14

Superb! Notice the 1-to-1 correspondence between the name column of the site DataFrame and the site column of the visited DataFrame. This is what made the 1-to-1 merge possible.  

---

## Many-to-1 data merge  

In a many-to-one (or one-to-many) merge, one of the values will be duplicated and recycled in the output. That is, one of the keys in the merge is not unique.  

Here, the two DataFrames site and visited have been pre-loaded once again. Note that this time, visited has multiple entries for the site column. Confirm this by exploring it in the IPython Shell.  

The .merge() method call is the same as the 1-to-1 merge from the previous exercise, but the data and output will be different.  

### Instructions :

 - Merge the site and visited DataFrames on the 'name' column of site and 'site' column of visited, exactly as you did in the previous exercise.
 - Print the merged DataFrame and then hit 'Submit Answer' to see the different output produced by this merge!

```python
print(site.shape)
print(site.head())
print("----------")
print(visited.shape)
print(visited.head())
print("----------")


# Merge the DataFrames: o2o
m2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Print o2o
print(m2o)

```

### Results :  

	<script.py> output:
		(3, 3)
			name    lat    long
		0   DR-1 -49.85 -128.57
		1   DR-3 -47.15 -126.72
		2  MSK-4 -48.87 -123.40
		----------
		(8, 3)
		   ident  site       dated
		0    619  DR-1  1927-02-08
		1    622  DR-1  1927-02-10
		2    734  DR-3  1939-01-07
		3    735  DR-3  1930-01-12
		4    751  DR-3  1930-02-26
		----------
			name    lat    long  ident   site       dated
		0   DR-1 -49.85 -128.57    619   DR-1  1927-02-08
		1   DR-1 -49.85 -128.57    622   DR-1  1927-02-10
		2   DR-1 -49.85 -128.57    844   DR-1  1932-03-22
		3   DR-3 -47.15 -126.72    734   DR-3  1939-01-07
		4   DR-3 -47.15 -126.72    735   DR-3  1930-01-12
		5   DR-3 -47.15 -126.72    751   DR-3  1930-02-26
		6   DR-3 -47.15 -126.72    752   DR-3         NaN
		7  MSK-4 -48.87 -123.40    837  MSK-4  1932-01-14

Great work! Notice how the site data is duplicated during this many-to-1 merge!  

---

## Many-to-many data merge  

The final merging scenario occurs when both DataFrames do not have unique keys for a merge. What happens here is that for each duplicated key, every pairwise combination will be created.  

Two example DataFrames that share common key values have been pre-loaded: df1 and df2. Another DataFrame df3, which is the result of df1 merged with df2, has been pre-loaded. All three DataFrames have been printed - look at the output and notice how pairwise combinations have been created. This example is to help you develop your intuition for many-to-many merges.  

Here, you'll work with the site and visited DataFrames from before, and a new survey DataFrame. Your task is to merge site and visited as you did in the earlier exercises. You will then merge this merged DataFrame with survey.  

Begin by exploring the site, visited, and survey DataFrames in the IPython Shell.  

### Instructions :

 - Merge the site and visited DataFrames on the 'name' column of site and 'site' column of visited, exactly as you did in the previous two exercises. Save the result as m2m.
 - Merge the m2m and survey DataFrames on the 'ident' column of m2m and 'taken' column of survey.
 - Hit 'Submit Answer' to print the first 20 lines of the merged DataFrame!

```python
print(site.shape)
print(site.head())
print("----------")
print(visited.shape)
print(visited.head())
print("----------")

# Merge site and visited: m2m
m2m = pd.merge(left=site, right=visited, left_on='name', right_on='site')


print(m2m.shape)
print(m2m.head())
print("----------")
print(survey.shape)
print(survey.head())
print("----------")

# Merge m2m and survey: m2m
m2m = pd.merge(left=m2m, right=survey, left_on='ident', right_on='taken')

# Print the first 20 lines of m2m
print(m2m.shape)
print(m2m.head(20))
```

### Results :  

	<script.py> output:
		(3, 3)
			name    lat    long
		0   DR-1 -49.85 -128.57
		1   DR-3 -47.15 -126.72
		2  MSK-4 -48.87 -123.40
		----------
		(8, 3)
		   ident  site       dated
		0    619  DR-1  1927-02-08
		1    622  DR-1  1927-02-10
		2    734  DR-3  1939-01-07
		3    735  DR-3  1930-01-12
		4    751  DR-3  1930-02-26
		----------
		(8, 6)
		   name    lat    long  ident  site       dated
		0  DR-1 -49.85 -128.57    619  DR-1  1927-02-08
		1  DR-1 -49.85 -128.57    622  DR-1  1927-02-10
		2  DR-1 -49.85 -128.57    844  DR-1  1932-03-22
		3  DR-3 -47.15 -126.72    734  DR-3  1939-01-07
		4  DR-3 -47.15 -126.72    735  DR-3  1930-01-12
		----------
		(21, 4)
		   taken person quant  reading
		0    619   dyer   rad     9.82
		1    619   dyer   sal     0.13
		2    622   dyer   rad     7.80
		3    622   dyer   sal     0.09
		4    734     pb   rad     8.41
		----------
		(21, 10)
			 name    lat    long  ident   site       dated  taken person quant  \
		0    DR-1 -49.85 -128.57    619   DR-1  1927-02-08    619   dyer   rad   
		1    DR-1 -49.85 -128.57    619   DR-1  1927-02-08    619   dyer   sal   
		2    DR-1 -49.85 -128.57    622   DR-1  1927-02-10    622   dyer   rad   
		3    DR-1 -49.85 -128.57    622   DR-1  1927-02-10    622   dyer   sal   
		4    DR-1 -49.85 -128.57    844   DR-1  1932-03-22    844    roe   rad   
		5    DR-3 -47.15 -126.72    734   DR-3  1939-01-07    734     pb   rad   
		6    DR-3 -47.15 -126.72    734   DR-3  1939-01-07    734   lake   sal   
		7    DR-3 -47.15 -126.72    734   DR-3  1939-01-07    734     pb  temp   
		8    DR-3 -47.15 -126.72    735   DR-3  1930-01-12    735     pb   rad   
		9    DR-3 -47.15 -126.72    735   DR-3  1930-01-12    735    NaN   sal   
		10   DR-3 -47.15 -126.72    735   DR-3  1930-01-12    735    NaN  temp   
		11   DR-3 -47.15 -126.72    751   DR-3  1930-02-26    751     pb   rad   
		12   DR-3 -47.15 -126.72    751   DR-3  1930-02-26    751     pb  temp   
		13   DR-3 -47.15 -126.72    751   DR-3  1930-02-26    751   lake   sal   
		14   DR-3 -47.15 -126.72    752   DR-3         NaN    752   lake   rad   
		15   DR-3 -47.15 -126.72    752   DR-3         NaN    752   lake   sal   
		16   DR-3 -47.15 -126.72    752   DR-3         NaN    752   lake  temp   
		17   DR-3 -47.15 -126.72    752   DR-3         NaN    752    roe   sal   
		18  MSK-4 -48.87 -123.40    837  MSK-4  1932-01-14    837   lake   rad   
		19  MSK-4 -48.87 -123.40    837  MSK-4  1932-01-14    837   lake   sal   
		
			reading  
		0      9.82  
		1      0.13  
		2      7.80  
		3      0.09  
		4     11.25  
		5      8.41  
		6      0.05  
		7    -21.50  
		8      7.22  
		9      0.06  
		10   -26.00  
		11     4.35  
		12   -18.50  
		13     0.10  
		14     2.19  
		15     0.09  
		16   -16.00  
		17    41.60  
		18     1.46  
		19     0.21

Excellent work! Notice how the keys are duplicated in this many-to-many merge!  
---