10/2017  
Datcamp - Merging DataFrames with pandas  

---

# Part 4 : Case Study - Summer Olympics 

To cement your new skills, you'll apply them by working on an in-depth study involving Olympic medal data. The analysis involves integrating your multi-DataFrame skills from this course and also skills you've gained in previous pandas courses. This is a rich dataset that will allow you to fully leverage your pandas data manipulation skills. Enjoy!  
 
## Loading Olympic edition DataFrame    

In this chapter, you'll be using The Guardian's Olympic medal dataset.  

Your first task here is to prepare a DataFrame editions from a tab-separated values (TSV) file.  

Initially, editions has 26 rows (one for each Olympic edition, i.e., a year in which the Olympics was held) and 7 columns: 'Edition', 'Bronze', 'Gold', 'Silver', 'Grand Total', 'City', and 'Country'.  

For the analysis that follows, you won't need the overall medal counts, so you want to keep only the useful columns from editions: 'Edition', 'Grand Total', City, and Country.  

### Instructions :  

 - Read file_path into a DataFrame called editions. The identifier file_path has been pre-defined with the filename 'Summer Olympic medallists 1896 to 2008 - EDITIONS.tsv'. You'll have to use the option sep='\t' because the file uses tabs to delimit fields (pd.read_csv() expects commas by default).
 - Select only the columns 'Edition', 'Grand Total', 'City', and 'Country' from editions.
 - Print the final DataFrame editions in entirety (there are only 26 rows). This has been done for you, so hit 'Submit Answer' to see the result!

```python
#Import pandas
import pandas as pd

# Create file path: file_path
file_path = 'Summer Olympic medallists 1896 to 2008 - EDITIONS.tsv'

# Load DataFrame from file_path: editions
editions = pd.read_csv(file_path,sep='\t')

# Extract the relevant columns: editions
editions = editions[['Edition', 'Grand Total', 'City', 'Country']]

# Print editions DataFrame
print(editions)
```

### Results :  

	<script.py> output:
		Edition  Grand Total         City                     Country
	    0      1896          151       Athens                      Greece
	    1      1900          512        Paris                      France
	    2      1904          470    St. Louis               United States
	    3      1908          804       London              United Kingdom
	    4      1912          885    Stockholm                      Sweden
	    5      1920         1298      Antwerp                     Belgium
	    6      1924          884        Paris                      France
	    7      1928          710    Amsterdam                 Netherlands
	    8      1932          615  Los Angeles               United States
	    9      1936          875       Berlin                     Germany
	    10     1948          814       London              United Kingdom
	    11     1952          889     Helsinki                     Finland
	    12     1956          885    Melbourne                   Australia
	    13     1960          882         Rome                       Italy
	    14     1964         1010        Tokyo                       Japan
	    15     1968         1031  Mexico City                      Mexico
	    16     1972         1185       Munich  West Germany (now Germany)
	    17     1976         1305     Montreal                      Canada
	    18     1980         1387       Moscow       U.S.S.R. (now Russia)
	    19     1984         1459  Los Angeles               United States
	    20     1988         1546        Seoul                 South Korea
	    21     1992         1705    Barcelona                       Spain
	    22     1996         1859      Atlanta               United States
	    23     2000         2015       Sydney                   Australia
	    24     2004         1998       Athens                      Greece
	    25     2008         2042      Beijing                       China

Great work! Next, you'll prepare a DataFrame of IOC codes.  

---

## Loading IOC codes DataFrame   

Your task here is to prepare a DataFrame ioc_codes from a comma-separated values (CSV) file.  

Initially, ioc_codes has 200 rows (one for each country) and 3 columns: 'Country', 'NOC', & 'ISO code'.  

For the analysis that follows, you want to keep only the useful columns from ioc_codes: 'Country' and 'NOC' (the column 'NOC' contains three-letter codes representing each country).  

### Instructions :  

 - Read file_path into a DataFrame called ioc_codes. The identifier file_path has been pre-defined with the filename 'Summer Olympic medallists 1896 to 2008 - IOC COUNTRY CODES.csv'.
 - Select only the columns 'Country' and 'NOC' from ioc_codes.
 - Print the leading 5 and trailing 5 rows of the DataFrame ioc_codes (there are 200 rows in total). This has been done for you, so hit 'Submit Answer' to see the result!

```python
# Import pandas
import pandas as pd

# Create the file path: file_path
file_path = 'Summer Olympic medallists 1896 to 2008 - IOC COUNTRY CODES.csv'

# Load DataFrame from file_path: ioc_codes
ioc_codes = pd.read_csv(file_path)

# Extract the relevant columns: ioc_codes
ioc_codes = ioc_codes[['Country', 'NOC']]

# Print first and last 5 rows of ioc_codes
print(ioc_codes.head())
print('-----------------------------------')
print(ioc_codes.tail())
```

### Results :  

	<script.py> output:
		       Country  NOC
	    0      Afghanistan  AFG
	    1          Albania  ALB
	    2          Algeria  ALG
	    3  American Samoa*  ASA
	    4          Andorra  AND
	    -----------------------------------
		         Country  NOC
	    196          Vietnam  VIE
	    197  Virgin Islands*  ISV
	    198            Yemen  YEM
	    199           Zambia  ZAM
	    200         Zimbabwe  ZIM


---

## Building medals DataFrame    

Here, you'll start with the DataFrame editions from the previous exercise.  

You have a sequence of files summer_1896.csv, summer_1900.csv, ..., summer_2008.csv, one for each Olympic edition (year).  

You will build up a dictionary medals_dict with the Olympic editions (years) as keys and DataFrames as values.  

The dictionary is built up inside a loop over the year of each Olympic edition (from the Index of editions).  

Once the dictionary of DataFrames is built up, you will combine the DataFrames using pd.concat().  

### Instructions :  

 - Within the for loop:
	 - Create the file path. This has been done for you.
	 - Read file_path into a DataFrame. Assign the result to the year key of medals_dict.
	 - Select only the columns 'Athlete', 'NOC', and 'Medal' from medals_dict[year].
	 - Create a new column called 'Edition' in the DataFrame medals_dict[year] whose entries are all year.
 - Concatenate the dictionary of DataFrames medals_dict into a DataFame called medals. Specify the keyword argument ignore_index=True to prevent repeated integer indices.
 - Print the first and last 5 rows of medals. This has been done for you, so hit 'Submit Answer' to see the result!

```python
# Import pandas
import pandas as pd

# Create empty dictionary: medals_dict
medals_dict = {}

for year in editions['Edition']:

    # Create the file path: file_path
    file_path = 'summer_{:d}.csv'.format(year)
    
    # Load file_path into a DataFrame: medals_dict[year]
    medals_dict[year] = pd.read_csv(file_path)
    
    # Extract relevant columns: medals_dict[year]
    medals_dict[year] = medals_dict[year][['Athlete', 'NOC', 'Medal']]
    
    # Assign year to column 'Edition' of medals_dict
    medals_dict[year]['Edition'] = year
    
# Concatenate medals_dict: medals
medals = pd.concat(medals_dict,ignore_index=True)

# Print first and last 5 rows of medals
print(medals.head())
print(medals.tail())
```

### Results :  

	<script.py> output:
		          Athlete  NOC   Medal  Edition
	    0       HAJOS, Alfred  HUN    Gold     1896
	    1    HERSCHMANN, Otto  AUT  Silver     1896
	    2   DRIVAS, Dimitrios  GRE  Bronze     1896
	    3  MALOKINIS, Ioannis  GRE    Gold     1896
	    4  CHASAPIS, Spiridon  GRE  Silver     1896
		                Athlete  NOC   Medal  Edition
	    29211        ENGLICH, Mirko  GER  Silver     2008
	    29212  MIZGAITIS, Mindaugas  LTU  Bronze     2008
	    29213       PATRIKEEV, Yuri  ARM  Bronze     2008
	    29214         LOPEZ, Mijain  CUB    Gold     2008
	    29215        BAROEV, Khasan  RUS  Silver     2008

---

## Counting medals by country/edition in a pivot table    

Here, you'll start with the concatenated DataFrame medals from the previous exercise.  

You can construct a pivot table to see the number of medals each country won in each year. The result is a new DataFrame with the Olympic edition on the Index and with 138 country NOC codes as columns. If you want a refresher on pivot tables, it may be useful to refer back to the relevant exercises in Manipulating DataFrames with pandas.  

### Instructions :  

 - Construct a pivot table from the DataFrame medals, aggregating by count (by specifying the aggfunc parameter). Use 'Edition' as the Index, 'Athlete' for the values, and 'NOC' for the columns.
 - Print the first & last 5 rows of medal_counts. This has been done for you, so hit 'Submit Answer' to see the results!

```python
print(medals.head(10))
print('------------')
print(medals.tail(10))
print('------------')

# Construct the pivot_table: medal_counts
medal_counts = medals.pivot_table(aggfunc='count',index='Edition',values='Athlete',columns='NOC')

# Print the first & last 5 rows of medal_counts
print(medal_counts.head())
print('------------')
print(medal_counts.tail())
```

### Results :  

	<script.py> output:
		             Athlete  NOC   Medal  Edition
	    0          HAJOS, Alfred  HUN    Gold     1896
	    1       HERSCHMANN, Otto  AUT  Silver     1896
	    2      DRIVAS, Dimitrios  GRE  Bronze     1896
	    3     MALOKINIS, Ioannis  GRE    Gold     1896
	    4     CHASAPIS, Spiridon  GRE  Silver     1896
	    5  CHOROPHAS, Efstathios  GRE  Bronze     1896
	    6          HAJOS, Alfred  HUN    Gold     1896
	    7       ANDREOU, Joannis  GRE  Silver     1896
	    8  CHOROPHAS, Efstathios  GRE  Bronze     1896
	    9          NEUMANN, Paul  AUT    Gold     1896
	    ------------
		                Athlete  NOC   Medal  Edition
	    29206      MINGUZZI, Andrea  ITA    Gold     2008
	    29207         FODOR, Zoltan  HUN  Silver     2008
	    29208       MAMBETOV, Asset  KAZ  Bronze     2008
	    29209         WHEELER, Adam  USA  Bronze     2008
	    29210    KHUSHTOV, Aslanbek  RUS    Gold     2008
	    29211        ENGLICH, Mirko  GER  Silver     2008
	    29212  MIZGAITIS, Mindaugas  LTU  Bronze     2008
	    29213       PATRIKEEV, Yuri  ARM  Bronze     2008
	    29214         LOPEZ, Mijain  CUB    Gold     2008
	    29215        BAROEV, Khasan  RUS  Silver     2008
	    ------------
	    NOC      AFG  AHO  ALG   ANZ  ARG  ARM  AUS   AUT  AZE  BAH  ...   URS  URU  \
	    Edition                                                      ...              
	    1896     NaN  NaN  NaN   NaN  NaN  NaN  2.0   5.0  NaN  NaN  ...   NaN  NaN   
	    1900     NaN  NaN  NaN   NaN  NaN  NaN  5.0   6.0  NaN  NaN  ...   NaN  NaN   
	    1904     NaN  NaN  NaN   NaN  NaN  NaN  NaN   1.0  NaN  NaN  ...   NaN  NaN   
	    1908     NaN  NaN  NaN  19.0  NaN  NaN  NaN   1.0  NaN  NaN  ...   NaN  NaN   
	    1912     NaN  NaN  NaN  10.0  NaN  NaN  NaN  14.0  NaN  NaN  ...   NaN  NaN   
	    
	    NOC        USA  UZB  VEN  VIE  YUG  ZAM  ZIM   ZZX  
	    Edition                                             
	    1896      20.0  NaN  NaN  NaN  NaN  NaN  NaN   6.0  
	    1900      55.0  NaN  NaN  NaN  NaN  NaN  NaN  34.0  
	    1904     394.0  NaN  NaN  NaN  NaN  NaN  NaN   8.0  
	    1908      63.0  NaN  NaN  NaN  NaN  NaN  NaN   NaN  
	    1912     101.0  NaN  NaN  NaN  NaN  NaN  NaN   NaN  
	    
	    [5 rows x 138 columns]
	    ------------
	    NOC      AFG  AHO  ALG  ANZ   ARG  ARM    AUS  AUT  AZE  BAH ...   URS  URU  \
	    Edition                                                      ...              
	    1992     NaN  NaN  2.0  NaN   2.0  NaN   57.0  6.0  NaN  1.0 ...   NaN  NaN   
	    1996     NaN  NaN  3.0  NaN  20.0  2.0  132.0  3.0  1.0  5.0 ...   NaN  NaN   
	    2000     NaN  NaN  5.0  NaN  20.0  1.0  183.0  4.0  3.0  6.0 ...   NaN  1.0   
	    2004     NaN  NaN  NaN  NaN  47.0  NaN  157.0  8.0  5.0  2.0 ...   NaN  NaN   
	    2008     1.0  NaN  2.0  NaN  51.0  6.0  149.0  3.0  7.0  5.0 ...   NaN  NaN   
	    
	    NOC        USA  UZB  VEN  VIE   YUG  ZAM  ZIM  ZZX  
	    Edition                                             
	    1992     224.0  NaN  NaN  NaN   NaN  NaN  NaN  NaN  
	    1996     260.0  2.0  NaN  NaN  26.0  1.0  NaN  NaN  
	    2000     248.0  4.0  NaN  1.0  26.0  NaN  NaN  NaN  
	    2004     264.0  5.0  2.0  NaN   NaN  NaN  3.0  NaN  
	    2008     315.0  6.0  1.0  1.0   NaN  NaN  4.0  NaN  
	    
	    [5 rows x 138 columns]

Great work! As you can see, the pivot table DataFrame has mostly NaN entries (because most countries do not win any medals in a given Olympic edition).  

---

## Computing fraction of medals per Olympic edition    

In this exercise, you'll start with the DataFrames editions, medals, & medal_counts from prior exercises.  

You can extract a Series with the total number of medals awarded in each Olympic edition.  

The DataFrame medal_counts can be divided row-wise by the total number of medals awarded each edition; the method .divide() performs the broadcast as you require.  

This gives you a normalized indication of each country's performance in each edition.  

### Instructions :  

 - et the index of the DataFrame editions to be 'Edition' (using the method .set_index()). Save the result as totals.
 - Extract the 'Grand Total' column from totals and assign the result back to totals.
 - Divide the DataFrame medal_counts by totals along each row. You will have to use the .divide() method with the option axis='rows'. Assign the result to fractions.
 - Print first & last 5 rows of the DataFrame fractions. This has been done for you, so hit 'Submit Answer' to see the results!

```python
print(editions.head())
print('-----------------')
# Set Index of editions: totals
totals = editions.set_index('Edition')
print(totals.head())
print('-----------------')

# Reassign totals['Grand Total']: totals
totals = totals['Grand Total']
print(totals.head())
print('-----------------')

# Divide medal_counts by totals: fractions
fractions = medal_counts.divide(totals,axis='rows')

# Print first & last 5 rows of fractions
print(fractions.head())
print('-----------------')
print(fractions.tail())
```

### Results :  

	<script.py> output:
	       Edition  Grand Total       City         Country
	    0     1896          151     Athens          Greece
	    1     1900          512      Paris          France
	    2     1904          470  St. Louis   United States
	    3     1908          804     London  United Kingdom
	    4     1912          885  Stockholm          Sweden
	    -----------------
		     Grand Total       City         Country
	    Edition                                        
	    1896             151     Athens          Greece
	    1900             512      Paris          France
	    1904             470  St. Louis   United States
	    1908             804     London  United Kingdom
	    1912             885  Stockholm          Sweden
	    -----------------
	    Edition
	    1896    151
	    1900    512
	    1904    470
	    1908    804
	    1912    885
	    Name: Grand Total, dtype: int64
	    -----------------
	    NOC      AFG  AHO  ALG       ANZ  ARG  ARM       AUS       AUT  AZE  BAH  \
	    Edition                                                                    
	    1896     NaN  NaN  NaN       NaN  NaN  NaN  0.013245  0.033113  NaN  NaN   
	    1900     NaN  NaN  NaN       NaN  NaN  NaN  0.009766  0.011719  NaN  NaN   
	    1904     NaN  NaN  NaN       NaN  NaN  NaN       NaN  0.002128  NaN  NaN   
	    1908     NaN  NaN  NaN  0.023632  NaN  NaN       NaN  0.001244  NaN  NaN   
	    1912     NaN  NaN  NaN  0.011299  NaN  NaN       NaN  0.015819  NaN  NaN   
	    
	    NOC        ...     URS  URU       USA  UZB  VEN  VIE  YUG  ZAM  ZIM       ZZX  
	    Edition    ...                                                                 
	    1896       ...     NaN  NaN  0.132450  NaN  NaN  NaN  NaN  NaN  NaN  0.039735  
	    1900       ...     NaN  NaN  0.107422  NaN  NaN  NaN  NaN  NaN  NaN  0.066406  
	    1904       ...     NaN  NaN  0.838298  NaN  NaN  NaN  NaN  NaN  NaN  0.017021  
	    1908       ...     NaN  NaN  0.078358  NaN  NaN  NaN  NaN  NaN  NaN       NaN  
	    1912       ...     NaN  NaN  0.114124  NaN  NaN  NaN  NaN  NaN  NaN       NaN  
	    
	    [5 rows x 138 columns]
	    -----------------
	    NOC          AFG  AHO       ALG  ANZ       ARG       ARM       AUS       AUT  \
	    Edition                                                                        
	    1992         NaN  NaN  0.001173  NaN  0.001173       NaN  0.033431  0.003519   
	    1996         NaN  NaN  0.001614  NaN  0.010758  0.001076  0.071006  0.001614   
	    2000         NaN  NaN  0.002481  NaN  0.009926  0.000496  0.090819  0.001985   
	    2004         NaN  NaN       NaN  NaN  0.023524       NaN  0.078579  0.004004   
	    2008     0.00049  NaN  0.000979  NaN  0.024976  0.002938  0.072968  0.001469   
	    
	    NOC           AZE       BAH ...   URS       URU       USA       UZB       VEN  \
	    Edition                     ...                                                 
	    1992          NaN  0.000587 ...   NaN       NaN  0.131378       NaN       NaN   
	    1996     0.000538  0.002690 ...   NaN       NaN  0.139860  0.001076       NaN   
	    2000     0.001489  0.002978 ...   NaN  0.000496  0.123077  0.001985       NaN   
	    2004     0.002503  0.001001 ...   NaN       NaN  0.132132  0.002503  0.001001   
	    2008     0.003428  0.002449 ...   NaN       NaN  0.154261  0.002938  0.000490   
	    
	    NOC           VIE       YUG       ZAM       ZIM  ZZX  
	    Edition                                               
	    1992          NaN       NaN       NaN       NaN  NaN  
	    1996          NaN  0.013986  0.000538       NaN  NaN  
	    2000     0.000496  0.012903       NaN       NaN  NaN  
	    2004          NaN       NaN       NaN  0.001502  NaN  
	    2008     0.000490       NaN       NaN  0.001959  NaN  
	    
	    [5 rows x 138 columns]

---

## Computing percentage change in fraction of medals won    

Here, you'll start with the DataFrames editions, medals, medal_counts, & fractions from prior exercises.  

To see if there is a host country advantage, you first want to see how the fraction of medals won changes from edition to edition.  

The expanding mean provides a way to see this down each column. It is the value of the mean with all the data available up to that point in time. If you are interested in learning more about pandas' expanding transformations, this section of the pandas documentation has additional information.  


### Instructions :  

 - Create mean_fractions by chaining the methods .expanding().mean() to fractions.
 - Compute the percentage change in mean_fractions down each column by applying .pct_change() and multiplying by 100. Assign the result to fractions_change.
 - Reset the index of fractions_change using the .reset_index() method. This will make 'Edition' an ordinary column.
 - Print the first and last 5 rows of the DataFrame fractions. This has been done for you, so hit 'Submit Answer' to see the results!

```python
print(fractions.head())
print('-------------------------')

# Apply the expanding mean: mean_fractions
mean_fractions = fractions.expanding().mean()
print(mean_fractions.head())
print('-------------------------')

# Compute the percentage change: fractions_change
fractions_change = mean_fractions.pct_change() * 100
print(fractions_change.head())
print('-------------------------')

# Reset the index of fractions_change: fractions_change
fractions_change = fractions_change.reset_index()

# Print first & last 5 rows of fractions_change
print(fractions_change.head())
print('-------------------------')
print(fractions_change.tail())
```

### Results :  

	<script.py> output:
	    NOC      AFG  AHO  ALG       ANZ  ARG  ARM       AUS       AUT  AZE  BAH  \
	    Edition                                                                    
	    1896     NaN  NaN  NaN       NaN  NaN  NaN  0.013245  0.033113  NaN  NaN   
	    1900     NaN  NaN  NaN       NaN  NaN  NaN  0.009766  0.011719  NaN  NaN   
	    1904     NaN  NaN  NaN       NaN  NaN  NaN       NaN  0.002128  NaN  NaN   
	    1908     NaN  NaN  NaN  0.023632  NaN  NaN       NaN  0.001244  NaN  NaN   
	    1912     NaN  NaN  NaN  0.011299  NaN  NaN       NaN  0.015819  NaN  NaN   
	    
	    NOC        ...     URS  URU       USA  UZB  VEN  VIE  YUG  ZAM  ZIM       ZZX  
	    Edition    ...                                                                 
	    1896       ...     NaN  NaN  0.132450  NaN  NaN  NaN  NaN  NaN  NaN  0.039735  
	    1900       ...     NaN  NaN  0.107422  NaN  NaN  NaN  NaN  NaN  NaN  0.066406  
	    1904       ...     NaN  NaN  0.838298  NaN  NaN  NaN  NaN  NaN  NaN  0.017021  
	    1908       ...     NaN  NaN  0.078358  NaN  NaN  NaN  NaN  NaN  NaN       NaN  
	    1912       ...     NaN  NaN  0.114124  NaN  NaN  NaN  NaN  NaN  NaN       NaN  
	    
	    [5 rows x 138 columns]
	    -------------------------
	    NOC      AFG  AHO  ALG       ANZ  ARG  ARM       AUS       AUT  AZE  BAH  \
	    Edition                                                                    
	    1896     NaN  NaN  NaN       NaN  NaN  NaN  0.013245  0.033113  NaN  NaN   
	    1900     NaN  NaN  NaN       NaN  NaN  NaN  0.011505  0.022416  NaN  NaN   
	    1904     NaN  NaN  NaN       NaN  NaN  NaN  0.011505  0.015653  NaN  NaN   
	    1908     NaN  NaN  NaN  0.023632  NaN  NaN  0.011505  0.012051  NaN  NaN   
	    1912     NaN  NaN  NaN  0.017466  NaN  NaN  0.011505  0.012804  NaN  NaN   
	    
	    NOC        ...     URS  URU       USA  UZB  VEN  VIE  YUG  ZAM  ZIM       ZZX  
	    Edition    ...                                                                 
	    1896       ...     NaN  NaN  0.132450  NaN  NaN  NaN  NaN  NaN  NaN  0.039735  
	    1900       ...     NaN  NaN  0.119936  NaN  NaN  NaN  NaN  NaN  NaN  0.053071  
	    1904       ...     NaN  NaN  0.359390  NaN  NaN  NaN  NaN  NaN  NaN  0.041054  
	    1908       ...     NaN  NaN  0.289132  NaN  NaN  NaN  NaN  NaN  NaN  0.041054  
	    1912       ...     NaN  NaN  0.254131  NaN  NaN  NaN  NaN  NaN  NaN  0.041054  
	    
	    [5 rows x 138 columns]
	    -------------------------
	    NOC      AFG  AHO  ALG        ANZ  ARG  ARM        AUS        AUT  AZE  BAH  \
	    Edition                                                                       
	    1896     NaN  NaN  NaN        NaN  NaN  NaN        NaN        NaN  NaN  NaN   
	    1900     NaN  NaN  NaN        NaN  NaN  NaN -13.134766 -32.304688  NaN  NaN   
	    1904     NaN  NaN  NaN        NaN  NaN  NaN   0.000000 -30.169386  NaN  NaN   
	    1908     NaN  NaN  NaN        NaN  NaN  NaN   0.000000 -23.013510  NaN  NaN   
	    1912     NaN  NaN  NaN -26.092774  NaN  NaN   0.000000   6.254438  NaN  NaN   
	    
	    NOC        ...      URS  URU         USA  UZB  VEN  VIE  YUG  ZAM  ZIM  \
	    Edition    ...                                                           
	    1896       ...      NaN  NaN         NaN  NaN  NaN  NaN  NaN  NaN  NaN   
	    1900       ...      NaN  NaN   -9.448242  NaN  NaN  NaN  NaN  NaN  NaN   
	    1904       ...      NaN  NaN  199.651245  NaN  NaN  NaN  NaN  NaN  NaN   
	    1908       ...      NaN  NaN  -19.549222  NaN  NaN  NaN  NaN  NaN  NaN   
	    1912       ...      NaN  NaN  -12.105733  NaN  NaN  NaN  NaN  NaN  NaN   
	    
	    NOC            ZZX  
	    Edition             
	    1896           NaN  
	    1900     33.561198  
	    1904    -22.642384  
	    1908      0.000000  
	    1912      0.000000  
	    
	    [5 rows x 138 columns]
	    -------------------------
	    NOC  Edition  AFG  AHO  ALG        ANZ  ARG  ARM        AUS        AUT  AZE  \
	    0       1896  NaN  NaN  NaN        NaN  NaN  NaN        NaN        NaN  NaN   
	    1       1900  NaN  NaN  NaN        NaN  NaN  NaN -13.134766 -32.304688  NaN   
	    2       1904  NaN  NaN  NaN        NaN  NaN  NaN   0.000000 -30.169386  NaN   
	    3       1908  NaN  NaN  NaN        NaN  NaN  NaN   0.000000 -23.013510  NaN   
	    4       1912  NaN  NaN  NaN -26.092774  NaN  NaN   0.000000   6.254438  NaN   
	    
	    NOC    ...      URS  URU         USA  UZB  VEN  VIE  YUG  ZAM  ZIM        ZZX  
	    0      ...      NaN  NaN         NaN  NaN  NaN  NaN  NaN  NaN  NaN        NaN  
	    1      ...      NaN  NaN   -9.448242  NaN  NaN  NaN  NaN  NaN  NaN  33.561198  
	    2      ...      NaN  NaN  199.651245  NaN  NaN  NaN  NaN  NaN  NaN -22.642384  
	    3      ...      NaN  NaN  -19.549222  NaN  NaN  NaN  NaN  NaN  NaN   0.000000  
	    4      ...      NaN  NaN  -12.105733  NaN  NaN  NaN  NaN  NaN  NaN   0.000000  
	    
	    [5 rows x 139 columns]
	    -------------------------
	    NOC  Edition  AFG  AHO        ALG  ANZ       ARG        ARM        AUS  \
	    21      1992  NaN  0.0  -7.214076  0.0 -6.767308        NaN   2.754114   
	    22      1996  NaN  0.0   8.959211  0.0  1.306696        NaN  10.743275   
	    23      2000  NaN  0.0  19.762488  0.0  0.515190 -26.935484  12.554986   
	    24      2004  NaN  0.0   0.000000  0.0  9.625365   0.000000   8.161162   
	    25      2008  NaN  0.0  -8.197807  0.0  8.588555  91.266408   6.086870   
	    
	    NOC       AUT        AZE ...   URS        URU       USA        UZB       VEN  \
	    21  -3.034840        NaN ...   0.0   0.000000 -1.329330        NaN  0.000000   
	    22  -3.876773        NaN ...   0.0   0.000000 -1.010378        NaN  0.000000   
	    23  -3.464221  88.387097 ...   0.0 -12.025323 -1.341842  42.258065  0.000000   
	    24  -2.186922  48.982144 ...   0.0   0.000000 -1.031922  21.170339 -1.615969   
	    25  -3.389836  31.764436 ...   0.0   0.000000 -0.450031  14.610625 -6.987342   
	    
	    NOC       VIE       YUG        ZAM        ZIM  ZZX  
	    21        NaN  0.000000   0.000000   0.000000  0.0  
	    22        NaN -2.667732 -10.758472   0.000000  0.0  
	    23        NaN -2.696445   0.000000   0.000000  0.0  
	    24   0.000000  0.000000   0.000000 -43.491929  0.0  
	    25  -0.661117  0.000000   0.000000 -23.316533  0.0  
	    
	    [5 rows x 139 columns]

---

## Building hosts DataFrame    

Your task here is to prepare a DataFrame hosts by left joining editions and ioc_codes.  

Once created, you will subset the Edition and NOC columns and set Edition as the Index.  

There are some missing NOC values; you will set those explicitly.  

Finally, you'll reset the Index & print the final DataFrame.  

### Instructions :  

 - Create the DataFrame hosts by doing a left join on DataFrames editions and ioc_codes (using pd.merge()).
 - Clean up hosts by subsetting and setting the Index.
 - Extract the columns 'Edition' and 'NOC'.
 - Set 'Edition' column as the Index.
 - Use the .loc[] accessor to find and assign the missing values to the 'NOC' column in hosts. This has been done for you.
Reset the index of hosts using .reset_index(), and then hit 'Submit Answer' to see what hosts looks like!

```python
# Import pandas
import pandas as pd

print(editions.head())
print('-----------------')
print(ioc_codes.head())
print('-----------------')

# Left join editions and ioc_codes: hosts
hosts = pd.merge(editions,ioc_codes,how='left')
print(hosts.head())
print('-----------------')

# Extract relevant columns and set index: hosts
hosts = hosts[['Edition','NOC']].set_index('Edition')
print(hosts.head())
print('-----------------')

# Fix missing 'NOC' values of hosts
print(hosts.loc[hosts.NOC.isnull()])
hosts.loc[1972, 'NOC'] = 'FRG'
hosts.loc[1980, 'NOC'] = 'URS'
hosts.loc[1988, 'NOC'] = 'KOR'
print(hosts.head())
print('-----------------')

# Reset Index of hosts: hosts
hosts = hosts.reset_index()

# Print hosts
print(hosts)
print('-----------------')
```

### Results :  

	<script.py> output:
	       Edition  Grand Total       City         Country
	    0     1896          151     Athens          Greece
	    1     1900          512      Paris          France
	    2     1904          470  St. Louis   United States
	    3     1908          804     London  United Kingdom
	    4     1912          885  Stockholm          Sweden
	    -----------------
		       Country  NOC
	    0      Afghanistan  AFG
	    1          Albania  ALB
	    2          Algeria  ALG
	    3  American Samoa*  ASA
	    4          Andorra  AND
	    -----------------
	       Edition  Grand Total       City         Country  NOC
	    0     1896          151     Athens          Greece  GRE
	    1     1900          512      Paris          France  FRA
	    2     1904          470  St. Louis   United States  USA
	    3     1908          804     London  United Kingdom  GBR
	    4     1912          885  Stockholm          Sweden  SWE
	    -----------------
		     NOC
	    Edition     
	    1896     GRE
	    1900     FRA
	    1904     USA
	    1908     GBR
	    1912     SWE
	    -----------------
		     NOC
	    Edition     
	    1972     NaN
	    1980     NaN
	    1988     NaN
		     NOC
	    Edition     
	    1896     GRE
	    1900     FRA
	    1904     USA
	    1908     GBR
	    1912     SWE
	    -----------------
		Edition  NOC
	    0      1896  GRE
	    1      1900  FRA
	    2      1904  USA
	    3      1908  GBR
	    4      1912  SWE
	    5      1920  BEL
	    6      1924  FRA
	    7      1928  NED
	    8      1932  USA
	    9      1936  GER
	    10     1948  GBR
	    11     1952  FIN
	    12     1956  AUS
	    13     1960  ITA
	    14     1964  JPN
	    15     1968  MEX
	    16     1972  FRG
	    17     1976  CAN
	    18     1980  URS
	    19     1984  USA
	    20     1988  KOR
	    21     1992  ESP
	    22     1996  USA
	    23     2000  AUS
	    24     2004  GRE
	    25     2008  CHN
	    -----------------

---

## Reshaping for analysis    

This exercise starts off with fractions_change and hosts already loaded.  

Your task here is to reshape the fractions_change DataFrame for later analysis.  

Initially, fractions_change is a wide DataFrame of 26 rows (one for each Olympic edition) and 139 columns (one for the edition and 138 for the competing countries).  

On reshaping with pd.melt(), as you will see, the result is a tall DataFrame with 3588 rows and 3 columns that summarizes the fractional change in the expanding mean of the percentage of medals won for each country in blocks.  

### Instructions :  

 - Create a DataFrame reshaped by reshaping the DataFrame fractions_change with pd.melt().
 - You'll need to use the keyword argument id_vars='Edition' to set the identifier variable.
 - You'll also need to use the keyword argument value_name='Change' to set the measured variables.
 - Print the shape of the DataFrames reshaped and fractions_change. This has been done for you.
 - Create a DataFrame chn by extracting all the rows from reshaped in which the three letter code for each country ('NOC') is 'CHN'.
 - Print the last 5 rows of the DataFrame chn using the .tail() method. This has been done for you, so hit 'Submit Answer' to see the results!

```python
# Import pandas
import pandas as pd

# Reshape fractions_change: reshaped
reshaped = pd.melt(fractions_change,id_vars='Edition',value_name='Change')

# Print reshaped.shape and fractions_change.shape
print(reshaped.shape, fractions_change.shape)

# Extract rows from reshaped where 'NOC' == 'CHN': chn
chn = reshaped[reshaped['NOC'] == 'CHN']

# Print last 5 rows of chn with .tail()
print(chn.tail())
```

### Results :  

	# Import pandas
	import pandas as pd

	# Reshape fractions_change: reshaped
	reshaped = pd.melt(fractions_change,id_vars='Edition',value_name='Change')

	# Print reshaped.shape and fractions_change.shape
	print(reshaped.shape, fractions_change.shape)

	# Extract rows from reshaped where 'NOC' == 'CHN': chn
	chn = reshaped[reshaped['NOC'] == 'CHN']

	# Print last 5 rows of chn with .tail()
	print(chn.tail())

Great work! On looking at the hosting countries from the last 5 Olympic editions and the fractional change of medals won by China the last 5 editions, you can see that China fared significantly better in 2008 (i.e., when China was the host country).  

---

## Merging to compute influence   

This exercise starts off with the DataFrames reshaped and hosts in the namespace.  

Your task is to merge the two DataFrames and tidy the result.  

The end result is a DataFrame summarizing the fractional change in the expanding mean of the percentage of medals won for the host country in each Olympic edition.  

### Instructions :  

 - Merge reshaped and hosts using an inner join. Remember, how='inner' is the default behavior for pd.merge().
 - Print the first 5 rows of the DataFrame merged. This has been done for you. You should see that the rows are jumbled chronologically.
 - Set the index of merged to be 'Edition' and sort the index.
 - Print the first 5 rows of the DataFrame influence. This has been done for you, so hit 'Submit Answer' to see the results!

```python
# Import pandas
import pandas as pd

# Merge reshaped and hosts: merged
merged = pd.merge(reshaped,hosts,how='inner')

# Print first 5 rows of merged
print(merged.head())
print('-------------------')

# Set Index of merged and sort it: influence
influence = merged.set_index('Edition').sort_index()

# Print first 5 rows of influence
print(influence.head())
print('-------------------')
```

### Results :  

	script.py> output:
	       Edition  NOC     Change
	    0     1956  AUS  54.615063
	    1     2000  AUS  12.554986
	    2     1920  BEL  54.757887
	    3     1976  CAN  -2.143977
	    4     2008  CHN  13.251332
	    -------------------
		     NOC      Change
	    Edition                 
	    1896     GRE         NaN
	    1900     FRA  198.002486
	    1904     USA  199.651245
	    1908     GBR  134.489218
	    1912     SWE   71.896226
	    -------------------
	    
Well done! It would be far more informative to visualize these results. This is exactly what you'll do in the next exercise!  

---

## Plotting influence of host country    

This final exercise starts off with the DataFrames influence and editions in the namespace. Your job is to plot the influence of being a host country.  

### Instructions :  

 - Create a Series called change by extracting the 'Change' column from influence.
 - Create a bar plot of change using the .plot() method with kind='bar'. Save the result as ax to permit further customization.
 - Customize the bar plot of change to improve readability:
 - Apply the method .set_ylabel("% Change of Host Country Medal Count") toax.
 - Apply the method .set_title("Is there a Host Country Advantage?") to ax.
 - Apply the method .set_xticklabels(editions['City']) to ax.
 - Reveal the final plot using plt.show().

```python
# Import pyplot
import matplotlib.pyplot as plt

# Extract influence['Change']: change
change = influence['Change']

# Make bar plot of change: ax
ax = change.plot(kind='bar')

# Customize the plot to improve readability
ax.set_ylabel("% Change of Host Country Medal Count")
ax.set_title("Is there a Host Country Advantage?")
ax.set_xticklabels(editions['City'])

# Display the plot
plt.show()
```

### Results :  

see : img/graph1  

Fantastic work! If you want to view a larger version of the figure, click the 'pop-out' next to 'Plots' to load it in a separate window. What do you think - is there a host country advantage?  

---