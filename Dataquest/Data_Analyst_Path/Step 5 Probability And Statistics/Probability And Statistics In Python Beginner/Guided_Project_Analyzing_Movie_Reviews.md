03/2017  
Dataquest : Data Analyst Path  
Step 5: Probability and Statistics  
SubStep : Probability and Statistics in Python: Beginner : Guided Project: Analyzing Movie Reviews  
samedi, 18. mars 2017 07:11 


---
# 1: Movie Reviews  

In this project, you'll be working with Jupyter notebook, and analyzing data on movie review scores. By the end, you'll have a notebook that you can add to your portfolio or build on top of on your own. If you need help at any point, you can consult our solution notebook here.  

The dataset is stored in the fandango_score_comparison.csv file. It contains information on how major movie review services rated movies. The data originally came from FiveThirtyEight.  

Here are the first few rows of the data, in CSV format:  

	FILM	RottenTomatoes	Metacritic	IMDB	Fandango_Stars	RT_norm	RT_user_norm	Fandango_votes
	0	Avengers: Age of Ultron (2015)	74	86	7.1	7.8	4.5	3.70	271107
	1	Cinderella (2015)	85	80	7.5	7.1	4.5	4.25	65709
	2	Ant-Man (2015)	80	90	8.1	7.8	4.5	4.00	103660
	3	Do You Believe? (2015)	18	84	4.7	5.4	4.5	0.90	3136
	4	Hot Tub Time Machine 2 (2015)	14	28	3.4	5.1	3.0	0.70	19560
	
Each row represents a single movie. Each column contains information about how the online moview review services RottenTomatoes, Metacritic, IMDB, and Fandango rated the movie. The dataset was put together to help detect bias in the movie review sites. Each of these sites has 2 types of score -- User scores, which aggregate user reviews, and Critic score, which aggregate professional critical reviews of the movie. Each service puts their ratings on a different scale:  

- RottenTomatoes - 0-100, in increments of 1.
- Metacritic - 0-100, in increments of 1.
- IMDB - 0-10, in increments of .1.
- Fandango - 0-5, in increments of .5.

Typically, the primary score shown by the sites will be the Critic score. Here are descriptions of some of the relevant columns in the dataset:  

- FILM -- the name of the movie.
- RottenTomatoes -- the RottenTomatoes (RT) critic score.
- RottenTomatoes_User -- the RT user score.
- Metacritic -- the Metacritic critic score.
- Metacritic_User -- the Metacritic user score.
- IMDB -- the IMDB score given to the movie.
- Fandango_Stars -- the number of stars Fandango gave the movie.

To make it easier to compare scores across services, the columns were normalized so their scale and rounding matched the Fandango ratings. Any column with the suffix _norm is the corresponding column changed to a 0-5 scale. For example, RT_norm takes the RottenTomatoes column and turns it into a 0-5 scale from a 0-100 scale. Any column with the suffix _round is the rounded version of another column. For example, RT_user_norm_round rounds the RT_user_norm column to the nearest .5.  


#### Instructions :

 - Read fandango_score_comparison.csv into a Dataframe named movies.
 - Display the movies DataFrame by just typing the variable name and running the code cell.
 - If you're unfamiliar with RottenTomatoes, Metacritic, IMDB, or Fandango, visit the websites to get a better handle on their review methodology.
 
```python
#1: Movie Reviews
import pandas as pd
movies = pd.read_csv("fandango_score_comparison.csv")
movies
```  

---
# 2: Histograms  

Now that you've read the dataset in, you can do some statistical exploration of the ratings columns. We'll primarily focus on the Metacritic_norm_round and the Fandango_Stars columns, which will let you see how Fandango and Metacritic differ in terms of review scores.  


#### Instructions :

 - Enable plotting in Jupyter notebook with import matplotlib.pyplot as plt and run the following magic %matplotlib inline.
 - Create a histogram of the Fandango_Stars column.
- Look critically at both histograms, and write up any differences you see in a markdown cell.
 
```python
#2: Histograms
import matplotlib.pyplot as plt
%matplotlib inline
plt.hist(movies["Fandango_Stars"])
plt.hist(movies["Metacritic_norm_round"])
```  

#### Results :  

see img/img60.png
see img/img61.png

---
# 3: Mean, Median, And Standard Deviation  

In the last screen, you may have noticed some differences between the Fandango and Metacritic scores. Metrics we've covered, including the mean, median, and standard deviation, allow you to quantify these differences. You can apply these metrics to the Fandango_Stars and Metacritic_norm_round columns to figure out how different they are.   


#### Instructions :

 - Calculate the mean of both Fandango_Stars and Metacritic_norm_round.
 - Calculate the median of both Fandango_Stars and Metacritic_norm_round.
 - Calculate the standard deviation of both Fandango_Stars and Metacritic_norm_round. You can use the numpy.std method to find this.
 - Print out all the values and look over them.
 - Look at the review methodologies for Metacritic and Fandango. You can find the metholodogies on their websites, or by using Google. Do you see any major differences? Write them up in a markdown cell.
 - Write up the differences in numbers in a markdown cell, including the following:
	- Why would the median for Metacritic_norm_round be lower than the mean, but the median for Fandango_Stars is higher than the mean? Recall that the mean is usually larger than the median when there are a few large values in the data, and lower when there are a few small values.
	- Why would the standard deviation for Fandango_Stars be much lower than the standard deviation for Metacritic_norm_round?
	- Why would the mean for Fandango_Stars be much higher than the mean for Metacritic_norm_round.
 
```python
#3: Mean, Median, And Standard Deviation
mean_fangado = movies["Fandango_Stars"].mean()
mean_metacritic = movies["Metacritic_norm_round"].mean()
print("Mean Fandango_Stars : ",mean_fangado)
print("Mean Metacritic_norm_round : ",mean_metacritic)
print("-------------")
median_fangado = movies["Fandango_Stars"].median()
median_metacritic = movies["Metacritic_norm_round"].median()
print("Median Fandango_Stars : ",median_fangado)
print("Median Metacritic_norm_round : ",median_metacritic)
print("-------------")
std_fangado = np.std(movies["Fandango_Stars"])
std_metacritic = np.std(movies["Metacritic_norm_round"])
print("Std Fandango_Stars : ",std_fangado)
print("Std Metacritic_norm_round : ",std_metacritic)
print("-------------")
```  

#### Results :  

	Mean Fandango_Stars :  4.08904109589
	Mean Metacritic_norm_round :  2.97260273973
	-------------
	Median Fandango_Stars :  4.0
	Median Metacritic_norm_round :  3.0
	-------------
	Std Fandango_Stars :  0.53853216127
	Std Metacritic_norm_round :  0.987561029704
	-------------

---
# 4: Scatter Plots  

We know the ratings tend to differ, but we don't know which movies tend to be the largest outliers. You can find this by making a scatterplot, then looking at which movies are far away from the others.  

You can also subtract the Fandango_Stars column from the Metacritic_norm_round column, take the absolute value, and sort movies based on the difference to find the movies with the largest differences between their Metacritic and Fandango ratings.  


#### Instructions :

 - Make a scatterplot that compares the Fandango_Stars column to the Metacritic_norm_round column.
 - Several movies appear to have low ratings in Metacritic and high ratings in Fandango, or vice versa. We can explore this further by finding the differences between the columns.
	- Subtract the Fandango_Stars column from the Metacritic_norm_round column, and assign to a new column, fm_diff, in movies.
	- Assign the absolute value of fm_diff to fm_diff. This will ensure that we don't only look at cases where Metacritic_norm_round is greater than Fandango_Stars.
You can calculate absolute values with the absolute function in NumPy.
	- Sort movies based on the fm_diff column, in descending order.
	- Print out the top 5 movies with the biggest differences between Fandango_Stars and Metacritic_norm_round.
 
```python
#4: Scatter Plots
plt.scatter(movies["Fandango_Stars"],movies["Metacritic_norm_round"])
movies["fm_diff"] = movies["Metacritic_norm_round"]-movies["Fandango_Stars"]
movies["fm_diff"] = abs(movies["fm_diff"])
movies = movies.sort_values("fm_diff",ascending=False)
print(movies.head())
```  

#### Results :  

	see img/img62.png
		                FILM  RottenTomatoes  RottenTomatoes_User  Metacritic  \
	3     Do You Believe? (2015)              18                   84          22   
	85         Little Boy (2015)              20                   81          30   
	47              Annie (2014)              27                   61          33   
	19             Pixels (2015)              17                   54          27   
	134  The Longest Ride (2015)              31                   73          33   

	     Metacritic_User  IMDB  Fandango_Stars  Fandango_Ratingvalue  RT_norm  \
	3                4.7   5.4             5.0                   4.5     0.90   
	85               5.9   7.4             4.5                   4.3     1.00   
	47               4.8   5.2             4.5                   4.2     1.35   
	19               5.3   5.6             4.5                   4.1     0.85   
	134              4.8   7.2             4.5                   4.5     1.55   

	     RT_user_norm   ...     RT_norm_round  RT_user_norm_round  \
	3            4.20   ...               1.0                 4.0   
	85           4.05   ...               1.0                 4.0   
	47           3.05   ...               1.5                 3.0   
	19           2.70   ...               1.0                 2.5   
	134          3.65   ...               1.5                 3.5   

	     Metacritic_norm_round  Metacritic_user_norm_round  IMDB_norm_round  \
	3                      1.0                         2.5              2.5   
	85                     1.5                         3.0              3.5   
	47                     1.5                         2.5              2.5   
	19                     1.5                         2.5              3.0   
	134                    1.5                         2.5              3.5   

	     Metacritic_user_vote_count  IMDB_user_vote_count  Fandango_votes  \
	3                            31                  3136            1793   
	85                           38                  5927             811   
	47                          108                 19222            6835   
	19                          246                 19521            3886   
	134                          49                 25214            2603   

	     Fandango_Difference  fm_diff  
	3                    0.5      4.0  
	85                   0.2      3.0  
	47                   0.3      3.0  
	19                   0.4      3.0  
	134                  0.0      3.0  

	[5 rows x 23 columns]

---
# 5: Correlations 

Let's see what the correlation coefficient between Fandango_Stars and Metacritic_norm_round is. This will help you determine if Fandango consistently has higher scores than Metacritic, or if only a few movies were assigned higher ratings.  
 
You can then create a linear regression to see what the predicted Fandango score would be based on the Metacritic score.  


#### Instructions :

 - Calculate the r-value measuring the correlation between Fandango_Stars and Metacritic_norm_round using the scipy.stats.pearsonr function.
 - The correlation is actually fairly low. Write up a markdown cell that discusses what this might mean.
 - Use the scipy.stats.linregress function create a linear regression with Metacritic_norm_round as the x-values and Fandango_Stars as the y-values.
 - Predict what a movie that got a 3.0 in Metacritic would get on Fandango using the formula pred_3 = 3 * slope + intercept.
 
```python
#5: Correlations
from scipy.stats import pearsonr
from scipy.stats import linregress
y = movies["Fandango_Stars"]
x = movies["Metacritic_norm_round"]
r_value, p_value = pearsonr(x,y)
slope, intercept, r_value, p_value, std_err = linregress(x,y)
pred_3 = 3 * slope + intercept

print("R between Fandango_Stars and Metacritic_norm_round : ",r_value)
print("Slope (x or m) : ",slope)
print("Intercept (b) : ",intercept)
print("Predict for 3 in Metacritic would : ",pred_3)
```  

#### Results :  

	R between Fandango_Stars and Metacritic_norm_round :  0.178449190739
	Slope (x or m) :  0.0973110779739
	Intercept (b) :  3.7997739189
	Predict for 3 in Metacritic would :  4.09170715282

---
# 6: Finding Residuals  

In the last screen, you created a linear regression for relating Metacritic_norm_round to Fandango_Stars. You can create a residual plot to better visualize how the line relates to the existing datapoints. This can help you see if two variables are linearly related or not.  


#### Instructions :

 - Predict what a movie that got a 1.0 in Metacritic would get on Fandango using the line from the last screen.
 - Predict what a movie that got a 5.0 in Metacritic would get on Fandango using the line from the last screen.
 - Make a scatter plot using the scatter function in matplotlib.pyplot.
 - On top of the scatter plot, use the plot function in matplotlib.pyplot to plot a line using the predicted values for 1.0 and 5.0.
	- Setup the x values as the list [1.0, 5.0].
	- The y values should be a list with the corresponding predictions.
	- Pass in both x and y to plot to create a line.
 - Set the x-limits of the plot to 1 and 5 using the pyplot.xlim() method.
 - Show the plot.
 
```python
#6: Finding Residuals
pred_1 = 1 * slope + intercept
pred_5 = 5 * slope + intercept
plt.scatter(movies["Metacritic_norm_round"],movies["Fandango_Stars"])
plt.plot([1.0, 5.0],[pred_1,pred_5])
plt.xlim(1,5)
```  

#### Results :  

see img/img63.png

---
# 7: Next Steps

That's it for the guided steps! We recommend exploring the data more on your own.  

Here are some potential next steps:  

- Explore the other rating services, IMDB and RottenTomatoes.
	- See how they differ from each other.
	- See how they differ from Fandango.
- See how user scores differ from critic scores.
- Acquire more recent review data, and see if the pattern of Fandango inflating reviews persists.
- Dig more into why certain movies had their scores inflated more than others.

We recommend creating a Github repository and placing this project there. It will help other people, including employers, see your work. As you start to put multiple projects on Github, you'll have the beginnings of a strong portfolio.  

You're welcome to keep working on the project here, but we recommend downloading it to your computer using the download icon above and working on it there.  

We hope this guided project has been a good experience, and please email us at hello@dataquest.io if you want to share your work!  


#### Instructions :

 - 
 
```python

```  

#### Results :  



---
# 1: Exploring The Data  


#### Instructions :

 - 
 
```python

```  

#### Results :  




---
# 1: Exploring The Data  


#### Instructions :

 - 
 
```python

```  

#### Results :  


---
# 1: Exploring The Data  


#### Instructions :

 - 
 
```python

```  

#### Results :  



---
# 1: Exploring The Data  


#### Instructions :

 - 
 
```python

```  

#### Results :  



---
# 1: Exploring The Data  


#### Instructions :

 - 
 
```python

```  

#### Results :  

