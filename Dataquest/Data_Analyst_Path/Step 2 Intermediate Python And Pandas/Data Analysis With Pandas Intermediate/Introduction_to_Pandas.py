"""
01/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Data Analysis With Pandas Intermediate : Introduction to Pandas
"""



"""
1: Introduction To Pandas
Pandas is a library that unifies the most common workflows that data analysts and data scientists previously relied on many different libraries for.
Pandas has quickly became an important tool in a data professional's toolbelt and is the most popular library for working with tabular data in Python.
Tabular data is any data that can be represented as rows and columns. The CSV files we've worked with in previous missions are all examples of tabular data.

To represent tabular data, pandas uses a custom data structure called a dataframe.
A dataframe is a highly efficient, 2-dimensional data structure that provides a suite of methods and attributes to quickly explore, analyze, and visualize data.
The dataframe is similar to the NumPy 2D array but adds support for many features that help you work with tabular data.

One of the biggest advantages that pandas has over NumPy is the ability to store mixed data types in rows and columns.
Many tabular datasets contain a range of data types and pandas dataframes handle mixed data types effortlessly while NumPy doesn't.
Pandas dataframes can also handle missing values gracefully using a custom object, NaN, to represent those values.
A common complaint with NumPy is its lack of an object to represent missing values and people end up having to find and replace these values manually.
In addition, pandas dataframes contain axis labels for both rows and columns and enable you to refer to elements in the dataframe more intuitively.
Since many tabular datasets contain column titles, this means that dataframes preserve the metadata from the file around the data.
"""



"""
2: Introduction To The Data
In this mission, you'll learn the basics of pandas while exploring a dataset from the United States Department of Agriculture (USDA). This dataset contains nutritional information on the most common foods Americans consume. Each column in the dataset shows a different attribute of the foods and each row describes a different food item.

Here are some of the columns in the dataset:

NDB_No - unique id of the food.
Shrt_Desc - name of the food.
Water_(g) - water content in grams.
Energ_Kcal - energy measured in kilo-calories.
Protein_(g) - protein measured in grams.
Cholestrl_(mg) - cholesterol in milligrams.
Here's a preview of the first few rows and columns in the dataset:

NDB_No	Shrt_Desc	Water_(g)	Energy_Kcal	Protein_(g)	Lipid_Tot_(g)	Ash_(g)	Carbohydrt_(g)	Fiber_TD_(g)	Sugar_Tot_(g)
1001	BUTTER WITH SALT	15.87	717	0.85	81.11	2.11	0.06	0.0	0.06
1002	BUTTER WHIPPED WITH SALT	15.87	717	0.85	81.11	2.11	0.06	0.0	0.06
1003	BUTTER OIL ANHYDROUS	0.24	876	0.28	99.48	0.00	0.00	0.0	0.0
1004	CHEESE BLUE	42.41	353	21.40	28.74	5.11	2.34	0.0	0.50
1005	CHEESE BRICK	41.11	371	23.24	29.68	3.18	2.79	0.0	0.51
"""


"""
3: Read In A CSV File
To use the Pandas library, we need to import it into the environment using the import keyword:


import pandas
We can then refer to the module using pandas and use dot notation to call its methods. To read a CSV file into a dataframe, we use the pandas.read_csv() function and pass in the file name as a string:


# To read in the file `crime_rates.csv` into a dataframe named crime_rates.
crime_rates = pandas.read_csv("crime_rates.csv")
You can read more about the parameters the read_csv() method takes to customize how a file is read in on the documentation page.

Instructions
Import the pandas library.
Use the pandas.read_csv() function to read the file "food_info.csv" into a dataframe named food_info.
Use the type() and print() functions to display the type of food_info to confirm that it's a dataframe object.
"""
food_info = pandas.read_csv("food_info.csv")
print(type(food_info))
""" Console output or Results
Output
<class 'pandas.core.frame.DataFrame'>
"""



"""
4: Exploring The DataFrame
Now that we've read the dataset into a dataframe, we can start using the dataframe methods to explore the data. To select the first 5 rows of a dataframe, use the dataframe method head(). When you call the head() method, pandas will return a new dataframe containing just the first 5 rows:


first_rows = food_info.head()
If you peek at the documentation, you'll notice that you can pass in an integer (n) into the head() method to display the first n rows instead of the first 5:


# First 3 rows.
print(food_info.head(3))
Because this dataframe contains many columns and rows, pandas uses ellipsis (...) to hide the columns and rows in the middle. Only the first few and the last few columns and rows are displayed to conserve space.

To access the full list of column names, use the columns attribute:


column_names = food_info.columns
Lastly, you can use the shape attribute to understand the dimensions of the dataframe. The shape attribute returns a tuple of integers representing the number of rows followed by the number of columns:


# Returns the tuple (8618,36) and assigns to `dimensions`.
dimensions = food_info.shape
# The number of rows, 8618.
num_rows = dimensions[0]
# The number of columns, 36.
num_cols = dimensions[1]
Instructions
Select the first 20 rows from food_info and assign to the variable first_twenty.
"""
print(food_info.head(3))
dimensions = food_info.shape
print(dimensions)
num_rows = dimensions[0]
print(num_rows)
num_cols = dimensions[1]
print(num_cols)
first_twenty = food_info.head(20)
print(first_twenty)
""" Console output or Results
Output
   NDB_No                 Shrt_Desc  Water_(g)  Energ_Kcal  Protein_(g)  \
0    1001          BUTTER WITH SALT      15.87         717         0.85
1    1002  BUTTER WHIPPED WITH SALT      15.87         717         0.85
2    1003      BUTTER OIL ANHYDROUS       0.24         876         0.28

   Lipid_Tot_(g)  Ash_(g)  Carbohydrt_(g)  Fiber_TD_(g)  Sugar_Tot_(g)  \
0          81.11     2.11            0.06           0.0           0.06
1          81.11     2.11            0.06           0.0           0.06
2          99.48     0.00            0.00           0.0           0.00

        ...        Vit_A_IU  Vit_A_RAE  Vit_E_(mg)  Vit_D_mcg  Vit_D_IU  \
0       ...          2499.0      684.0        2.32        1.5      60.0
1       ...          2499.0      684.0        2.32        1.5      60.0
2       ...          3069.0      840.0        2.80        1.8      73.0

   Vit_K_(mcg)  FA_Sat_(g)  FA_Mono_(g)  FA_Poly_(g)  Cholestrl_(mg)
0          7.0      51.368       21.021        3.043           215.0
1          7.0      50.489       23.426        3.012           219.0
2          8.6      61.924       28.732        3.694           256.0

[3 rows x 36 columns]
(8618, 36)
8618
36
    NDB_No                                         Shrt_Desc  Water_(g)  \
0     1001                                  BUTTER WITH SALT      15.87
1     1002                          BUTTER WHIPPED WITH SALT      15.87
2     1003                              BUTTER OIL ANHYDROUS       0.24
3     1004                                       CHEESE BLUE      42.41
4     1005                                      CHEESE BRICK      41.11
5     1006                                       CHEESE BRIE      48.42
6     1007                                  CHEESE CAMEMBERT      51.80
7     1008                                    CHEESE CARAWAY      39.28
8     1009                                    CHEESE CHEDDAR      37.10
9     1010                                   CHEESE CHESHIRE      37.65
10    1011                                      CHEESE COLBY      38.20
11    1012               CHEESE COTTAGE CRMD LRG OR SML CURD      79.79
12    1013                       CHEESE COTTAGE CRMD W/FRUIT      79.64
13    1014  CHEESE COTTAGE NONFAT UNCRMD DRY LRG OR SML CURD      81.01
14    1015                  CHEESE COTTAGE LOWFAT 2% MILKFAT      81.24
15    1016                  CHEESE COTTAGE LOWFAT 1% MILKFAT      82.48
16    1017                                      CHEESE CREAM      54.44
17    1018                                       CHEESE EDAM      41.56
18    1019                                       CHEESE FETA      55.22
19    1020                                    CHEESE FONTINA      37.92

    Energ_Kcal  Protein_(g)  Lipid_Tot_(g)  Ash_(g)  Carbohydrt_(g)  \
0          717         0.85          81.11     2.11            0.06
1          717         0.85          81.11     2.11            0.06
2          876         0.28          99.48     0.00            0.00
3          353        21.40          28.74     5.11            2.34
4          371        23.24          29.68     3.18            2.79
5          334        20.75          27.68     2.70            0.45
6          300        19.80          24.26     3.68            0.46
7          376        25.18          29.20     3.28            3.06
8          406        24.04          33.82     3.71            1.33
9          387        23.37          30.60     3.60            4.78
10         394        23.76          32.11     3.36            2.57
11          98        11.12           4.30     1.41            3.38
12          97        10.69           3.85     1.20            4.61
13          72        10.34           0.29     1.71            6.66
14          81        10.45           2.27     1.27            4.76
15          72        12.39           1.02     1.39            2.72
16         342         5.93          34.24     1.32            4.07
17         357        24.99          27.80     4.22            1.43
18         264        14.21          21.28     5.20            4.09
19         389        25.60          31.14     3.79            1.55

    Fiber_TD_(g)  Sugar_Tot_(g)       ...        Vit_A_IU  Vit_A_RAE  \
0            0.0           0.06       ...          2499.0      684.0
1            0.0           0.06       ...          2499.0      684.0
2            0.0           0.00       ...          3069.0      840.0
3            0.0           0.50       ...           721.0      198.0
4            0.0           0.51       ...          1080.0      292.0
5            0.0           0.45       ...           592.0      174.0
6            0.0           0.46       ...           820.0      241.0
7            0.0            NaN       ...          1054.0      271.0
8            0.0           0.28       ...           994.0      263.0
9            0.0            NaN       ...           985.0      233.0
10           0.0           0.52       ...           994.0      264.0
11           0.0           2.67       ...           140.0       37.0
12           0.2           2.38       ...           146.0       38.0
13           0.0           1.85       ...             8.0        2.0
14           0.0           4.00       ...           225.0       68.0
15           0.0           2.72       ...            41.0       11.0
16           0.0           3.21       ...          1343.0      366.0
17           0.0           1.43       ...           825.0      243.0
18           0.0           4.09       ...           422.0      125.0
19           0.0           1.55       ...           913.0      261.0

    Vit_E_(mg)  Vit_D_mcg  Vit_D_IU  Vit_K_(mcg)  FA_Sat_(g)  FA_Mono_(g)  \
0         2.32        1.5      60.0          7.0      51.368       21.021
1         2.32        1.5      60.0          7.0      50.489       23.426
2         2.80        1.8      73.0          8.6      61.924       28.732
3         0.25        0.5      21.0          2.4      18.669        7.778
4         0.26        0.5      22.0          2.5      18.764        8.598
5         0.24        0.5      20.0          2.3      17.410        8.013
6         0.21        0.4      18.0          2.0      15.259        7.023
7          NaN        NaN       NaN          NaN      18.584        8.275
8         0.78        0.6      24.0          2.9      19.368        8.428
9          NaN        NaN       NaN          NaN      19.475        8.671
10        0.28        0.6      24.0          2.7      20.218        9.280
11        0.08        0.1       3.0          0.0       1.718        0.778
12        0.04        0.0       0.0          0.4       2.311        1.036
13        0.01        0.0       0.0          0.0       0.169        0.079
14        0.08        0.0       0.0          0.0       1.235        0.516
15        0.01        0.0       0.0          0.1       0.645        0.291
16        0.29        0.6      25.0          2.9      19.292        8.620
17        0.24        0.5      20.0          2.3      17.572        8.125
18        0.18        0.4      16.0          1.8      14.946        4.623
19        0.27        0.6      23.0          2.6      19.196        8.687

    FA_Poly_(g)  Cholestrl_(mg)
0         3.043           215.0
1         3.012           219.0
2         3.694           256.0
3         0.800            75.0
4         0.784            94.0
5         0.826           100.0
6         0.724            72.0
7         0.830            93.0
8         1.433           102.0
9         0.870           103.0
10        0.953            95.0
11        0.123            17.0
12        0.124            13.0
13        0.003             7.0
14        0.083            12.0
15        0.031             4.0
16        1.437           110.0
17        0.665            89.0
18        0.591            89.0
19        1.654           116.0

[20 rows x 36 columns]
"""



"""
5: Indexing
When you read in a file into a dataframe, pandas uses the values in the first row (also known as the header) for the column labels and the row number for the row labels. Collectively, the labels are referred to as the index. dataframes contain both a row index and a column index. Here's a diagram that displays some of the column and row labels for food_info:

The labels allow us to refer to values in the dataframe, which we'll learn more about in the rest of this mission.
"""





"""
6: Series
The Series object is a core data structure that pandas uses to represent rows and columns. A Series is a labelled collection of values similar to the NumPy vector. The main advantage of Series objects is the ability to utilize non-integer labels. NumPy arrays can only utilize integer labels for indexing.

Pandas utilizes this feature to provide more context when returning a row or a column from a dataframe. For example, when you select a row from a dataframe, instead of just returning the values in that row as a list, pandas returns a Series object that contains the column labels as well as the corresponding values:
"""





"""
7: Selecting A Row
While we use bracket notation to access elements in a NumPy array or a standard list, we need to use the pandas method loc[] to select rows in a dataframe. The loc[] method allows you to select rows by row labels. Recall that when you read a file into a dataframe, pandas uses the row number (or position) as each row's label. Pandas uses zero-indexing, so the first row is at index 0, the second row at index 1, and so on.

If you're interested in accessing a single row, pass in the row label to the loc[] method. Python will return an error if you don't pass in a valid row label:


# Series object representing the row at index 0.
food_info.loc[0]
​
# Series object representing the seventh row.
food_info.loc[6]
​
# Will throw an error: "KeyError: 'the label [8620] is not in the [index]'"
food_info.loc[8620]
When accessing an individual row, pandas returns a Series object containing the column names and that row's value for each column. In the following code cell, we select the first and seventh rows and display them using the print() function.

Instructions
Assign the 100th row of food_info to the variable hundredth_row.
Display hundredth_row using the print() function.
"""
hundredth_row = food_info.loc[99]
print(hundredth_row)
""" Console output or Results
Output
NDB_No                                  1111
Shrt_Desc          MILK SHAKES THICK VANILLA
Water_(g)                              74.45
Energ_Kcal                               112
Protein_(g)                             3.86
Lipid_Tot_(g)                           3.03
Ash_(g)                                 0.91
Carbohydrt_(g)                         17.75
Fiber_TD_(g)                               0
Sugar_Tot_(g)                          17.75
Calcium_(mg)                             146
Iron_(mg)                                0.1
Magnesium_(mg)                            12
Phosphorus_(mg)                          115
Potassium_(mg)                           183
Sodium_(mg)                               95
Zinc_(mg)                               0.39
Copper_(mg)                            0.051
Manganese_(mg)                         0.014
Selenium_(mcg)                           2.3
Vit_C_(mg)                                 0
Thiamin_(mg)                            0.03
Riboflavin_(mg)                        0.195
Niacin_(mg)                            0.146
Vit_B6_(mg)                            0.042
Vit_B12_(mcg)                           0.52
Vit_A_IU                                  91
Vit_A_RAE                                 25
Vit_E_(mg)                              0.05
Vit_D_mcg                                1.2
Vit_D_IU                                  48
Vit_K_(mcg)                              0.2
FA_Sat_(g)                             1.886
FA_Mono_(g)                            0.875
FA_Poly_(g)                            0.113
Cholestrl_(mg)                            12
Name: 99, dtype: object
"""




"""
8: Data Types
When you displayed individual rows, represented as Series objects, you may have noticed the text "dtype: object" after the last value. dtype: object refers to the data type, or dtype, of that Series. The object dtype is equivalent to the string type in Python. Pandas borrows from the NumPy type system and contains the following dtypes:

object - for representing string values.
int - for representing integer values.
float - for representing float values.
datetime - for representing time values.
bool - for representing Boolean values.
When reading a file into a dataframe, pandas analyzes the values and infers each column's types. To access the types for each column, use the DataFrame.dtypes attribute to return a Series containing each column name and its corresponding type. Read more about data types on the Pandas documentation.

Instructions
This step is a demo. Play around with code or advance to the next step.
"""
print(food_info.dtypes)
""" Console output or Results
Output
NDB_No               int64
Shrt_Desc           object
Water_(g)          float64
Energ_Kcal           int64
Protein_(g)        float64
Lipid_Tot_(g)      float64
Ash_(g)            float64
Carbohydrt_(g)     float64
Fiber_TD_(g)       float64
Sugar_Tot_(g)      float64
Calcium_(mg)       float64
Iron_(mg)          float64
Magnesium_(mg)     float64
Phosphorus_(mg)    float64
Potassium_(mg)     float64
Sodium_(mg)        float64
Zinc_(mg)          float64
Copper_(mg)        float64
Manganese_(mg)     float64
Selenium_(mcg)     float64
Vit_C_(mg)         float64
Thiamin_(mg)       float64
Riboflavin_(mg)    float64
Niacin_(mg)        float64
Vit_B6_(mg)        float64
Vit_B12_(mcg)      float64
Vit_A_IU           float64
Vit_A_RAE          float64
Vit_E_(mg)         float64
Vit_D_mcg          float64
Vit_D_IU           float64
Vit_K_(mcg)        float64
FA_Sat_(g)         float64
FA_Mono_(g)        float64
FA_Poly_(g)        float64
Cholestrl_(mg)     float64
dtype: object
"""



"""
9: Selecting Multiple Rows
If you're interested in accessing multiple rows of the dataframe, you can pass in either a slice of row labels or a list of row labels and pandas will return a dataframe. Note that unlike slicing lists in Python, a slice of a dataframe using .loc[] will include both the start and the end row:


# DataFrame containing the rows at index 3, 4, 5, and 6 returned.
food_info.loc[3:6]
​
# DataFrame containing the rows at index 2, 5, and 10 returned. Either of the following work.
# Method 1
two_five_ten = [2,5,10]
food_info.loc[two_five_ten]
​
# Method 2
food_info.loc[[2,5,10]]
Instructions
Select the last 5 rows of food_info and assign to the variable last_rows.
"""
print("Rows 3, 4, 5 and 6")
print(food_info.loc[3:6])

print("Rows 2, 5, and 10")
two_five_ten = [2,5,10]
print(food_info.loc[two_five_ten])

last_rows = food_info.loc[food_info.shape[0]-5:food_info.shape[0]]
print(last_rows)
print(food_info.shape[0])
""" Console output or Results
Output
Rows 3, 4, 5 and 6
   NDB_No         Shrt_Desc  Water_(g)  Energ_Kcal  Protein_(g)  \
3    1004       CHEESE BLUE      42.41         353        21.40
4    1005      CHEESE BRICK      41.11         371        23.24
5    1006       CHEESE BRIE      48.42         334        20.75
6    1007  CHEESE CAMEMBERT      51.80         300        19.80

   Lipid_Tot_(g)  Ash_(g)  Carbohydrt_(g)  Fiber_TD_(g)  Sugar_Tot_(g)  \
3          28.74     5.11            2.34           0.0           0.50
4          29.68     3.18            2.79           0.0           0.51
5          27.68     2.70            0.45           0.0           0.45
6          24.26     3.68            0.46           0.0           0.46

        ...        Vit_A_IU  Vit_A_RAE  Vit_E_(mg)  Vit_D_mcg  Vit_D_IU  \
3       ...           721.0      198.0        0.25        0.5      21.0
4       ...          1080.0      292.0        0.26        0.5      22.0
5       ...           592.0      174.0        0.24        0.5      20.0
6       ...           820.0      241.0        0.21        0.4      18.0

   Vit_K_(mcg)  FA_Sat_(g)  FA_Mono_(g)  FA_Poly_(g)  Cholestrl_(mg)
3          2.4      18.669        7.778        0.800            75.0
4          2.5      18.764        8.598        0.784            94.0
5          2.3      17.410        8.013        0.826           100.0
6          2.0      15.259        7.023        0.724            72.0

[4 rows x 36 columns]
Rows 2, 5, and 10
    NDB_No             Shrt_Desc  Water_(g)  Energ_Kcal  Protein_(g)  \
2     1003  BUTTER OIL ANHYDROUS       0.24         876         0.28
5     1006           CHEESE BRIE      48.42         334        20.75
10    1011          CHEESE COLBY      38.20         394        23.76

    Lipid_Tot_(g)  Ash_(g)  Carbohydrt_(g)  Fiber_TD_(g)  Sugar_Tot_(g)  \
2           99.48     0.00            0.00           0.0           0.00
5           27.68     2.70            0.45           0.0           0.45
10          32.11     3.36            2.57           0.0           0.52

         ...        Vit_A_IU  Vit_A_RAE  Vit_E_(mg)  Vit_D_mcg  Vit_D_IU  \
2        ...          3069.0      840.0        2.80        1.8      73.0
5        ...           592.0      174.0        0.24        0.5      20.0
10       ...           994.0      264.0        0.28        0.6      24.0

    Vit_K_(mcg)  FA_Sat_(g)  FA_Mono_(g)  FA_Poly_(g)  Cholestrl_(mg)
2           8.6      61.924       28.732        3.694           256.0
5           2.3      17.410        8.013        0.826           100.0
10          2.7      20.218        9.280        0.953            95.0

[3 rows x 36 columns]
      NDB_No                   Shrt_Desc  Water_(g)  Energ_Kcal  Protein_(g)  \
8613   83110             MACKEREL SALTED      43.00         305        18.50
8614   90240  SCALLOP (BAY&SEA) CKD STMD      70.25         111        20.54
8615   90480                  SYRUP CANE      26.00         269         0.00
8616   90560                   SNAIL RAW      79.20          90        16.10
8617   93600            TURTLE GREEN RAW      78.50          89        19.80

      Lipid_Tot_(g)  Ash_(g)  Carbohydrt_(g)  Fiber_TD_(g)  Sugar_Tot_(g)  \
8613          25.10    13.40            0.00           0.0            0.0
8614           0.84     2.97            5.41           0.0            0.0
8615           0.00     0.86           73.14           0.0           73.2
8616           1.40     1.30            2.00           0.0            0.0
8617           0.50     1.20            0.00           0.0            0.0

           ...        Vit_A_IU  Vit_A_RAE  Vit_E_(mg)  Vit_D_mcg  Vit_D_IU  \
8613       ...           157.0       47.0        2.38       25.2    1006.0
8614       ...             5.0        2.0        0.00        0.0       2.0
8615       ...             0.0        0.0        0.00        0.0       0.0
8616       ...           100.0       30.0        5.00        0.0       0.0
8617       ...           100.0       30.0        0.50        0.0       0.0

      Vit_K_(mcg)  FA_Sat_(g)  FA_Mono_(g)  FA_Poly_(g)  Cholestrl_(mg)
8613          7.8       7.148        8.320        6.210            95.0
8614          0.0       0.218        0.082        0.222            41.0
8615          0.0       0.000        0.000        0.000             0.0
8616          0.1       0.361        0.259        0.252            50.0
8617          0.1       0.127        0.088        0.170            50.0

[5 rows x 36 columns]
8618
"""



"""
10: Selecting Individual Columns
When accessing a column in a dataframe, pandas returns a Series object containing the row label and each row's value for that column. To access a single column, use bracket notation and pass in the column name as a string:


# Series object representing the "NDB_No" column.
ndb_col = food_info["NDB_No"]
​
# You can instead access a column by passing in a string variable.
col_name = "NDB_No"
ndb_col = food_info[col_name]
Instructions
Assign the "FA_Sat_(g)" column to the variable saturated_fat.
Assign the "Cholestrl_(mg)" column to the variable cholesterol.
"""
# Series object.
ndb_col = food_info["NDB_No"]
print(ndb_col)

# Display the type of the column to confirm it's a Series object.
print(type(ndb_col))

saturated_fat = food_info["FA_Sat_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]
""" Console output or Results
<class 'pandas.core.series.Series'>
"""




"""
11: Selecting Multiple Columns By Name
To select multiple columns, pass in a list of strings representing the column names and pandas will return a dataframe containing only the values in those columns. The following code returns a dataframe containing the "Zinc_(mg)" and "Copper_(mg)" columns, in that order:


columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]
​
# Skipping the assignment.
zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]
When selecting multiple columns, the order of the columns in the returned dataframe matches the order of the column names in the list of strings that you passed in. This allows you to easily explore specific columns that may not be positioned next to each other in the dataframe.

Instructions
Select the 'Selenium_(mcg)' and 'Thiamin_(mg)' columns and assign the resulting dataframe to selenium_thiamin.
"""
zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]

columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]

selenium_thiamin = food_info[["Selenium_(mcg)", "Thiamin_(mg)"]]
print(type(selenium_thiamin))
""" Console output or Results
Output
<class 'pandas.core.frame.DataFrame'>
"""




"""
12: Practice
To help solidify the concepts learned in this mission, complete the following exercise.

Instructions
Select and display only the columns that use grams for measurement (that end with "(g)"). To accomplish this:
Use the columns attribute to return the column names in food_info and convert to a list by calling the method tolist()
Create a new list, gram_columns, containing only the column names that end in "(g)". The string method endswith() returns True if the string object calling the method ends with the string passed into the parentheses.
Pass gram_columns into bracket notation to select just those columns and assign the resulting dataframe to gram_df
Then use the dataframe method head() to display the first 3 rows of gram_df.
"""
print(food_info.columns)
print(food_info.head(2))

columnlist = food_info.columns.tolist()
print(columnlist[0:5])

gram_columns = []
for column in columnlist:
    if column.endswith("(g)"):
        gram_columns.append(column)

gram_df = food_info[gram_columns]
print(gram_df.head(3))
""" Console output or Results
Output
Index(['NDB_No', 'Shrt_Desc', 'Water_(g)', 'Energ_Kcal', 'Protein_(g)',
       'Lipid_Tot_(g)', 'Ash_(g)', 'Carbohydrt_(g)', 'Fiber_TD_(g)',
       'Sugar_Tot_(g)', 'Calcium_(mg)', 'Iron_(mg)', 'Magnesium_(mg)',
       'Phosphorus_(mg)', 'Potassium_(mg)', 'Sodium_(mg)', 'Zinc_(mg)',
       'Copper_(mg)', 'Manganese_(mg)', 'Selenium_(mcg)', 'Vit_C_(mg)',
       'Thiamin_(mg)', 'Riboflavin_(mg)', 'Niacin_(mg)', 'Vit_B6_(mg)',
       'Vit_B12_(mcg)', 'Vit_A_IU', 'Vit_A_RAE', 'Vit_E_(mg)', 'Vit_D_mcg',
       'Vit_D_IU', 'Vit_K_(mcg)', 'FA_Sat_(g)', 'FA_Mono_(g)', 'FA_Poly_(g)',
       'Cholestrl_(mg)'],
      dtype='object')
   NDB_No                 Shrt_Desc  Water_(g)  Energ_Kcal  Protein_(g)  \
0    1001          BUTTER WITH SALT      15.87         717         0.85
1    1002  BUTTER WHIPPED WITH SALT      15.87         717         0.85

   Lipid_Tot_(g)  Ash_(g)  Carbohydrt_(g)  Fiber_TD_(g)  Sugar_Tot_(g)  \
0          81.11     2.11            0.06           0.0           0.06
1          81.11     2.11            0.06           0.0           0.06

        ...        Vit_A_IU  Vit_A_RAE  Vit_E_(mg)  Vit_D_mcg  Vit_D_IU  \
0       ...          2499.0      684.0        2.32        1.5      60.0
1       ...          2499.0      684.0        2.32        1.5      60.0

   Vit_K_(mcg)  FA_Sat_(g)  FA_Mono_(g)  FA_Poly_(g)  Cholestrl_(mg)
0          7.0      51.368       21.021        3.043           215.0
1          7.0      50.489       23.426        3.012           219.0

[2 rows x 36 columns]
['NDB_No', 'Shrt_Desc', 'Water_(g)', 'Energ_Kcal', 'Protein_(g)']
   Water_(g)  Protein_(g)  Lipid_Tot_(g)  Ash_(g)  Carbohydrt_(g)  \
0      15.87         0.85          81.11     2.11            0.06
1      15.87         0.85          81.11     2.11            0.06
2       0.24         0.28          99.48     0.00            0.00

   Fiber_TD_(g)  Sugar_Tot_(g)  FA_Sat_(g)  FA_Mono_(g)  FA_Poly_(g)
0           0.0           0.06      51.368       21.021        3.043
1           0.0           0.06      50.489       23.426        3.012
2           0.0           0.00      61.924       28.732        3.694
"""





"""
13: Next Steps
In this mission, we introduced the key data structures in pandas and learned the basics of exploring data. In the next mission, you'll learn how to transform columns, normalize columns, and sort a dataframe.
"""
