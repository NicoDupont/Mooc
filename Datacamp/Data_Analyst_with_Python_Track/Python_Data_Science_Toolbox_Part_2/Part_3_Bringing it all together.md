05/2017  
Datcamp - Python Data Science Toolbox (Part 2)  

---
 
# Part 3 : Bringing it all together!

This chapter will allow you to apply your newly acquired skills towards wrangling and extracting meaningful information from a real-world dataset - the World Bank's World Development Indicators dataset! You'll have the chance to write your own functions and list comprehensions as you work with iterators and generators and solidify your Python Data Science chops. Enjoy!  

## Dictionaries for data science

For this exercise, you'll use what you've learned about the zip() function and combine two lists into a dictionary.  

These lists are actually extracted from a bigger dataset file of world development indicators from the World Bank. For pedagogical purposes, we have pre-processed this dataset into the lists that you'll be working with.  

The first list feature_names contains header names of the dataset and the second list row_vals contains actual values of a row from the dataset, corresponding to each of the header names.  

### Instructions :

- Create a zip object by calling zip() and passing to it feature_names and row_vals. Assign the result to zipped_lists.
- Create a dictionary from the zipped_lists zip object by calling dict() with zipped_lists. Assign the resulting dictionary to rs_dict.

```python
# Zip lists: zipped_lists
zipped_lists = zip(feature_names,row_vals)

# Create a dictionary: rs_dict
rs_dict = dict(zipped_lists)

# Print the dictionary
print(rs_dict)
```

### Results :  

	<script.py> output:
	    {'IndicatorCode': 'SP.ADO.TFRT', 'Value': '133.56090740552298', 'Year': '1960', 'IndicatorName': 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'CountryCode': 'ARB', 'CountryName': 'Arab World'}

---

## Writing a function to help you

Suppose you needed to repeat the same process done in the previous exercise to many, many rows of data. Rewriting your code again and again could become very tedious, repetitive, and unmaintainable.  

In this exercise, you will create a function to house the code you wrote earlier to make things easier and much more concise. Why? This way, you only need to call the function and supply the appropriate lists to create your dictionaries! Again, the lists feature_names and row_vals are preloaded and these contain the header names of the dataset and actual values of a row from the dataset, respectively.  

### Instructions :

- Define the function lists2dict() with two parameters: first is list1 and second is list2.
- Return the resulting dictionary rs_dict in lists2dict().
- Call the lists2dict() function with the arguments feature_names and row_vals. Assign the result of the function call to rs_fxn.

```python
# Define lists2dict()
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return rs_dict
    

# Call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names,row_vals)

# Print rs_fxn
print(rs_fxn)
```

### Results :  

	<script.py> output:
	    {'IndicatorCode': 'SP.ADO.TFRT', 'Value': '133.56090740552298', 'Year': '1960', 'IndicatorName': 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'CountryCode': 'ARB', 'CountryName': 'Arab World'}

---

## Using a list comprehension

This time, you're going to use the lists2dict() function you defined in the last exercise to turn a bunch of lists into a list of dictionaries with the help of a list comprehension.  

The lists2dict() function has already been preloaded, together with a couple of lists, feature_names and row_lists. feature_names contains the header names of the World Bank dataset and row_lists is a list of lists, where each sublist is a list of actual values of a row from the dataset.  

Your goal is to use a list comprehension to generate a list of dicts, where the keys are the header names and the values are the row entries.  

### Instructions :

- Inspect the contents of row_lists by printing the first two lists in row_lists.
- Create a list comprehension that generates a dictionary using lists2dict() for each sublist in row_lists. The keys are from the feature_names list and the values are the row entries in row_lists. Use sublist as your iterator variable and assign the resulting list of dictionaries to list_of_dicts.
- Look at the first two dictionaries in list_of_dicts by printing them out.

```python
# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names,sublist) for sublist in row_lists]

# Print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])
```

### Results :  

	<script.py> output:
	    ['Arab World', 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', '1960', '133.56090740552298']
	    ['Arab World', 'ARB', 'Age dependency ratio (% of working-age population)', 'SP.POP.DPND', '1960', '87.7976011532547']
	    {'IndicatorCode': 'SP.ADO.TFRT', 'Value': '133.56090740552298', 'Year': '1960', 'IndicatorName': 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'CountryCode': 'ARB', 'CountryName': 'Arab World'}
	    {'IndicatorCode': 'SP.POP.DPND', 'Value': '87.7976011532547', 'Year': '1960', 'IndicatorName': 'Age dependency ratio (% of working-age population)', 'CountryCode': 'ARB', 'CountryName': 'Arab World'}

---

## Turning this all into a DataFrame

You've zipped lists together, created a function to house your code, and even used the function in a list comprehension to generate a list of dictionaries. That was a lot of work and you did a great job!  

You will now use of all these to convert the list of dictionaries into a pandas DataFrame. You will see how convenient it is to generate a DataFrame from dictionaries with the DataFrame() function from the pandas package.  

The lists2dict() function, feature_names list, and row_lists list have been preloaded for this exercise.  

Go for it!  

### Instructions :

-     To use the DataFrame() function you need, first import the pandas package with the alias pd.
-     Create a DataFrame from the list of dictionaries in list_of_dicts by calling pd.DataFrame(). Assign the resulting DataFrame to df.
-     Inspect the contents of df by printing the head of the DataFrame.

```python
# Import the pandas package
import pandas as pd

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df.head())
```

### Results :  

	<script.py> output:
	      CountryCode CountryName   IndicatorCode  \
	    0         ARB  Arab World     SP.ADO.TFRT   
	    1         ARB  Arab World     SP.POP.DPND   
	    2         ARB  Arab World  SP.POP.DPND.OL   
	    3         ARB  Arab World  SP.POP.DPND.YG   
	    4         ARB  Arab World  MS.MIL.XPRT.KD   
	    
		                                   IndicatorName               Value  Year  
	    0  Adolescent fertility rate (births per 1,000 wo...  133.56090740552298  1960  
	    1  Age dependency ratio (% of working-age populat...    87.7976011532547  1960  
	    2  Age dependency ratio, old (% of working-age po...   6.634579191565161  1960  
	    3  Age dependency ratio, young (% of working-age ...   81.02332950839141  1960  
	    4        Arms exports (SIPRI trend indicator values)           3000000.0  1960

---

## Processing data in chunks (1)

Sometimes, data sources can be so large in size that storing the entire dataset in memory becomes too resource-intensive. In this exercise, you will process the first 1000 rows of a file line by line, to create a dictionary of the counts of how many times each country appears in a column in the dataset.  

The csv file 'world_dev_ind.csv' is in your current directory for your use. To begin, you need to open a connection to this file using what is known as a context manager. For example, the command with open('datacamp.csv') as datacamp binds the csv file 'datacamp.csv' as datacamp in the context manager. Here, the with statement is the context manager, and its purpose is to ensure that resources are efficiently allocated when opening a connection to a file.  

If you'd like to learn more about context managers, refer to the DataCamp course on Importing Data in Python.  

### Instructions :

- Use open() to bind the csv file 'world_dev_ind.csv' as file in the context manager.
- Complete the for loop so that it iterates 1000 times to perform the loop body and process only the first 1000 rows of data of the file.

```python
# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Skip the column names
    file.readline()

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 1000 rows
    for j in range(1000):

        # Split the current line into a list: line
        line = file.readline().split(',')

        # Get the value for the first column: first_col
        first_col = line[0]

        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1

        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1
```

### Results :  

	<script.py> output:
	    {'Europe & Central Asia (all income levels)': 109, 'East Asia & Pacific (all income levels)': 122, 'Europe & Central Asia (developing only)': 89, 'Heavily indebted poor countries (HIPC)': 18, 'Arab World': 80, 'East Asia & Pacific (developing only)': 123, 'Caribbean small states': 77, 'European Union': 116, 'Central Europe and the Baltics': 71, 'Fragile and conflict affected situations': 76, 'Euro area': 119}

---

## Writing a generator to load data in chunks (2)

In the previous exercise, you processed a file line by line for a given number of lines. What if, however, you want to do this for the entire file?  

In this case, it would be useful to use generators. Generators allow users to lazily evaluate data. This concept of lazy evaluation is useful when you have to deal with very large datasets because it lets you generate values in an efficient manner by yielding only chunks of data at a time instead of the whole thing at once.  

In this exercise, you will define a generator function read_large_file() that produces a generator object which yields a single line from a file each time next() is called on it. The csv file 'world_dev_ind.csv' is in your current directory for your use.  

Note that when you open a connection to a file, the resulting file object is already a generator! So out in the wild, you won't have to explicitly create generator objects in cases such as this. However, for pedagogical reasons, we are having you practice how to do this here with the read_large_file() function. Go for it!  


### Instructions :


-     In the function read_large_file(), read a line from file_object by using the method readline(). Assign the result to data.
-     In the function read_large_file(), yield the line read from the file data.
-     In the context manager, create a generator object gen_file by calling your generator function read_large_file() and passing file to it.
-     Print the first three lines produced by the generator object gen_file using next().


```python
# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        # Yield the line of data
        yield data
        
# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))
```

### Results :  

	Wonderful work! Note that since a file object is already a generator, you don't have to explicitly create a generator object with your read_large_file() function. However, it is still good to practice how to create generators - well done!

	<script.py> output:
	    CountryName,CountryCode,IndicatorName,IndicatorCode,Year,Value
	    
	    Arab World,ARB,"Adolescent fertility rate (births per 1,000 women ages 15-19)",SP.ADO.TFRT,1960,133.56090740552298
	    
	    Arab World,ARB,Age dependency ratio (% of working-age population),SP.POP.DPND,1960,87.7976011532547

---

## Writing a generator to load data in chunks (3)

Great! You've just created a generator function that you can use to help you process large files.  

Now let's use your generator function to process the World Bank dataset like you did previously. You will process the file line by line, to create a dictionary of the counts of how many times each country appears in a column in the dataset. For this exercise, however, you won't process just 1000 rows of data, you'll process the entire dataset!  

The generator function read_large_file() and the csv file 'world_dev_ind.csv' are preloaded and ready for your use. Go for it!  

### Instructions :


-     Bind the file 'world_dev_ind.csv' to file in the context manager with open().
-     Complete the for loop so that it iterates over the generator from the call to read_large_file() to process all the rows of the file.

```python
# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

# Print            
print(counts_dict)
```

### Results :  

	<script.py> output:
	    {'High income': 131, 'Arab World': 80, 'Other small states': 63, 'OECD members': 130, 'CountryName': 1, 'Europe & Central Asia (all income levels)': 109, 'Middle income': 138, 'Latin America & Caribbean (developing only)': 133, 'Middle East & North Africa (all income levels)': 89, 'European Union': 116, 'Caribbean small states': 77, 'Lower middle income': 126, 'Euro area': 119, 'Latin America & Caribbean (all income levels)': 130, 'Least developed countries: UN classification': 78, 'South Asia': 36, 'East Asia & Pacific (all income levels)': 122, 'North America': 123, 'Low income': 80, 'High income: nonOECD': 68, 'Low & middle income': 138, 'Pacific island small states': 66, 'East Asia & Pacific (developing only)': 123, 'Europe & Central Asia (developing only)': 89, 'Heavily indebted poor countries (HIPC)': 99, 'Small states': 69, 'High income: OECD': 127, 'Central Europe and the Baltics': 71, 'Fragile and conflict affected situations': 76, 'Middle East & North Africa (developing only)': 94}

---

## Writing an iterator to load data in chunks (1)

Another way to read data too large to store in memory in chunks is to read the file in as DataFrames of a certain length, say, 100. For example, with the pandas package (imported as pd), you can do pd.read_csv(filename, chunksize=100). This creates an iterable reader object, which means that you can use next() on it.  

In this exercise, you will read a file in small DataFrame chunks with read_csv(). You're going to use the World Bank Indicators data 'ind_pop.csv', available in your current directory, to look at the urban population indicator for numerous countries and years.  

### Instructions :


-     Use pd.read_csv() to read in 'ind_pop.csv' in chunks of size 10. Assign the result to df_reader.
-     Print the first two chunks from df_reader.

```python
# Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('ind_pop.csv', chunksize=10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))
```

### Results :  

	<script.py> output:
		                             CountryName CountryCode  \
	    0                                 Arab World         ARB   
	    1                     Caribbean small states         CSS   
	    2             Central Europe and the Baltics         CEB   
	    3    East Asia & Pacific (all income levels)         EAS   
	    4      East Asia & Pacific (developing only)         EAP   
	    5                                  Euro area         EMU   
	    6  Europe & Central Asia (all income levels)         ECS   
	    7    Europe & Central Asia (developing only)         ECA   
	    8                             European Union         EUU   
	    9   Fragile and conflict affected situations         FCS   
	    
		               IndicatorName      IndicatorCode  Year      Value  
	    0  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  31.285384  
	    1  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  31.597490  
	    2  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  44.507921  
	    3  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  22.471132  
	    4  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  16.917679  
	    5  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  62.096947  
	    6  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  55.378977  
	    7  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  38.066129  
	    8  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  61.212898  
	    9  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  17.891972  
		                                  CountryName CountryCode  \
	    10         Heavily indebted poor countries (HIPC)         HPC   
	    11                                    High income         HIC   
	    12                           High income: nonOECD         NOC   
	    13                              High income: OECD         OEC   
	    14  Latin America & Caribbean (all income levels)         LCN   
	    15    Latin America & Caribbean (developing only)         LAC   
	    16   Least developed countries: UN classification         LDC   
	    17                            Low & middle income         LMY   
	    18                                     Low income         LIC   
	    19                            Lower middle income         LMC   
	    
		                IndicatorName      IndicatorCode  Year      Value  
	    10  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  12.236046  
	    11  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  62.680332  
	    12  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  56.107863  
	    13  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  64.285435  
	    14  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  49.284688  
	    15  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  44.863308  
	    16  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960   9.616261  
	    17  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  21.272894  
	    18  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  11.498396  
	    19  Urban population (% of total)  SP.URB.TOTL.IN.ZS  1960  19.810513

---

## Writing an iterator to load data in chunks (2)

In the previous exercise, you used read_csv() to read in DataFrame chunks from a large dataset. In this exercise, you will read in a file using a bigger DataFrame chunk size and then process the data from the first chunk.  

To process the data, you will create another DataFrame composed of only the rows from a specific country. You will then zip together two of the columns from the new DataFrame, 'Total Population' and 'Urban population (% of total)'. Finally, you will create a list of tuples from the zip object, where each tuple is composed of a value from each of the two columns mentioned.  

You're going to use the data from 'ind_pop_data.csv', available in your current directory. Pandas has been imported as pd.  

### Instructions :

-     Use pd.read_csv() to read in the file in 'ind_pop_data.csv' in chunks of size 1000. Assign the result to urb_pop_reader.
-     Get the first DataFrame chunk from the iterable urb_pop_reader and assign this to df_urb_pop.
-     Select only the rows of df_urb_pop that have a 'CountryCode' of 'CEB'. To do this, compare whether df_urb_pop['CountryCode'] is equal to 'CEB' within the square brackets in df_urb_pop[____].
-     Using zip(), zip together the 'Total Population' and 'Urban population (% of total)' columns of df_pop_ceb. Assign the resulting zip object to pops.

```python
# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)
```

### Results :  

	<script.py> output:
		                           CountryName CountryCode  Year  \
	    0                               Arab World         ARB  1960   
	    1                   Caribbean small states         CSS  1960   
	    2           Central Europe and the Baltics         CEB  1960   
	    3  East Asia & Pacific (all income levels)         EAS  1960   
	    4    East Asia & Pacific (developing only)         EAP  1960   
	    
	       Total Population  Urban population (% of total)  
	    0      9.249590e+07                      31.285384  
	    1      4.190810e+06                      31.597490  
	    2      9.140158e+07                      44.507921  
	    3      1.042475e+09                      22.471132  
	    4      8.964930e+08                      16.917679  
	    [(91401583.0, 44.507921139002597), (92237118.0, 45.206665319194002), (93014890.0, 45.866564696018003), (93845749.0, 46.5340927663649), (94722599.0, 47.208742980352604)]


---

## Writing an iterator to load data in chunks (3)

You're getting used to reading and processing data in chunks by now. Let's push your skills a little further by adding a column to a DataFrame.  

In this exercise, you will be using a list comprehension to create the values for a new column 'Total Urban Population' from the list of tuples that you generated earlier. Recall from the previous exercise that the first and second elements of each tuple consist of, respectively, values from the columns 'Total Population' and 'Urban population (% of total)'. The values in this new column 'Total Urban Population', therefore, are the product of the first and second element in each tuple. Furthermore, because the 2nd element is a percentage, you need to divide the entire result by 100, or alternatively, multiply it by 0.01.  

You will also plot the data from this new column to create a visualization of the urban population data.  

You're going to use the data from 'ind_pop_data.csv', available in your current directory. The packages pandas and matplotlib.pyplot have been imported as pd and plt respectively for your use.  

### Instructions :

-     Use pd.read_csv() to read in the file 'ind_pop_data.csv' in chunks of size 1000. Assign the result to urb_pop_reader.
-     Write a list comprehension to generate a list of values from pops_list for the new column 'Total Urban Population'. Use tup as the iterator variable. The output expression should be the product of the first and second element in each tuple in pops_list. Because the 2nd element is a percentage, you also need to either multiply the result by 0.01 or divide it by 100. In addition, note that the column 'Total Urban Population' should only be able to take on integer values. To ensure this, make sure you cast the output expression to an integer with int().
-     Create a scatter plot where the x-axis are values from the 'Year' column and the y-axis are values from the 'Total Urban Population' column.

```python
# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], 
            df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(tup[0]*(tup[1]*0.01)) for tup in pops_list]

# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()
```

### Results :  

	see img/graph1.svg

---

## Writing an iterator to load data in chunks (4)

In the previous exercises, you've only processed the data from the first DataFrame chunk. This time, you will aggregate the results over all the DataFrame chunks in the dataset. This basically means you will be processing the entire dataset now. This is neat because you're going to be able to process the entire large dataset by just working on smaller pieces of it!  

You're going to use the data from 'ind_pop_data.csv', available in your current directory. The packages pandas and matplotlib.pyplot have been imported as pd and plt respectively for your use.  

### Instructions :

-     Initialize an empty DataFrame data using pd.DataFrame().
-     In the for loop, iterate over urb_pop_reader to be able to process all the DataFrame chunks in the dataset.
-     Using append() on data, append df_pop_ceb to data.

```python
# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Initialize empty DataFrame: data
data = pd.DataFrame()

# Iterate over each DataFrame chunk
for df_urb_pop in urb_pop_reader:

    # Check out specific country: df_pop_ceb
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

    # Zip DataFrame columns of interest: pops
    pops = zip(df_pop_ceb['Total Population'],
                df_pop_ceb['Urban population (% of total)'])

    # Turn zip object into list: pops_list
    pops_list = list(pops)

    # Use list comprehension to create new DataFrame column 'Total Urban Population'
    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1]) for tup in pops_list]
    
    # Append DataFrame chunk to data: data
    data = data.append(df_pop_ceb)

# Plot urban population data
data.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()
```

### Results :  

	see img/graph2.svg

---

## Writing an iterator to load data in chunks (5)

This is the last leg. You've learned a lot about processing a large dataset in chunks. In this last exercise, you will put all the code for processing the data into a single function so that you can reuse the code without having to rewrite the same things all over again.  

You're going to define the function plot_pop() which takes two arguments: the filename of the file to be processed, and the country code of the rows you want to process in the dataset.  

Because all of the previous code you've written in the previous exercises will be housed in plot_pop(), calling the function already does the following:  

-     Loading of the file chunk by chunk,
-     Creating the new column of urban population values, and
-     Plotting the urban population data.

That's a lot of work, but the function now makes it convenient to repeat the same process for whatever file and country code you want to process and visualize!  

You're going to use the data from 'ind_pop_data.csv', available in your current directory. The packages pandas and matplotlib.pyplot has been imported as pd and plt respectively for your use.  

After you are done, take a moment to look at the plots and reflect on the new skills you have acquired. The journey doesn't end here! If you have enjoyed working with this data, you can continue exploring it using the pre-processed version available on Kaggle.  


### Instructions :

-     Define the function plot_pop() that has two arguments: first is filename for the file to process and second is country_code for the country to be processed in the dataset.
-     Call plot_pop() to process the data for country code 'CEB' in the file 'ind_pop_data.csv'.
-     Call plot_pop() to process the data for country code 'ARB' in the file 'ind_pop_data.csv'.

```python
# Define plot_pop()
def plot_pop(filename, country_code):

    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    # Initialize empty DataFrame: data
    data = pd.DataFrame()
    
    # Iterate over each DataFrame chunk
    for df_urb_pop in urb_pop_reader:
        # Check out specific country: df_pop_ceb
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

        # Zip DataFrame columns of interest: pops
        pops = zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Urban population (% of total)'])

        # Turn zip object into list: pops_list
        pops_list = list(pops)

        # Use list comprehension to create new DataFrame column 'Total Urban Population'
        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1]) for tup in pops_list]
    
        # Append DataFrame chunk to data: data
        data = data.append(df_pop_ceb)

    # Plot urban population data
    data.plot(kind='scatter', x='Year', y='Total Urban Population')
    plt.show()

# Set the filename: fn
fn = 'ind_pop_data.csv'

# Call plot_pop for country code 'CEB'
plot_pop(fn,'CEB')

# Call plot_pop for country code 'ARB'
plot_pop(fn,'ARB')
```

### Results :  

	see img/graph3.svg
	see img/graph4.svg
