"""
02/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Data Cleaning : Data Cleaning Walkthrough Cleaning The Data
"""

"""
1: Getting Started With A Data Science Project
At many points in your career, you'll need to be able to build complete, end-to-end data science projects on your own.
Data science projects are usually one of two things:

An exploration and analysis of a set of data.
An example would be analyzing donors to political campaigns, making a plot, then sharing your analysis of the plot with other.
An operational system that works with data that is constantly updated, and generates predictions.
An example would be an algorithm that pulls in stock ticker data daily and makes predictions about which stocks will go up and down.
Being able to create projects will be useful in several different contexts:

Projects allow you to construct a portfolio, which is critical in being hired as a data analyst or scientist.
Projects help teach you new skills and reinforce existing concepts.
Most "real-world" data science or analysis work consists of developing internal projects.
Projects allow you to investigate interesting phenomena and satisfy your curiosity.
If you want to be employed as a data scientist or data analyst, or if you're merely curious about the world, building projects can be immensely rewarding.

Here's an example of a finished project.
https://github.com/dataquestio/loan-prediction

In this mission, we'll walk through the first part of a complete data science project.
In this project, we'll go from acquiring raw data all the way through to analyzing it.
The project will focus on exploration and analysis of a set of data.
We'll develop our data cleaning and storytelling skills, which will enable us to build complete projects on our own.

In this mission, we'll primarily focus on data exploration, and combining several messy datasets into one clean one that enables us to analyze it easily.
In the next few missions, we'll work through the rest of our project, and do meaningful analysis.

The first step in creating a project is to decide on your topic. You want the topic to be something you're interested in, and are motivated to explore.
It's very obvious when people are making projects just to make them, and when people are making projects because they're genuinely interested in exploring the data.

The two ways to find a good topic are:

Think about what sectors or angles you're really interested in, then find datasets in those sectors.
Explore many datasets, and find one that seems interesting enough to explore.
If you pick either course, here are some good sites to start with:

Data.gov -- contains government data.
https://www.data.gov/
/r/datasets -- a subreddit that has hundreds of interesting datasets.
https://reddit.com/r/datasets
Awesome datasets -- a list of datasets, hosted on Github.
https://github.com/caesar0301/awesome-public-datasets
rs.io -- a great blog post with hundreds of interesting datasets.
http://rs.io/100-interesting-data-sets-for-statistics/
In real-world data science, you often won't find a nice single dataset that you can browse.
You might have to aggregate disparate data sources, or do a good amount of data cleaning.

For the purposes of this project, we'll be using data about New York City public schools, which can be found here.
"""




"""
2: Finding All The Relevant Datasets
Once you've picked a topic, you'll want to pick an angle you want to investigate.
It's important to pick an angle that's ambitious enough to have enough depth to analyze, but isn't so complicated that it makes it hard to get started.
You want to finish the project, and you want your results to be interesting to others.

One of the most controversial issues in the US educational system is the efficacy of standardized tests, and whether they are unfair to certain groups.
Given our prior knowledge about this topic, investigating the correlations between SAT scores and demographic factors might be an interesting angle to take.
We could correlate SAT scores with factors like race, gender, income, and more.

The SAT, or Scholastic Aptitude Test, is a test that high schoolers take in the US before applying to college.
Colleges take the test scores into account when making admissions decisions, so it's fairly important to do well on.
The test is divided into 3 sections, each of which is scored out of 800 points.
The total score is out of 2400 (although this has changed back and forth a few times, the scores in this dataset are out of 2400).
High schools are often ranked by their average SAT scores, and high SAT scores are considered a sign of how good a school district is.

We have a dataset of SAT scores here, and a dataset that contains information on each high school here. Here are the first few rows of the SAT data:

see sat.png

Unfortunately, both datasets together aren't enough to fully give us all the demographic factors we want to correlate SAT scores to.
We'll need to supplement our data with other datasets in order to analyze the factors we want to.

There are several related datasets on the same website that cover demographic information and test scores.
Here are the links to all of the datasets we'll be using:

SAT scores by school -- SAT scores for each high school in New York City.
School attendance -- attendance information on every school in NYC.
Class size -- class size information for each school in NYC.
AP test results -- Advanced Placement exam results for each high school. High schools students in the US can choose to take AP exams.
There are several AP exams, one for each subject. Passing an AP exam can get you college credit in that subject.
Graduation outcomes -- percentage of students who graduated, and other outcome information.
Demographics -- demographic information for each school.
School survey -- surveys of parents, teachers, and students at each school.
All of these datasets are interrelated, and we'll need to combine them into a single dataset before we can do the correlations we want.
"""




"""
3: Finding Background Information
Before we move into coding, we'll need to do some background research.
This will help us avoid costly mistakes caused by not fully understanding the data.
An example of this would be thinking that a column represents something other than what it does.
Background research will also help us better understand how to combine and analyze the data.

In this case, we'll want to research:

New York City  https://en.wikipedia.org/wiki/New_York_City
The SAT https://en.wikipedia.org/wiki/SAT
Schools in New York City  https://en.wikipedia.org/wiki/List_of_high_schools_in_New_York_City
Our data  https://data.cityofnewyork.us/data?cat=education
From looking at these, we can learn a few things:

The SAT is only administered to high schoolers, so we'll want to focus on high schools.
New York City is divided into 5 boroughs, which are essentially distinct regions.
Schools in New York City are divided into several school districts, each of which can contains dozens of schools.
Not all the schools in all of the datasets are high schools, so we'll need to do some data cleaning.
Each school in New York City has a unique code called a DBN, or District Borough Number.
By aggregating data by district, we can use the district mapping data to plot district-by-district differences.
"""




"""
4: Reading In The Data
Once we've done our background research, we're ready to read in the data.
For your convenience, we've placed all the data into the schools folder.
Here are all the files in the schools folder:

ap_2010.csv -- contains data on AP test results.   https://data.cityofnewyork.us/Education/AP-College-Board-2010-School-Level-Results/itfs-ms3e
class_size.csv -- contains data on class size.  https://data.cityofnewyork.us/Education/2010-2011-Class-Size-School-level-detail/urz7-pzb3
demographics.csv -- contains data on demographics.  https://data.cityofnewyork.us/Education/School-Demographics-and-Accountability-Snapshot-20/ihfw-zy9j
graduation.csv -- contains data on graduation outcomes.  https://data.cityofnewyork.us/Education/Graduation-Outcomes-Classes-Of-2005-2010-School-Le/vh2h-md7a
hs_directory.csv -- a directory of high schools.   https://data.cityofnewyork.us/Education/DOE-High-School-Directory-2014-2015/n3p6-zve2
sat_results.csv -- data on sat scores.  https://data.cityofnewyork.us/Education/SAT-Results/f9bf-2cp4
survey_all.txt -- data on surveys from all schools.  https://data.cityofnewyork.us/Education/NYC-School-Survey-2011/mnz3-dyi8
survey_d75.txt -- data on surveys from New York City district 75. https://data.cityofnewyork.us/Education/NYC-School-Survey-2011/mnz3-dyi8
http://schools.nyc.gov/academics/specialEducation/D75/default.htm
survey_all.txt and survey_d75.txt are in more complicated formats than the rest of the files.
For now, we'll focus on reading in the csv files only, and then explore them.

We'll read each file into a Pandas Dataframe, and then store all of the Dataframes in a dictionary.
This will make it easy to reference the Dataframes later on, while storing them all into a single variable for convenience.

Instructions
Read each of the files in the list data_files into a Pandas Dataframe using the read_csv function.
Recall that each of the datasets are contained within the schools folder. E.g. the path to ap_2010.csv is schools/ap_2010.csv.
Add each of the Dataframes to the dictionary data, using the base of the filename as the key. For example, ap_2010.csv would turn into ap_2010.
At the end, data should have the following keys:
ap_2010
class_size
demographics
graduation
hs_directory
sat_results
At the end, each key in data should have the corresponding Dataframe as the value.
"""
import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]

data = {}
for files in data_files:
    df = pd.read_csv("schools/{0}".format(files))
    dfname = files.replace(".csv","")
    data[dfname] = df
""" Console Output or results

"""




"""
5: Exploring The SAT Data
The main dataset that we're interested in is the SAT dataset, which corresponds to the dictionary key sat_results.
This contains information about the SAT scores for each high school in New York City.
We eventually want to correlate items from this dataset with items from the other datasets.

Let's explore sat_results to see what we can discover.
Exploring the Dataframe will enable us to understand the structure of the data, which will make it easier to analyze.

Instructions
Display the first 5 rows of the SAT scores data.
Use the key sat_results to access the SAT scores Dataframe stored in the dictionary data.
Use the head method alolng with the print function to display the first 5 rows of the Dataframe.
"""
print(data["sat_results"].head())
""" Console Output or results
Output
      DBN                                    SCHOOL NAME  \
0  01M292  HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES
1  01M448            UNIVERSITY NEIGHBORHOOD HIGH SCHOOL
2  01M450                     EAST SIDE COMMUNITY SCHOOL
3  01M458                      FORSYTH SATELLITE ACADEMY
4  01M509                        MARTA VALLE HIGH SCHOOL

  Num of SAT Test Takers SAT Critical Reading Avg. Score SAT Math Avg. Score  \
0                     29                             355                 404
1                     91                             383                 423
2                     70                             377                 402
3                      7                             414                 401
4                     44                             390                 433

  SAT Writing Avg. Score
0                    363
1                    366
2                    370
3                    359
4                    384
"""




"""
6: Exploring The Other Data
When we printed out the first 5 rows of the SAT data, we got results like this:


DBN                                    SCHOOL NAME  \
0  01M292  HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES
1  01M448            UNIVERSITY NEIGHBORHOOD HIGH SCHOOL
2  01M450                     EAST SIDE COMMUNITY SCHOOL
3  01M458                      FORSYTH SATELLITE ACADEMY
4  01M509                        MARTA VALLE HIGH SCHOOL
​
  Num of SAT Test Takers SAT Critical Reading Avg. Score SAT Math Avg. Score  \
0                     29                             355                 404
1                     91                             383                 423
2                     70                             377                 402
3                      7                             414                 401
4                     44                             390                 433
​
  SAT Writing Avg. Score
0                    363
1                    366
2                    370
3                    359
4                    384
From looking at the data, we can make a few observations:

The DBN appears to be a unique ID for each school.
From looking at the first few rows of names, we only have data about high schools.
There's only a single row for each high school, so each DBN is unique in the SAT data.
We may eventually want to combine the three columns that contain SAT scores -- SAT Critical Reading Avg., Score SAT Math Avg. Score, and SAT Writing Avg.
Score into a single column to make it easier to analyze.
Given these observations, let's explore the other datasets to see if we can get any insight into how to combine the datasets.

Instructions
Loop through each key in data. For each key:
Display the first 5 rows of the Dataframe associated with the key.
"""
for key, value in data.items():
    print(data[key].head())
    print("---------------------")
    print("---------------------")
""" Console Output or results
Output
      DBN                                    SCHOOL NAME  \
0  01M292  HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES
1  01M448            UNIVERSITY NEIGHBORHOOD HIGH SCHOOL
2  01M450                     EAST SIDE COMMUNITY SCHOOL
3  01M458                      FORSYTH SATELLITE ACADEMY
4  01M509                        MARTA VALLE HIGH SCHOOL

  Num of SAT Test Takers SAT Critical Reading Avg. Score SAT Math Avg. Score  \
0                     29                             355                 404
1                     91                             383                 423
2                     70                             377                 402
3                      7                             414                 401
4                     44                             390                 433

  SAT Writing Avg. Score
0                    363
1                    366
2                    370
3                    359
4                    384
---------------------
---------------------
   CSD BOROUGH SCHOOL CODE                SCHOOL NAME GRADE  PROGRAM TYPE  \
0    1       M        M015  P.S. 015 Roberto Clemente     0K       GEN ED
1    1       M        M015  P.S. 015 Roberto Clemente     0K          CTT
2    1       M        M015  P.S. 015 Roberto Clemente     01       GEN ED
3    1       M        M015  P.S. 015 Roberto Clemente     01          CTT
4    1       M        M015  P.S. 015 Roberto Clemente     02       GEN ED

  CORE SUBJECT (MS CORE and 9-12 ONLY) CORE COURSE (MS CORE and 9-12 ONLY)  \
0                                    -                                   -
1                                    -                                   -
2                                    -                                   -
3                                    -                                   -
4                                    -                                   -

  SERVICE CATEGORY(K-9* ONLY)  NUMBER OF STUDENTS / SEATS FILLED  \
0                           -                               19.0
1                           -                               21.0
2                           -                               17.0
3                           -                               17.0
4                           -                               15.0

   NUMBER OF SECTIONS  AVERAGE CLASS SIZE  SIZE OF SMALLEST CLASS  \
0                 1.0                19.0                    19.0
1                 1.0                21.0                    21.0
2                 1.0                17.0                    17.0
3                 1.0                17.0                    17.0
4                 1.0                15.0                    15.0

   SIZE OF LARGEST CLASS DATA SOURCE  SCHOOLWIDE PUPIL-TEACHER RATIO
0                   19.0         ATS                             NaN
1                   21.0         ATS                             NaN
2                   17.0         ATS                             NaN
3                   17.0         ATS                             NaN
4                   15.0         ATS                             NaN
---------------------
---------------------
      DBN                       Name  schoolyear fl_percent  frl_percent  \
0  01M015  P.S. 015 ROBERTO CLEMENTE    20052006       89.4          NaN
1  01M015  P.S. 015 ROBERTO CLEMENTE    20062007       89.4          NaN
2  01M015  P.S. 015 ROBERTO CLEMENTE    20072008       89.4          NaN
3  01M015  P.S. 015 ROBERTO CLEMENTE    20082009       89.4          NaN
4  01M015  P.S. 015 ROBERTO CLEMENTE    20092010                    96.5

   total_enrollment prek   k grade1 grade2    ...     black_num black_per  \
0               281   15  36     40     33    ...            74      26.3
1               243   15  29     39     38    ...            68      28.0
2               261   18  43     39     36    ...            77      29.5
3               252   17  37     44     32    ...            75      29.8
4               208   16  40     28     32    ...            67      32.2

  hispanic_num hispanic_per white_num white_per male_num male_per female_num  \
0          189         67.3         5       1.8    158.0     56.2      123.0
1          153         63.0         4       1.6    140.0     57.6      103.0
2          157         60.2         7       2.7    143.0     54.8      118.0
3          149         59.1         7       2.8    149.0     59.1      103.0
4          118         56.7         6       2.9    124.0     59.6       84.0

  female_per
0       43.8
1       42.4
2       45.2
3       40.9
4       40.4

[5 rows x 38 columns]
---------------------
---------------------
      dbn                                        school_name       boro  \
0  17K548                Brooklyn School for Music & Theatre   Brooklyn
1  09X543                   High School for Violin and Dance      Bronx
2  09X327        Comprehensive Model School Project M.S. 327      Bronx
3  02M280     Manhattan Early College School for Advertising  Manhattan
4  28Q680  Queens Gateway to Health Sciences Secondary Sc...     Queens

  building_code    phone_number    fax_number grade_span_min  grade_span_max  \
0          K440    718-230-6250  718-230-6262              9              12
1          X400    718-842-0687  718-589-9849              9              12
2          X240    718-294-8111  718-294-8109              6              12
3          M520  718-935-3477             NaN              9              10
4          Q695    718-969-3155  718-969-3552              6              12

  expgrade_span_min  expgrade_span_max  \
0               NaN                NaN
1               NaN                NaN
2               NaN                NaN
3                 9               14.0
4               NaN                NaN

                         ...                          \
0                        ...
1                        ...
2                        ...
3                        ...
4                        ...

                                          priority02  \
0                    Then to New York City residents
1  Then to New York City residents who attend an ...
2  Then to Bronx students or residents who attend...
3  Then to New York City residents who attend an ...
4  Then to Districts 28 and 29 students or residents

                                          priority03  \
0                                                NaN
1                Then to Bronx students or residents
2  Then to New York City residents who attend an ...
3          Then to Manhattan students or residents
4               Then to Queens students or residents

                            priority04                       priority05  \
0                                  NaN                              NaN
1      Then to New York City residents                              NaN
2  Then to Bronx students or residents  Then to New York City residents
3      Then to New York City residents                              NaN
4      Then to New York City residents                              NaN

  priority06  priority07 priority08  priority09 priority10  \
0        NaN         NaN        NaN         NaN        NaN
1        NaN         NaN        NaN         NaN        NaN
2        NaN         NaN        NaN         NaN        NaN
3        NaN         NaN        NaN         NaN        NaN
4        NaN         NaN        NaN         NaN        NaN

                                          Location 1
0  883 Classon Avenue\nBrooklyn, NY 11225\n(40.67...
1  1110 Boston Road\nBronx, NY 10456\n(40.8276026...
2  1501 Jerome Avenue\nBronx, NY 10452\n(40.84241...
3  411 Pearl Street\nNew York, NY 10038\n(40.7106...
4  160-20 Goethals Avenue\nJamaica, NY 11432\n(40...

[5 rows x 58 columns]
---------------------
---------------------
      DBN                             SchoolName AP Test Takers   \
0  01M448           UNIVERSITY NEIGHBORHOOD H.S.              39
1  01M450                 EAST SIDE COMMUNITY HS              19
2  01M515                    LOWER EASTSIDE PREP              24
3  01M539         NEW EXPLORATIONS SCI,TECH,MATH             255
4  02M296  High School of Hospitality Management               s

  Total Exams Taken Number of Exams with scores 3 4 or 5
0                49                                   10
1                21                                    s
2                26                                   24
3               377                                  191
4                 s                                    s
---------------------
---------------------
    Demographic     DBN                            School Name    Cohort  \
0  Total Cohort  01M292  HENRY STREET SCHOOL FOR INTERNATIONAL      2003
1  Total Cohort  01M292  HENRY STREET SCHOOL FOR INTERNATIONAL      2004
2  Total Cohort  01M292  HENRY STREET SCHOOL FOR INTERNATIONAL      2005
3  Total Cohort  01M292  HENRY STREET SCHOOL FOR INTERNATIONAL      2006
4  Total Cohort  01M292  HENRY STREET SCHOOL FOR INTERNATIONAL  2006 Aug

   Total Cohort Total Grads - n Total Grads - % of cohort Total Regents - n  \
0             5               s                         s                 s
1            55              37                     67.3%                17
2            64              43                     67.2%                27
3            78              43                     55.1%                36
4            78              44                     56.4%                37

  Total Regents - % of cohort Total Regents - % of grads  \
0                           s                          s
1                       30.9%                      45.9%
2                       42.2%                      62.8%
3                       46.2%                      83.7%
4                       47.4%                      84.1%

             ...            Regents w/o Advanced - n  \
0            ...                                   s
1            ...                                  17
2            ...                                  27
3            ...                                  36
4            ...                                  37

  Regents w/o Advanced - % of cohort Regents w/o Advanced - % of grads  \
0                                  s                                 s
1                              30.9%                             45.9%
2                              42.2%                             62.8%
3                              46.2%                             83.7%
4                              47.4%                             84.1%

  Local - n Local - % of cohort   Local - % of grads Still Enrolled - n  \
0         s                   s                    s                  s
1        20               36.4%                54.1%                 15
2        16                 25%  37.200000000000003%                  9
3         7                  9%                16.3%                 16
4         7                  9%                15.9%                 15

  Still Enrolled - % of cohort Dropped Out - n Dropped Out - % of cohort
0                            s               s                         s
1                        27.3%               3                      5.5%
2                        14.1%               9                     14.1%
3                        20.5%              11                     14.1%
4                        19.2%              11                     14.1%

[5 rows x 23 columns]
---------------------
---------------------
"""



"""
7: Reading In The Survey Data
In the last step, we saw a group of Dataframes that looked like this:


CSD BOROUGH SCHOOL CODE                SCHOOL NAME GRADE  PROGRAM TYPE  \
0    1       M        M015  P.S. 015 Roberto Clemente     0K       GEN ED
1    1       M        M015  P.S. 015 Roberto Clemente     0K          CTT
2    1       M        M015  P.S. 015 Roberto Clemente     01       GEN ED
3    1       M        M015  P.S. 015 Roberto Clemente     01          CTT
4    1       M        M015  P.S. 015 Roberto Clemente     02       GEN ED
From the first few rows of each dataset, we can make some observations:

Each dataset appears to have either a DBN column, or the information to create a DBN column, so this is how we'll combine our datasets into one.
We can match up rows from different datasets that have the same DBN and combine their columns.
Some fields look interesting for mapping, particularly Location 1, which contains coordinates inside a larger string.
Some of the datasets appear to contain multiple rows for each school (repeated DBN values), which means we’ll have to do some preprocessing to ensure that DBN is unique within each dataset.
If we don't do this, it will cause issues when we combine the datasets, because we might be merging two rows in one dataset with one row in another dataset.
Before we proceed with unifying the datasets, it will be useful to ensure we have all the data we want to unify.
We mentioned the survey data, survey_all.txt and survey_d75.txt, earlier, but we didn't read them in, because they were in a slightly more complex format.

Each survey text file looks like this:


dbn bn  schoolname  d75 studentssurveyed    highschool  schooltype  rr_s
"01M015"    "M015"  "P.S. 015 Roberto Clemente" 0   "No"    0   "Elementary School"     88
The files are tab delimited, and are encoded with Windows-1252 encoding. An encoding defines how the contents of a file are stored in binary.
The most common encodings are UTF-8 and ASCII.
Windows-1252 is rarely used, and can cause errors when files are read in if its not specified. If you want to read more about encodings, here's a good primer.
http://kunststube.net/encoding/

We'll need to specify the encoding and delimiter to the Pandas read_csv function in order to ensure the surveys are read in properly.

After we read in the survey data, we'll want to combine it into a single Dataframe. We can do this with the Pandas concat function.


z = pd.concat([x,y], axis=0)
The above code will combine the Dataframes x and y by essentially appending y to the end of x.
The combined Dataframe z will have as many rows as the rows in x plus the rows in y.

Instructions
Read in survey_all.txt.
Use the read_csv function to read survey_all.txt into the variable all_survey. Recall that this file is located in the schools folder.
Specify the keyword argument delimiter="\t".
Specify the keyword argument encoding="windows-1252".
Read in survey_d75.txt.
Use the read_csv function to read schools/survey_d75.txt into the variable d75_survey. Recall that this file is located in the schools folder.
Specify the keyword argument delimiter="\t".
Specify the keyword argument encoding="windows-1252".
Combine d75_survey and all_survey into a single Dataframe.
Use the Pandas concat function, along with the keyword argument axis=0 to combine d75_survey and all_survey into the Dataframe survey.
Pass in all_survey first then d75_survey when calling the concat function.
Display the first 5 rows of survey using the head function.
"""
all_survey = pd.read_csv("schools/survey_all.txt", delimiter="\t", encoding="windows-1252")
d75_survey = pd.read_csv("schools/survey_d75.txt", delimiter="\t", encoding="windows-1252")
survey = pd.concat([all_survey, d75_survey], axis=0)
print(survey.head())
""" Console Output or results
Output
     N_p    N_s   N_t  aca_p_11  aca_s_11  aca_t_11  aca_tot_11    bn  \
0   90.0    NaN  22.0       7.8       NaN       7.9         7.9  M015
1  161.0    NaN  34.0       7.8       NaN       9.1         8.4  M019
2  367.0    NaN  42.0       8.6       NaN       7.5         8.0  M020
3  151.0  145.0  29.0       8.5       7.4       7.8         7.9  M034
4   90.0    NaN  23.0       7.9       NaN       8.1         8.0  M063

   com_p_11  com_s_11   ...    t_q8c_1  t_q8c_2  t_q8c_3 t_q8c_4  t_q9  \
0       7.6       NaN   ...       29.0     67.0      5.0     0.0   NaN
1       7.6       NaN   ...       74.0     21.0      6.0     0.0   NaN
2       8.3       NaN   ...       33.0     35.0     20.0    13.0   NaN
3       8.2       5.9   ...       21.0     45.0     28.0     7.0   NaN
4       7.9       NaN   ...       59.0     36.0      5.0     0.0   NaN

   t_q9_1  t_q9_2  t_q9_3  t_q9_4  t_q9_5
0     5.0    14.0    52.0    24.0     5.0
1     3.0     6.0     3.0    78.0     9.0
2     3.0     5.0    16.0    70.0     5.0
3     0.0    18.0    32.0    39.0    11.0
4    10.0     5.0    10.0    60.0    15.0

[5 rows x 2773 columns]
"""




"""
8: Cleaning Up The Surveys
In the last step, you should have seen output that looked like this:


N_p  N_s  N_t  aca_p_11  aca_s_11  aca_t_11  aca_tot_11    bn  com_p_11  \
0   90  NaN   22       7.8       NaN       7.9         7.9  M015       7.6
1  161  NaN   34       7.8       NaN       9.1         8.4  M019       7.6
There are two immediate facts that we can see in the data:

There are over 2000 columns in the data, almost all of which we won't need.
We'll need to filter this to remove columns to make it easier to work with.
The fewer columns, the easier it is to print out the Dataframe, and to find correlations across the whole Dataframe.
The survey data has a dbn column that we'll want to convert to uppercase (DBN) for consistency with the other datasets.
We'll need to filter the columns to remove the ones we don't need.
Luckily, we have a data dictionary that we can find at the original data download location.
The dictionary tells us what each column represents.
Based on our knowledge of the problem and the analysis we're trying to do, we can use the data dictionary to determine which columns to use.

Here's a preview of the data dictionary:

see xj5ud4r.png

Based on the dictionary, it looks like these are the relevant columns:

["dbn", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11",
"aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11",]
These columns will give us aggregate survey data about how parents, teachers, and students feel about school safety, academic performance, and more.
It will also give us the DBN, which allows us to uniquely identify the school.

Before we filter out columns, we'll want to copy the data from the dbn column into a new column called DBN. We can copy columns like this:


survey["new_column"] = survey["old_column"]
Instructions
Copy the data from the dbn column of survey into a new column in survey called DBN.
Filter survey so it only contains the columns listed above. You can do this with the loc method.
Remember that we renamed dbn to DBN -- make sure to change the list of columns to keep accordingly.
Assign the Dataframe survey to the key survey in the dictionary data.
At the end, the value in data["survey"] should be a Dataframe with 23 columns and 1702 rows.
"""
survey["DBN"] = survey["dbn"]
survey = survey.loc[:,["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11",]]
data["survey"] = survey
print(data["survey"].head())
print("--------------------")
print("--------------------")
print(data["survey"].info())
""" Console Output or results
Output
      DBN  rr_s  rr_t  rr_p    N_s   N_t    N_p  saf_p_11  com_p_11  eng_p_11  \
0  01M015   NaN    88    60    NaN  22.0   90.0       8.5       7.6       7.5
1  01M019   NaN   100    60    NaN  34.0  161.0       8.4       7.6       7.6
2  01M020   NaN    88    73    NaN  42.0  367.0       8.9       8.3       8.3
3  01M034  89.0    73    50  145.0  29.0  151.0       8.8       8.2       8.0
4  01M063   NaN   100    60    NaN  23.0   90.0       8.7       7.9       8.1

      ...      eng_t_11  aca_t_11  saf_s_11  com_s_11  eng_s_11  aca_s_11  \
0     ...           7.6       7.9       NaN       NaN       NaN       NaN
1     ...           8.9       9.1       NaN       NaN       NaN       NaN
2     ...           6.8       7.5       NaN       NaN       NaN       NaN
3     ...           6.8       7.8       6.2       5.9       6.5       7.4
4     ...           7.8       8.1       NaN       NaN       NaN       NaN

   saf_tot_11  com_tot_11  eng_tot_11  aca_tot_11
0         8.0         7.7         7.5         7.9
1         8.5         8.1         8.2         8.4
2         8.2         7.3         7.5         8.0
3         7.3         6.7         7.1         7.9
4         8.5         7.6         7.9         8.0

[5 rows x 23 columns]
--------------------
--------------------
<class 'pandas.core.frame.DataFrame'>
Int64Index: 1702 entries, 0 to 55
Data columns (total 23 columns):
DBN           1702 non-null object
rr_s          1041 non-null float64
rr_t          1702 non-null int64
rr_p          1702 non-null int64
N_s           1036 non-null float64
N_t           1700 non-null float64
N_p           1696 non-null float64
saf_p_11      1696 non-null float64
com_p_11      1696 non-null float64
eng_p_11      1696 non-null float64
aca_p_11      1696 non-null float64
saf_t_11      1700 non-null float64
com_t_11      1700 non-null float64
eng_t_11      1700 non-null float64
aca_t_11      1700 non-null float64
saf_s_11      1036 non-null float64
com_s_11      1036 non-null float64
eng_s_11      1036 non-null float64
aca_s_11      1036 non-null float64
saf_tot_11    1702 non-null float64
com_tot_11    1702 non-null float64
eng_tot_11    1702 non-null float64
aca_tot_11    1702 non-null float64
dtypes: float64(20), int64(2), object(1)
memory usage: 319.1+ KB
None
"""




"""
9: Inserting DBN Fields
When we explored all the datasets, we noticed that not every dataset had a DBN column.
Specifically, class_size and hs_directory do not have the column.
In the case of hs_directory, it has a dbn column, so we can just rename it.

However, class_size doesn't appear to have the column at all. Here are the first few rows of the dataset:


CSD BOROUGH SCHOOL CODE                SCHOOL NAME GRADE  PROGRAM TYPE  \
0    1       M        M015  P.S. 015 Roberto Clemente     0K       GEN ED
1    1       M        M015  P.S. 015 Roberto Clemente     0K          CTT
2    1       M        M015  P.S. 015 Roberto Clemente     01       GEN ED
3    1       M        M015  P.S. 015 Roberto Clemente     01          CTT
4    1       M        M015  P.S. 015 Roberto Clemente     02       GEN ED
And here are the first few rows of the sat_results data, which does have a DBN column:


DBN                                    SCHOOL NAME  \
0  01M292  HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES
1  01M448            UNIVERSITY NEIGHBORHOOD HIGH SCHOOL
2  01M450                     EAST SIDE COMMUNITY SCHOOL
3  01M458                      FORSYTH SATELLITE ACADEMY
4  01M509                        MARTA VALLE HIGH SCHOOL
From looking at these rows, it appears that the DBN is just a combination of the CSD and SCHOOL CODE columns in class_size.
The main difference is that the DBN is padded so the CSD is always two digits -- we'll need to add a leading 0 to the CSD if the CSD is less than two digits long for consistency.
Here's a diagram illustrating what we need to do:

see img1.png

As you can see, whenever the CSD is less than two digits long, we need to add a leading 0.
We can accomplish this using the Pandas apply method, along with a custom function that:

Takes in a number.
Converts the number to a string using the str function.
Check the length of the string using the len function.
If the string is two digits long, return the string.
If the string is one digit long, add a 0 to the front of the string, then return it.
You can use the string method zfill to do this.
Once we have the padded CSD, we can use the + operator to combine the values in the CSD and SCHOOL CODE columns.

Here's an example:

dataframe["new_column"] = dataframe["column_one"] + dataframe["column_two"]
And here's a diagram of how this works:

see im2.png

Instructions
Copy the dbn column in hs_directory into a new column called DBN.
Create a new column called padded_csd in the class_size dataset.
Use the apply method along with a custom function to generate this column.
Make sure to apply the function along the data["class_size"]["CSD"] column.
Use the + operator along with the padded_csd and SCHOOL CODE columns of class_size, then assign the result to the DBN column of class_size.
Display the first few rows of class_size to double check the DBN column.
"""
data["hs_directory"]["DBN"] = data["hs_directory"]["dbn"]

def pad_csd(num):
    string_representation = str(num)
    if len(string_representation) > 1:
        return string_representation
    else:
        return string_representation.zfill(2)

data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(pad_csd)
data["class_size"]["DBN"] = data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"]
print(data["class_size"].head())
""" Console Output or results
Output
   CSD BOROUGH SCHOOL CODE                SCHOOL NAME GRADE  PROGRAM TYPE  \
0    1       M        M015  P.S. 015 Roberto Clemente     0K       GEN ED
1    1       M        M015  P.S. 015 Roberto Clemente     0K          CTT
2    1       M        M015  P.S. 015 Roberto Clemente     01       GEN ED
3    1       M        M015  P.S. 015 Roberto Clemente     01          CTT
4    1       M        M015  P.S. 015 Roberto Clemente     02       GEN ED

  CORE SUBJECT (MS CORE and 9-12 ONLY) CORE COURSE (MS CORE and 9-12 ONLY)  \
0                                    -                                   -
1                                    -                                   -
2                                    -                                   -
3                                    -                                   -
4                                    -                                   -

  SERVICE CATEGORY(K-9* ONLY)  NUMBER OF STUDENTS / SEATS FILLED  \
0                           -                               19.0
1                           -                               21.0
2                           -                               17.0
3                           -                               17.0
4                           -                               15.0

   NUMBER OF SECTIONS  AVERAGE CLASS SIZE  SIZE OF SMALLEST CLASS  \
0                 1.0                19.0                    19.0
1                 1.0                21.0                    21.0
2                 1.0                17.0                    17.0
3                 1.0                17.0                    17.0
4                 1.0                15.0                    15.0

   SIZE OF LARGEST CLASS DATA SOURCE  SCHOOLWIDE PUPIL-TEACHER RATIO  \
0                   19.0         ATS                             NaN
1                   21.0         ATS                             NaN
2                   17.0         ATS                             NaN
3                   17.0         ATS                             NaN
4                   15.0         ATS                             NaN

  padded_csd     DBN
0         01  01M015
1         01  01M015
2         01  01M015
3         01  01M015
4         01  01M015
"""




"""
10: Combining The SAT Scores
We're now almost ready to combine our datasets into one.
Before we do, let's take some time to calculate variables that will be useful in our analysis.
We've already discussed one such variable -- a column that combines all of the SAT scores into one number.
This will make it much easier to correlate with demographic factors, because it's a single number, not three.

In order to generate this column, we'll first need to convert the SAT Math Avg.
Score, SAT Critical Reading Avg. Score, and SAT Writing Avg.
Score in the sat_results dataset from the object (string) data type to a numeric datatype.
We can use the to_numeric function to do this conversion.
Without doing this conversion, we won't be able to add up the columns.

It's important to pass the keyword argument errors="coerce" when we call to_numeric, so that any invalid strings that can't be converted to numbers are instead treated as missing values.

After the conversion, we can just use the + operator to add all three columns together.

Instructions
Convert the SAT Math Avg. Score, SAT Critical Reading Avg. Score, and SAT Writing Avg.
Score in the sat_results dataset from the object (string) data type to a numeric datatype.
Use the to_numeric function on each of the columns, and assign the result back to the same column.
Pass in the keyword argument errors="coerce".
Create a column called sat_score in sat_results that is the combined SAT score for each student.
Add up SAT Math Avg. Score, SAT Critical Reading Avg.
Score, and SAT Writing Avg. Score, and assign to the sat_score column of sat_results.
Display the first few rows of the sat_score column of sat_results to verify that everything went okay.
"""
col_list = ["SAT Math Avg. Score","SAT Critical Reading Avg. Score","SAT Writing Avg. Score"]
for col in col_list:
    data["sat_results"][col] = pd.to_numeric(data["sat_results"][col], errors='coerce')

data["sat_results"]["sat_score"] = data["sat_results"]["SAT Math Avg. Score"] + data["sat_results"]["SAT Critical Reading Avg. Score"] + data["sat_results"]["SAT Writing Avg. Score"]

print(data["sat_results"]["sat_score"][0:5])
""" Console Output or results
Output
0    1122.0
1    1172.0
2    1149.0
3    1174.0
4    1207.0
Name: sat_score, dtype: float64
"""




"""
11: Parsing Coordinates For Each School
Next, we'll want to parse the coordinates for each school.
This will enable us to map out the schools, and figure out any geographic patterns in the data.
Currently, the coordinates are in a text field called Location 1 in the hs_directory dataset.

We can look at the first few rows:


0    883 Classon Avenue\nBrooklyn, NY 11225\n(40.67...
1    1110 Boston Road\nBronx, NY 10456\n(40.8276026...
2    1501 Jerome Avenue\nBronx, NY 10452\n(40.84241...
3    411 Pearl Street\nNew York, NY 10038\n(40.7106...
4    160-20 Goethals Avenue\nJamaica, NY 11432\n(40...
As you can see, this field contains a lot of information that we don't need.
We need to extract the coordinates, which are in parentheses at the end of the field.
Here's an example:

1110 Boston Road\nBronx, NY 10456\n(40.8276026690005, -73.90447525699966)
We want to extract the latitude, 40.8276026690005, and the longitude, -73.90447525699966.
Together, the latitude and longitude make up a pair of coordinates, and allow us to uniquely locate any place on Earth.

We can do this using a regular expression. The following regular expression will pull out everything inside the parentheses:

import re
re.findall("\(.+, .+\)", "1110 Boston Road\nBronx, NY 10456\n(40.8276026690005, -73.90447525699966)")
The regular expression will pull out (40.8276026690005, -73.90447525699966).
We'll need to do further processing on this using the split and replace methods on strings to extract each coordinate.

Instructions
Write a function that:
Takes in a string.
Uses the regular expression above to extract the coordinates.
Uses string manipulation functions to pull out the latitude.
Returns the latitude.
Use the apply method to apply the function across the Location 1 column of hs_directory. Assign the result to the lat column of hs_directory.
Display the first few rows of hs_directory to verify the results.
"""
import re

def latitude(str):
    coord = re.findall("\(.+, .+\)", str)
    lat = coord[0].replace("(","").replace(")","").split(",")[0]
    return lat


data["hs_directory"]["lat"] = data["hs_directory"]["Location 1"].apply(latitude)
print(data["hs_directory"]["lat"][0:5])
""" Console Output or results
Output
0     40.67029890700047
1      40.8276026690005
2    40.842414068000494
3     40.71067947100045
4    40.718810094000446
Name: lat, dtype: object
"""



"""
12: Extracting The Longitude
In the last screen, we parsed the latitude from the Location 1 column.
Now we'll just need to do the same for the longitude.

Once we have the latitude and the longitude, we'll need to convert them to numeric values.
We can use the to_numeric function to convert them to numbers from strings.

Instructions
Write a function that:
Takes in a string.
Uses the regular expression above to extract the coordinates.
Uses string manipulation functions to pull out the longitude.
Returns the longitude.
Use the apply method to apply the function across the Location 1 column of hs_directory.
ssign the result to the lon column of hs_directory.
Use the to_numeric function to convert the lat and lon columns of hs_directory to numeric.
Specify the errors="coerce" keyword argument to handle missing values properly.
Display the first few rows of hs_directory to verify the results.
"""
import re

def longitude(str):
    coord = re.findall("\(.+, .+\)", str)
    long = coord[0].replace("(","").replace(")","").split(",")[1]
    return long


data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(longitude)
print(data["hs_directory"]["lon"][0:5])
print("----------------------")

data["hs_directory"]["lat"] = pd.to_numeric(data["hs_directory"]["lat"], errors='coerce')
data["hs_directory"]["lon"] = pd.to_numeric(data["hs_directory"]["lon"], errors='coerce')

print(data["hs_directory"].head())
print("----------------------")
""" Console Output or results
Output
0     -73.96164787599963
1     -73.90447525699966
2     -73.91616158599965
3     -74.00080702099967
4     -73.80650045499965
Name: lon, dtype: object
----------------------
      dbn                                        school_name       boro  \
0  17K548                Brooklyn School for Music & Theatre   Brooklyn
1  09X543                   High School for Violin and Dance      Bronx
2  09X327        Comprehensive Model School Project M.S. 327      Bronx
3  02M280     Manhattan Early College School for Advertising  Manhattan
4  28Q680  Queens Gateway to Health Sciences Secondary Sc...     Queens

  building_code    phone_number    fax_number grade_span_min  grade_span_max  \
0          K440    718-230-6250  718-230-6262              9              12
1          X400    718-842-0687  718-589-9849              9              12
2          X240    718-294-8111  718-294-8109              6              12
3          M520  718-935-3477             NaN              9              10
4          Q695    718-969-3155  718-969-3552              6              12

  expgrade_span_min  expgrade_span_max    ...      \
0               NaN                NaN    ...
1               NaN                NaN    ...
2               NaN                NaN    ...
3                 9               14.0    ...
4               NaN                NaN    ...

                        priority05 priority06 priority07 priority08  \
0                              NaN        NaN        NaN        NaN
1                              NaN        NaN        NaN        NaN
2  Then to New York City residents        NaN        NaN        NaN
3                              NaN        NaN        NaN        NaN
4                              NaN        NaN        NaN        NaN

  priority09  priority10                                         Location 1  \
0        NaN         NaN  883 Classon Avenue\nBrooklyn, NY 11225\n(40.67...
1        NaN         NaN  1110 Boston Road\nBronx, NY 10456\n(40.8276026...
2        NaN         NaN  1501 Jerome Avenue\nBronx, NY 10452\n(40.84241...
3        NaN         NaN  411 Pearl Street\nNew York, NY 10038\n(40.7106...
4        NaN         NaN  160-20 Goethals Avenue\nJamaica, NY 11432\n(40...

      DBN        lat        lon
0  17K548  40.670299 -73.961648
1  09X543  40.827603 -73.904475
2  09X327  40.842414 -73.916162
3  02M280  40.710679 -74.000807
4  28Q680  40.718810 -73.806500

[5 rows x 61 columns]
----------------------
"""




"""
13: Next Steps
We're almost ready to combine our datasets! We've come a long way in this mission -- we've gone from picking a topic for a project to acquiring the data to having clean data that we're almost ready to combine.

Along the way, we've learned:

How to handle files with different formats and columns.
How to get ready to unify multiple files.
Using text processing to extract coordinates from a string.
How to convert columns from strings to numbers.
In real-world data science projects, you'll constantly be learning as you work on them.
Each project is unique, and there will always be quirks that you don't quite know how to handle.
The key is to be willing to try different approaches, and to have a general framework in your head for how to move from Step A to Step B.

In the next mission, we'll finish cleaning the datasets, then combine them so we can analyze them.
"""
