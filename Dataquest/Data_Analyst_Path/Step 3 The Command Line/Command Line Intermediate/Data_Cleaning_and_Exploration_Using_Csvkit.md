02/2017  
Dataquest : Data Analyst Path  
Step 3: The Command Line  
SubStep : Command Line: Intermediate : Data Cleaning and Exploration Using Csvkit  
dimanche, 26. février 2017 04:10 


---
#1: Csvkit
So far, we've been using the default command line tools to clean, munge, and explore data. Tools like wc and head are useful tools, but weren't designed specifically for working with datasets and are limited in many ways. These tools lack features specific to working with tabular datasets, like parsing the header row or understanding the row and column layout. Because of this, in the Data Munging Using the Command Line challenge, you had to specifically compute the number of lines in each CSV file using the wc tool and use that number to select just the non-header rows using the tail tool. You then had to repeat this for each CSV file you were trying to merge into the resulting, single file!  

In this mission, we'll learn about the Csvkit library, which supercharges your workflow by adding 13 new command line tools specifically for working with CSV files. We'll focus on these 5 tools from Csvkit:  

- csvstack: for stacking rows from multiple CSV files.
- csvlook: renders CSV in pretty table format.
- csvcut: for selecting specific columns from a CSV file.
- csvstat: for calculating descriptive statistics for some or all columns.
- csvgrep: for filtering tabular data using specific criteria.

We'll be using csvkit version 0.9.1 in this mission and you can read about the installation procedure in the documentation. We'll continue to work with the same 3 datasets on housing affordability:  

- Hud_2005.csv,
- Hud_2007.csv,
- Hud_2013.csv.


---
#2: Csvstack
To start, let's circle back to the task of merging 3 CSV files into 1 file. We can use csvstack tool to consolidate the rows from multiple CSV files and redirect the stdout to a new file:  

```bash
csvstack file1.csv file2.csv file3.csv > final.csv
```

As long as the header row for each file in the stdin to csvstack is the same, the first row in the resulting file will match this header row. After the header row, final.csv will contain all of the non-header rows from file1.csv, then all of the non-header rows from file2.csv, then finally the non-header rows from file3.csv. If you don't redirect the stdout of csvstack to a file or a tool like head, the full output will be rendered in the terminal. This can cause your terminal to grind to a halt as it tries to process and display all of the output and you want to be extra careful to avoid doing so.  

If you peeked at the documentation, you may have noticed that the behavior of csvstack can be modified using a few different flags. For example,  

if you want to be able to trace the file where each row originated from in the merged file, you can use the -g flag to specify a grouping value for each filename. When stacking the rows from a file, csvstack will add the corresponding value in a new column. Lastly, you can use the -n flag to specify the name of this new column. The following code will create a new column named origin, containing the values 1, 2, or 3 depending on which file that row originated from:  

```bash
csvstack -n origin -g 1,2,3 file1.csv file2.csv file3.csv > final.csv
```

The rows in final.csv that originated from file1.csv will contain the value 1 in the origin column and those from file2.csv will contain the value 2 in the origin column. Let's now use csvstack to combine the 3 datasets on U.S. housing affordability from the last challenge.  

##Instructions  

 - Merge Hud_2005.csv, Hud_2007.csv, and Hud_2013.csv in that order into one file:
	- Name the resulting file Combined_hud.csv.
	- Add an extra column named year which contains the year value from the file name for each row. E.g. the rows that originated from Hud_2005.csv should have 2005 as the value in the year column.
 - Use head to preview the first few rows of Combined_hud.csv.
 - Use the wc command with the l flag to confirm that the merged file contains 154118 rows.
 
 ```bash
 csvstack -n year -g 2005,2007,2013 Hud_2005.csv Hud_2007.csv Hud_2013.csv > Combined_hud.csv
 head Combined_hud.csv
 wc -l Combined_hud.csv
 ```

####Results: 

```bash
/home/dq$ csvstack -n origin -g 1,2,3 Hud_2005.csv Hud_2007.csv Hud_2013.csv > C
ombined_hud.csv                                                                 
/home/dq$ rm Combined_hud.csv                                                   
/home/dq$ csvstack -n year-g 2005,2007,2013 Hud_2005.csv Hud_2007.csv Hud_2013.c
sv > Combined_hud.csv                                                           
[Errno 2] No such file or directory: '2005,2007,2013'                           
/home/dq$ csvstack -n year-g 2005,2007,2013 Hud_2005.csv Hud_2007.csv Hud_2013.c
sv > Combined_hud.csv                                                           
[Errno 2] No such file or directory: '2005,2007,2013'                           
/home/dq$ csvstack -n year -g 2005,2007,2013 Hud_2005.csv Hud_2007.csv Hud_2013.
csv > Combined_hud.csv                                                          
/home/dq$ head Combined.csv                                                     
head: cannot open ‘Combined.csv’ for reading: No such file or directory         
/home/dq$ head Combined_hud.csv                                                 
year,AGE1,BURDEN,FMR,FMTBEDRMS,FMTBUILT,TOTSAL                                  
2005,43,0.513,680,'3 3BR','1980-1989',20000                                     
2005,44,0.223,760,'4 4BR+','1980-1989',71000                                    
2005,58,0.218,680,'3 3BR','1980-1989',63000                                     
2005,22,0.217,519,'1 1BR','1980-1989',27040                                     
2005,48,0.283,600,'1 1BR','1980-1989',14000                                     
2005,42,0.292,788,'3 3BR','1980-1989',42000                                     
2005,-9,-9.000,702,'2 2BR','1980-1989',-9                                       
2005,23,0.145,546,'2 2BR','1980-1989',48000                                     
2005,51,0.296,680,'3 3BR','1980-1989',58000                                     
/home/dq$ wc -l Combined_hud.csv                                                
154118 Combined_hud.csv  
```



---
#3: Csvlook
While head allows you to quickly observe the first few rows in a file, it doesn't attempt to format the rendered output at all. CSV files are tabular and it's incredibly useful to observe this structure and other data tools like Pandas and Microsoft Excel factored that notion in when displaying tabular data. Thankfully, we can use the csvlook tool to display tabular data in the table format we're used to.  

The csvlook tool parses CSV formatted data from it's stdin and outputs a pretty formatted table representation of that data to it's stdout:  

```bash
head -10 final.csv | csvlook
```

Let's use csvlook to explore the first few rows from the CSV file we created in the last screen.  

##Instructions  
 - Use csvlook to preview the first 10 rows from Combined_hud.csv.
 
 ```bash
 head -10 Combined_hud.csv | csvlook
 ```

####Results: 

```bash
/home/dq$ head -10 Combined_hud.csv | csvlook                                   
|-------+------+--------+-----+-----------+-------------+---------|             
|  year | AGE1 | BURDEN | FMR | FMTBEDRMS | FMTBUILT    | TOTSAL  |             
|-------+------+--------+-----+-----------+-------------+---------|             
|  2005 | 43   | 0.513  | 680 | '3 3BR'   | '1980-1989' | 20000   |             
|  2005 | 44   | 0.223  | 760 | '4 4BR+'  | '1980-1989' | 71000   |             
|  2005 | 58   | 0.218  | 680 | '3 3BR'   | '1980-1989' | 63000   |             
|  2005 | 22   | 0.217  | 519 | '1 1BR'   | '1980-1989' | 27040   |             
|  2005 | 48   | 0.283  | 600 | '1 1BR'   | '1980-1989' | 14000   |             
|  2005 | 42   | 0.292  | 788 | '3 3BR'   | '1980-1989' | 42000   |             
|  2005 | -9   | -9.000 | 702 | '2 2BR'   | '1980-1989' | -9      |             
|  2005 | 23   | 0.145  | 546 | '2 2BR'   | '1980-1989' | 48000   |             
|  2005 | 51   | 0.296  | 680 | '3 3BR'   | '1980-1989' | 58000   |             
|-------+------+--------+-----+-----------+-------------+---------|
```




---
#4: Csvcut
Csvlook returned a table formatted output of the merged CSV file. Let's now explore individual columns using the csvcut tool. Using the csvcut command with just the -n flag parses and displays all the columns in a CSV file along with an unique integer identifier for each column:  

```bash
csvcut -n Combined_hud.csv
```

will output:

>1: year
>2: AGE1
>3: BURDEN
>4: FMR
>5: FMTBEDRMS
>6: FMTBUILT
>7: TOTSAL

You can use the integer identifier for each column and the -cc flag to select just a specific column:

```bash
csvcut -c 1 Combined_hud.csv
```

will output just the year column. You want to avoid displaying the entire column since it contains 154118 rows and your terminal window will severely come to a halt attempting to display all that information. Instead, you can pipe the column output to head to preview just the first n rows.  

##Instructions  
 - Use csvcut to return all of the column names from Combined_hud.csv.
 - Use csvcut to display just the first 10 values in the AGE1 column.
 
```bash
csvcut -n Combined_hud.csv
csvcut -c 2 Combined_hud.csv | head
```

####Results: 

```bash
/home/dq$ csvcut -n Combined_hud.csv                                            
  1: year                                                                       
  2: AGE1                                                                       
  3: BURDEN                                                                     
  4: FMR                                                                        
  5: FMTBEDRMS                                                                  
  6: FMTBUILT                                                                   
  7: TOTSAL                                                                     
/home/dq$ csvcut -c 2 Combined_hud.csv | head                                   
AGE1                                                                            
43                                                                              
44                                                                              
58                                                                              
22                                                                              
48                                                                              
42                                                                              
-9                                                                              
23                                                                              
51
```




---
#5: Csvstat
Now that we know how to select specific columns, we can select a column and pipe it to the csvstat tool to calculate summary statistics for that column:  

```bash
csvcut -c 4 Combined_hud.csv | csvstat
```

This calculates a full suite of summary statistics, including:  

- max,
- min,
- sum,
- mean,
- median,
- standard deviation.

Depending on the size of the data, the full summary statistics for a column can take a long time and you often just want a specific summary statistic. You can use -- flags to choose specific summary statistics, which will greatly improve the speed:  

```bash
# Just the max value.
csvcut -c 2 Combined_hud.csv | csvstat --max
# Just the mean value.
csvcut -c 2 Combined_hud.csv | csvstat --mean
# Just the number of null values.
csvcut -c 2 Combined_hud.csv | csvstat --nulls
```

You can see a full list of flags in the documentation. If you want to calculate summary statistics over all the columns in a CSV file, you can pass the file to csvstat directly:  

```bash
csvstat Combined_hud.csv
```

##Instructions  
 - Use csvstat to calculate just the mean for each column in Combined_hud.csv.
 
```bash
csvstat --mean Combined_hud.csv
```

####Results: 

```bash
/home/dq$ csvstat --mean Combined_hud.csv                                       
  1. year: 2008.9044232628457                                                   
  2. AGE1: 46.511215505103266                                                   
  3. BURDEN: 5.303764743668771                                                  
  4. FMR: 1037.1186695822005                                                    
  5. FMTBEDRMS: None                                                            
  6. FMTBUILT: None                                                             
  7. TOTSAL: 44041.841931779105
```




---
#6: Csvcut | Csvstat
Let's use csvcut and csvstat to search for any problematic values in the AGE1 column.  

##Instructions  
 - Use csvstat to calculate the full summary statistics for just the AGE1 column.
 
 ```bash
 csvcut -c 2 Combined_hud.csv | csvstat
 ```

####Results: 


```bash
/home/dq$ csvcut -c 2 Combined_hud.csv | csvstat                                
  1. AGE1                                                                       
        <class 'int'>                                                           
        Nulls: False                                                            
        Min: -9                                                                 
        Max: 93                                                                 
        Sum: 7168169                                                            
        Mean: 46.511215505103266                                                
        Median: 48                                                              
        Standard Deviation: 23.04901451351246                                   
        Unique values: 80                                                       
        5 most frequent values:                                                 
                -9:     11553                                                   
                50:     3208                                                    
                45:     3056                                                    
                40:     3040                                                    
                48:     3006                                                    
                                                                                
Row count: 154117
```



---
#7: Csvgrep
You'll notice that -9 is the most common value in the AGE1 column, which is problematic since age values have to be greater than 0. We can use csvgrep to select all the rows that match a specific pattern to dive a bit deeper. By default, csvgrep will search all of the rows in the dataset but we can restrict the search to specific columns using the -c flag (just like with csvcut). We then use the -m flag to specify the pattern:  

```bash
csvgrep -c 2 -m -9 Combined_hud.csv
```

This command will return all rows from Combined_hud.csv with -9 as the value for the AGE1 column. The behavior of csvgrep can be customized using the flags. For example, you can use the -r flag to pass in a regular expression as the pattern instead. We're now going to combined several of the tools we've talked about so far so that you can see the real power of using the csvkit tools combined with other CLI tools.  

##Instructions  
 - Display the first 10 rows from Combined_hud.csv where the value for the AGE1 column is -9 in a pretty table format.

```bash
csvgrep -c 2 -m -9 Combined_hud.csv | head -n10 | csvlook
```

####Results: 


```bash
/home/dq$ csvgrep -c 2 -m -9 Combined_hud.csv | head -n10 | csvlook             
|-------+------+--------+------+-----------+-------------+---------|            
|  year | AGE1 | BURDEN | FMR  | FMTBEDRMS | FMTBUILT    | TOTSAL  |            
|-------+------+--------+------+-----------+-------------+---------|            
|  2005 | -9   | -9.000 | 702  | '2 2BR'   | '1980-1989' | -9      |            
|  2005 | -9   | -9.000 | 531  | '1 1BR'   | '1980-1989' | -9      |            
|  2005 | -9   | -9.000 | 1034 | '3 3BR'   | '2000-2009' | -9      |            
|  2005 | -9   | -9.000 | 631  | '1 1BR'   | '1980-1989' | -9      |            
|  2005 | -9   | -9.000 | 712  | '4 4BR+'  | '1990-1999' | -9      |            
|  2005 | -9   | -9.000 | 1006 | '3 3BR'   | '2000-2009' | -9      |            
|  2005 | -9   | -9.000 | 631  | '1 1BR'   | '1980-1989' | -9      |            
|  2005 | -9   | -9.000 | 712  | '3 3BR'   | '2000-2009' | -9      |            
|  2005 | -9   | -9.000 | 1087 | '3 3BR'   | '2000-2009' | -9      |            
|-------+------+--------+------+-----------+-------------+---------|  
```




---
#8: Filtering Out Problematic Rows
Let's now filter out all of these problematic rows from the dataset since they have data quality issues. Csvkit wasn't developed with a sharp focus on editing existing files, and the easiest way to filter rows is to create a separate file with just the rows we're interested in. To accomplish this, we can redirect the output of csvgrep to a file. So far, we've only used csvgrep to select rows that match a specific pattern. We need to instead select the rows that don't match a pattern, which we can specify with the -i flag. You can read more about this flag in the documentation.  

##Instructions  
 - Select all rows where the value for AGE1 isn't -9 and write just those rows to positive_ages_only.csv.
 
```bash
csvgrep -c 2 -m -9 -i Combined_hud.csv > positive_ages_only.csv
```

####Results: 

```bash
/home/dq$ csvgrep -c 2 -m -9 -i Combined_hud.csv > positive_ages_only.csv
```




---
#9: Next Steps
In this challenge, you learned how to use the csvkit library to explore and clean CSV files. You should use csvkit whenever you need to quickly transform or explore data from the command line, but remember that it has a few limitations:

 - Csvkit is not optimized for speed and struggles to run some commands over larger files.

 - Csvkit has very limited capabilities for actually editing problematic values in a dataset, sin ce the community behind the library aspired to keep the library small and lightweight.