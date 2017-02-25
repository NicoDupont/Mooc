"""
02/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Data Cleaning : Guided Project: Analyzing NYC High School Data
"""


"""
1: Introduction
In the last three missions, we explored the relationship between SAT scores and demographic factors in New York City public schools.
For a brief bit of background, the SAT, or Scholastic Aptitude Test, is a test given to graduating high schoolers in the US every year.
The SAT has 3 sections, each of which is worth a maximum of 800 points. The SAT is used by colleges to determine which students to admit.
High average SAT scores are usually indicative of a good school.

New York City has published data on the SAT scores of students, along with additional demographic datasets.
In the last three missions, we combined the following datasets into a single, clean, Pandas Dataframe:

SAT scores by school -- SAT scores for each high school in New York City.
School attendance -- attendance information on every school in NYC.
Class size -- class size information for each school in NYC.
AP test results -- Advanced Placement exam results for each high school. Passing AP exams can get you college credit in the US.
Graduation outcomes -- percentage of students who graduated, and other outcome information.
Demographics -- demographic information for each school.
School survey -- surveys of parents, teachers, and students at each school.
New York City has a significant immigrant population, and is very diverse, so comparing demographic factors such as race, income, and gender with SAT scores is a good way to figure out if the SAT is a fair test.
If certain racial groups consistently performed better on the SAT, we would have some evidence that the SAT is unfair, for example.

In the last mission, we started doing some analysis. We'll extend that analysis in this mission.
As you can see, we've included the code to read in all of the data, combine it, and create correlations in the notebook.
If you want to see the finish notebook, with solutions to all the steps, you can find it here.

The Dataframe combined contains all of our data, and is what we'll be using in our analysis.

Instructions
Setup matplotlib to work in Jupyter notebook.
There are several fields in combined that originally came from a survey of parents, teachers, and students.
Make a bar plot of the correlations between these fields and sat_score.
You can find a list of the fields in the survey_fields variable in the notebook.
Consult the data dictionary that is part of the zip file that you can download here.
Are there any surprising correlations that you found?
Write up your results in a markdown cell.
"""
# 1: Introduction
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
%matplotlib inline
corfil = combined.corr()["sat_score"][survey_fields]
print(corfil)
corfil.plot.bar()
""" Console Outputs or Results
DBN                NaN
rr_s          0.232199
rr_t         -0.023386
rr_p          0.047925
N_s           0.423463
N_t           0.291463
N_p           0.421530
saf_p_11      0.122913
com_p_11     -0.115073
eng_p_11      0.020254
aca_p_11      0.035155
saf_t_11      0.313810
com_t_11      0.082419
eng_t_10           NaN
aca_t_11      0.132348
saf_s_11      0.337639
com_s_11      0.187370
eng_s_11      0.213822
aca_s_11      0.339435
saf_tot_11    0.318753
com_tot_11    0.077310
eng_tot_11    0.100102
aca_tot_11    0.190966
Name: sat_score, dtype: float64

see plot6.png

"""




"""
2: Safety And SAT Scores
In the last screen, you may have noticed that saf_t_11 and saf_s_11, both of which measure perceived safety at school, correlated highly with sat_score.
In this screen, we'll dig more into this relationship, and try to figure out which schools have low safety scores.

Instructions
Investigate safety scores.
Make a scatterplot of the saf_s_11 column vs the sat_score in combined.
Write a markdown cell of your conclusions about safety and SAT scores.
Map out safety scores.
Compute the average safety score for each district.
Make a map that shows safety scores by district.
Write a markdown cell of your conclusions about safety by area of New York City.
You may want to read up on the boroughs of New York City.
"""
# 2: Safety And SAT Scores
combined.plot.scatter(x="saf_s_11",y="sat_score")
# average safety score for each district and map
import numpy as np
districts = combined.groupby("school_dist").agg(np.mean)
districts.reset_index(inplace=True)

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

m.scatter(longitudes, latitudes, s=50, zorder=2, latlon=True, c=districts["saf_s_11"], cmap="summer")
plt.show()
""" Console Outputs or Results
see plot7.png
see plot8.png
"""




"""
3: Race And SAT Scores
There are a few columns that indicate the percentage of each race at a given school:

white_per
asian_per
black_per
hispanic_per
By plotting out the correlations between these columns and sat_score, we can see if there are any racial differences in SAT performance.

Instructions
Investigate racial differences in SAT scores.
Make a scatterplot of the correlations between the columns above and sat_score.
Write up a markdown cell containing your findings. Are there any unexpected correlations?
Explore schools with low SAT scores and a high hispanic_per.
Make a scatterplot of hispanic_per versus sat_score.
What does the scatterplot show? Write a markdown cell with any interesting observsations.
Research any schools with a greater than 95% hispanic_per.
Find the names of schools from the data.
Use Wikipedia and Google to research the names of the schools.
Is there anything interesting about these particular schools? Write up a markdown cell with your findings.
Research any schools with a less than 10% hispanic_per, and greater than 1800 average SAT score.
Find the names of schools from the data.
Use Wikipedia and Google to research the names of the schools.
Is there anything interesting about these particular schools? Write up a markdown cell with your findings.
"""
#3: Race And SAT Scores
race_fields = ["white_per", "asian_per", "black_per", "hispanic_per"]
combined.corr()["sat_score"][race_fields].plot.bar()
combined.plot.scatter(x="hispanic_per",y="sat_score")
hispanic_per95 = combined[combined["hispanic_per"] > 95]["SCHOOL NAME"]
print(hispanic_per95)
print("-----------------------")
print("-----------------------")
hispanic_per10 = combined[(combined["hispanic_per"] < 10) & (combined["sat_score"] > 1800)]["SCHOOL NAME"]
print(hispanic_per10)
""" Console Outputs or Results

see plot9.png
see plot10.png

44                         MANHATTAN BRIDGES HIGH SCHOOL
82      WASHINGTON HEIGHTS EXPEDITIONARY LEARNING SCHOOL
89     GREGORIO LUPERON HIGH SCHOOL FOR SCIENCE AND M...
125                  ACADEMY FOR LANGUAGE AND TECHNOLOGY
141                INTERNATIONAL SCHOOL FOR LIBERAL ARTS
176     PAN AMERICAN INTERNATIONAL HIGH SCHOOL AT MONROE
253                            MULTICULTURAL HIGH SCHOOL
286               PAN AMERICAN INTERNATIONAL HIGH SCHOOL
Name: SCHOOL NAME, dtype: object
-----------------------
-----------------------
37                                STUYVESANT HIGH SCHOOL
151                         BRONX HIGH SCHOOL OF SCIENCE
187                       BROOKLYN TECHNICAL HIGH SCHOOL
327    QUEENS HIGH SCHOOL FOR THE SCIENCES AT YORK CO...
356                  STATEN ISLAND TECHNICAL HIGH SCHOOL
Name: SCHOOL NAME, dtype: object



"""




"""
4: Gender And SAT Scores
There are two columns that indicate the percentage of each gender at a school:

male_per
female_per
We can plot out the correlations between each percentage and sat_score.

Instructions
Investigate gender differences in SAT scores.
Make a scatterplot of the correlations between the columns above and sat_score.
Write up a markdown cell containing your findings. Are there any unexpected correlations?
Investigate schools high SAT scores and a high female_per.
Make a scatterplot of female_per versus sat_score.
What does the scatterplot show? Write a markdown cell with any interesting observsations.
Research any schools with a greater than 60% female_per, and greater than 1700 average SAT score.
Find the names of schools from the data.
Use Wikipedia and Google to research the names of the schools.
Is there anything interesting about these particular schools? Write up a markdown cell with your findings.
"""
# 4: Gender And SAT Scores
Gender_fields = ["male_per", "female_per"]
combined.corr()["sat_score"][Gender_fields].plot.bar()
combined.plot.scatter(x="female_per", y="sat_score")
per60 = combined[(combined["female_per"] > 60) & (combined["sat_score"] > 1700)]["SCHOOL NAME"]
print(per60)

""" Console Outputs or Results
see plot11.png

5                         BARD HIGH SCHOOL EARLY COLLEGE
26                         ELEANOR ROOSEVELT HIGH SCHOOL
60                                    BEACON HIGH SCHOOL
61     FIORELLO H. LAGUARDIA HIGH SCHOOL OF MUSIC & A...
302                          TOWNSEND HARRIS HIGH SCHOOL
Name: SCHOOL NAME, dtype: object
"""




"""
5: AP Scores Vs SAT Scores
In the US, the Advanced Placement, or AP, exams, are exams that high schoolers take in order to gain college credit.
AP exams can be taken in many different subjects, and passing the AP exam means that colleges may grant you credits.

It makes sense that the number of students who took the AP exam in a school and SAT scores would be highly correlated, and let's dig into the relationship.
Since total_enrollment is highly correlated with sat_score, we don't want to bias our results, so we'll instead look at the percentage of students in each school who took at least one AP exam.

Instructions
Compute the percentage of students in each school that took the AP exam.
Divide the AP Test Takers column by the total_enrollment column.
The name AP Test Takers has a space at the end, don't forget to add it!
Assign the result to the ap_per column.
Investigate the relationship between AP scores and SAT scores.
Make a scatterplot of ap_per versus sat_score.
What does the scatterplot show? Write a markdown cell with any interesting observsations.
"""
# 5: AP Scores Vs SAT Scores
combined["ap_per"] = combined["AP Test Takers ] / combined["total_enrollment"]
combined.plot.scatter(x="ap_per", y="sat_score")
""" Console Outputs or Results
see plot12.png

"""




"""
6: Next Steps
We've done quite a bit of investigation into demographics and SAT scores in this guided project.
There's still quite a bit of analysis left to do, however. Here are some potential next steps:

Looking at class size and SAT scores.
Figuring out the best area to live in based on school performance.
If we combine this with a property values dataset, we could find the cheapest place where there are good school.
Looking into the differences between parent, teacher, and student responses to surveys.
Assigning a score to schools based on sat_score and other attributes.
We recommend creating a Github repository and placing this project there.
It will help other people, including employers, see your work.
As you start to put multiple projects on Github, you'll have the beginnings of a strong portfolio.

You're welcome to keep working on the project here, but we recommend downloading it to your computer using the download icon above and working on it there.

We hope this guided project has been a good experience, and please email us at hello@dataquest.io if you want to share your work!
"""

""" Console Outputs or Results

"""
