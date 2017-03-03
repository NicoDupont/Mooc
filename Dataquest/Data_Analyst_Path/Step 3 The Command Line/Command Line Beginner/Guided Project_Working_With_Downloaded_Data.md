02/2017  
Dataquest : Data Analyst Path  
Step 3: The Command Line  
SubStep : Command Line: Beginner : Guided Project: Working With Downloaded Data  
samedi, 25. février 2017 10:54 


---
#1: Extracting Downloaded Data
Almost all of the data you work with as a data scientist will be downloaded from a remote source, such as the internet. Downloaded files are sometimes in a format that allows for immediate analysis, like the CSV format. Other times, the data will be in an archive format like TAR and ZIP. These formats compress one or more files into a single file. This reduces the overall size, making the files faster to download, and allows for multiple data files to be bundled into a single archive file.  

In this guided project, we'll be working with an education dataset in ZIP format. We'll learn how to extract the files inside and work with them.  

You may have noticed that the interface for this guided project is a bit different than the other interfaces. At the bottom is a terminal, where you'll be running commands. At the top is an editor, where you can edit files, such as Python scripts. To the left is a file browser, which allows you to view folders and open files for editing.  

see img/img3.png

The dataset we'll work with, called the Civil Rights Data Collection, contains information on educational achievement and opportunities in the US, broken down by race and school. For example, the dataset contains information the number of students of each racial group are enrolled in advanced classes in each school. Each row is a different school, and each column is an indicator of academic achievement.

For the purposes of this exercise, we'll be using a version of the data set that only contains 1 out of every 100 rows in the original data set. If you want the original data, you can download it here.

Here are the first few rows of the data set:  

see img/img4.png  

5 rows × 1929 columns  

Before we load the data and start analyzing it, we'll need to extract the actual data files from the archive file, crdc201314csv.zip. In order to extract files from a ZIP archive, we can use the unzip command. The unzip command can be called on the file test.zip like this:  

```bash 
unzip test.zip
```

The above command will extract all of the files from the archive test.zip into the current directory. Once the files have been extracted from an archive, it's good practice to delete the archive file to save space.  



##Instructions  
- List out the contents of the current directory with the ls command, and take note of the archive file crdc201314csv.zip.
- Extract the files in crdc201314csv.zip using the unzip command.
- List out the contents of the current directory, and make sure there are 4 new data files.
- Delete crdc201314csv.zip.

```bash  
ls
unzip crdc201314csv.zip
ls
rm crdc201314csv.zip
```

####Results: 

```bash  
/home/dq/scripts$ unzip crdc201314csv.zip                                       
Archive:  crdc201314csv.zip                                                     
  inflating: CRDC2013_14.csv                                                    
  inflating: CRDC2013_14content.csv                                             
  inflating: CRDC_documentation_csv.txt                                         
  inflating: CRDC_usage_agreement.txt                                           
/home/dq/scripts$ ls                                                            
CRDC2013_14content.csv  crdc201314csv.zip           CRDC_usage_agreement.txt    
CRDC2013_14.csv         CRDC_documentation_csv.txt  read.py                     
/home/dq/scripts$ rm crdc201314csv.zip
```



---
#2: Running A Python Script To Explore The Columns
Because the data set has over 2000 columns, there's a separate file that explains what each column means. The explanation file is CRDC2013_14content.csv, and the data file is CRDC2013_14.csv.  

We'll need to create a Python script, load CRDC2013_14content.csv using pandas, then figure out a few columns to explore in more depth.  

As you may recall from a previous mission, in order to run a script from the command line, we'll need to add a few lines. Let's say the following lines are in a file called read.py:  

```python 
if __name__ == "__main__":
    print("Program executed successfully!")
``` 
We could run the above script by running python read.py.  

We'll have to run our Python script using a virtual environment that has pandas installed. The virtual environment we need to activate is in the /dataquest/system/env/python3 folder. As you may recall from a previous mission, we'll need to run source /dataquest/system/env/python3/bin/activate to activate the virtual environment.  

##Instructions  
 - Activate the python3 virtual environment.
 - Run pip freeze to verify that pandas is installed and available.
 - Edit read.py so that it will run from the command line.
 - Add lines to read.py to:
	- Import pandas.
	- Read CRDC2013_14content.csv into a pandas DataFrame called contents.
		- Print the first few rows of contents.
 - Run read.py from the terminal, and verify that it worked properly.
 - Continue exploring the contents DataFrame to find any column names that interest you.

```bash  
source /dataquest/system/env/python3/bin/activate
pip freeze
python3 read.py
```

```python  
import pandas as pd
contents = pd.read_csv("CRDC2013_14content.csv")
print(contents.head())
print(contents.columns)
```

####Results: 

```bash  
/home/dq/scripts$ source /dataquest/system/env/python3/bin/activate    
(python3) /home/dq/scripts$ pip freeze                                 
appdirs==1.4.0                                                         
backports-abc==0.5
...
(python3) /home/dq/scripts$ python3 read.py
```




---
#3: Using Pandas To Find Patterns In The Data
Now that we've looked at the column names in more depth, some interesting columns may have popped out. Here are some that are potentially interesting:  

 - JJ -- indicates if the school is part of a juvenile justice facility, or youth prison.  
 - SCH_STATUS_MAGNET -- indicates if the school is a magnet school, an advanced school for students who score highly on certain tests.  

In order to explore any interesting patterns here, we can use Series.value_counts() to find unique values in each column. This will tell us how many schools are juvenile justice facilities or magnet schools.  

We can also count up how many students are in juvenile justice facilities by building a pivot table using the pandas.pivot_table() function. The pivot table will allow us to aggregate TOT_ENR_M, and TOT_ENR_F, which contain the total enrollment in the school of men and women, by JJ and SCH_STATUS_MAGNET. This will count up how many students are in magnet schools, or in juvenile justice facilities.  

For example, the below Python code will create a pivot table that counts up how many male and female students are in juvenile justice facilities:  

```python 
import pandas as pd
​
pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum")
```
##Instructions  
 - Create a new file called exploration.py that can be run from the command line.
 - In exploration.py:
	- Read CRDC2013_14.csv into a pandas DataFrame called data.
		- Make sure to specify the keyword argument encoding="Latin-1" to read the file in properly.
	- Call the value_counts method on the columns JJ and SCH_STATUS_MAGNET to count up how many schools fall into each category.
		- Print out the results so you see them when you run the script.
 - Execute exploration.py.
 - In exploration.py:
	- Construct two pivot tables that aggregate TOT_ENR_M and TOT_ENR_F based on JJ and SCH_STATUS_MAGNET.
		- Print out the results so you see them when you run the script.
 - Execute exploration.py.
 - Create a text file called findings.txt that summarizes any interesting patterns you've observed.

```bash  
touch exploration.py
python3 exploration.py
touch findings.txt
```

```python  
import pandas as pd
data = pd.read_csv("CRDC2013_14.csv",encoding="Latin-1")
#print(data.head())
#print(data.columns)
print(data["JJ"].value_counts())
print("--------")
print("--------")
print(data["SCH_STATUS_MAGNET"].value_counts())
print("--------")
print("--------")
pivoJJ = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum")
pivoSCH = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc="sum")
print(pivoJJ)
print("--------")
print("--------")
print(pivoSCH)
```

####Results: 

```bash  
(python3) /home/dq/scripts$ python3 exploration.py                     
NO     992                                                             
YES      8                                                             
Name: JJ, dtype: int64                                                 
NO     948                                                             
YES     52                                                             
Name: SCH_STATUS_MAGNET, dtype: int64 
     TOT_ENR_F  TOT_ENR_M                                              
JJ                                                                     
NO      252915     266702                                              
YES         71        427                                              
--------                                                               
--------  
                  TOT_ENR_F  TOT_ENR_M                                
SCH_STATUS_MAGNET                                                      
NO                    232487     245629                                
YES                    20499      21500  
```





---
#4: Using Pandas To Explore Enrollment By Race
There are several columns in the data that indicate school attributes broken down by race and gender. These start with the attribute name, like SCH_ENR, which indicates school enrollment. They then add a racial codename, like BL. Finally, they add a gender codename, like F. To put our example together, we get SCH_ENR_HI_F, which is hispanic female enrollment in the school.  

Here are the other racial group codenames:  

 - HI -- Hispanic.
 - AM -- American Indian.
 - AS -- Asian.
 - HP -- Hawaiian or Pacific Islander.
 - BL -- Black.
 - WH -- White.
 - TR -- Two or more races.

Here are the gender codenames:  

 - F -- Female.
 - M -- Male.

The column names for a certain attribute contain all possible combinations of racial and gender codenames. Below, we'll list out all the columns that indicate school enrollment for each racial and gender group:  

 - SCH_ENR_HI_M
 - SCH_ENR_HI_F
 - SCH_ENR_AM_M
 - SCH_ENR_AM_F
 - SCH_ENR_AS_M
 - SCH_ENR_AS_F
 - SCH_ENR_HP_M
 - SCH_ENR_HP_F
 - SCH_ENR_BL_M
 - SCH_ENR_BL_F
 - SCH_ENR_WH_M
 - SCH_ENR_WH_F
 - SCH_ENR_TR_M
 - SCH_ENR_TR_F

Additionally, there are also two columns that indicate total enrollment by gender:    

 - TOT_ENR_M -- total male enrollment.
 - TOT_ENR_F -- total female enrollment.

There are several other attributes that have the same pattern of combining racial and gender codenames to get column names, including:  

 - SCH_HBREPORTED_DIS -- students reported as harrased or bullied
 - SCH_DISCWODIS_EXPWOE -- students without disabilities who were expelled from school
 - SCH_RET_G12 -- students who started and completed grade 12.

##Instructions  
 - Create a new file called enrollment.py that will run from the command line.
 - In enrollment.py:
	- Read in the data file using pandas.
	- Create a column called total_enrollment that adds the TOT_ENR_M and TOT_ENR_F columns.
	- Compute the sums of all the columns that break down enrollment by race and gender.
	- Compute the sum of the total_enrollment column, and assign to the variable all_enrollment.
	- Divide the sums of the columns by all_enrollment to figure out what percentage of enrollment each race/gender group is.
		- Print out the results.
 - Run enrollment.py.
 - Compare the results to the overall population of the US broken down by race and gender, which you can find here and here.
	- To make the analysis simpler, you can assume that the gender ratio in the US is 1:1.
 - Add any interesting patterns you've found to findings.txt.

```bash  
touch enrollment.py
source /dataquest/system/env/python3/bin/activate
python3 enrollment.py
```

```python  
import pandas as pd
data = pd.read_csv("CRDC2013_14.csv",encoding="Latin-1")
#Create a column called total_enrollment that adds the TOT_ENR_M and TOT_ENR_F columns.
data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
print(data.head(2))
print("-----------")
print("-----------")
#Compute the sums of all the columns that break down enrollment by race and gender.
col = ["SCH_ENR_HI_M"
,"SCH_ENR_HI_F"
,"SCH_ENR_AM_M"
,"SCH_ENR_AM_F"
,"SCH_ENR_AS_M"
,"SCH_ENR_AS_F"
,"SCH_ENR_HP_M"
,"SCH_ENR_HP_F"
,"SCH_ENR_BL_M"
,"SCH_ENR_BL_F"
,"SCH_ENR_WH_M"
,"SCH_ENR_WH_F"
,"SCH_ENR_TR_M"
,"SCH_ENR_TR_F"]
sum_col = {}
for c in col:
    sum_col[c] = data[c].sum()

print(sum_col)
print("-----------")
print("-----------")
# Compute the sum of the total_enrollment column, and assign to the variable all_enrollment.
all_enrollment = data["total_enrollment"].sum()
print(all_enrollment)
print("-----------")
print("-----------")
# Divide the sums of the columns by all_enrollment to figure out what percentage of enrollment each race/gender group is.
# Print out the results.
per_col = {}
for col, value in sum_col.items():
    per_col[col] = (sum_col[col] / all_enrollment) * 100

print(per_col)
print("-----------")
print("-----------")
```

####Results: 

```bash  
{'SCH_ENR_TR_M': 1.5212020418561278, 'SCH_ENR_HI_M': 13.442604039491265, 'SCH_EN
R_AS_M': 2.5740461244147932, 'SCH_ENR_HP_M': 0.18053699662574624, 'SCH_ENR_WH_F'
: 24.138507829999135, 'SCH_ENR_TR_F': 1.5265854666756391, 'SCH_ENR_BL_F': 6.9121
252030800884, 'SCH_ENR_AS_F': 2.4696461359507031, 'SCH_ENR_AM_M': 0.725031964084
86592, 'SCH_ENR_AM_F': 0.68984743758591849, 'SCH_ENR_WH_M': 25.707583899714486, 
'SCH_ENR_HP_F': 0.18841986868288743, 'SCH_ENR_HI_F': 12.715264893340898, 'SCH_EN
R_BL_M': 7.2085980984974469} 
```





---
#5: Moving The Data Files To A Separate Folder
When you're working with data files, it's common to put them in a folder called data. This makes it easy to separate out your scripts, findings, and the source data. In cases where the source data is several hundred megabytes, it also makes it easier to just share your code and findings without the data.  

In order to do this, we'll need to create a folder, then move the data files. Finally, we'll need to rewrite our Python scripts to load the data files from the folder.  

##Instructions  
 - Create a folder called data in the current folder.
 - Move the data files to the data folder. This includes:
	- CRDC_documentation_csv.txt
	- CRDC_usage_agreement.txt
	- CRDC2013_14.csv
	- CRDC2013_14content.csv
 - Edit read.py, exploration.py, and enrollment.py to access the data files inside the folder.

```bash  
mkdir data
mv CRDC_documentation_csv.txt ~/scripts/data/CRDC_documentation_csv.txt
mv CRDC_usage_agreement.txt ~/scripts/data/CRDC_usage_agreement.txt
mv CRDC2013_14.csv ~/scripts/data/CRDC2013_14.csv
mv CRDC2013_14content.csv ~/scripts/data/CRDC2013_14content.csv
```

```python
data = pd.read_csv("~/scripts/data/CRDC2013_14.csv",encoding="Latin-1")
```

####Results: 

```bash  
(python3) /home/dq/scripts$ mkdir data                                          
(python3) /home/dq/scripts$ mv CRDC_documentation_csv.txt ~/scripts/data/CRDC_do
cumentation_csv.txt                                                             
(python3) /home/dq/scripts$ mv CRDC_usage_agreement.txt ~/scripts/data/CRDC_usag
e_agreement.txt                                                                 
(python3) /home/dq/scripts$ mv CRDC2013_14.csv ~/scripts/data/CRDC2013_14.csv   
(python3) /home/dq/scripts$ mv CRDC2013_14content.csv ~/scripts/data/CRDC2013_14
content.csv
```




---
#6: Next Steps
Now that you've read in the files and found some interesting columns, you can dig in and analyze the data more.  
There are quite a few interesting angles you could explore:  

 - Look into expulsions, which is when students are kicked out of school permanently. Columns such as SCH_DISCWODIS_EXPWOE_HI_M and TOT_DISCWODIS_EXPZT_F contain information on expulsions.
 - Explore gender and race differences in SAT scores. Columns such as SCH_SATACT_HI_M contain this information.
 - Figure out the racial and gender breakdown at different types of schools, such as magnet schools.
 - Look into how many students are in gifted and talented or advanced placement classes.
 - See how racial differences in enrollment change from preschool to high school.
 - Investigate school bullying. This information is contained in columns like SCH_HBDISCIPLINED_DIS_HI_M.
It's recommended that you download these files, and work on your own machine. Downloading the full dataset from here is also recommended. If you find anything interesting while exploring this data set, please let us know!  
