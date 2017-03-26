03/2017  
Dataquest : Data Analyst Path  
Step 5: Probability and Statistics  
SubStep : Probability and Statistics in Python: Beginner : Challenge Descriptive Statistics  
vendredi, 17. mars 2017 11:25


---
# 1: Introduction  

In this challenge, you'll practice the statistical techniques you learned in the previous missions. These techniques are referred to collectively as descriptive statistics since they're used to describe and understand a dataset and not directly for prediction.  

The FiveThirtyEight team recently released a dataset containing the critics scores for a sample of movies that have substantive (at least 30) user and critic reviews from IMDB, Rotten Tomatoes, Metacritic, IMDB, and Fandango. Whenever a movie is released, movie review sites ask their approved network of critics and their site's user base to rate the movie. These scores are aggregated and the average score from both groups are posted on their site for each movie.  

Here are links to the page for Star Trek Beyond for each site:  

 - Rotten Tomatoes
 - Fandango
 - Metacritic
 - IMDB

The dataset contains information on most movies from 2014 and 2015 and was used to help the team at FiveThirtyEight explore Fandango's suspiciously high ratings. You can read their analysis here.  

You'll be working with the file fandango_score_comparison.csv, which you can download from their Github repo. Here are some of the columns in the dataset:  

 - FILM - film name.
 - RottenTomatoes - Rotten Tomatoes critics average score.
 - RottenTomatoes_User - Rotten Tomatoes user average score.
 - RT_norm - Rotten Tomatoes critics average score (normalized to a 0 to 5 point scale).
 - RT_user_norm - Rotten Tomatoes user average score (normalized to a 0 to 5 point scale).
 - Metacritic - Metacritic critics average score.
 - Metacritic_user_nom - Metacritic user average score (normalized to a 0 to 5 point scale).
 - Metacritic_norm - Metacritic critics average score (normalized to a 0 to 5 point scale).
 - Fandango_Ratingvalue - Fandango user average score (0 to 5 stars).
 - IMDB_norm - IMDB user average score (normalized to a 0 to 5 point scale).

The full column list and descriptions are available at FiveThirtyEight's Github repo. Let's focus on the normalized user scores for now and generate histograms to better understand each site's distributions.    

#### Instructions :

 - Create a matplotlib subplot grid with the following properties:
	- 4 rows by 1 column,
	- figsize of 5 (width) by 12 (height),
	- each Axes instance should have an x-value range of 0.0 to 5.0.
 - Generate the following histograms:
	- First plot (top most): Histogram of normalized Rotten Tomatoes scores by users.
	- Second plot: Histogram of normalized Metacritic scores by users.
	- Third plot: Histogram of Fandango scores by users.
	- Fourth plot (bottom most): Histogram of IMDB scores by users.

```python
import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")

fig = plt.figure(figsize=(5, 12))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)
ax1.set_xlim(0, 5)
ax2.set_xlim(0, 5)
ax3.set_xlim(0, 5)
ax4.set_xlim(0, 5)

#ax1.hist(movie_reviews["RT_user_norm"])
#ax2.hist(movie_reviews["Metacritic_user_nom"])
#ax3.hist(movie_reviews["Fandango_Ratingvalue"])
#ax4.hist(movie_reviews["IMDB_norm"])

movie_reviews["RT_user_norm"].hist(ax=ax1)
movie_reviews["Metacritic_user_nom"].hist(ax=ax2)
movie_reviews["Fandango_Ratingvalue"].hist(ax=ax3)
movie_reviews["IMDB_norm"].hist(ax=ax4)

plt.show()
```  

#### Results :  

see img/img35.png

---
# 2: Mean  

The most obvious things that stick out is that essentially all of the Fandango average user reviews are greater than 3 on a 5 point scale. The distributions of the Rotten Tomatoes and Metacritic scores, on the other hand, more closely resemble a normal distribution, which is generally what you'd expect if you knew nothing else. This is because the normal distribution is the most common distribution in nature and is used to approximate many phenomenon. Starting with the assumption that a phemonenon is normal is incredibly common, especially when you don't have a clear generative model to understand how the data was generated.  

Now that you hopefully have some visual understanding of these scores, let's calculate some statistical measures to see how the properties the histograms suggested are reflected in numerical values. Let's focus on just the normalized user reviews in this mission.    

#### Instructions :

 - Write a function, named calc_mean, that returns the mean for the values in a Series object.
	- Recall that you can return the values in a Series using the values attribute.

Select just the columns containing normalized user reviews and assign to a separate Dataframe named user_reviews. Those columns are: RT_user_norm, Metacritic_user_nom, Fandango_Ratingvalue, IMDB_norm.  

Use the Dataframe method apply to apply the calc_mean function over the filtered Dataframe user_reviews.  

 - Assign the mean of RT_user_norm to rt_mean.
 - Assign the mean of Metacritic_user_nom to mc_mean.
 - Assign the mean of Fandango_Ratingvalue to fg_mean.
 - Assign the mean of IMDB_norm to id_mean.
 - Use the variables display below the code output window or print statements to observe each value.

```python
def calc_mean(serie):
    vals = serie.values
    return sum(vals)/len(vals)

user_reviews = movie_reviews[["RT_user_norm","Metacritic_user_nom","Fandango_Ratingvalue","IMDB_norm"]]

rt_mean = calc_mean(user_reviews["RT_user_norm"])
mc_mean = calc_mean(user_reviews["Metacritic_user_nom"])
fg_mean = calc_mean(user_reviews["Fandango_Ratingvalue"])
id_mean = calc_mean(user_reviews["IMDB_norm"])

print("Rotten Tomatoes (mean):", rt_mean)
print("Metacritic (mean):", mc_mean)
print("Fandango (mean):",fg_mean)
print("IMDB (mean):",id_mean)

# or Dataquest solution :

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean    

columns = ["RT_user_norm", "Metacritic_user_nom", "Fandango_Ratingvalue", "IMDB_norm"]
user_reviews = movie_reviews[columns]
user_reviews_means = user_reviews.apply(calc_mean)

rt_mean = user_reviews_means["RT_user_norm"]
mc_mean = user_reviews_means["Metacritic_user_nom"]
fg_mean = user_reviews_means["Fandango_Ratingvalue"]
id_mean = user_reviews_means["IMDB_norm"]

print("Rotten Tomatoes (mean):", rt_mean)
print("Metacritic (mean):", mc_mean)
print("Fandango (mean):",fg_mean)
print("IMDB (mean):",id_mean)
```  

#### Results :  

	Output
	Rotten Tomatoes (mean): 3.19383561644
	Metacritic (mean): 3.2595890411
	Fandango (mean): 3.84520547945
	IMDB (mean): 3.36849315068


---
# 3: Variance And Standard Deviation  

It seems like the Fandango user reviews have the highest mean and skew the most towards to the higher end compared to the other review sites. Let's now calculate variance and standard deviation to better understand the spreads.   

#### Instructions :

 - To calculate the variance:
	- write a function, named calc_variance, that returns the variance for the values in a Series object.
 - To calculate the standard deviation:
	- use the output of the calc_variance function since standard deviation is a simple calculation away from variance.
 - Calculate the variance and standard deviation for the RT_user_norm column and assign to rt_var and rt_stdev respectively.
 - Calculate the variance and standard deviation for the Metacritic_user_nom column and assign to mc_var and mc_stdev respectively.
 - Calculate the variance and standard deviation for the Fandango_Ratingvalue column and assign to fg_var and fg_stdev respectively.
 - Calculate the variance and standard deviation for the IMDB_norm column and assign to id_var and id_stdev respectively.
 - Use the variables display below the code output window or print statements to observe each value.

```python
def calc_variance(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    variance = 0
    for s in vals:
        difference = s - mean
        square_difference = difference ** 2
        variance += square_difference
    return variance / len(vals)

def calc_std(var):
    return var ** (1/2)


rt_var = calc_variance(user_reviews["RT_user_norm"])
rt_stdev = calc_std(rt_var)

mc_var = calc_variance(user_reviews["Metacritic_user_nom"])
mc_stdev = calc_std(mc_var)

fg_var = calc_variance(user_reviews["Fandango_Ratingvalue"])
fg_stdev = calc_std(fg_var)

id_var = calc_variance(user_reviews["IMDB_norm"])
id_stdev = calc_std(id_var)

print("RT_user_norm (Mean)",rt_var)
print("RT_user_norm (Std)",rt_stdev)
print("-----------------")
print("Metacritic_user_nom (Mean)",mc_var)
print("Metacritic_user_nom (Std)",mc_stdev)
print("-----------------")
print("Fandango_Ratingvalue (Mean)",fg_var)
print("Fandango_Ratingvalue (Std)",fg_stdev)
print("-----------------")
print("IMDB_norm (Mean)",id_var)
print("IMDB_norm (Std)",id_stdev)
print("-----------------")
```  

#### Results :  

	Output
	RT_user_norm (Mean) 0.995578438731
	RT_user_norm (Std) 0.997786770173
	-----------------
	Metacritic_user_nom (Mean) 0.566654625633
	Metacritic_user_nom (Std) 0.752764654878
	-----------------
	Fandango_Ratingvalue (Mean) 0.251107149559
	Fandango_Ratingvalue (Std) 0.501105926486
	-----------------
	IMDB_norm (Mean) 0.228219647213
	IMDB_norm (Std) 0.47772340032
	-----------------


---
# 4: Scatter Plots  

The mean and variance values you calculated in the last screens should match the visual intuition the histograms gave you. Rotten Tomatoes and Metacritic have more spread out scores (high variance) and the mean is around 3. Fandango, on the other hand, has low spread (low variance) and a much higher mean, which could imply that the site has a strong bias towards higher reviews. IMDB is somewhere in the middle, with a low variance, like Fandango's user reviews, but a much more moderate mean value.  

So it seems like something is especially fishy about Fandango's ratings, which was the inspiration behind the FiveThirtyEight post to begin with. Since Fandango's main business is selling movie tickets, it's possible their primary incentive may differ from pure review sites like Rotten Tomatoes or Metacritic.  

Let's now explore if Fandango's user ratings are at least relatively correct. More precisely, are movies that are highly rated on Rotten Tomatoes, IMDB, and Metacritic also highly rated on Fandango?  

We can accomplish that by understanding how Fandango's scores and related to scores from Rotten Tomatoes and Metacritic. First things first, let's get a visual sense by generating scatter plots.    

#### Instructions :

 - Create a matplotlib subplot grid with the following properties:
	- 3 rows by 1 column,
	- figsize of 4 (width) by 8 (height),
	- each Axes instance should have an x-value range of 0.0 to 5.0.
 - Generate the following scatter plot (y-axis vs x-axis):
	- First plot (top most): Fandango user reviews vs. Rotten Tomatoes user reviews.
	- Second plot: Fandango user reviews vs. Metacritic user reviews.
	- Third plot (bottom most): Fandango user reviews vs. IMDB user reviews.

```python
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure(figsize=(4, 8))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)
ax1.set_xlim(0, 5)
ax2.set_xlim(0, 5)
ax3.set_xlim(0, 5)


ax1.scatter(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
ax2.scatter(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
ax3.scatter(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

plt.show()
```  

#### Results :  

see img/img36.png


---
# 5: Covariance  

It seems like Rotten Tomatoes and IMDB user reviews correlate the most with Fandango user reviews while Metacritic only weakly correlates. Let's write a function that to calculates the covariance values in this screen and a function to calculate the correlation values in the next screen.  

Here's the formula for computing the covariance between 2 variables: cov(x,y)=∑ni=1(xi−x¯)(yi−y¯)ncov(x,y)=∑i=1n(xi−x¯)(yi−y¯)n.    

#### Instructions :

 - Write a function, named calc_covariance, that computes the covariance between the values of 2 Series objects.

 Use the calc_covariance function you wrote to:  

 - Compute the covariance between the RT_user_norm and Fandango_Ratingvalue columns. Assign the result to rt_fg_covar.
 - Compute the covariance between the Metacritic_user_nom and Fandango_Ratingvalue columns. Assign the result to mc_fg_covar.
 - Compute the covariance between the IMDB_norm and Fandango_Ratingvalue columns. Assign the result to id_fg_covar.
 - Use the variables display below the code output window or print statements to observe each value.

```python
import numpy as np

def calc_covariance(x,y):
    sx = x.values
    sy = y.values
    x_mean = np.mean(sx)
    y_mean = np.mean(sy)
    x_len = len(sx)
    sumofxy = 0
    for i in range(0,x_len):
        sumofxy += (sx[i]-x_mean)*(sy[i]-y_mean)

    cov = sumofxy / x_len
    return cov

rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"],movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"],movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"],movie_reviews["Fandango_Ratingvalue"])

print("covariance between the RT_user_norm and Fandango_Ratingvalue : ",rt_fg_covar)
print("covariance between the Metacritic_user_nom and Fandango_Ratingvalue : ",mc_fg_covar)
print("covariance between the IMDB_norm and Fandango_Ratingvalue : ",id_fg_covar)

#or Dataquest Solution

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean
def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

print("Covariance between Rotten Tomatoes and Fandango:", rt_fg_covar)
print("Covariance between Metacritic and Fandango", mc_fg_covar)
print("Covariance between IMDB and Fandango", id_fg_covar)
```  

#### Results :  

	Output
	covariance between the RT_user_norm and Fandango_Ratingvalue :  0.362162225558
	covariance between the Metacritic_user_nom and Fandango_Ratingvalue :  0.127100769375
	covariance between the IMDB_norm and Fandango_Ratingvalue :  0.143718802777


---
# 6: Correlation  

Interestingly, Rotten Tomatoes covaries strongly with Fandango (0.36) compared to Metacritic (0.13) and IMDB (0.14). Finally, let's calculate the correlation values by using the calc_covariance a function from the previous step.  

Here's the full formula for correlation:  

see img/img37.png  
cov(x,y)σxσycov(x,y)σxσy.

where cov is shorthand for the covariance function, and σσ represents the standard deviation.   

#### Instructions :

 - Write a function, named calc_correlation, that uses the calc_covariance and calc_variance functions to calculate the correlation for 2 Series objects. The function should have 2 parameters, one for each Series object.
 - Compute the correlation between the RT_user_norm and Fandango_Ratingvalue columns and assign the result to rt_fg_corr.
 - Compute the correlation between the Metacritic_user_nom and Fandango_Ratingvalue columns and assign the result to mc_fg_corr.
 - Compute the correlation between the IMDB_norm and Fandango_Ratingvalue columns and assign the result to id_fg_corr.
Use the variables display below the code output window or print statements to observe each value.

```python
def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

def calc_correlation(series_one, series_two):
    cov = calc_covariance(series_one, series_two)
    std1 = calc_variance(series_one) ** (1/2)
    std2 = calc_variance(series_two) ** (1/2)
    corr =  cov / (std1 * std2)
    return corr
    
rt_fg_corr = calc_correlation(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_corr = calc_correlation(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_corr = calc_correlation(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

print("correlation between the RT_user_norm and Fandango_Ratingvalue : ",rt_fg_corr)
print("correlation between the Metacritic_user_nom and Fandango_Ratingvalue : ",mc_fg_corr)
print("correlation between the IMDB_norm and Fandango_Ratingvalue : ",id_fg_corr)

```  

#### Results :  

	Output
	correlation between the RT_user_norm and Fandango_Ratingvalue :  0.724328994249
	correlation between the Metacritic_user_nom and Fandango_Ratingvalue :  0.336945314265
	correlation between the IMDB_norm and Fandango_Ratingvalue :  0.600354177263


---
# 7: Next Steps  

As the scatter plots suggested, Rotten Tomatoes and IMDB correlate the strongest with Fandango, with correlation values of 0.72 and 0.60 respectively. Metacritic, on the other hand, only has a correlation value of 0.34 with Fandango. While covariance and correlation values may seem complicated to compute and hard to reason with, their best use case is in comparing relationships like we did in this challenge.  

In the next mission, we'll explore the basics of linear regression, which is a powerful machine learning technique.   