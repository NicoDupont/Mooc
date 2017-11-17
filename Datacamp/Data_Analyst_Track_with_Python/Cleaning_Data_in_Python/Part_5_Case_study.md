10/2017  
Datacamp - Cleaning Data in Python  

---

In this final chapter, you'll apply all of the data cleaning techniques you've learned in this course towards tidying a real-world, messy dataset obtained from the Gapminder Foundation. Once you're done, not only will you have a clean and tidy dataset, you'll also be ready to start working on your own data science projects using the power of Python!  

# Part 5 : Case Study   


## Exploratory analysis  

Whenever you obtain a new dataset, your first task should always be to do some exploratory analysis to get a better understanding of the data and diagnose it for any potential issues.  

The Gapminder data for the 19th century has been loaded into a DataFrame called g1800s. In the IPython Shell, use pandas methods such as .head(), .info(), and .describe(), and DataFrame attributes like .columns and .shape to explore it.  

Use the information that you acquire from your exploratory analysis to choose the true statement from the options provided below.  

### Possible Answers :

 - 1 - The DataFrame has 259 rows and 100 columns.
 - 2 - The DataFrame has no missing values encoded as NaN.
 - 3 - 100 of the columns are of type float64 and 1 column is of type object.
 - 4 - The DataFrame takes up 203.2+ KB of memory.

```python
print(g1800s.info())
```

### Results :  answer 3  

	In [1]: print(g1800s.info())
	<class 'pandas.core.frame.DataFrame'>
	RangeIndex: 260 entries, 0 to 259
	Columns: 101 entries, Life expectancy to 1899
	dtypes: float64(100), object(1)
	memory usage: 205.2+ KB
	None

	In [2]: print(g1800s.describe)
	<bound method NDFrame.describe of               Life expectancy   1800   1801   1802   1803   1804   1805  \
	0                    Abkhazia    NaN    NaN    NaN    NaN    NaN    NaN   
	1                 Afghanistan  28.21  28.20  28.19  28.18  28.17  28.16   
	2       Akrotiri and Dhekelia    NaN    NaN    NaN    NaN    NaN    NaN   
	3                     Albania  35.40  35.40  35.40  35.40  35.40  35.40   
	4                     Algeria  28.82  28.82  28.82  28.82  28.82  28.82   
	5              American Samoa    NaN    NaN    NaN    NaN    NaN    NaN   
	6                     Andorra    NaN    NaN    NaN    NaN    NaN    NaN   
	7                      Angola  26.98  26.98  26.98  26.98  26.98  26.98   
	8                    Anguilla    NaN    NaN    NaN    NaN    NaN    NaN   
	9         Antigua and Barbuda  33.54  33.54  33.54  33.54  33.54  33.54   
	10                  Argentina  33.20  33.20  33.20  33.20  33.20  33.20   
	11                    Armenia  34.00  34.00  34.00  34.00  34.00  34.00   
	12                      Aruba  34.42  34.42  34.42  34.42  34.42  34.42   
	13                  Australia  34.05  34.05  34.05  34.05  34.05  34.05   
	14                    Austria  34.40  34.40  34.40  34.40  34.40  34.40   
	15                 Azerbaijan  29.17  29.17  29.17  29.17  29.17  29.17   
	16                    Bahamas  35.18  35.18  35.18  35.18  35.18  35.18   
	17                    Bahrain  30.30  30.30  30.30  30.30  30.30  30.30   
	18                 Bangladesh  25.50  25.50  25.50  25.50  25.50  25.50   
	19                   Barbados  32.12  32.12  32.12  32.12  32.12  32.12   
	20                    Belarus  36.20  36.20  36.20  36.20  36.20  36.20   
	21                    Belgium  40.00  40.01  40.02  40.02  40.03  40.04   
	22                     Belize  26.50  26.50  26.50  26.50  26.50  26.50   
	23                      Benin  31.00  31.00  31.00  31.00  31.00  31.00   
	24                    Bermuda    NaN    NaN    NaN    NaN    NaN    NaN   
	25                     Bhutan  28.80  28.80  28.80  28.80  28.80  28.80   
	26                    Bolivia  33.00  33.00  33.00  33.00  33.00  33.00   
	27     Bosnia and Herzegovina  35.10  35.10  35.10  35.10  35.10  35.10   
	28                   Botswana  33.60  33.60  33.60  33.60  33.60  33.60   
	29                     Brazil  32.00  32.00  32.00  32.00  32.00  32.00   
	..                        ...    ...    ...    ...    ...    ...    ...   
	230       Trinidad and Tobago  32.90  32.90  32.90  32.90  32.90  32.90   
	231                   Tunisia  28.80  28.80  28.80  28.80  28.80  28.80   
	232                    Turkey  35.00  35.00  35.00  35.00  35.00  35.00   
	233              Turkmenistan  24.00  24.00  24.00  24.00  24.00  24.00   
	234  Turks and Caicos Islands    NaN    NaN    NaN    NaN    NaN    NaN   
	235                    Tuvalu    NaN    NaN    NaN    NaN    NaN    NaN   
	236                    Uganda  25.30  25.30  25.30  25.30  25.30  25.30   
	237                   Ukraine  36.60  36.60  36.60  36.60  36.60  36.60   
	238      United Arab Emirates  30.70  30.70  30.70  30.70  30.70  30.70   
	239            United Kingdom  38.65  37.35  38.62  37.32  41.44  42.32   
	240             United States  39.41  39.41  39.41  39.41  39.41  39.41   
	241                   Uruguay  32.90  32.90  32.90  32.90  32.90  32.90   
	242                      USSR    NaN    NaN    NaN    NaN    NaN    NaN   
	243                Uzbekistan  26.93  26.93  26.93  26.93  26.93  26.93   
	244          Wallis et Futuna    NaN    NaN    NaN    NaN    NaN    NaN   
	245                   Vanuatu  24.30  24.30  24.30  24.30  24.30  24.30   
	246                 Venezuela  32.20  32.20  32.20  32.20  32.20  32.20   
	247        West Bank and Gaza  32.10  32.10  32.10  32.10  32.10  32.10   
	248              West Germany    NaN    NaN    NaN    NaN    NaN    NaN   
	249            Western Sahara  34.75  34.75  34.75  34.75  34.75  34.75   
	250                   Vietnam  32.00  32.00  32.00  32.00  32.00  32.00   
	251     Virgin Islands (U.S.)  33.40  33.40  33.40  33.40  33.40  33.40   
	252      North Yemen (former)    NaN    NaN    NaN    NaN    NaN    NaN   
	253      South Yemen (former)    NaN    NaN    NaN    NaN    NaN    NaN   
	254                     Yemen  23.39  23.39  23.39  23.39  23.39  23.39   
	255                Yugoslavia    NaN    NaN    NaN    NaN    NaN    NaN   
	256                    Zambia  32.60  32.60  32.60  32.60  32.60  32.60   
	257                  Zimbabwe  33.70  33.70  33.70  33.70  33.70  33.70   
	258                     Åland    NaN    NaN    NaN    NaN    NaN    NaN   
	259               South Sudan  26.67  26.67  26.67  26.67  26.67  26.67   

		  1806   1807   1808  ...     1890   1891   1892   1893   1894   1895  \
	0      NaN    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN   
	1    28.15  28.14  28.13  ...    27.29  27.28  27.27  27.26  27.25  27.24   
	2      NaN    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN   
	3    35.40  35.40  35.40  ...    35.40  35.40  35.40  35.40  35.40  35.40   
	4    28.82  28.82  28.82  ...    28.82  28.82  28.82  28.82  28.82  28.82   
	5      NaN    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN   
	6      NaN    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN   
	7    26.98  26.98  26.98  ...    26.98  26.98  26.98  26.98  26.98  26.98   
	8      NaN    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN   
	9    33.54  33.54  33.54  ...    33.54  33.54  33.54  33.54  33.54  33.54   
	10   33.20  33.20  33.20  ...    34.00  33.86  33.72  33.58  33.44  33.30   
	11   34.00  34.00  34.00  ...    35.00  35.20  35.40  35.60  35.80  36.00   
	12   34.42  34.42  34.42  ...    34.42  34.42  34.42  34.42  34.42  34.42   
	13   34.05  34.05  34.05  ...    44.63  45.16  45.69  46.22  46.75  47.28   
	14   34.40  34.40  34.40  ...    37.07  37.30  37.77  38.24  38.71  39.18   
	15   29.17  29.17  29.17  ...    30.17  30.37  30.57  30.77  30.97  31.17   
	16   35.18  35.18  35.18  ...    35.18  35.18  35.18  35.18  35.18  35.18   
	17   30.30  30.30  30.30  ...    30.30  30.30  30.30  30.30  30.30  30.30   
	18   25.50  25.50  25.50  ...    22.72  21.60  21.00  22.36  22.18  22.00   
	19   32.12  32.12  32.12  ...    32.12  32.12  32.12  32.12  32.12  32.12   
	20   36.20  36.20  36.20  ...    36.20  36.20  36.20  36.20  36.20  36.20   
	21   40.05  40.06  40.06  ...    44.14  44.06  43.16  44.44  46.65  45.46   
	22   26.50  26.50  26.50  ...    26.50  26.50  26.50  26.50  26.50  26.50   
	23   31.00  31.00  31.00  ...    31.00  31.00  31.00  31.00  31.00  31.00   
	24     NaN    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN   
	25   28.80  28.80  28.80  ...    28.80  28.80  28.80  28.80  28.80  28.80   
	26   33.00  33.00  33.00  ...    33.00  33.00  33.00  33.00  33.00  33.00   
	27   35.10  35.10  35.10  ...    35.10  35.10  35.10  35.10  35.10  35.10   
	28   33.60  33.60  33.60  ...    33.60  33.60  33.60  33.60  33.60  33.60   
	29   32.00  32.00  32.00  ...    31.98  31.98  31.98  31.98  31.98  31.98   
	..     ...    ...    ...  ...      ...    ...    ...    ...    ...    ...   
	230  32.90  32.90  32.90  ...    38.80  38.80  38.80  38.80  38.80  38.80   
	231  28.80  28.80  28.80  ...    28.80  28.80  28.80  28.80  28.80  28.80   
	232  35.00  35.00  35.00  ...    35.00  35.00  35.00  35.00  35.00  35.00   
	233  24.00  24.00  24.00  ...    23.46  23.66  23.86  24.06  24.26  24.46   
	234    NaN    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN   
	235    NaN    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN   
	236  25.30  25.30  25.30  ...    25.30  25.30  25.30  25.30  25.30  25.30   
	237  36.60  36.60  36.60  ...    36.60  36.60  36.60  36.60  36.60  36.60   
	238  30.70  30.70  30.70  ...    30.70  30.70  30.70  30.70  30.70  30.70   
	239  43.22  40.05  40.35  ...    44.75  44.29  45.51  44.87  48.34  45.73   
	240  39.41  39.41  39.41  ...    45.21  45.58  45.95  46.33  46.70  47.07   
	241  32.90  32.90  32.90  ...    32.90  32.90  32.90  32.90  32.90  32.90   
	242    NaN    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN   
	243  26.93  26.93  26.93  ...    27.93  28.13  28.33  28.53  28.73  28.93   
	244    NaN    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN   
	245  24.30  24.30  24.30  ...    24.30  24.30  24.30  24.30  24.30  24.30   
	246  32.20  32.20  32.20  ...    32.20  32.20  32.20  32.20  32.20  32.20   
	247  32.10  32.10  32.10  ...    32.10  32.10  32.10  32.10  32.10  32.10   
	248    NaN    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN   
	249  34.75  34.75  34.75  ...    34.75  34.75  34.75  34.75  34.75  34.75   
	250  32.00  32.00  32.00  ...    32.00  32.00  32.00  32.00  32.00  32.00   
	251  33.40  33.40  33.40  ...    33.40  33.40  33.40  33.40  33.40  33.40   
	252    NaN    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN   
	253    NaN    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN   
	254  23.39  23.39  23.39  ...    23.39  23.39  23.39  23.39  23.39  23.39   
	255    NaN    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN   
	256  32.60  32.60  32.60  ...    32.60  32.60  32.60  32.60  32.60  32.60   
	257  33.70  33.70  33.70  ...    33.70  33.70  33.70  33.70  33.70  33.70   
	258    NaN    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN   
	259  26.67  26.67  26.67  ...    26.67  26.67  26.67  26.67  26.67  26.67   

		  1896   1897   1898   1899  
	0      NaN    NaN    NaN    NaN  
	1    27.23  27.22  27.21  27.20  
	2      NaN    NaN    NaN    NaN  
	3    35.40  35.40  35.40  35.40  
	4    28.82  28.82  28.82  28.82  
	5      NaN    NaN    NaN    NaN  
	6      NaN    NaN    NaN    NaN  
	7    26.98  26.98  26.98  26.98  
	8      NaN    NaN    NaN    NaN  
	9    33.54  33.54  33.54  33.54  
	10   34.00  34.70  35.40  36.10  
	11   36.20  36.40  36.23  36.06  
	12   34.42  34.42  34.42  34.42  
	13   47.81  48.34  48.87  49.40  
	14   39.65  40.12  40.59  41.06  
	15   31.37  31.57  31.40  31.23  
	16   35.18  35.18  35.18  35.18  
	17   30.30  30.30  30.30  30.30  
	18   20.00  19.00  21.86  21.82  
	19   32.12  32.12  32.12  32.12  
	20   36.20  36.20  36.20  36.20  
	21   48.06  48.82  48.12  46.49  
	22   26.50  26.50  26.50  26.50  
	23   31.00  31.00  31.00  31.00  
	24     NaN    NaN    NaN    NaN  
	25   28.80  28.80  28.80  28.80  
	26   33.00  33.00  33.00  33.00  
	27   35.10  35.10  35.10  35.10  
	28   33.60  33.60  33.60  33.60  
	29   31.98  31.98  31.98  31.98  
	..     ...    ...    ...    ...  
	230  38.80  38.80  38.80  38.80  
	231  28.80  28.80  28.80  28.80  
	232  35.00  35.00  35.00  35.00  
	233  24.66  24.86  24.69  24.52  
	234    NaN    NaN    NaN    NaN  
	235    NaN    NaN    NaN    NaN  
	236  25.30  25.30  25.30  25.30  
	237  36.60  36.60  36.60  36.60  
	238  30.70  30.70  30.70  30.70  
	239  47.41  47.23  46.98  46.13  
	240  47.44  47.81  48.18  48.56  
	241  32.90  32.90  32.90  32.90  
	242    NaN    NaN    NaN    NaN  
	243  29.13  29.33  29.16  28.99  
	244    NaN    NaN    NaN    NaN  
	245  24.30  24.30  24.30  24.30  
	246  32.20  32.20  32.20  32.20  
	247  32.10  32.10  32.10  32.10  
	248    NaN    NaN    NaN    NaN  
	249  34.75  34.75  34.75  34.75  
	250  32.00  32.00  32.00  32.00  
	251  33.40  33.40  33.40  33.40  
	252    NaN    NaN    NaN    NaN  
	253    NaN    NaN    NaN    NaN  
	254  23.39  23.39  23.39  23.39  
	255    NaN    NaN    NaN    NaN  
	256  32.60  32.60  32.60  32.60  
	257  33.70  33.70  33.70  33.70  
	258    NaN    NaN    NaN    NaN  
	259  26.67  26.67  26.67  26.67  

	[260 rows x 101 columns]>

	In [3]: print(g1800s.columns)
	Index(['Life expectancy', '1800', '1801', '1802', '1803', '1804', '1805',
		   '1806', '1807', '1808',
		   ...
		   '1890', '1891', '1892', '1893', '1894', '1895', '1896', '1897', '1898',
		   '1899'],
		  dtype='object', length=101)

	In [4]: print(g1800s.shape)
	(260, 101)

	In [5]: print(g1800s.info())
	<class 'pandas.core.frame.DataFrame'>
	RangeIndex: 260 entries, 0 to 259
	Columns: 101 entries, Life expectancy to 1899
	dtypes: float64(100), object(1)
	memory usage: 205.2+ KB
	None

Exactly! This information is provided by the g1800s.info(). 'Life expectancy' is the only column in the DataFrame that is not of type float64.  

---

## Visualizing your data  

Since 1800, life expectancy around the globe has been steadily going up. You would expect the Gapminder data to confirm this.  

The DataFrame g1800s has been pre-loaded. Your job in this exercise is to create a scatter plot with life expectancy in '1800' on the x-axis and life expectancy in '1899' on the y-axis.  

Here, the goal is to visually check the data for insights as well as errors. When looking at the plot, pay attention to whether the scatter plot takes the form of a diagonal line, and which points fall below or above the diagonal line. This will inform how life expectancy in 1899 changed (or did not change) compared to 1800 for different countries. If points fall on a diagonal line, it means that life expectancy remained the same!  

### Instructions :

 - Import matplotlib.pyplot as plt.
 - Use the .plot() method on g1800s with kind='scatter' to create a scatter plot with '1800' on the x-axis and '1899' on the y-axis.
 - Display the plot.

```python
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

print(g1800s.head())

# Create the scatter plot
g1800s.plot(kind='scatter', x='1800', y='1899')

# Specify axis labels
plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

# Specify axis limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# Display the plot
plt.show()
```

### Results :  

	img : img/graph5.svg

	<script.py> output:
				 Life expectancy   1800   1801   1802   1803   1804   1805   1806  \
		0               Abkhazia    NaN    NaN    NaN    NaN    NaN    NaN    NaN   
		1            Afghanistan  28.21  28.20  28.19  28.18  28.17  28.16  28.15   
		2  Akrotiri and Dhekelia    NaN    NaN    NaN    NaN    NaN    NaN    NaN   
		3                Albania  35.40  35.40  35.40  35.40  35.40  35.40  35.40   
		4                Algeria  28.82  28.82  28.82  28.82  28.82  28.82  28.82   
		
			1807   1808  ...     1890   1891   1892   1893   1894   1895   1896  \
		0    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN    NaN   
		1  28.14  28.13  ...    27.29  27.28  27.27  27.26  27.25  27.24  27.23   
		2    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN    NaN   
		3  35.40  35.40  ...    35.40  35.40  35.40  35.40  35.40  35.40  35.40   
		4  28.82  28.82  ...    28.82  28.82  28.82  28.82  28.82  28.82  28.82   
		
			1897   1898   1899  
		0    NaN    NaN    NaN  
		1  27.22  27.21  27.20  
		2    NaN    NaN    NaN  
		3  35.40  35.40  35.40  
		4  28.82  28.82  28.82  
		
		[5 rows x 101 columns]

Excellent work! As you can see, there are a surprising number of countries that fall on the diagonal line. In fact, examining the DataFrame reveals that the life expectancy for 140 of the 260 countries did not change at all in the 19th century! This is possibly a result of not having access to the data for all the years back then. In this way, visualizing your data can help you uncover insights as well as diagnose it for errors.  

---

## Loading and viewing your data

Since you are given life expectancy level data by country and year, you could ask questions about how much the average life expectancy changes over each year.  

Before continuing, however, it's important to make sure that the following assumptions about the data are true:  

 - 'Life expectancy' is the first column (index 0) of the DataFrame.  
 - The other columns contain either null or numeric values.  
 - The numeric values are all greater than or equal to 0.  
 - There is only one instance of each country.  

You can write a function that you can apply over the entire DataFrame to verify some of these assumptions. Note that spending the time to write such a script will help you when working with other datasets as well.  

### Instructions :

 - Define a function called check_null_or_valid() that takes in one argument: row_data.
 - Inside the function, convert no_na to a numeric data type using pd.to_numeric().
 - Write an assert statement to make sure the first column (index 0) of the g1800s DataFrame is 'Life expectancy'.
 - Write an assert statement to test that all the values are valid for the g1800s DataFrame. Use the check_null_or_valid() function placed inside the .apply() method for this. Note that because you're applying it over the entire DataFrame, and not just one column, you'll have to chain the .all() method twice, and remember that you don't have to use () for functions placed inside .apply().
 - Write an assert statement to make sure that each country occurs only once in the data. Use the .value_counts() method on the 'Life expectancy' column for this. Specifically, index 0 of .value_counts() will contain the most frequently occuring value. If this is equal to 1 for the 'Life expectancy' column, then you can be certain that no country appears more than once in the data.

```python
def check_null_or_valid(row_data):
    """Function that takes a row of data,
    drops all missing values,
    and checks if all remaining values are greater than or equal to 0
    """
    no_na = row_data.dropna()[1:-1]
    numeric = pd.to_numeric(no_na)
    ge0 = numeric >= 0
    return ge0

# Check whether the first column is 'Life expectancy'
assert g1800s.columns[0] == 'Life expectancy'

# Check whether the values in the row are valid
assert g1800s.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()

# Check that there is only one instance of each country
assert g1800s['Life expectancy'].value_counts()[0] == 1

```

### Results :  

	

---



## Assembling your data    

Here, three DataFrames have been pre-loaded: g1800s, g1900s, and g2000s. These contain the Gapminder life expectancy data for, respectively, the 19th century, the 20th century, and the 21st century.  

Your task in this exercise is to concatenate them into a single DataFrame called gapminder. This is a row-wise concatenation, similar to how you concatenated the monthly Uber datasets in Chapter 3.  

### Instructions :

 - Use pd.concat() to concatenate g1800s, g1900s, and g2000s into one DataFrame called gapminder. Make sure you pass DataFrames to pd.concat() in the form of a list.
 - Print the shape and the head of the concatenated DataFrame.

```python
# Concatenate the DataFrames row-wise
gapminder = pd.concat([g1800s,g1900s,g2000s])

# Print the shape of gapminder
print(gapminder.shape)

# Print the head of gapminder
print(gapminder.head())
```

### Results :  

	<script.py> output:
		(780, 218)
			1800   1801   1802   1803   1804   1805   1806   1807   1808   1809  \
		0    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN   
		1  28.21  28.20  28.19  28.18  28.17  28.16  28.15  28.14  28.13  28.12   
		2    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN   
		3  35.40  35.40  35.40  35.40  35.40  35.40  35.40  35.40  35.40  35.40   
		4  28.82  28.82  28.82  28.82  28.82  28.82  28.82  28.82  28.82  28.82   
		
				   ...            2008  2009  2010  2011  2012  2013  2014  2015  \
		0          ...             NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   
		1          ...             NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   
		2          ...             NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   
		3          ...             NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   
		4          ...             NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   
		
		   2016        Life expectancy  
		0   NaN               Abkhazia  
		1   NaN            Afghanistan  
		2   NaN  Akrotiri and Dhekelia  
		3   NaN                Albania  
		4   NaN                Algeria  
		
		[5 rows x 218 columns]
		
Great work! All the Gapminder data, from 1800 to 2016, is now contained in one DataFrame.  

---

## Reshaping your data  

Now that you have all the data combined into a single DataFrame, the next step is to reshape it into a tidy data format.  

Currently, the gapminder DataFrame has a separate column for each year. What you want instead is a single column that contains the year, and a single column that represents the average life expectancy for each year and country. By having year in its own column, you can use it as a predictor variable in a later analysis.  

You can convert the DataFrame into the desired tidy format by melting it.  

### Instructions :

 - Reshape gapminder by melting it. Keep 'Life expectancy' fixed by specifying it as an argument to the id_vars parameter.
 - Rename the three columns of the melted DataFrame to 'country', 'year', and 'life_expectancy' by passing them in as a list to gapminder_melt.columns.
 - Print the head of the melted DataFrame.

```python
print(gapminder.head())

# Melt gapminder: gapminder_melt
gapminder_melt = pd.melt(frame=gapminder,id_vars='Life expectancy')

# Rename the columns
gapminder_melt.columns = ['country','year','life_expectancy']

# Print the head of gapminder_melt
print(gapminder_melt.head())
```

### Results :  

	<script.py> output:
			1800   1801   1802   1803   1804   1805   1806   1807   1808   1809  \
		0    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN   
		1  28.21  28.20  28.19  28.18  28.17  28.16  28.15  28.14  28.13  28.12   
		2    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN    NaN   
		3  35.40  35.40  35.40  35.40  35.40  35.40  35.40  35.40  35.40  35.40   
		4  28.82  28.82  28.82  28.82  28.82  28.82  28.82  28.82  28.82  28.82   
		
				   ...            2008  2009  2010  2011  2012  2013  2014  2015  \
		0          ...             NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   
		1          ...             NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   
		2          ...             NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   
		3          ...             NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   
		4          ...             NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   
		
		   2016        Life expectancy  
		0   NaN               Abkhazia  
		1   NaN            Afghanistan  
		2   NaN  Akrotiri and Dhekelia  
		3   NaN                Albania  
		4   NaN                Algeria  
		
		[5 rows x 218 columns]
						 country  year  life_expectancy
		0               Abkhazia  1800              NaN
		1            Afghanistan  1800            28.21
		2  Akrotiri and Dhekelia  1800              NaN
		3                Albania  1800            35.40
		4                Algeria  1800            28.82
		
Well done! Having the data in this tidy format will make subsequent analysis far easier.  

---

## Checking the data types  

Now that your data is in the proper shape, you need to ensure that the columns are of the proper data type. That is, you need to ensure that country is of type object, year is of type int64, and life_expectancy is of type float64.  

The tidy DataFrame has been pre-loaded as gapminder. Explore it in the IPython Shell using the .info() method. Notice that the column 'year' is of type object. This is incorrect, so you'll need to use the pd.to_numeric() function to convert it to a numeric data type.  

NumPy and pandas have been pre-imported as np and pd.  

### Instructions :

 - Convert the year column of gapminder using pd.to_numeric().
 - Assert that the country column is of type np.object. This has been done for you.
 - Assert that the year column is of type np.int64.
 - Assert that the life_expectancy column is of type np.float64.

```python
print(gapminder.dtypes)
print('---------------')
# Convert the year column to numeric
gapminder.year = pd.to_numeric(gapminder.year)

# Test if country is of type object
assert gapminder.country.dtypes == np.object

# Test if year is of type int64
assert gapminder.year.dtypes == np.int64

# Test if life_expectancy is of type float64
assert gapminder.life_expectancy.dtypes == np.float64

print(gapminder.dtypes)
```

### Results :  

	<script.py> output:
		country             object
		year                object
		life_expectancy    float64
		dtype: object
		---------------
		country             object
		year                 int64
		life_expectancy    float64
		dtype: object

Excellent work! Since the assert statements did not throw any errors, you can be sure that your columns have the correct data types!  		
		
---



## Looking at country spellings  

Having tidied your DataFrame and checked the data types, your next task in the data cleaning process is to look at the 'country' column to see if there are any special or invalid characters you may need to deal with.  

It is reasonable to assume that country names will contain:  

 - The set of lower and upper case letters.
 - Whitespace between words.
 - Periods for any abbreviations.
 
To confirm that this is the case, you can leverage the power of regular expressions again. For common operations like this, Python has a built-in string method - str.contains() - which takes a regular expression pattern, and applies it to the Series, returning True if there is a match, and False otherwise.  

Since here you want to find the values that do not match, you have to invert the boolean, which can be done using ~. This Boolean series can then be used to get the Series of countries that have invalid names.  
 
### Instructions :

 - Create a Series called countries consisting of the 'country' column of gapminder.
 - Drop all duplicates from countries using the .drop_duplicates() method.
 - Write a regular expression that tests your assumptions of what characters belong in countries:
	 - Anchor the pattern to match exactly what you want by placing a ^ in the beginning and $ in the end.
	 - Use A-Za-z to match the set of lower and upper case letters, \. to match periods, and \s to match whitespace between words.
 - Use str.contains() to create a Boolean vector representing values that match the pattern.
 - Invert the mask by placing a ~ before it.
 - Subset the countries series using the .loc[] accessor and mask_inverse. Then hit 'Submit Answer' to see the invalid country names!

```python
# Create the series of countries: countries
countries = gapminder.country
print(countries.head())
print('-----------------')

# Drop all the duplicates from countries
countries = countries.drop_duplicates()

# Write the regular expression: pattern
pattern = '^[A-Za-z\.\s]*$'

# Create the Boolean vector: mask
mask = countries.str.contains(pattern)

# Invert the mask: mask_inverse
mask_inverse = ~mask

# Subset countries using mask_inverse: invalid_countries
invalid_countries = countries.loc[mask_inverse]

# Print invalid_countries
print(invalid_countries)
```

### Results :  

	<script.py> output:
		0                 Abkhazia
		1              Afghanistan
		2    Akrotiri and Dhekelia
		3                  Albania
		4                  Algeria
		Name: country, dtype: object
		-----------------
		49            Congo, Dem. Rep.
		50                 Congo, Rep.
		53               Cote d'Ivoire
		73      Falkland Is (Malvinas)
		93               Guinea-Bissau
		98            Hong Kong, China
		118    United Korea (former)\n
		131               Macao, China
		132             Macedonia, FYR
		145      Micronesia, Fed. Sts.
		161            Ngorno-Karabakh
		187             St. Barthélemy
		193     St.-Pierre-et-Miquelon
		225                Timor-Leste
		251      Virgin Islands (U.S.)
		252       North Yemen (former)
		253       South Yemen (former)
		258                      Åland
		Name: country, dtype: object

Excellent work! As you can see, not all these country names are actually invalid so maybe the assumptions need to be tweaked a little. However, there certainly are a few cases worth further investigation, such as St. Barth?lemy. Whenever you are dealing with columns of raw data consisting of strings, it is important to check them for consistency like this.  

---

## More data cleaning and processing  

It's now time to deal with the missing data. There are several strategies for this: You can drop them, fill them in using the mean of the column or row that the missing value is in (also known as imputation), or, if you are dealing with time series data, use a forward fill or backward fill, in which you replace missing values in a column with the most recent known value in the column. See pandas Foundations for more on forward fill and backward fill.  

In general, it is not the best idea to drop missing values, because in doing so you may end up throwing away useful information. In this data, the missing values refer to years where no estimate for life expectancy is available for a given country. You could fill in, or guess what these life expectancies could be by looking at the average life expectancies for other countries in that year, for example. Whichever strategy you go with, it is important to carefully consider all options and understand how they will affect your data.  

In this exercise, you'll practice dropping missing values. Your job is to drop all the rows that have NaN in the life_expectancy column. Before doing so, it would be valuable to use assert statements to confirm that year and country do not have any missing values.  

Begin by printing the shape of gapminder in the IPython Shell prior to dropping the missing values. Complete the exercise to find out what its shape will be after dropping the missing values!  

### Instructions :

 - Assert that country and year do not contain any missing values. The first assert statement has been written for you. Note the chaining of the .all() method to pd.notnull() to confirm that all values in the column are not null.
 - Drop the rows in the data where any observation in life_expectancy is missing. As you confirmed that country and year don't have missing values, you can use the .dropna() method on the entire gapminder DataFrame, because any missing values would have to be in the life_expectancy column. The .dropna() method has the default keyword arguments axis=0 and how='any', which specify that rows with any missing values should be dropped.
 - Print the shape of gapminder.

```python
print(gapminder.shape)
print('------------')
# Assert that country does not contain any missing values
assert pd.notnull(gapminder.country).all()

# Assert that year does not contain any missing values
assert pd.notnull(gapminder.year).all()

# Drop the missing values
gapminder = gapminder.dropna()

# Print the shape of gapminder
print(gapminder.shape)

```

### Results :  

	<script.py> output:
		(169260, 3)
		------------
		(43857, 3)

		
Great work! After dropping the missing values from 'life_expectancy', the number of rows in the DataFrame has gone down from 169260 to 43857. In general, you should avoid dropping too much of your data, but if there is no reasonable way to fill in or impute missing values, then dropping the missing data may be the best solution.  
		
---

## Wrapping up  

Now that you have a clean and tidy dataset, you can do a bit of visualization and aggregation. In this exercise, you'll begin by creating a histogram of the life_expectancy column. You should not get any values under 0 and you should see something reasonable on the higher end of the life_expectancy age range.  

Your next task is to investigate how average life expectancy changed over the years. To do this, you need to subset the data by each year, get the life_expectancy column from each subset, and take an average of the values. You can achieve this using the .groupby() method. This .groupby() method is covered in greater depth in Manipulating DataFrames with pandas.  

Finally, you can save your tidy and summarized DataFrame to a file using the .to_csv() method.  

Matplotlib and pandas have been pre-imported as plt and pd. Go for it!  

### Instructions :

 - Create a histogram of the life_expectancy column using the .plot() method of gapminder. Specify kind='hist'.
 - Group gapminder by 'year' and aggregate 'life_expectancy' by the mean. To do this:
	- Use the .groupby() method on gapminder with 'year' as the argument. Then select 'life_expectancy' and chain the .mean() method to it.
 - Print the head and tail of gapminder_agg. This has been done for you.
 - Create a line plot of average life expectancy per year by using the .plot() method (without any arguments) on gapminder_agg.
 - Save gapminder and gapminder_agg to csv files called 'gapminder.csv' and 'gapminder_agg.csv', respectively, using the .to_csv() method.

```python
# Add first subplot
plt.subplot(2, 1, 1) 

# Create a histogram of life_expectancy
gapminder.life_expectancy.plot(kind='hist')

# Group gapminder: gapminder_agg
gapminder_agg = gapminder.groupby('year')['life_expectancy'].mean()

# Print the head of gapminder_agg
print(gapminder_agg.head())

# Print the tail of gapminder_agg
print(gapminder_agg.tail())

# Add second subplot
plt.subplot(2, 1, 2)

# Create a line plot of life expectancy per year
gapminder_agg.plot(x='year',y='life_expectancy')

# Add title and specify axis labels
plt.title('Life expectancy over the years')
plt.ylabel('Life expectancy')
plt.xlabel('Year')

# Display the plots
plt.tight_layout()
plt.show()
```

### Results :  

	graph : img/graph6;svg
	<script.py> output:
		year
		1800    31.486020
		1801    31.448905
		1802    31.463483
		1803    31.377413
		1804    31.446318
		Name: life_expectancy, dtype: float64
		year
		2012    71.663077
		2013    71.916106
		2014    72.088125
		2015    72.321010
		2016    72.556635
		Name: life_expectancy, dtype: float64

Amazing work! You've stepped through each stage of the data cleaning process and your data is now ready for serious analysis! Looking at the line plot, it seems like life expectancy has, as expected, increased over the years. There is a surprising dip around 1920 that may be worth further investigation!  

---