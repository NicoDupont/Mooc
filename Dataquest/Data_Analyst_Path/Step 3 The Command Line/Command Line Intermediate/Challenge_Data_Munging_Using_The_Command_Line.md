02/2017  
Dataquest : Data Analyst Path  
Step 3: The Command Line  
SubStep : Command Line: Intermediate : Challenge: Data Munging Using The Command Line  
dimanche, 26. février 2017 02:31 



---
#1: Data Munging
In this challenge, you'll practice the command line concepts you've learned so far by munging datasets using just the command line. Data munging involves transforming datasets to make them easier to work with. Some datasets are too large to load into Python, so looking at them or transforming them beforehand can be useful. Even for smaller datasets, simple exploration on the command line is faster than exploration in Python, and file-based tasks like unifying datasets can be faster on the command line.  

You'll be interacting with datasets on U.S. housing affordability from the U.S. Department of Housing & Urban Development in this challenge. To start things off, let's explore the datasets in the first few steps.  


##Instructions  
- List all of the files in the current directory (the home directory), including the file names, permissions, formats, and sizes.


```bash  
ls -l
```

####Results: 

```bash  
/home/dq$ ls -l                                                                 
total 6672                                                                      
-rwxr-xr-x 1 dq dq 2051577 Feb 26 13:30 Hud_2005.csv                            
-rwxr-xr-x 1 dq dq 1874334 Feb 26 13:30 Hud_2007.csv                            
-rwxr-xr-x 1 dq dq 2902856 Feb 26 13:30 Hud_2013.csv
```



---
#2: Data Exploration
It looks like there are 3 different CSV files, each corresponding to a separate year.  

You learned about the tail command to display the last n rows in a file. To display the first n rows (10 by default), you can instead us the head command.  


##Instructions  
- Use the head command to display the first 10 rows of each of the 3 CSV files.


```bash  
head Hud_2005.csv
head Hud_2007.csv
head Hud_2013.csv
```

####Results: 

```bash  
/home/dq$ head Hud_2005.csv                                                     
AGE1,BURDEN,FMR,FMTBEDRMS,FMTBUILT,TOTSAL                                       
43,0.513,680,'3 3BR','1980-1989',20000                                          
44,0.2225915493,760,'4 4BR+','1980-1989',71000                                  
58,0.2178312657,680,'3 3BR','1980-1989',63000                                   
22,0.21745562129999998,519,'1 1BR','1980-1989',27040                            
48,0.28285714289999997,600,'1 1BR','1980-1989',14000                            
42,0.2922857143,788,'3 3BR','1980-1989',42000                                   
-9,-9.0,702,'2 2BR','1980-1989',-9                                              
23,0.14475,546,'2 2BR','1980-1989',48000                                        
51,0.2962,680,'3 3BR','1980-1989',58000                                         
/home/dq$ head Hud_2007.csv                                                     
AGE1,BURDEN,FMR,FMTBEDRMS,FMTBUILT,TOTSAL                                       
-9,-9.0,1048,'3 3BR','2000-2009',-9                                             
69,0.1207594937,1048,'3 3BR','2000-2009',0                                      
45,0.3683076923,757,'3 3BR','1980-1989',26000                                   
47,0.099419707,847,'4 4BR+','1980-1989',126000                                  
30,0.1340625,616,'2 2BR','1980-1989',42000                                      
50,0.2824,605,'1 1BR','1980-1989',15000                                         
44,0.0885517241,807,'3 3BR','1980-1989',145000                                  
-9,-9.0,778,'2 2BR','1980-1989',-9                                              
24,0.07925,599,'2 2BR','1980-1989',96000
/home/dq$ head Hud_2013.csv                                                     
AGE1,BURDEN,FMR,FMTBEDRMS,FMTBUILT,TOTSAL                                       
82,0.35491926090000003,956,'2 2BR','2000-2009',0                                
50,0.047527264699999995,1100,'4 4BR+','1980-1989',123000                        
53,0.6027025095,1100,'4 4BR+','1980-1989',28000                                 
67,0.1039106145,949,'3 3BR','1980-1989',0                                       
26,0.094019035,737,'2 2BR','1980-1989',96900                                    
56,0.5564822846,657,'1 1BR','1980-1989',15000                                   
50,0.1998227609,988,'3 3BR','1980-1989',70001                                   
26,0.366,773,'2 2BR','1980-1989',20000                                          
60,0.1165841647,1125,'3 3BR','1980-1989',107000
```




---
#3: Filtering
The goal is to eventually get this into a Pandas Dataframe so let's combine the datasets into one file so it can be read in easily. Since each dataset contains the same columns, you need to combine the datasets into one file. You can't, however, just use append the full contents of each file to one final file since each dataset contains the header row. The consolidated file should only contain the header row once (in the first row). You need to instead append the header row to the consolidated file once, then append only the non-header rows from the 3 datasets to the consolidated file.  

Here's a reminder of how the first 10 rows of Hud_2013.csv looks like:  

![img1](https://dq-content.s3.amazonaws.com/D1jLnjY.png  "img1")

Since the header row is always the first row in each of the datasets, you can just select all rows after the header row. You can use the command wc along with the l flag to return the number of lines for a specified file. You can use each file's line count combined with the tail command to return the last n lines of a file.  

##Instructions  
- Create the file combined_hud.csv and append the header row from one of the datasets.
- Select all non-header rows from Hud_2005.csv and append to combined_hud.csv.
- Display the first 10 rows in combined_hud.csv to verify your work.


```bash  
wc -l Hud_2005.csv
head -n 1 Hud_2005.csv > combined_hud.csv
tail -n 46853 Hud_2005.csv >> combined_hud.csv
head combined_hud.csv
```

####Results: 

```bash  
/home/dq$ wc -l Hud_2005.csv                                                    
46854 Hud_2005.csv                                                              
/home/dq$ head 1 Hud_2005.csv > combined_hud.csv                                
head: cannot open ‘1’ for reading: No such file or directory                    
/home/dq$ head -n 1 Hud_2005.csv > combined_hud.csv                             
/home/dq$ tail -n 46853 Hud_2005.csv >> combined_hud.csv                        
/home/dq$ head combined_hud.csv                                                 
AGE1,BURDEN,FMR,FMTBEDRMS,FMTBUILT,TOTSAL                                       
43,0.513,680,'3 3BR','1980-1989',20000                                          
44,0.2225915493,760,'4 4BR+','1980-1989',71000                                  
58,0.2178312657,680,'3 3BR','1980-1989',63000                                   
22,0.21745562129999998,519,'1 1BR','1980-1989',27040                            
48,0.28285714289999997,600,'1 1BR','1980-1989',14000                            
42,0.2922857143,788,'3 3BR','1980-1989',42000                                   
-9,-9.0,702,'2 2BR','1980-1989',-9                                              
23,0.14475,546,'2 2BR','1980-1989',48000                                        
51,0.2962,680,'3 3BR','1980-1989',58000
```





---
#4: Consolidating Datasets
Looks good! Now finish the job by adding in the data from the other datasets.  


##Instructions  
- Append the remaining datasets in the order of the years they describe.
	- Select all non-header rows from Hud_2007.csv and append to combined_hud.csv.
	- Select all non-header rows from Hud_2013.csv and append to combined_hud.csv.
- Display the last 10 rows of combined_hud.csv and verify that they match the last 10 rows of Hud_2013.csv.


```bash  
wc -l Hud_2007.csv
wc -l Hud_2013.csv
tail -n 42729 Hud_2007.csv >> combined_hud.csv 
tail -n 64535 Hud_2013.csv >> combined_hud.csv 
tail combined_hud.csv
tail Hud_2013.csv
```

####Results: 

```bash  
/home/dq$ wc -l Hud_2007.csv                                                    
42730 Hud_2007.csv                                                              
/home/dq$ wc -l Hud_2013.csv                                                    
64536 Hud_2013.csv                                                              
/home/dq$ tail -n 42729 Hud_2007.csv >> combined_hud.csv                        
/home/dq$ tail -n 64535 Hud_2013.csv >> combined_hud.csv
/home/dq$ tail combined_hud.csv                                                 
-9,-9.0,1430,'3 3BR','1940-1959',-9                                             
58,0.1714816491,973,'1 1BR','1960-1979',42000                                   
54,0.17504740870000002,702,'1 1BR','1940-1959',48000                            
71,0.44792626729999996,652,'2 2BR','1960-1979',0                                
32,0.4738463158,1285,'1 1BR','-5',38000                                         
55,1.1845714286,556,'1 1BR','-5',0                                              
37,0.0,966,'2 2BR','1940-1959',75000                                            
23,0.6649322059,2701,'3 3BR','1940-1959',40000                                  
57,0.0834180739,770,'1 1BR','-5',60000                                          
66,0.0,542,'1 1BR','After 2010',0                                               
/home/dq$ tail Hud_2013.csv                                                     
-9,-9.0,1430,'3 3BR','1940-1959',-9                                             
58,0.1714816491,973,'1 1BR','1960-1979',42000                                   
54,0.17504740870000002,702,'1 1BR','1940-1959',48000                            
71,0.44792626729999996,652,'2 2BR','1960-1979',0                                
32,0.4738463158,1285,'1 1BR','-5',38000                                         
55,1.1845714286,556,'1 1BR','-5',0                                              
37,0.0,966,'2 2BR','1940-1959',75000                                            
23,0.6649322059,2701,'3 3BR','1940-1959',40000                                  
57,0.0834180739,770,'1 1BR','-5',60000                                          
66,0.0,542,'1 1BR','After 2010',0     
```



---
#5: Counting
Now that you have a consolidated dataset, you can start to answer basic questions on the entire dataset.  


##Instructions  
- Count and display the number of lines in combined_hud.csv containing 1980-1989.


```bash  
grep "1980-1989" combined_hud.csv | wc -l
```

####Results: 

```bash  
/home/dq$ grep "1980-1989" combined_hud.csv | wc -l                             
19711
```




---
#6: Next Steps
In this challenge, you learned about a few useful commands for exploring files and practiced data munging from the command line. Next in this course is a guided project where you'll explore how to create Python scripts from the command line for more robust and reusable logic.  
