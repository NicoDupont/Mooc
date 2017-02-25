"""
02/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Data Cleaning : Combining The Data
"""

"""
1: Condensing The Data
In the last mission, we started investigating the relationship between SAT scores and demographic factors.
In order to do this, we acquired several datasets about New York City public schools.
We manipulated these datasets, and found that we could combine them all using the DBN column.
Currently, all the datasets are stored as keys in the data dictionary. Each individual dataset is a Pandas Dataframe.

In this mission, we'll clean the data some more, then combine the data to create a single clean dataset.
We'll then compute correlations and do some analysis.

The first step that we'll need to take before we can combine the data is to condense some of the datasets.
In the last mission, we noticed that while sat_results was unique on the DBN column, and only contained a single row for each unique DBN value, some of the other datasets, such as class_size had duplicated DBN values.

The first step we'll need to take is to condense these datasets so that each value in the DBN column is unique.
If not, we'll have issues when it comes time to combine the datasets.
While the main dataset that we want to analyze, sat_results, has unique DBN values for every high school in NYC, other datasets are not as clean.
One row in the sat_results dataset may match to multiple columns in the class_size dataset, for example.
This will create problems, as we don't know which entry in the class_size dataset is "correct", and should be combined with the value from sat_results.
Here's a small example diagram:

see im3.png

In the above diagram, we can't just combine the rows, because class_size has multiple rows that match each row in sat_results.

In order to solve this issue, we'll condense the class_size, graduation, and demographics datasets so that DBN is unique.

"""


"""
2: Condensing Class Size
The first dataset that we'll condense is class_size. The first few rows of class_size look like this:

CSD	BOROUGH	SCHOOL CODE	SCHOOL NAME	GRADE	PROGRAM TYPE	CORE SUBJECT (MS CORE and 9-12 ONLY)	CORE COURSE (MS CORE and 9-12 ONLY)	SERVICE CATEGORY(K-9* ONLY)	NUMBER OF STUDENTS / SEATS FILLED	NUMBER OF SECTIONS	AVERAGE CLASS SIZE	SIZE OF SMALLEST CLASS	SIZE OF LARGEST CLASS	DATA SOURCE	SCHOOLWIDE PUPIL-TEACHER RATIO	padded_csd	DBN
0	1	M	M015	P.S. 015 Roberto Clemente	0K	GEN ED	-	-	-	19.0	1.0	19.0	19.0	19.0	ATS	NaN	01	01M015
1	1	M	M015	P.S. 015 Roberto Clemente	0K	CTT	-	-	-	21.0	1.0	21.0	21.0	21.0	ATS	NaN	01	01M015
2	1	M	M015	P.S. 015 Roberto Clemente	01	GEN ED	-	-	-	17.0	1.0	17.0	17.0	17.0	ATS	NaN	01	01M015
3	1	M	M015	P.S. 015 Roberto Clemente	01	CTT	-	-	-	17.0	1.0	17.0	17.0	17.0	ATS	NaN	01	01M015
4	1	M	M015	P.S. 015 Roberto Clemente	02	GEN ED	-	-	-	15.0	1.0	15.0	15.0	15.0	ATS	NaN	01	01M015
As you can see, the first few rows all pertain to the same school, which is why the DBN is repeated. It looks like each school has multiple values for GRADE, PROGRAM TYPE, CORE SUBJECT (MS CORE and 9-12 ONLY), and CORE COURSE (MS CORE and 9-12 ONLY).

If we look at the unique values for GRADE, we get the following:


array(['0K', '01', '02', '03', '04', '05', '0K-09', nan, '06', '07', '08',
       'MS Core', '09-12', '09'], dtype=object)
Since we're dealing with high schools, we only care about grades 9 through 12.
Thus, we can only pick rows where the GRADE column is 09-12.

If we look at the unique values for PROGRAM TYPE, we get the following:

array(['GEN ED', 'CTT', 'SPEC ED', nan, 'G&T'], dtype=object)
Each school can have multiple program types.
Since GEN ED is by far the biggest category, let's only select rows where PROGRAM TYPE is GEN ED.

Instructions
Create a new variable called class_size, and assign the value of data["class_size"] to it.
Filter class_size so the GRADE column only contains the value 09-12.
Note that the name of the GRADE column actually has a space at the end, and you'll get an error if you're missing it.
Filter class_size so that the PROGRAM TYPE column only contains the value GEN ED.
Display the first 5 rows of class_size to verify.
"""
class_size = data["class_size"]
class_size = class_size[class_size["GRADE "] == "09-12"]
class_size = class_size[class_size["PROGRAM TYPE"] == "GEN ED"]
print(class_size.head())
""" Console Outputs or Results
     CSD BOROUGH SCHOOL CODE                                    SCHOOL NAME  \
225    1       M        M292  Henry Street School for International Studies
226    1       M        M292  Henry Street School for International Studies
227    1       M        M292  Henry Street School for International Studies
228    1       M        M292  Henry Street School for International Studies
229    1       M        M292  Henry Street School for International Studies

    GRADE  PROGRAM TYPE CORE SUBJECT (MS CORE and 9-12 ONLY)  \
225  09-12       GEN ED                              ENGLISH
226  09-12       GEN ED                              ENGLISH
227  09-12       GEN ED                              ENGLISH
228  09-12       GEN ED                              ENGLISH
229  09-12       GEN ED                                 MATH

    CORE COURSE (MS CORE and 9-12 ONLY) SERVICE CATEGORY(K-9* ONLY)  \
225                           English 9                           -
226                          English 10                           -
227                          English 11                           -
228                          English 12                           -
229                  Integrated Algebra                           -

     NUMBER OF STUDENTS / SEATS FILLED  NUMBER OF SECTIONS  \
225                               63.0                 3.0
226                               79.0                 3.0
227                               38.0                 2.0
228                               69.0                 3.0
229                               53.0                 3.0

     AVERAGE CLASS SIZE  SIZE OF SMALLEST CLASS  SIZE OF LARGEST CLASS  \
225                21.0                    19.0                   25.0
226                26.3                    24.0                   31.0
227                19.0                    16.0                   22.0
228                23.0                    13.0                   30.0
229                17.7                    16.0                   21.0

    DATA SOURCE  SCHOOLWIDE PUPIL-TEACHER RATIO padded_csd     DBN
225       STARS                             NaN         01  01M292
226       STARS                             NaN         01  01M292
227       STARS                             NaN         01  01M292
228       STARS                             NaN         01  01M292
229       STARS                             NaN         01  01M292
"""




"""
3: Computing Average Class Sizes
As you saw when you displayed class_size in the last screen, DBN is still not completely unique.
This is due to the CORE COURSE (MS CORE and 9-12 ONLY) and CORE SUBJECT (MS CORE and 9-12 ONLY) columns.

Both CORE COURSE (MS CORE and 9-12 ONLY) and CORE SUBJECT (MS CORE and 9-12 ONLY) seem to pertain to different kinds of classes.
For example, here are the unique values for CORE SUBJECT (MS CORE and 9-12 ONLY):


array(['ENGLISH', 'MATH', 'SCIENCE', 'SOCIAL STUDIES'], dtype=object)
We don't want to only select a certain type of class in which to base our class size data on.
We want our class size data to be for every single class a school offers.
What we can do is take the average across all the classes a school offers.
This will give us unique DBN values, but also incorporate as much data as possible into the average.

Luckily, we can use the groupby method to help us with this.
The groupby method will split up a Dataframe into unique groups based on a column.
We can then use the agg method to find the mean of each column.

Let's say we had this dataset:

see im4.png

We would split it into 4 separate groups, one with the DBN 01M292, one with the DBN 01M332, one with the DBN 01M378, and one with the DBN 01M448 using the groupby method:

see im5.png
see im6.png

Then, we can compute the averages for the AVERAGE CLASS SIZE column in each of the 4 groups using the agg method:

see im7.png

After grouping a Dataframe and aggregating based on it, the index will become the column the grouping was done on (in this case DBN), and it will no longer be a column.
In order to move DBN back to a column, we'll need to use reset_index.
This will reset the index to a list of integers, and make DBN a column again.

Instructions
Find the average values for each column for each DBN in class_size
Use the groupby method to group class_size by DBN.
Use the agg method, along with the numpy.mean function as an argument, to calculate the average of each group.
Assign the result back to class_size.
Reset the index, making DBN a column again.
Use the reset_index method, along with the keyword argument inplace=True.
Assign class_size back to the class_size key of the data dictionary.
Display the first few rows of data["class_size"] to verify everything went okay.
"""
import numpy as np
print(class_size.head())
print("----------------------")
print("----------------------")
print("----------------------")
class_size = class_size.groupby("DBN").agg(np.mean)
print(class_size.head())
print("----------------------")
print("----------------------")
print("----------------------")
class_size.reset_index(inplace=True)
data["class_size"] = class_size
print(data["class_size"].head())
""" Console Outputs or Results
Output
     CSD BOROUGH SCHOOL CODE                                    SCHOOL NAME  \
225    1       M        M292  Henry Street School for International Studies
226    1       M        M292  Henry Street School for International Studies
227    1       M        M292  Henry Street School for International Studies
228    1       M        M292  Henry Street School for International Studies
229    1       M        M292  Henry Street School for International Studies

    GRADE  PROGRAM TYPE CORE SUBJECT (MS CORE and 9-12 ONLY)  \
225  09-12       GEN ED                              ENGLISH
226  09-12       GEN ED                              ENGLISH
227  09-12       GEN ED                              ENGLISH
228  09-12       GEN ED                              ENGLISH
229  09-12       GEN ED                                 MATH

    CORE COURSE (MS CORE and 9-12 ONLY) SERVICE CATEGORY(K-9* ONLY)  \
225                           English 9                           -
226                          English 10                           -
227                          English 11                           -
228                          English 12                           -
229                  Integrated Algebra                           -

     NUMBER OF STUDENTS / SEATS FILLED  NUMBER OF SECTIONS  \
225                               63.0                 3.0
226                               79.0                 3.0
227                               38.0                 2.0
228                               69.0                 3.0
229                               53.0                 3.0

     AVERAGE CLASS SIZE  SIZE OF SMALLEST CLASS  SIZE OF LARGEST CLASS  \
225                21.0                    19.0                   25.0
226                26.3                    24.0                   31.0
227                19.0                    16.0                   22.0
228                23.0                    13.0                   30.0
229                17.7                    16.0                   21.0

    DATA SOURCE  SCHOOLWIDE PUPIL-TEACHER RATIO padded_csd     DBN
225       STARS                             NaN         01  01M292
226       STARS                             NaN         01  01M292
227       STARS                             NaN         01  01M292
228       STARS                             NaN         01  01M292
229       STARS                             NaN         01  01M292
----------------------
----------------------
----------------------
        CSD  NUMBER OF STUDENTS / SEATS FILLED  NUMBER OF SECTIONS  \
DBN
01M292    1                            88.0000            4.000000
01M332    1                            46.0000            2.000000
01M378    1                            33.0000            1.000000
01M448    1                           105.6875            4.750000
01M450    1                            57.6000            2.733333

        AVERAGE CLASS SIZE  SIZE OF SMALLEST CLASS  SIZE OF LARGEST CLASS  \
DBN
01M292           22.564286                   18.50              26.571429
01M332           22.000000                   21.00              23.500000
01M378           33.000000                   33.00              33.000000
01M448           22.231250                   18.25              27.062500
01M450           21.200000                   19.40              22.866667

        SCHOOLWIDE PUPIL-TEACHER RATIO
DBN
01M292                             NaN
01M332                             NaN
01M378                             NaN
01M448                             NaN
01M450                             NaN
----------------------
----------------------
----------------------
      DBN  CSD  NUMBER OF STUDENTS / SEATS FILLED  NUMBER OF SECTIONS  \
0  01M292    1                            88.0000            4.000000
1  01M332    1                            46.0000            2.000000
2  01M378    1                            33.0000            1.000000
3  01M448    1                           105.6875            4.750000
4  01M450    1                            57.6000            2.733333

   AVERAGE CLASS SIZE  SIZE OF SMALLEST CLASS  SIZE OF LARGEST CLASS  \
0           22.564286                   18.50              26.571429
1           22.000000                   21.00              23.500000
2           33.000000                   33.00              33.000000
3           22.231250                   18.25              27.062500
4           21.200000                   19.40              22.866667

   SCHOOLWIDE PUPIL-TEACHER RATIO
0                             NaN
1                             NaN
2                             NaN
3                             NaN
4                             NaN
"""



"""
4: Condensing Demographics
Now that we've finished condensing class_size, let's condense demographics. The first few rows look like this:

DBN	Name	schoolyear	fl_percent	frl_percent	total_enrollment	prek	k	grade1	grade2	...	black_num	black_per	hispanic_num	hispanic_per	white_num	white_per	male_num	male_per	female_num	female_per
0	01M015	P.S. 015 ROBERTO CLEMENTE	20052006	89.4	NaN	281	15	36	40	33	...	74	26.3	189	67.3	5	1.8	158.0	56.2	123.0	43.8
1	01M015	P.S. 015 ROBERTO CLEMENTE	20062007	89.4	NaN	243	15	29	39	38	...	68	28.0	153	63.0	4	1.6	140.0	57.6	103.0	42.4
2	01M015	P.S. 015 ROBERTO CLEMENTE	20072008	89.4	NaN	261	18	43	39	36	...	77	29.5	157	60.2	7	2.7	143.0	54.8	118.0	45.2
3	01M015	P.S. 015 ROBERTO CLEMENTE	20082009	89.4	NaN	252	17	37	44	32	...	75	29.8	149	59.1	7	2.8	149.0	59.1	103.0	40.9
4	01M015	P.S. 015 ROBERTO CLEMENTE	20092010		96.5	208	16	40	28	32	...	67	32.2	118	56.7	6	2.9	124.0	59.6	84.0	40.4
In this case, the only column that prevents a given DBN from being unique is schoolyear.
We only want to select rows where schoolyear is 20112012, to get the most recent year, and to match our SAT results data.

Instructions
Filter demographics, and only select only rows in data["demographics"] where schoolyear is 20112012.
schoolyear is actually an integer, so be careful about how you perform your comparison.
Display the first few rows of data["demographics"] to verify that the filtering worked.
"""
data["demographics"] = data["demographics"][data["demographics"]["schoolyear"] == 20112012]
print(data["demographics"].head())
""" Console Outputs or Results
Output
       DBN                                              Name  schoolyear  \
6   01M015  P.S. 015 ROBERTO CLEMENTE                           20112012
13  01M019  P.S. 019 ASHER LEVY                                 20112012
20  01M020  PS 020 ANNA SILVER                                  20112012
27  01M034  PS 034 FRANKLIN D ROOSEVELT                         20112012
35  01M063  PS 063 WILLIAM MCKINLEY                             20112012

   fl_percent  frl_percent  total_enrollment prek    k grade1 grade2  \
6         NaN         89.4               189   13   31     35     28
13        NaN         61.5               328   32   46     52     54
20        NaN         92.5               626   52  102    121     87
27        NaN         99.7               401   14   34     38     36
35        NaN         78.9               176   18   20     30     21

      ...     black_num black_per hispanic_num hispanic_per white_num  \
6     ...            63      33.3          109         57.7         4
13    ...            81      24.7          158         48.2        28
20    ...            55       8.8          357         57.0        16
27    ...            90      22.4          275         68.6         8
35    ...            41      23.3          110         62.5        15

   white_per male_num male_per female_num female_per
6        2.1     97.0     51.3       92.0       48.7
13       8.5    147.0     44.8      181.0       55.2
20       2.6    330.0     52.7      296.0       47.3
27       2.0    204.0     50.9      197.0       49.1
35       8.5     97.0     55.1       79.0       44.9

[5 rows x 38 columns]
"""




"""
5: Condensing Graduation
Finally, we'll need to condense the graduation dataset. Here are the first few rows:

Demographic	DBN	School Name	Cohort	Total Cohort	Total Grads - n	Total Grads - % of cohort	Total Regents - n	Total Regents - % of cohort	Total Regents - % of grads	...	Regents w/o Advanced - n	Regents w/o Advanced - % of cohort	Regents w/o Advanced - % of grads	Local - n	Local - % of cohort	Local - % of grads	Still Enrolled - n	Still Enrolled - % of cohort	Dropped Out - n	Dropped Out - % of cohort
0	Total Cohort	01M292	HENRY STREET SCHOOL FOR INTERNATIONAL	2003	5	s	s	s	s	s	...	s	s	s	s	s	s	s	s	s	s
1	Total Cohort	01M292	HENRY STREET SCHOOL FOR INTERNATIONAL	2004	55	37	67.3%	17	30.9%	45.9%	...	17	30.9%	45.9%	20	36.4%	54.1%	15	27.3%	3	5.5%
2	Total Cohort	01M292	HENRY STREET SCHOOL FOR INTERNATIONAL	2005	64	43	67.2%	27	42.2%	62.8%	...	27	42.2%	62.8%	16	25%	37.200000000000003%	9	14.1%	9	14.1%
3	Total Cohort	01M292	HENRY STREET SCHOOL FOR INTERNATIONAL	2006	78	43	55.1%	36	46.2%	83.7%	...	36	46.2%	83.7%	7	9%	16.3%	16	20.5%	11	14.1%
4	Total Cohort	01M292	HENRY STREET SCHOOL FOR INTERNATIONAL	2006 Aug	78	44	56.4%	37	47.4%	84.1%	...	37	47.4%	84.1%	7	9%	15.9%	15	19.2%	11	14.1%
In the graduation data, the Demographic and Cohort columns are what prevent DBN from being unique. A Cohort appears to be which year the data was recorded for, and the Demographic appears to be in which group the data was collected. In this case, we want to pick data from the most recent Cohort available, 2006. We also want data from the full cohort, so we'll only pick rows where Demographic is Total Cohort.

Instructions
Filter graduation, and only select rows where the Cohort column equals 2006.
Filter graduation, and only select rows where the Demographic column equals Total Cohort.
Display the first few rows of data["graduation"], to verify that everything worked properly.
"""
data["graduation"] = data["graduation"][data["graduation"]["Cohort"] == "2006"]
data["graduation"] = data["graduation"][data["graduation"]["Demographic"] == "Total Cohort"]
print(data["graduation"].head())
""" Console Outputs or Results
Output
     Demographic     DBN                            School Name Cohort  \
3   Total Cohort  01M292  HENRY STREET SCHOOL FOR INTERNATIONAL   2006
10  Total Cohort  01M448    UNIVERSITY NEIGHBORHOOD HIGH SCHOOL   2006
17  Total Cohort  01M450             EAST SIDE COMMUNITY SCHOOL   2006
24  Total Cohort  01M509                MARTA VALLE HIGH SCHOOL   2006
31  Total Cohort  01M515  LOWER EAST SIDE PREPARATORY HIGH SCHO   2006

    Total Cohort Total Grads - n Total Grads - % of cohort Total Regents - n  \
3             78              43                     55.1%                36
10           124              53                     42.7%                42
17            90              70                     77.8%                67
24            84              47                       56%                40
31           193             105                     54.4%                91

   Total Regents - % of cohort Total Regents - % of grads  \
3                        46.2%                      83.7%
10                       33.9%                      79.2%
17         74.400000000000006%                      95.7%
24                       47.6%                      85.1%
31                       47.2%                      86.7%

              ...            Regents w/o Advanced - n  \
3             ...                                  36
10            ...                                  34
17            ...                                  67
24            ...                                  23
31            ...                                  22

   Regents w/o Advanced - % of cohort Regents w/o Advanced - % of grads  \
3                               46.2%                             83.7%
10                              27.4%                             64.2%
17                74.400000000000006%                             95.7%
24                              27.4%                             48.9%
31                              11.4%                               21%

   Local - n Local - % of cohort Local - % of grads Still Enrolled - n  \
3          7                  9%              16.3%                 16
10        11                8.9%              20.8%                 46
17         3                3.3%               4.3%                 15
24         7  8.300000000000001%              14.9%                 25
31        14                7.3%              13.3%                 53

   Still Enrolled - % of cohort Dropped Out - n Dropped Out - % of cohort
3                         20.5%              11                     14.1%
10                        37.1%              20       16.100000000000001%
17                        16.7%               5                      5.6%
24                        29.8%               5                        6%
31                        27.5%              35       18.100000000000001%

[5 rows x 23 columns]
"""



"""
6: Converting AP Test Scores
We're almost ready to combine all of the datasets.
The only remaining thing to do is to convert the AP test scores to numeric values from strings.
The Advanced Placement, or AP, exams are taken by high school students.
There are several AP exams, each corresponding to a school subject.
If a high schooler passes a test with a high score, they may receive college credit.
The AP is scored on a 1 to 5 scale, with anything 3 or higher being a "passing" score.
Many high schoolers, particularly those who go to academically challenging high schools, take AP exams.
AP exams are much rarer in schools that lack funding or don't have much academic rigor.

It will be interesting to see if AP exam scores are correlated with SAT scores across high schools.
In order to determine this, we'll need to convert the AP exam scores in the ap_2010 dataset to numeric values first.

There are three columns we'll need to convert:

AP Test Takers (note that there's a trailing space)
Total Exams Taken
Number of Exams with scores 3 4 or 5
Note that the first column above, AP Test Takers, has a trailing space at the end.

Instructions
Convert each of the following columns in ap_2010 to numeric values using the to_numeric function with the keyword argument errors="coerce".
AP Test Takers
Total Exams Taken
Number of Exams with scores 3 4 or 5
Display the first few rows of ap_2010 to confirm.
"""
cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
for col in cols:
    data["ap_2010"][col] = pd.to_numeric(data["ap_2010"][col],errors="coerce")

print(data["ap_2010"].head())
""" Console Outputs or Results
Output
      DBN                             SchoolName  AP Test Takers   \
0  01M448           UNIVERSITY NEIGHBORHOOD H.S.             39.0
1  01M450                 EAST SIDE COMMUNITY HS             19.0
2  01M515                    LOWER EASTSIDE PREP             24.0
3  01M539         NEW EXPLORATIONS SCI,TECH,MATH            255.0
4  02M296  High School of Hospitality Management              NaN

   Total Exams Taken  Number of Exams with scores 3 4 or 5
0               49.0                                  10.0
1               21.0                                   NaN
2               26.0                                  24.0
3              377.0                                 191.0
4                NaN                                   NaN
"""




"""
7: Types Of Joins
Before we merge our data, we'll need to decide on what kind of merge strategy we want to use.
We'll be using the Pandas merge function, which supports four types of joins, left, right, inner, and outer.
Each of these join types dictates how rows are combined.

We'll be using the DBN to match up rows, which is how we'll know which row from the first dataset combines with the row from the second dataset.
It's possible that even though the DBN is unique within each dataset, that there may be DBN values that exist in one dataset but not another.
This is because the data is from different years, and each dataset has other inconsistencies in terms of how it was gathered.
There may also be human and other errors in play.
Therefore, we may not find matches in all of the datasets for the DBN values in sat_results, and other datasets may have DBN values that don't exist in sat_results.

We'll merge two datasets at a time.
So, for example, we'll merge sat_results and hs_directory, then merge the result with ap_2010, then merge the result with class_size, and so on until we've merged all of the datasets.
Once we merge all of the datasets, we'll have roughly the same number of rows, but each row will have columns from all the datasets.

Which merge strategy we pick will affect how many rows we end up with. Let's look at each strategy.

Let's say we're merging the following two datasets:

see im8.png

With an inner merge, we'd only combine rows where the same DBN existed in both datasets. We'd end up with this:

see im9.png

With a left merge, we'll only use DBN values from the Dataframe on the "left" of the merge.
In this case, sat_results is on the left. Any rows that have a DBN in sat_results but not class_size will be assigned null values for the columns in class_size:

see im10.png

With a right merge, we'll only use DBN values from the Dataframe on the "right" of the merge. In this case, class_size is on the right:

see im11.png

With an outer merge, we'll take any DBN values from either sat_results or class_size:

see im12.png

As you can see, each merge strategy comes with advantages.
Depending on your merge strategy, you may preserve rows at the expense of more missing column data, or have less missing data at the expense of fewer rows.
Choosing a merge strategy is an important choice, and it's worth thinking through the data you have, and what tradeoffs you want to make.

Since what we care about in this project is figuring out what correlates with SAT score, we'll want to preserve as many rows as possible from sat_results while minimizing null values.

This means that we may need to take different merge strategies with different datasets.
Some of the datasets are missing many DBN values, so a left join is more appropriate, because we don't want to lose too many rows when we merge.
If we did an inner join in this case, we would lose the data for many high schools.

Some of the datasets have almost all the same DBN values as sat_results and have important information, so an inner join is okay in this case.
For example, we wouldn't be able to do most of our analysis if a lot of rows were missing information from demographics.
Thus, we do an inner join to avoid missing data in these columns.
"""



"""
8: Performing The Left Joins
Both the ap_2010 and the graduation datasets have many missing DBN values, so we'll use a left join when we join the sat_results dataset with them.
A left join means that our final Dataframe will have all the same DBN values as the original sat_results Dataframe.

We'll need to use the Pandas merge method to merge Dataframes.
The "left" Dataframe is the Dataframe we call the method on, whereas the "right" Dataframe is the one we pass into merge.

Because we're using the DBN column to join the Dataframes, we'll need to specify the keyword argument on="DBN" when calling merge.

We'll first assign data["sat_results"] to the variable combined. We'll then merge all the other Dataframes with combined.
At the end, combined will have all of the columns from all of the datasets.

Instructions
Use the Pandas merge method to merge the ap_2010 dataset into combined.
Make sure to specify how="left" as a keyword argument to get the right join type.
Make sure to assign the result of the merge operation back to combined.
Use the Pandas merge method to merge the graduation dataset into combined.
Make sure to specify how="left" as a keyword argument to get the right join type.
Make sure to assign the result of the merge operation back to combined.
Display the first few rows of combined to verify the right operations happened.
Display the shape of the Dataframe to see how many rows now exist.
"""
combined = data["sat_results"]
combined = combined.merge(data["ap_2010"],how="left",on="DBN")
combined = combined.merge(data["graduation"],how="left",on="DBN")
print(combined.head())
print("---------------")
print("---------------")
print(combined.shape)
""" Console Outputs or Results
Output
      DBN                                    SCHOOL NAME  \
0  01M292  HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES
1  01M448            UNIVERSITY NEIGHBORHOOD HIGH SCHOOL
2  01M450                     EAST SIDE COMMUNITY SCHOOL
3  01M458                      FORSYTH SATELLITE ACADEMY
4  01M509                        MARTA VALLE HIGH SCHOOL

  Num of SAT Test Takers  SAT Critical Reading Avg. Score  \
0                     29                            355.0
1                     91                            383.0
2                     70                            377.0
3                      7                            414.0
4                     44                            390.0

   SAT Math Avg. Score  SAT Writing Avg. Score  sat_score  \
0                404.0                   363.0     1122.0
1                423.0                   366.0     1172.0
2                402.0                   370.0     1149.0
3                401.0                   359.0     1174.0
4                433.0                   384.0     1207.0

                     SchoolName  AP Test Takers   Total Exams Taken  \
0                           NaN              NaN                NaN
1  UNIVERSITY NEIGHBORHOOD H.S.             39.0               49.0
2        EAST SIDE COMMUNITY HS             19.0               21.0
3                           NaN              NaN                NaN
4                           NaN              NaN                NaN

             ...             Regents w/o Advanced - n  \
0            ...                                   36
1            ...                                   34
2            ...                                   67
3            ...                                  NaN
4            ...                                   23

  Regents w/o Advanced - % of cohort Regents w/o Advanced - % of grads  \
0                              46.2%                             83.7%
1                              27.4%                             64.2%
2                74.400000000000006%                             95.7%
3                                NaN                               NaN
4                              27.4%                             48.9%

  Local - n  Local - % of cohort Local - % of grads Still Enrolled - n  \
0         7                   9%              16.3%                 16
1        11                 8.9%              20.8%                 46
2         3                 3.3%               4.3%                 15
3       NaN                  NaN                NaN                NaN
4         7   8.300000000000001%              14.9%                 25

  Still Enrolled - % of cohort Dropped Out - n Dropped Out - % of cohort
0                        20.5%              11                     14.1%
1                        37.1%              20       16.100000000000001%
2                        16.7%               5                      5.6%
3                          NaN             NaN                       NaN
4                        29.8%               5                        6%

[5 rows x 33 columns]
---------------
---------------
(479, 33)
"""




"""
9: Performing The Inner Joins
Now that we've done the left joins, we still have class_size, demographics, survey, and hs_directory left to merge into combined.
Because these files contain information that's more valuable to our analysis, and because they have fewer missing DBN values, we'll use the inner join type when merging these into combined.

Instructions
Merge class_size, then demographics, then survey, then hs_directory into combined.
Be sure to follow the exact order above.
Remember to specify the correct column to join on, and the correct join type.
Display the first few rows of combined to verify the right operations happened.
Display the shape of the Dataframe to see how many rows now exist.
"""
combined = combined.merge(data["class_size"],how="inner", on="DBN")
combined = combined.merge(data["demographics"],how="inner", on="DBN")
combined = combined.merge(data["survey"],how="inner", on="DBN")
combined = combined.merge(data["hs_directory"],how="inner", on="DBN")
print(combined.head())
print("---------------")
print("---------------")
print(combined.shape)
""" Console Outputs or Results
      DBN                                        SCHOOL NAME  \
0  01M292      HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES
1  01M448                UNIVERSITY NEIGHBORHOOD HIGH SCHOOL
2  01M450                         EAST SIDE COMMUNITY SCHOOL
3  01M509                            MARTA VALLE HIGH SCHOOL
4  01M539  NEW EXPLORATIONS INTO SCIENCE, TECHNOLOGY AND ...

  Num of SAT Test Takers  SAT Critical Reading Avg. Score  \
0                     29                            355.0
1                     91                            383.0
2                     70                            377.0
3                     44                            390.0
4                    159                            522.0

   SAT Math Avg. Score  SAT Writing Avg. Score  sat_score  \
0                404.0                   363.0     1122.0
1                423.0                   366.0     1172.0
2                402.0                   370.0     1149.0
3                433.0                   384.0     1207.0
4                574.0                   525.0     1621.0

                       SchoolName  AP Test Takers   Total Exams Taken  \
0                             NaN              NaN                NaN
1    UNIVERSITY NEIGHBORHOOD H.S.             39.0               49.0
2          EAST SIDE COMMUNITY HS             19.0               21.0
3                             NaN              NaN                NaN
4  NEW EXPLORATIONS SCI,TECH,MATH            255.0              377.0

     ...                                   priority04  \
0    ...      Then to Manhattan students or residents
1    ...                                          NaN
2    ...                                          NaN
3    ...                                          NaN
4    ...                                          NaN

                        priority05 priority06 priority07  priority08  \
0  Then to New York City residents        NaN        NaN         NaN
1                              NaN        NaN        NaN         NaN
2                              NaN        NaN        NaN         NaN
3                              NaN        NaN        NaN         NaN
4                              NaN        NaN        NaN         NaN

  priority09 priority10                                         Location 1  \
0        NaN        NaN  220 Henry Street\nNew York, NY 10002\n(40.7137...
1        NaN        NaN  200 Monroe Street\nNew York, NY 10002\n(40.712...
2        NaN        NaN  420 East 12 Street\nNew York, NY 10009\n(40.72...
3        NaN        NaN  145 Stanton Street\nNew York, NY 10002\n(40.72...
4        NaN        NaN  111 Columbia Street\nNew York, NY 10002\n(40.7...

         lat        lon
0  40.713764 -73.985260
1  40.712332 -73.984797
2  40.729783 -73.983041
3  40.720569 -73.985673
4  40.718725 -73.979426

[5 rows x 159 columns]
---------------
---------------
(363, 159)
"""



"""
10: Filling In Missing Values
You may have noticed that doing inner joins meant that we "lost" 116 rows from sat_results.
This is because the DBN values that existed in sat_results couldn't be found in the other datasets.
his is worth investigating, but for our purposes, we're looking for high-level correlations, so we don't need to dive into which DBNs are missing.

What you also may have noticed in the last screen is that we now have many columns with null, or NaN values.
This is due to us choosing to do left joins, where some columns may not have had data.
The dataset also had some missing values to begin with.
If we hadn't done a left join, all the rows with missing data would have been lost in the merge process instead, which wouldn't have left us with many high schools in our dataset.

There are many ways to handle missing data, which we'll cover in more detail later on.
For now, we'll just fill in the missing values with the mean value of the column. Here's a diagram:

see im13.png

In the diagram above, the mean of the first column is (1800 + 1600 + 2200 + 2300) / 4, or 1975, and the mean of the second column is (20 + 30 + 30 + 50) / 4, or 32.5. We fill in the missing values with the column means, which allows us to proceed with analysis that can't deal with missing values (like correlations).

We can fill in missing data in Pandas using the fillna method.
This method will replace any missing values in a Dataframe with values that we specify.
We can compute the means of every column using the mean method.
If we pass the results of the mean method into the fillna method, Pandas will fill in the missing values in each column with the mean of that column.

Here's an example:

means = df.mean()
df = df.fillna(means)
Note that if a column consists entirely of null or NaN values, then Pandas will not be able to fill in the missing values when you use the fillna method along with the mean method, because there won't be a mean.

We should fill any remaining NaN or null values after the initial replacement with the value 0. We can do this by passing 0 into the fillna method.

Instructions
Compute the means of all the columns in combined using the mean method.
Fill in any missing values in combined with the column means using the fillna method.
Fill in any remaining missing values in combined with 0 using the fillna method.
Display the first few rows of combined to verify the right operations happened.

"""
means = combined.mean()
combined = combined.fillna(means)
print(combined.head())
print("---------------")
print("---------------")
combined = combined.fillna(value=0)
print(combined.head())
""" Console Outputs or Results
Output
      DBN                                        SCHOOL NAME  \
0  01M292      HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES
1  01M448                UNIVERSITY NEIGHBORHOOD HIGH SCHOOL
2  01M450                         EAST SIDE COMMUNITY SCHOOL
3  01M509                            MARTA VALLE HIGH SCHOOL
4  01M539  NEW EXPLORATIONS INTO SCIENCE, TECHNOLOGY AND ...

  Num of SAT Test Takers  SAT Critical Reading Avg. Score  \
0                     29                            355.0
1                     91                            383.0
2                     70                            377.0
3                     44                            390.0
4                    159                            522.0

   SAT Math Avg. Score  SAT Writing Avg. Score  sat_score  \
0                404.0                   363.0     1122.0
1                423.0                   366.0     1172.0
2                402.0                   370.0     1149.0
3                433.0                   384.0     1207.0
4                574.0                   525.0     1621.0

                       SchoolName  AP Test Takers   Total Exams Taken  \
0                             NaN       129.028846         197.038462
1    UNIVERSITY NEIGHBORHOOD H.S.        39.000000          49.000000
2          EAST SIDE COMMUNITY HS        19.000000          21.000000
3                             NaN       129.028846         197.038462
4  NEW EXPLORATIONS SCI,TECH,MATH       255.000000         377.000000

     ...                                   priority04  \
0    ...      Then to Manhattan students or residents
1    ...                                          NaN
2    ...                                          NaN
3    ...                                          NaN
4    ...                                          NaN

                        priority05 priority06 priority07  priority08  \
0  Then to New York City residents        NaN        NaN         NaN
1                              NaN        NaN        NaN         NaN
2                              NaN        NaN        NaN         NaN
3                              NaN        NaN        NaN         NaN
4                              NaN        NaN        NaN         NaN

  priority09 priority10                                         Location 1  \
0        NaN        NaN  220 Henry Street\nNew York, NY 10002\n(40.7137...
1        NaN        NaN  200 Monroe Street\nNew York, NY 10002\n(40.712...
2        NaN        NaN  420 East 12 Street\nNew York, NY 10009\n(40.72...
3        NaN        NaN  145 Stanton Street\nNew York, NY 10002\n(40.72...
4        NaN        NaN  111 Columbia Street\nNew York, NY 10002\n(40.7...

         lat        lon
0  40.713764 -73.985260
1  40.712332 -73.984797
2  40.729783 -73.983041
3  40.720569 -73.985673
4  40.718725 -73.979426

[5 rows x 159 columns]
---------------
---------------
      DBN                                        SCHOOL NAME  \
0  01M292      HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES
1  01M448                UNIVERSITY NEIGHBORHOOD HIGH SCHOOL
2  01M450                         EAST SIDE COMMUNITY SCHOOL
3  01M509                            MARTA VALLE HIGH SCHOOL
4  01M539  NEW EXPLORATIONS INTO SCIENCE, TECHNOLOGY AND ...

  Num of SAT Test Takers  SAT Critical Reading Avg. Score  \
0                     29                            355.0
1                     91                            383.0
2                     70                            377.0
3                     44                            390.0
4                    159                            522.0

   SAT Math Avg. Score  SAT Writing Avg. Score  sat_score  \
0                404.0                   363.0     1122.0
1                423.0                   366.0     1172.0
2                402.0                   370.0     1149.0
3                433.0                   384.0     1207.0
4                574.0                   525.0     1621.0

                       SchoolName  AP Test Takers   Total Exams Taken  \
0                               0       129.028846         197.038462
1    UNIVERSITY NEIGHBORHOOD H.S.        39.000000          49.000000
2          EAST SIDE COMMUNITY HS        19.000000          21.000000
3                               0       129.028846         197.038462
4  NEW EXPLORATIONS SCI,TECH,MATH       255.000000         377.000000

     ...                                   priority04  \
0    ...      Then to Manhattan students or residents
1    ...                                            0
2    ...                                            0
3    ...                                            0
4    ...                                            0

                        priority05 priority06 priority07  priority08  \
0  Then to New York City residents          0          0           0
1                                0          0          0           0
2                                0          0          0           0
3                                0          0          0           0
4                                0          0          0           0

  priority09 priority10                                         Location 1  \
0          0          0  220 Henry Street\nNew York, NY 10002\n(40.7137...
1          0          0  200 Monroe Street\nNew York, NY 10002\n(40.712...
2          0          0  420 East 12 Street\nNew York, NY 10009\n(40.72...
3          0          0  145 Stanton Street\nNew York, NY 10002\n(40.72...
4          0          0  111 Columbia Street\nNew York, NY 10002\n(40.7...

         lat        lon
0  40.713764 -73.985260
1  40.712332 -73.984797
2  40.729783 -73.983041
3  40.720569 -73.985673
4  40.718725 -73.979426

[5 rows x 159 columns]
"""




"""
11: Adding A School District Column
We've finished cleaning and combining our data! We now have a clean dataset on which we can base our analysis.
One type of analysis that we might want to do is mapping out statistics on a school district level.
In order to help us do this, it will be useful to add a column that specifies the school district to the dataset.

The school district is just the first two characters of the DBN.
We can apply a function over the DBN column of combined that pulls out the first two letters.

We can use indexing to extract the first few characters of a string, like this:


name = "Sinbad"
print(name[0:2])
Instructions
Write a function that extracts the first 2 characters of a string, and returns them.
Apply the function to the DBN column of combined, and assign the result to the school_dist column of combined.
Display the first few items in the school_dist column of combined to verify.
"""
def extracts21thchar(str):
    extract = str[0:2]
    return extract

combined["school_dist"] = combined["DBN"].apply(extracts21thchar)
print(combined.head())

""" Console Outputs or Results
Output
      DBN                                        SCHOOL NAME  \
0  01M292      HENRY STREET SCHOOL FOR INTERNATIONAL STUDIES
1  01M448                UNIVERSITY NEIGHBORHOOD HIGH SCHOOL
2  01M450                         EAST SIDE COMMUNITY SCHOOL
3  01M509                            MARTA VALLE HIGH SCHOOL
4  01M539  NEW EXPLORATIONS INTO SCIENCE, TECHNOLOGY AND ...

  Num of SAT Test Takers  SAT Critical Reading Avg. Score  \
0                     29                            355.0
1                     91                            383.0
2                     70                            377.0
3                     44                            390.0
4                    159                            522.0

   SAT Math Avg. Score  SAT Writing Avg. Score  sat_score  \
0                404.0                   363.0     1122.0
1                423.0                   366.0     1172.0
2                402.0                   370.0     1149.0
3                433.0                   384.0     1207.0
4                574.0                   525.0     1621.0

                       SchoolName  AP Test Takers   Total Exams Taken  \
0                               0       129.028846         197.038462
1    UNIVERSITY NEIGHBORHOOD H.S.        39.000000          49.000000
2          EAST SIDE COMMUNITY HS        19.000000          21.000000
3                               0       129.028846         197.038462
4  NEW EXPLORATIONS SCI,TECH,MATH       255.000000         377.000000

      ...                           priority05 priority06 priority07  \
0     ...      Then to New York City residents          0          0
1     ...                                    0          0          0
2     ...                                    0          0          0
3     ...                                    0          0          0
4     ...                                    0          0          0

  priority08  priority09 priority10  \
0          0           0          0
1          0           0          0
2          0           0          0
3          0           0          0
4          0           0          0

                                          Location 1        lat        lon  \
0  220 Henry Street\nNew York, NY 10002\n(40.7137...  40.713764 -73.985260
1  200 Monroe Street\nNew York, NY 10002\n(40.712...  40.712332 -73.984797
2  420 East 12 Street\nNew York, NY 10009\n(40.72...  40.729783 -73.983041
3  145 Stanton Street\nNew York, NY 10002\n(40.72...  40.720569 -73.985673
4  111 Columbia Street\nNew York, NY 10002\n(40.7...  40.718725 -73.979426

  school_dist
0          01
1          01
2          01
3          01
4          01

[5 rows x 160 columns]
"""



"""
12: Next Steps
We now have a clean dataset that we can analyze! We've done a lot in this mission -- we've gone from starting with several messy datasets to having one clean, combined, dataset that we can analyze.

Along the way, we've learned:

How to deal with missing values.
Different types of merges.
How to condense datasets down.
Computing averages across Dataframes.
Being able to clean and combine datasets is one of the most critical skills any data analyst or scientist can learn.
Most of the time, you won't have nice clean datasets to analyze, and almost all data science work involves data cleaning.

In the next mission, we'll do some analysis on our clean data, including finding correlations and mapping.
"""
