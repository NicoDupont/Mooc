"""
Datacamp - Manipulating DataFrames with pandas
https://www.datacamp.com/courses/manipulating-dataframes-with-pandas
Part 4 : Grouping data
Python 3.X
"""



"""
In this chapter, you'll learn how to identify and split DataFrames by groups or categories for further aggregation or analysis.
You'll also learn how to transform and filter your data, including how to detect outliers and impute missing values.
Knowing how to effectively group data in pandas can be a seriously powerful addition to your data science toolbox.
"""



""" answer : 3
Advantages of categorical data types
50xp
What are the main advantages of storing data explicitly as categorical types instead of object types?

Possible Answers
Computations are faster. 1
Categorical data require less space in memory. 2
All of the above. 3
None of the above. 4
"""




"""
Grouping by multiple columns
100xp
In this exercise, you will return to working with the Titanic dataset from Chapter 1 and use .groupby() to analyze the distribution of passengers who boarded the Titanic.

The 'pclass' column identifies which class of ticket was purchased by the passenger and the 'embarked' column indicates at which of the three ports the passenger boarded the Titanic. 'S' stands for Southampton, England, 'C' for Cherbourg, France and 'Q' for Queenstown, Ireland.

Your job is to first group by the 'pclass' column and count the number of rows in each class using the 'survived' column. You will then group by the 'embarked' and 'pclass' columns and count the number of passengers.

The DataFrame has been pre-loaded as titanic.

Instructions
Group by the 'pclass' column and save the result as by_class.
Aggregate the 'survived' column of by_class using .count(). Save the result as count_by_class.
Print count_by_class. This has been done for you.
Group titanic by the 'embarked' and 'pclass' columns. Save the result as by_mult.
Aggregate the 'survived' column of by_mult using .count(). Save the result as count_mult.
Print count_mult. This has been done for you, so hit 'Submit Answer' to view the result.
"""
# Group titanic by 'pclass'
by_class = titanic.groupby('pclass')

# Aggregate 'survived' column of by_class by count
count_by_class = by_class['survived'].count()

# Print count_by_class
print(count_by_class)
print('----------------')

# Group titanic by 'embarked' and 'pclass'
by_mult = titanic.groupby(['embarked','pclass'])

# Aggregate 'survived' column of by_mult by count
count_mult = by_mult['survived'].count()

# Print count_mult
print(count_mult)
""" results or consol output
In [1]: titanic.head()
Out[1]:
   pclass  survived                                             name     sex  \
0       1         1                    Allen, Miss. Elisabeth Walton  female
1       1         1                   Allison, Master. Hudson Trevor    male
2       1         0                     Allison, Miss. Helen Loraine  female
3       1         0             Allison, Mr. Hudson Joshua Creighton    male
4       1         0  Allison, Mrs. Hudson J C (Bessie Waldo Daniels)  female

     age  sibsp  parch  ticket      fare    cabin embarked boat   body  \
0  29.00      0      0   24160  211.3375       B5        S    2    NaN
1   0.92      1      2  113781  151.5500  C22 C26        S   11    NaN
2   2.00      1      2  113781  151.5500  C22 C26        S  NaN    NaN
3  30.00      1      2  113781  151.5500  C22 C26        S  NaN  135.0
4  25.00      1      2  113781  151.5500  C22 C26        S  NaN    NaN

                         home.dest
0                     St Louis, MO
1  Montreal, PQ / Chesterville, ON
2  Montreal, PQ / Chesterville, ON
3  Montreal, PQ / Chesterville, ON
4  Montreal, PQ / Chesterville, ON

<script.py> output:
    pclass
    1    323
    2    277
    3    709
    Name: survived, dtype: int64
    ----------------
    embarked  pclass
    C         1         141
              2          28
              3         101
    Q         1           3
              2           7
              3         113
    S         1         177
              2         242
              3         495
    Name: survived, dtype: int64
"""






"""
Grouping by another series
100xp
In this exercise, you'll use two data sets from Gapminder.org to investigate the average life expectancy (in years) at birth in 2010 for the 6 continental regions. To do this you'll read the life expectancy data per country into one pandas DataFrame and the association between country and region into another.

By setting the index of both DataFrames to the country name, you'll then use the region information to group the countries in the life expectancy DataFrame and compute the mean value for 2010.

The life expectancy CSV file is available to you in the variable life_fname and the regions filename is available in the variable regions_fname.

Instructions
Read life_fname into a DataFrame called life and set the index to 'Country'.
Read regions_fname into a DataFrame called regions and set the index to 'Country'.
Group life by the region column of regions and store the result in life_by_region.
Print the mean over the 2010 column of life_by_region.
"""
# Read life_fname into a DataFrame: life
life = pd.read_csv(life_fname, index_col='Country')
print(life.head())
print('----------')
# Read regions_fname into a DataFrame: regions
regions = pd.read_csv(regions_fname, index_col='Country')
print(regions.head())
print('----------')
# Group life by regions['region']: life_by_region
life_by_region = life.groupby(regions['region'])

# Print the mean over the '2010' column of life_by_region
print(life_by_region['2010'].mean())

""" results or consol output
<script.py> output:
                           1964    1965    1966    1967    1968    1969    1970  \
    Country
    Afghanistan          33.639  34.152  34.662  35.170  35.674  36.172  36.663
    Albania              65.475  65.863  66.122  66.316  66.500  66.702  66.948
    Algeria              47.953  48.389  48.806  49.205  49.592  49.976  50.366
    Angola               34.604  35.007  35.410  35.816  36.222  36.627  37.032
    Antigua and Barbuda  63.775  64.149  64.511  64.865  65.213  65.558  65.898

                           1971    1972    1973   ...      2004    2005    2006  \
    Country                                       ...
    Afghanistan          37.143  37.614  38.075   ...    56.583  57.071  57.582
    Albania              67.251  67.595  67.966   ...    75.725  75.949  76.124
    Algeria              50.767  51.195  51.670   ...    69.682  69.854  70.020
    Angola               37.439  37.846  38.247   ...    48.036  48.572  49.041
    Antigua and Barbuda  66.232  66.558  66.875   ...    74.355  74.544  74.729

                           2007    2008    2009    2010    2011    2012    2013
    Country
    Afghanistan          58.102  58.618  59.124  59.612  60.079  60.524  60.947
    Albania              76.278  76.433  76.598  76.780  76.979  77.185  77.392
    Algeria              70.180  70.332  70.477  70.615  70.747  70.874  71.000
    Angola               49.471  49.882  50.286  50.689  51.094  51.498  51.899
    Antigua and Barbuda  74.910  75.087  75.263  75.437  75.610  75.783  75.954

    [5 rows x 50 columns]
    ----------
                                             region
    Country
    Afghanistan                          South Asia
    Albania                   Europe & Central Asia
    Algeria              Middle East & North Africa
    Angola                       Sub-Saharan Africa
    Antigua and Barbuda                     America
    ----------
    region
    America                       74.037350
    East Asia & Pacific           73.405750
    Europe & Central Asia         75.656387
    Middle East & North Africa    72.805333
    South Asia                    68.189750
    Sub-Saharan Africa            57.575080
    Name: 2010, dtype: float64
"""






"""
Computing multiple aggregates of multiple columns
100xp
The .agg() method can be used with a tuple or list of aggregations as input. When applying multiple aggregations on multiple columns, the aggregated DataFrame has a multi-level column index.

In this exercise, you're going to group passengers on the Titanic by 'pclass' and aggregate the 'age' and 'fare' columns by the functions 'max' and 'median'. You'll then use multi-level selection to find the oldest passenger per class and the median fare price per class.

The DataFrame has been pre-loaded as titanic.

Instructions
Group titanic by 'pclass' and save the result as by_class.
Select the 'age' and 'fare' columns from by_class and save the result as by_class_sub.
Aggregate by_class_sub using 'max' and 'median'. You'll have to pass 'max' and 'median' in the form of a list to .agg().
Use .loc[] to print all of the rows and the column specification ('age','max'). This has been done for you.
Use .loc[] to print all of the rows and the column specification ('fare','median').
"""
print(titanic.head())
print('------------------------------')
# Group titanic by 'pclass': by_class
by_class = titanic.groupby('pclass')

# Select 'age' and 'fare'
by_class_sub = by_class[['age','fare']]

# Aggregate by_class_sub by 'max' and 'median': aggregated
aggregated = by_class_sub.agg(['max','median'])
print('------------------------------')
# Print the maximum age in each class
print(aggregated.loc[:, ('age','max')])
print('------------------------------')
# Print the medium fare in each class
print(aggregated.loc[:,('fare','median')])
""" results or consol output
<script.py> output:
       pclass  survived                                             name     sex  \
    0       1         1                    Allen, Miss. Elisabeth Walton  female
    1       1         1                   Allison, Master. Hudson Trevor    male
    2       1         0                     Allison, Miss. Helen Loraine  female
    3       1         0             Allison, Mr. Hudson Joshua Creighton    male
    4       1         0  Allison, Mrs. Hudson J C (Bessie Waldo Daniels)  female

         age  sibsp  parch  ticket      fare    cabin embarked boat   body  \
    0  29.00      0      0   24160  211.3375       B5        S    2    NaN
    1   0.92      1      2  113781  151.5500  C22 C26        S   11    NaN
    2   2.00      1      2  113781  151.5500  C22 C26        S  NaN    NaN
    3  30.00      1      2  113781  151.5500  C22 C26        S  NaN  135.0
    4  25.00      1      2  113781  151.5500  C22 C26        S  NaN    NaN

                             home.dest
    0                     St Louis, MO
    1  Montreal, PQ / Chesterville, ON
    2  Montreal, PQ / Chesterville, ON
    3  Montreal, PQ / Chesterville, ON
    4  Montreal, PQ / Chesterville, ON
    ------------------------------
    ------------------------------
    pclass
    1    80.0
    2    70.0
    3    74.0
    Name: (age, max), dtype: float64
    ------------------------------
    pclass
    1    60.0000
    2    15.0458
    3     8.0500
    Name: (fare, median), dtype: float64
"""






"""
Aggregating on index levels/fields
100xp
If you have a DataFrame with a multi-level row index, the individual levels can be used to perform the groupby. This allows advanced aggregation techniques to be applied along one or more levels in the index and across one or more columns.

In this exercise you'll use the full Gapminder dataset which contains yearly values of life expectancy, population, child mortality (per 1,000) and per capita gross domestic product (GDP) for every country in the world from 1964 to 2013.

Your job is to create a multi-level DataFrame of the columns 'Year', 'Region' and 'Country'. Next you'll group the DataFrame by the 'Year' and 'Region' levels. Finally, you'll apply a dictionary aggregation to compute the total population, spread of per capita GDP values and average child mortality rate.

The Gapminder CSV file is is available as 'gapminder.csv'.

Instructions
Read 'gapminder.csv' into a DataFrame with index_col=['Year','region','Country']. Sort the index.
Group gapminder with a level of ['Year','region']. Save the result as by_year_region.
Define the function spread which returns the maximum and minimum of an input series. This has been done for you.
Create a dictionary with 'population':'sum', 'child_mortality':'mean' and 'gdp':spread as aggregator. This has been done for you.
Use the dictionary to aggregate by_year_region. Save the result as aggregated.
Print the last 6 entries of aggregated. This has been done for you, so hit 'Submit Answer' to view the result.
"""
# Read the CSV file into a DataFrame and sort the index: gapminder
gapminder = pd.read_csv('gapminder.csv',index_col=['Year','region','Country']).sort_index()
print(type(gapminder))
print(gapminder.columns)
print('--------------')
print(gapminder.info())
print('--------------')
# Group gapminder by 'Year' and 'region: by_year_region
by_year_region = gapminder.groupby(level=['Year','region'])

# Define the function to compute spread: spread
def spread(series):
    return series.max() - series.min()

# Create the dictionary: aggregator
aggregator = {'population':'sum', 'child_mortality':'mean', 'gdp':spread}

# Aggregate by_year_region using the dictionary: aggregated
aggregated = by_year_region.agg(aggregator)

# Print the last 6 entries of aggregated
print(aggregated.tail(6))
""" results or consol output
<script.py> output:
    <class 'pandas.core.frame.DataFrame'>
    Index(['fertility', 'life', 'population', 'child_mortality', 'gdp'], dtype='object')
    --------------
    <class 'pandas.core.frame.DataFrame'>
    MultiIndex: 10111 entries, (1964, America, Antigua and Barbuda) to (2013, Sub-Saharan Africa, Zimbabwe)
    Data columns (total 5 columns):
    fertility          10100 non-null float64
    life               10111 non-null float64
    population         10108 non-null float64
    child_mortality    9210 non-null float64
    gdp                9000 non-null float64
    dtypes: float64(5)
    memory usage: 436.6+ KB
    None
    --------------
                                       population       gdp  child_mortality
    Year region
    2013 America                     9.629087e+08   49634.0        17.745833
         East Asia & Pacific         2.244209e+09  134744.0        22.285714
         Europe & Central Asia       8.968788e+08   86418.0         9.831875
         Middle East & North Africa  4.030504e+08  128676.0        20.221500
         South Asia                  1.701241e+09   11469.0        46.287500
         Sub-Saharan Africa          9.205996e+08   32035.0        76.944490
"""






"""
Grouping on a function of the index
100xp
Groubpy operations can also be performed on transformations of the index values. In the case of a DateTimeIndex, we can extract portions of the datetime over which to group.

In this exercise you'll read in a set of sample sales data from February 2015 and assign the 'Date' column as the index. Your job is to group the sales data by the day of the week and aggregate the sum of the 'Units' column.

Is there a day of the week that is more popular for customers? To find out, you're going to use .strftime('%a') to transform the index datetime values to abbreviated days of the week.

The sales data CSV file is available to you as 'sales.csv'.

Instructions
Read 'sales.csv' into a DataFrame with index_col='Date' and parse_dates=True.
Create a groupby object with sales.index.strftime('%a') as input and assign it to by_day.
Aggregate the 'Units' column of by_day with the .sum() method. Save the result as units_sum.
Print units_sum. This has been done for you, so hit 'Submit Answer' to see the result.
"""
# Read file: sales
sales = pd.read_csv('sales.csv',index_col='Date',parse_dates=True)
print(sales.head())
print('----------------')
# Create a groupby object: by_day
by_day = sales.groupby(sales.index.strftime('%a'))

# Create sum: units_sum
units_sum = by_day['Units'].sum()

# Print units_sum
print(units_sum)

""" results or consol output
<script.py> output:
                                 Company   Product  Units
    Date
    2015-02-02 08:30:00            Hooli  Software      3
    2015-02-02 21:00:00        Mediacore  Hardware      9
    2015-02-03 14:00:00          Initech  Software     13
    2015-02-04 15:30:00        Streeplex  Software     13
    2015-02-04 22:00:00  Acme Coporation  Hardware     14
    ----------------
    Mon    48
    Sat     7
    Thu    59
    Tue    13
    Wed    48
    Name: Units, dtype: int64
"""





"""
Detecting outliers with Z-Scores
100xp
As Dhavide demonstrated in the video using the zscore function, you can apply a .transform() method after grouping to apply a function to groups of data independently. The z-score is also useful to find outliers: a z-score value of +/- 3 is generally considered to be an outlier.

In this example, you're going to normalize the Gapminder data in 2010 for life expectancy and fertility by the z-score per region. Using boolean indexing, you will filter out countries that have high fertility rates and low life expectancy for their region.

The Gapminder DataFrame for 2010 indexed by 'Country' is provided for you as gapminder_2010.

Instructions
Import zscore from scipy.stats.
Group gapminder_2010 by 'region' and transform the ['life','fertility'] columns by zscore.
Construct a boolean Series of the bitwise or between standardized['life'] < -3 and standardized['fertility'] > 3.
Filter gapminder_2010 using .loc[] and the outliers Boolean Series. Save the result as gm_outliers.
Print gm_outliers. This has been done for you, so hit 'Submit Answer' to see the results.
"""
# Import zscore
from scipy.stats import zscore

# Group gapminder_2010: standardized
standardized = gapminder_2010.groupby('region')['life','fertility'].transform(zscore)

# Construct a Boolean Series to identify outliers: outliers
outliers = (standardized['life'] < -3) | (standardized['fertility'] > 3)

# Filter gapminder_2010 by the outliers: gm_outliers
gm_outliers = gapminder_2010.loc[outliers]
# Print gm_outliers
print(gm_outliers)
""" results or consol output
<script.py> output:
                 fertility    life  population  child_mortality     gdp  \
    Country
    Guatemala        3.974  71.100  14388929.0             34.5  6849.0
    Haiti            3.350  45.000   9993247.0            208.8  1518.0
    Tajikistan       3.780  66.830   6878637.0             52.6  2110.0
    Timor-Leste      6.237  65.952   1124355.0             63.8  1777.0

                                region
    Country
    Guatemala                  America
    Haiti                      America
    Tajikistan   Europe & Central Asia
    Timor-Leste    East Asia & Pacific
"""






"""
Filling missing data (imputation) by group
100xp
Many statistical and machine learning packages cannot determine the best action to take when missing data entries are encountered. Dealing with missing data is natural in pandas (both in using the default behavior and in defining a custom behavior). In Chapter 1, you practiced using the .dropna() method to drop missing values. Now, you will practice imputing missing values. You can use .groupby() and .transform() to fill missing data appropriately for each group.

Your job is to fill in missing 'age' values for passengers on the Titanic with the median age from their 'gender' and 'pclass'. To do this, you'll group by the 'sex' and 'pclass' columns and transform each group with a custom function to call .fillna() and impute the median value.

The DataFrame has been pre-loaded as titanic. Explore it in the IPython Shell by printing the output of titanic.tail(10). Notice in particular the NaNs in the 'age' column.

Instructions
Group titanic by 'sex' and 'pclass'. Save the result as by_sex_class.
Write a function called impute_median() that fills missing values with the median of a series. This has been done for you.
Call .transform() with impute_median on the 'age' column of by_sex_class.
Print the output of titanic.tail(10). This has been done for you - hit 'Submit Answer' to see how the missing values have now been imputed.
"""
# Create a groupby object: by_sex_class
by_sex_class = titanic.groupby(['sex','pclass'])

# Write a function that imputes median
def impute_median(series):
    return series.fillna(series.median())

# Impute age and assign to titanic['age']
titanic['age'] = by_sex_class['age'].transform(impute_median)

# Print the output of titanic.tail(10)
print(titanic.tail(10))

""" results or consol output
<script.py> output:
          pclass  survived                                     name     sex   age  \
    1299       3         0                      Yasbeck, Mr. Antoni    male  27.0
    1300       3         1  Yasbeck, Mrs. Antoni (Selini Alexander)  female  15.0
    1301       3         0                     Youseff, Mr. Gerious    male  45.5
    1302       3         0                        Yousif, Mr. Wazli    male  25.0
    1303       3         0                    Yousseff, Mr. Gerious    male  25.0
    1304       3         0                     Zabour, Miss. Hileni  female  14.5
    1305       3         0                    Zabour, Miss. Thamine  female  22.0
    1306       3         0                Zakarian, Mr. Mapriededer    male  26.5
    1307       3         0                      Zakarian, Mr. Ortin    male  27.0
    1308       3         0                       Zimmerman, Mr. Leo    male  29.0

          sibsp  parch  ticket     fare cabin embarked boat   body home.dest
    1299      1      0    2659  14.4542   NaN        C    C    NaN       NaN
    1300      1      0    2659  14.4542   NaN        C  NaN    NaN       NaN
    1301      0      0    2628   7.2250   NaN        C  NaN  312.0       NaN
    1302      0      0    2647   7.2250   NaN        C  NaN    NaN       NaN
    1303      0      0    2627  14.4583   NaN        C  NaN    NaN       NaN
    1304      1      0    2665  14.4542   NaN        C  NaN  328.0       NaN
    1305      1      0    2665  14.4542   NaN        C  NaN    NaN       NaN
    1306      0      0    2656   7.2250   NaN        C  NaN  304.0       NaN
    1307      0      0    2670   7.2250   NaN        C  NaN    NaN       NaN
    1308      0      0  315082   7.8750   NaN        S  NaN    NaN       NaN
"""






"""
Other transformations with .apply
100xp
The .apply() method when used on a groupby object performs an arbitrary function on each of the groups. These functions can be aggregations, transformations or more complex workflows. The .apply() method will then combine the results in an intelligent way.

In this exercise, you're going to analyze economic disparity within regions of the world using the Gapminder data set for 2010. To do this you'll define a function to compute the aggregate spread of per capita GDP in each region and the individual country's z-score of the regional per capita GDP. You'll then select three countries - United States, Great Britain and China - to see a summary of the regional GDP and that country's z-score against the regional mean.

The 2010 Gapminder DataFrame is provided for you as gapminder_2010. Pandas has been imported as pd.

The following function has been defined for your use:

def disparity(gr):
    # Compute the spread of gr['gdp']: s
    s = gr['gdp'].max() - gr['gdp'].min()
    # Compute the z-score of gr['gdp'] as (gr['gdp']-gr['gdp'].mean())/gr['gdp'].std(): z
    z = (gr['gdp'] - gr['gdp'].mean())/gr['gdp'].std()
    # Return a DataFrame with the inputs {'z(gdp)':z, 'regional spread(gdp)':s}
    return pd.DataFrame({'z(gdp)':z , 'regional spread(gdp)':s})
Instructions
Group gapminder_2010 by 'region'. Save the result as regional.
Apply the provided disparity function on regional, and save the result as reg_disp.
Use .loc[] to select ['United States','United Kingdom','China'] from reg_disp and print the results.
"""
# Group gapminder_2010 by 'region': regional
regional = gapminder_2010.groupby('region')

# Apply the disparity function on regional: reg_disp
reg_disp = regional.apply(disparity)

# Print the disparity of 'United States', 'United Kingdom', and 'China'
print(reg_disp.loc[('United States','United Kingdom','China'),:])
""" results or consol output
<script.py> output:
                    regional spread(gdp)    z(gdp)
    Country
    United States                47855.0  3.013374
    United Kingdom               89037.0  0.572873
    China                        96993.0 -0.432756
"""






"""
Grouping and filtering with .apply()
100xp

By using .apply(), you can write functions that filter rows within groups. The .apply() method will handle the iteration over individual groups and then re-combine them back into a Series or DataFrame.

In this exercise you'll take the Titanic data set and analyze survival rates from the 'C' deck, which contained the most passengers. To do this you'll group the dataset by 'sex' and then use the .apply() method on a provided user defined function which calculates the mean survival rates on the 'C' deck:

def c_deck_survival(gr):

    c_passengers = gr['cabin'].str.startswith('C').fillna(False)

    return gr.loc[c_passengers, 'survived'].mean()

The DataFrame has been pre-loaded as titanic.
Instructions

    Group titanic by 'sex'. Save the result as by_sex.
    Apply the provided c_deck_survival function on the by_sex DataFrame. Save the result as c_surv_by_sex.
    Print c_surv_by_sex.

"""
print(titanic.head())
print('----------------')
# Create a groupby object using titanic over the 'sex' column: by_sex
by_sex = titanic.groupby('sex')

# Call by_sex.apply with the function c_deck_survival and print the result
c_surv_by_sex = by_sex.apply(c_deck_survival)

# Print the survival rates
print(c_surv_by_sex)

""" results or consol output
<script.py> output:
       pclass  survived                                             name     sex  \
    0       1         1                    Allen, Miss. Elisabeth Walton  female
    1       1         1                   Allison, Master. Hudson Trevor    male
    2       1         0                     Allison, Miss. Helen Loraine  female
    3       1         0             Allison, Mr. Hudson Joshua Creighton    male
    4       1         0  Allison, Mrs. Hudson J C (Bessie Waldo Daniels)  female

         age  sibsp  parch  ticket      fare    cabin embarked boat   body  \
    0  29.00      0      0   24160  211.3375       B5        S    2    NaN
    1   0.92      1      2  113781  151.5500  C22 C26        S   11    NaN
    2   2.00      1      2  113781  151.5500  C22 C26        S  NaN    NaN
    3  30.00      1      2  113781  151.5500  C22 C26        S  NaN  135.0
    4  25.00      1      2  113781  151.5500  C22 C26        S  NaN    NaN

                             home.dest
    0                     St Louis, MO
    1  Montreal, PQ / Chesterville, ON
    2  Montreal, PQ / Chesterville, ON
    3  Montreal, PQ / Chesterville, ON
    4  Montreal, PQ / Chesterville, ON
    ----------------
    sex
    female    0.913043
    male      0.312500
    dtype: float64
"""




"""
Grouping and filtering with .filter()
100xp

You can use groupby with the .filter() method to remove whole groups of rows from a DataFrame based a boolean condition.

In this exercise, you'll take the February sales data and remove entries from companies that purchased less than 35 Units in the whole month.

First, you'll identify how many units each company bought for verification. Next you'll use the .filter() method after grouping by 'Company' to remove all rows belonging to companies whose sum over the 'Units' column was less than 35. Finally, verify that the three companies whose total Units purchased were less than 35 have been filtered out from the DataFrame.
Instructions

    Group sales by 'Company'. Save the result as by_company.
    Compute and print the sum of the 'Units' column of by_company.
    Call .filter() on by_company with lambda g:g['Units'].sum() > 35 as input and print the result.

"""
# Read the CSV file into a DataFrame: sales
sales = pd.read_csv('sales.csv', index_col='Date', parse_dates=True)
print(sales.head())
print('----------------')
# Group sales by 'Company': by_company
by_company = sales.groupby('Company')

# Compute the sum of the 'Units' of by_company: by_com_sum
by_com_sum = by_company['Units'].sum()
print(by_com_sum)

# Filter 'Units' where the sum is > 35: by_com_filt
by_com_filt = by_company.filter(lambda g:g['Units'].sum() > 35)
print(by_com_filt)

""" results or consol output
<script.py> output:
                                 Company   Product  Units
    Date
    2015-02-02 08:30:00            Hooli  Software      3
    2015-02-02 21:00:00        Mediacore  Hardware      9
    2015-02-03 14:00:00          Initech  Software     13
    2015-02-04 15:30:00        Streeplex  Software     13
    2015-02-04 22:00:00  Acme Coporation  Hardware     14
    ----------------
    Company
    Acme Coporation    34
    Hooli              30
    Initech            30
    Mediacore          45
    Streeplex          36
    Name: Units, dtype: int64
                           Company   Product  Units
    Date
    2015-02-02 21:00:00  Mediacore  Hardware      9
    2015-02-04 15:30:00  Streeplex  Software     13
    2015-02-09 09:00:00  Streeplex   Service     19
    2015-02-09 13:00:00  Mediacore  Software      7
    2015-02-19 11:00:00  Mediacore  Hardware     16
    2015-02-19 16:00:00  Mediacore   Service     10
    2015-02-21 05:00:00  Mediacore  Software      3
    2015-02-26 09:00:00  Streeplex   Service      4
"""





"""
Filtering and grouping with .map()
100xp

You have seen how to group by a column, or by multiple columns. Sometimes, you may instead want to group by a function/transformation of a column. The key here is that the Series is indexed the same way as the DataFrame. You can also mix and match column grouping with Series grouping.

In this exercise your job is to investigate survival rates of passengers on the Titanic by 'age' and 'pclass'. In particular, the goal is to find out what fraction of children under 10 survived in each 'pclass'. You'll do this by first creating a boolean array where True is passengers under 10 years old and False is passengers over 10. You'll use .map() to change these values to strings.

Finally, you'll group by the under 10 series and the 'pclass' column and aggregate the 'survived' column. The 'survived' column has the value 1 if the passenger survived and 0 otherwise. The mean of the 'survived' column is the fraction of passengers who lived.

The DataFrame has been pre-loaded for you as titanic.
Instructions

    Create a Boolean Series of titanic['age'] < 10 and call .map with {True:'under 10', False:'over 10'}.
    Group titanic by the under10 Series and then compute and print the mean of the 'survived' column.
    Group titanic by the under10 Series as well as the 'pclass' column and then compute and print the mean of the 'survived' column.

"""
print(titanic.head())
print('----------------')
# Create the Boolean Series: under10
under10 = (titanic['age'] < 10).map({True:'under 10', False:'over 10'})

# Group by under10 and compute the survival rate
survived_mean_1 = titanic.groupby(under10)['survived'].mean()
print(survived_mean_1)
print('----------------')

# Group by under10 and pclass and compute the survival rate
survived_mean_2 = titanic.groupby([under10,'pclass'])['survived'].mean()
print(survived_mean_2)
print('----------------')
""" results or consol output
<script.py> output:
       pclass  survived                                             name     sex  \
    0       1         1                    Allen, Miss. Elisabeth Walton  female
    1       1         1                   Allison, Master. Hudson Trevor    male
    2       1         0                     Allison, Miss. Helen Loraine  female
    3       1         0             Allison, Mr. Hudson Joshua Creighton    male
    4       1         0  Allison, Mrs. Hudson J C (Bessie Waldo Daniels)  female

         age  sibsp  parch  ticket      fare    cabin embarked boat   body  \
    0  29.00      0      0   24160  211.3375       B5        S    2    NaN
    1   0.92      1      2  113781  151.5500  C22 C26        S   11    NaN
    2   2.00      1      2  113781  151.5500  C22 C26        S  NaN    NaN
    3  30.00      1      2  113781  151.5500  C22 C26        S  NaN  135.0
    4  25.00      1      2  113781  151.5500  C22 C26        S  NaN    NaN

                             home.dest
    0                     St Louis, MO
    1  Montreal, PQ / Chesterville, ON
    2  Montreal, PQ / Chesterville, ON
    3  Montreal, PQ / Chesterville, ON
    4  Montreal, PQ / Chesterville, ON
    ----------------
    age
    over 10     0.366748
    under 10    0.609756
    Name: survived, dtype: float64
    ----------------
    age       pclass
    over 10   1         0.617555
              2         0.380392
              3         0.238897
    under 10  1         0.750000
              2         1.000000
              3         0.446429
    Name: survived, dtype: float64
    ----------------
"""
