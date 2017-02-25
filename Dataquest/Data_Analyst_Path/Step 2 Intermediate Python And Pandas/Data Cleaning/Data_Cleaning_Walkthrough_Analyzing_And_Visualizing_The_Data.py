"""
02/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Data Cleaning : Analyzing And Visualizing The Data
"""

"""
1: Analyzing The Data
In the last two missions, we started investigating the relationship between SAT scores and demographic factors.
In order to do this, we acquired several datasets about New York City public schools.
We cleaned and combined these datasets to get a single dataset, combined, that we're now ready to analyze and visualize.

In this mission, we'll find correlations, make plots, then make maps using the combined Pandas Dataframe.

The first step that we'll take is to find correlations between every column and sat_score. This will help us figure out what columns might be interesting to investigate more or plot out. After this, we'll be able to do more analysis and make maps using the columns that we identify.
"""


"""
2: Finding Correlations
Correlations tell us how closely related two columns are.
We'll be using the r value, also called Pearson's correlation coefficient, which measures how closely two sequences of numbers are correlated.
There's a more thorough explanation of the r value in the statistics course, but we'll go through a quick example now.
An r value falls between -1 and 1, and tells you if the two columns are positively correlated, not correlated, or negatively correlated.
The closer to 1 the r value is, the more strongly positively correlated the columns are.
The closer to -1 the r value is, the more strongly negatively correlated the columns are.
The closer to 0 the r value is, the less the columns are correlated.

In the following diagram, both columns are strongly positively correlated -- when the value in class_size is high, the value in sat_score is also high, and vice versa:

see im14.png

The r value for the columns in the above diagram is .99.

In the following diagram, both columns are strongly negatively correlated -- when the value in class_size is high, the value in sat_score is low, and when the value in sat_score is high, the value in class_size is low:

see im15.png

The r value for the columns in the above diagram is -.99.

In the following diagram, both columns are not correlated -- class_size and sat_score do not have any strong pattern in their values:

see im16.png

The r value for the columns in the above diagram is -.02, which is very close to 0.

In general r-values above .25 or below -.25 are enough to qualify a correlation as interesting.
An r-value isn't perfect, and doesn't indicate that there is a correlation. It just indicates the possiblity of one.
To really assess whether or not a correlation exists, you need to look at the data using a scatterplot, and see the "shape" of the data.
For example, here's a scatterplot with a very strong negative r-value, -.73:

see correlation.png

Notice how in the above image, all of the points appear to fall along a line. This indicates a correlation.

Here's a scatterplot with an r-value, .15, that indicates a weak correlation:

see no_correlation.png

Notice how in the above image, the data points go in several directions, and there's no clear linear relationship.
We'll dive more into how to explore correlations later on in the statistics content, but this quick primer should be enough to get us through this project.

Since we're interested in exploring the fairness of the SAT, finding that demographic factors like race and gender are strongly positively or negatively correlated with SAT scores would be an interesting result that merited investigation.
For example, if men tended to score more highly on the SAT, it would indicate that the SAT is potentially unfair to women.

We can use the Pandas corr method to find correlations between columns in a Dataframe.
The result of the method is a Dataframe where each column and row index is the name of a column in the original dataset.

Instructions
Use the corr method on the combined Dataframe to find all possible correlations.
Assign the result to correlations.
Filter correlations so that only correlations for the column sat_score are shown.
Display all the rows in correlations to explore the correlations.

"""
correlations = combined.corr(method='pearson')["sat_score"]
print(correlations)
""" Console Outputs or Results
 Output
SAT Critical Reading Avg. Score         0.986820
SAT Math Avg. Score                     0.972643
SAT Writing Avg. Score                  0.987771
sat_score                               1.000000
AP Test Takers                          0.523140
Total Exams Taken                       0.514333
Number of Exams with scores 3 4 or 5    0.463245
Total Cohort                            0.325144
CSD                                     0.042948
NUMBER OF STUDENTS / SEATS FILLED       0.394626
NUMBER OF SECTIONS                      0.362673
AVERAGE CLASS SIZE                      0.381014
SIZE OF SMALLEST CLASS                  0.249949
SIZE OF LARGEST CLASS                   0.314434
SCHOOLWIDE PUPIL-TEACHER RATIO               NaN
schoolyear                                   NaN
fl_percent                                   NaN
frl_percent                            -0.722225
total_enrollment                        0.367857
ell_num                                -0.153778
ell_percent                            -0.398750
sped_num                                0.034933
sped_percent                           -0.448170
asian_num                               0.475445
asian_per                               0.570730
black_num                               0.027979
black_per                              -0.284139
hispanic_num                            0.025744
hispanic_per                           -0.396985
white_num                               0.449559
                                          ...
rr_p                                    0.047925
N_s                                     0.423463
N_t                                     0.291463
N_p                                     0.421530
saf_p_11                                0.122913
com_p_11                               -0.115073
eng_p_11                                0.020254
aca_p_11                                0.035155
saf_t_11                                0.313810
com_t_11                                0.082419
eng_t_10                                     NaN
aca_t_11                                0.132348
saf_s_11                                0.337639
com_s_11                                0.187370
eng_s_11                                0.213822
aca_s_11                                0.339435
saf_tot_11                              0.318753
com_tot_11                              0.077310
eng_tot_11                              0.100102
aca_tot_11                              0.190966
grade_span_max                               NaN
expgrade_span_max                            NaN
zip                                    -0.063977
total_students                          0.407827
number_programs                         0.117012
priority08                                   NaN
priority09                                   NaN
priority10                                   NaN
lat                                    -0.121029
lon                                    -0.132222
Name: sat_score, dtype: float64
"""



"""
3: Plotting Enrollment
In the last screen, you should have seen output like this:


SAT Critical Reading Avg. Score         9.868201e-01
SAT Math Avg. Score                     9.726430e-01
SAT Writing Avg. Score                  9.877708e-01
sat_score                               1.000000e+00
AP Test Takers                          5.231404e-01
Total Exams Taken                       5.143334e-01
Number of Exams with scores 3 4 or 5    4.632450e-01
Total Cohort                            3.251440e-01
CSD                                     4.294755e-02
NUMBER OF STUDENTS / SEATS FILLED       3.946260e-01
NUMBER OF SECTIONS                      3.626733e-01
AVERAGE CLASS SIZE                      3.810143e-01
SIZE OF SMALLEST CLASS                  2.499489e-01
SIZE OF LARGEST CLASS                   3.144343e-01
SCHOOLWIDE PUPIL-TEACHER RATIO                   NaN
schoolyear                                       NaN
fl_percent                                       NaN
frl_percent                            -7.222246e-01
total_enrollment                        3.678569e-01
ell_num                                -1.537782e-01
ell_percent                            -3.987497e-01
sped_num                                3.493309e-02
sped_percent                           -4.481703e-01
asian_num                               4.754451e-01
asian_per                               5.707302e-01
black_num                               2.797915e-02
black_per                              -2.841395e-01
hispanic_num                            2.574353e-02
hispanic_per                           -3.969849e-01
white_num                               4.495586e-01
                                            ...
rr_p                                    4.792452e-02
N_s                                     4.234629e-01
N_t                                     2.914630e-01
N_p                                     4.215300e-01
saf_p_11                                1.229128e-01
com_p_11                               -1.150735e-01
eng_p_11                                2.025411e-02
aca_p_11                                3.515462e-02
saf_t_11                                3.138103e-01
com_t_11                                8.241942e-02
eng_t_10                                         NaN
aca_t_11                                1.323477e-01
saf_s_11                                3.376387e-01
com_s_11                                1.873702e-01
eng_s_11                                2.138216e-01
aca_s_11                                3.394355e-01
saf_tot_11                              3.187535e-01
com_tot_11                              7.731020e-02
eng_tot_11                              1.001018e-01
aca_tot_11                              1.909660e-01
grade_span_max                                   NaN
expgrade_span_max                                NaN
zip                                    -6.397683e-02
total_students                          4.078270e-01
number_programs                         1.170116e-01
priority08                                       NaN
priority09                                       NaN
priority10                                       NaN
lat                                     2.212011e-15
lon                                     2.576191e-15
T
he numbers above represent the r-value between the sat_score column and the named column.
The numbers are in scientific notation, which is a way to more easily represent numbers with a lot of decimal places.
9.868201e-01 is equal to .9868201, 4.294755e-02 is equal to .04294755, and -3.969849e-01 is equal to -.3969849. The number after the e- just means "move the decimal point this many digits to the left".

Unsurprisingly, SAT Critical Reading Avg. Score, SAT Math Avg. Score, SAT Writing Avg. Score, and sat_score are strongly correlated with sat_score.

We can also make some other observations:

total_enrollment correlates strongly positively with sat_score, which is surprising, because you'd think smaller schools, which focused more on the student, would have higher scores.
However, it looks like the opposite -- bigger schools tend to do better on the SAT.
Other columns that are proxies for enrollment, like total_students, N_s, N_p, N_t, AP Test Takers, Total Exams Taken, and NUMBER OF SECTIONS correlate as well.
The percentage of females at a school (female_per), and the number of females (female_num) correlate positively with SAT score, whereas the percentage of males (male_per), and the number of males (male_num) correlate negatively.
This potentially indicates than women do better on the SAT than men.
How highly teachers and students rated safety at the school (saf_t_11, and saf_s_11) correlates with sat_score.
How highly students rated academic standards (aca_s_11) correlates with sat_score, but this does not hold for teachers and parents (aca_p_11 and aca_t_11).
There is a significant racial inequality in SAT scores (white_per, asian_per, black_per, hispanic_per).
The percentage of English language learners at the school (ell_percent, frl_percent) correlates strongly negatively with SAT scores.
Since enrollment seems to have such a strong correlation, let's make a scatterplot of total_enrollment vs sat_score.
Each point in the scatterplot will represent a high school, so we'll be able to see if there are any interesting patterns.

We can plot columns in a Dataframe using the plot accessor on a Dataframe. We can directly use different plot types.
For example df.plot.scatter(x="A", y="b") will create a scatterplot of columns A and B.

Instructions
Create a scatterplot of total_enrollment versus sat_score.
"""
import matplotlib.pyplot as plt
combined.plot.scatter(x="total_enrollment", y="sat_score")
plt.show()
""" Console Outputs or Results
 plot1.png
"""



"""
4: Exploring Schools With Low SAT Scores And Enrollment
From looking at the plot we just generated, it doesn't appear that there's an extremely strong correlation between sat_score and total_enrollment.
If there was a very strong correlation, we'd expect all the points to be arranged in a line.
Instead, there's a large cluster of schools, then a few schools going off in 3 different directions.

However, there is an interesting cluster of points at the bottom left where total_enrollment and sat_score are both low.
This cluster may be what is causing our r-value to be so high. It's worth extracting the names of the schools in this cluster, so we can research them more.

Instructions
Filter the combined Dataframe, and only keep rows where total_enrollment is under 1000, and sat_score is under 1000. Assign the result to low_enrollment.
Display all the items in the School Name column of low_enrollment.
Use Wikipedia and Google to research the names of the schools. Can you discover anything interesting about them?
"""
low_enrollment = combined[(combined["total_enrollment"] < 1000) & (combined["sat_score"] < 1000)]
print(low_enrollment["School Name"])
""" Console Outputs or Results
 Output
91       INTERNATIONAL COMMUNITY HIGH SCHOOL
125                                        0
126          BRONX INTERNATIONAL HIGH SCHOOL
139    KINGSBRIDGE INTERNATIONAL HIGH SCHOOL
141    INTERNATIONAL SCHOOL FOR LIBERAL ARTS
176                                        0
179            HIGH SCHOOL OF WORLD CULTURES
188       BROOKLYN INTERNATIONAL HIGH SCHOOL
225    INTERNATIONAL HIGH SCHOOL AT PROSPECT
237               IT TAKES A VILLAGE ACADEMY
253                MULTICULTURAL HIGH SCHOOL
286    PAN AMERICAN INTERNATIONAL HIGH SCHOO
Name: School Name, dtype: object
"""


"""
5: Plotting Language Learning Percentage
From our research in the last screen, we found that most of the high schools with low total enrollment and low SAT scores are actually schools with a high percentage of English language learners enrolled.
This indicates that it's actually ell_percent that correlates strongly with sat_score instead of total_enrollment.
To explore this relationship more, let's plot out ell_percent vs sat_score.

Instructions
Create a scatterplot of ell_percent versus sat_score.
"""
combined.plot.scatter(x="ell_percent", y="sat_score")
plt.show()
""" Console Outputs or Results
see plot2.png
"""



"""
6: Mapping The Schools
It looks like ell_percent correlates with sat_score more strongly, because the scatterplot is more linear.
However, there's still the cluster with very high ell_percent and low sat_score, which is the same group of international high schools that we investigated earlier.

In order to explore this relationship, we'll want to map out ell_percent by school district, so we can more easily see which parts of the city have a lot of English language learners.

In order to do this, we'll need to be able to create maps.
We learned how to use the basemap package to do this in the Visualizing Geographic Data mission The basemap package allows us to create high-quality maps, plot points over them, then draw coastlines and other features.

We extracted the coordinates of all the schools earlier, and stored them in the lat and lon columns.
This will enable us to plot all of the schools onto a map of the US, centered on New York City.

We can setup the map itself like this:


m = Basemap(
    projection='merc',
    llcrnrlat=40.496044,
    urcrnrlat=40.915256,
    llcrnrlon=-74.255735,
    urcrnrlon=-73.700272,
    resolution='i'
)
​
m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)
The code above will create a plot, centered on New York City (llcrnrlat, urcrnrlat, llcrnrlon, and urcrnrlon define the corners of the area that's shown), and will draw coastlines and rivers accordingly.

Now, all we need to do is convert our lat and lon coordinates into x and y coordinates so we can plot them on top of the map.
This will show us where all the schools in our dataset are located.

As you may recall, in order to plot coordinates using basemap, you need to:

Convert the Pandas Series containing the latitude and longitude to lists using the tolist method.
Make a scatterplot using the longitudes and latitudes with the scatter method on the Basemap object.
Show the plot using the show method.
Additionally, we need to make sure we pass a few keyword arguments to the scatter method:

s -- this affects the size of the point that represents each school on the map.
zorder -- this affects where the points that represent schools will be drawn in the z axis.
If we set it to 2, the points will be drawn on top of the continents, which is where we want them.
latlon -- this is a Boolean that specifies whether we're passing in latitude and longitude coordinates instead of x/y plot coordinates.
Instructions
Setup the map using the code snippet from above that creates the map and draws rivers, coastlines, and boundaries.
Convert the lon column of combined to a list, and assign it to the longitudes variable.
Convert the lat column of combined to a list, and assign it to the latitudes variable.
Call the scatter method on m, and pass in longitudes and latitudes as arguments.
Make sure to pass in longitudes and latitudes in the right order.
Pass in the keyword argument s=20 to increase the size of the points in the scatterplot.
Pass in the keyword argument zorder=2 to plot the points on top of the rest of the map. Otherwise the points will show up underneath the land.
Pass in the keyword argument latlon=True to indicate that we're passing in latitude and longitude coordinates, not axis coordinates.
Show the plot using the show method.
"""
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

m = Basemap(
    projection='merc',
    llcrnrlat=40.496044,
    urcrnrlat=40.915256,
    llcrnrlon=-74.255735,
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

longitudes = combined["lon"].tolist()
latitudes = combined["lat"].tolist()

m.scatter(longitudes,latitudes,s=20,zorder=2,latlon=True)
plt.show()
""" Console Outputs or Results
 see plot3.png
"""



"""
7: Plotting Out Statistics
From the map above, we can see that schools are the most dense in Manhattan (the top of the map), and less dense in Brooklyn, The Bronx, Queens, and Staten Island.

Now that we can plot out the positions of the schools, we can start to display meaningful information on maps, such as the percentage of English language learners by area.

We can shade each point in the scatterplot by passing the keyword argument c into the scatter method.
The c keyword argument will accept a sequence of numbers, and will shade points corresponding to lower numbers or higher numbers differently.

Whatever sequence of numbers we pass into the c keyword argument will be converted to a range from 0 to 1.
These values will then be mapped onto a color map.
Matplotlib has quite a few default colormaps.
In our case, we'll use the summer colormap, which results in green points when the associated number is low, and yellow when it's high.

For example, let's say we plotted ell_percent by school.
If we pass in the keyword argument c=combined["ell_percent"], then any school with a high ell_percent would be shaded yellow, and any school with a low ell_percent would be shaded green.
We can specify a colormap by passing the cmap keyword argument to the scatter method.

Instructions
Setup the map using the code snippet from before that creates the map and draws rivers, coastlines, and boundaries.
Call the scatter method on m, and pass in longitudes and latitudes as arguments.
Make sure to pass in longitudes and latitudes in the right order.
Pass in the keyword argument s=20 to increase the size of the points in the scatterplot.
Pass in the keyword argument zorder=2 to plot the points on top of the rest of the map. Otherwise the points will show up underneath the land.
Pass in the keyword argument latlon=True to indicate that we're passing in latitude and longitude coordinates, not axis coordinates.
Pass in the keyword argument c, with the value combined["ell_percent"] to plot the ell_percent.
Pass in the keyword argument cmap="summer" to get the right color scheme.
Show the plot using the show method.

"""
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

m = Basemap(
    projection='merc',
    llcrnrlat=40.496044,
    urcrnrlat=40.915256,
    llcrnrlon=-74.255735,
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

longitudes = combined["lon"].tolist()
latitudes = combined["lat"].tolist()

m.scatter(longitudes,latitudes,s=20,zorder=2,latlon=True,c=combined["ell_percent"],cmap="summer")
plt.show()
""" Console Outputs or Results
see plot4.png
"""



"""
8: Calculating District Level Statistics
Unfortunately, due to the number of schools, it's hard to interpret the map we made in the last screen.
It looks like uptown Manhattan and parts of Queens have a higher ell_percent, but we can't be sure.
One way to make it easier to read very granular statistics is to aggregate them.
In this case, we can aggregate based on district, which will enable us to plot ell_percent district by district instead of school by school.

In the last mission, we used the groupby and agg methods to find the mean class size for every unique DBN.
The principle is the exact same, except here we'd find the mean of each column for every unique value in school_dist.

Instructions
Find the average values for each column for each school_dist in combined
Use the groupby method to group combined by school_dist.
Use the agg method, along with the numpy.mean function as an argument, to calculate the average of each group.
Assign the result to the variable districts.
Reset the index of districts, making school_dist a column again.
Use the reset_index method, along with the keyword argument inplace=True.
Display the first few rows of districts to verify everything went okay.
"""
import numpy as np
print(combined.head())
print("----------------------")
print("----------------------")
print("----------------------")
districts = combined.groupby("school_dist").agg(np.mean)
print(districts.head())
print("----------------------")
print("----------------------")
print("----------------------")
districts.reset_index(inplace=True)
print(districts.head())
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
----------------------
----------------------
----------------------
             SAT Critical Reading Avg. Score  SAT Math Avg. Score  \
school_dist
01                                441.833333           473.333333
02                                426.619092           444.186256
03                                428.529851           437.997512
04                                402.142857           416.285714
05                                427.159915           438.236674

             SAT Writing Avg. Score    sat_score  AP Test Takers   \
school_dist
01                       439.333333  1354.500000       116.681090
02                       424.832836  1295.638184       128.908454
03                       426.915672  1293.443035       156.183494
04                       405.714286  1224.142857       129.016484
05                       419.666098  1285.062687        85.722527

             Total Exams Taken  Number of Exams with scores 3 4 or 5  \
school_dist
01                  173.019231                            135.800000
02                  201.516827                            157.495833
03                  244.522436                            193.087500
04                  183.879121                            151.035714
05                  115.725275                            142.464286

             Total Cohort  CSD  NUMBER OF STUDENTS / SEATS FILLED    ...      \
school_dist                                                          ...
01              93.500000  1.0                         115.244241    ...
02             158.647849  2.0                         149.818949    ...
03             183.384409  3.0                         156.005994    ...
04             113.857143  4.0                         132.362265    ...
05             143.677419  5.0                         120.623901    ...

             grade_span_max  expgrade_span_max           zip  total_students  \
school_dist
01                     12.0               12.0  10003.166667      659.500000
02                     12.0               12.0  10023.770833      621.395833
03                     12.0               12.0  10023.750000      717.916667
04                     12.0               12.0  10029.857143      580.857143
05                     12.0               12.0  10030.142857      609.857143

             number_programs  priority08  priority09  priority10        lat  \
school_dist
01                  1.333333         0.0         0.0         0.0  40.719022
02                  1.416667         0.0         0.0         0.0  40.739699
03                  2.000000         0.0         0.0         0.0  40.781574
04                  1.142857         0.0         0.0         0.0  40.793449
05                  1.142857         0.0         0.0         0.0  40.817077

                   lon
school_dist
01          -73.982377
02          -73.991386
03          -73.977370
04          -73.943215
05          -73.949251

[5 rows x 67 columns]
----------------------
----------------------
----------------------
  school_dist  SAT Critical Reading Avg. Score  SAT Math Avg. Score  \
0          01                       441.833333           473.333333
1          02                       426.619092           444.186256
2          03                       428.529851           437.997512
3          04                       402.142857           416.285714
4          05                       427.159915           438.236674

   SAT Writing Avg. Score    sat_score  AP Test Takers   Total Exams Taken  \
0              439.333333  1354.500000       116.681090         173.019231
1              424.832836  1295.638184       128.908454         201.516827
2              426.915672  1293.443035       156.183494         244.522436
3              405.714286  1224.142857       129.016484         183.879121
4              419.666098  1285.062687        85.722527         115.725275

   Number of Exams with scores 3 4 or 5  Total Cohort  CSD    ...      \
0                            135.800000     93.500000  1.0    ...
1                            157.495833    158.647849  2.0    ...
2                            193.087500    183.384409  3.0    ...
3                            151.035714    113.857143  4.0    ...
4                            142.464286    143.677419  5.0    ...

   grade_span_max  expgrade_span_max           zip  total_students  \
0            12.0               12.0  10003.166667      659.500000
1            12.0               12.0  10023.770833      621.395833
2            12.0               12.0  10023.750000      717.916667
3            12.0               12.0  10029.857143      580.857143
4            12.0               12.0  10030.142857      609.857143

   number_programs  priority08  priority09  priority10        lat        lon
0         1.333333         0.0         0.0         0.0  40.719022 -73.982377
1         1.416667         0.0         0.0         0.0  40.739699 -73.991386
2         2.000000         0.0         0.0         0.0  40.781574 -73.977370
3         1.142857         0.0         0.0         0.0  40.793449 -73.943215
4         1.142857         0.0         0.0         0.0  40.817077 -73.949251

[5 rows x 68 columns]
"""


"""
9: Plotting Ell_percent By District
Now that we've taken the mean of all the columns, we can plot out ell_percent by district.
Not only did we find the mean of ell_percent, we also took the mean of the lon and lat columns, which will give us the coordinates for the center of each district.

Instructions
Setup the map using the code snippet from before that creates the map and draws rivers, coastlines, and boundaries.
Convert the lon column of districts to a list, and assign it to the longitudes variable.
Convert the lat column of districts to a list, and assign it to the latitudes variable.
Call the scatter method on m, and pass in longitudes and latitudes as arguments.
Make sure to pass in longitudes and latitudes in the right order.
Pass in the keyword argument s=50 to increase the size of the points in the scatterplot.
Pass in the keyword argument zorder=2 to plot the points on top of the rest of the map. Otherwise the points will show up underneath the land.
Pass in the keyword argument latlon=True to indicate that we're passing in latitude and longitude coordinates, not axis coordinates.
Pass in the keyword argument c, with the value districts["ell_percent"] to plot the ell_percent.
Pass in the keyword argument cmap="summer" to get the right color scheme.
Show the plot using the show method.
"""
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

m = Basemap(
    projection='merc',
    llcrnrlat=40.496044,
    urcrnrlat=40.915256,
    llcrnrlon=-74.255735,
    urcrnrlon=-73.700272,
    resolution='i'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

longitudes = districts["lon"].tolist()
latitudes = districts["lat"].tolist()

m.scatter(longitudes,latitudes,s=50,zorder=2,latlon=True,c=districts["ell_percent"],cmap="summer")
plt.show()
""" Console Outputs or Results
see plot5.png
"""



"""
10: Next Steps
We've now found correlations, created visualizations, and mapped out our schools!
We now have all the tools we need to analyze this data in more depth.

Along the way, we've learned:

How to create school and district-level maps.
How to find correlations, and what they mean.
Why we should plot out data instead of only relying on the r-value.
That ell_percent correlates strongly negatively with sat_score.
We're now able to analyze and explain quirks in datasets. This is a critical part of any data science job.

Up next is a guided project where we'll use the tools we've developed in this mission to do more in-depth analysis of the New York City high school data.
"""
