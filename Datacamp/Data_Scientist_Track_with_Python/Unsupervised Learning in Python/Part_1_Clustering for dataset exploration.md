11/2017  
# Datacamp - Unsupervised Learning in Python (Data Scientist Track with Python)  
[Unsupervised Learning in Python](https://www.datacamp.com/courses/unsupervised-learning-in-python)

---

***Course Description***  

Say you have a collection of customers with a variety of characteristics such as age, location, and financial history, and you wish to discover patterns and sort them into clusters. Or perhaps you have a set of texts, such as wikipedia pages, and you wish to segment them into categories based on their content. This is the world of unsupervised learning, called as such because you are not guiding, or supervising, the pattern discovery by some prediction task, but instead uncovering hidden structure from unlabeled data. Unsupervised learning encompasses a variety of techniques in machine learning, from clustering to dimension reduction to matrix factorization. In this course, you'll learn the fundamentals of unsupervised learning and implement the essential algorithms using scikit-learn and scipy. You will learn how to cluster, transform, visualize, and extract insights from unlabeled datasets, and end the course by building a recommender system to recommend popular musical artists.     
 
# Part 1 : Clustering for dataset exploration   

Learn how to discover the underlying groups (or "clusters") in a dataset. By the end of this chapter, you'll be clustering companies using their stock market prices, and distinguishing different species by clustering their measurements.    

## How many clusters?    

You are given an array points of size 300x2, where each row gives the (x, y) co-ordinates of a point on a map. Make a scatter plot of these points, and use the scatter plot to guess how many clusters there are.  

matplotlib.pyplot has already been imported as plt. In the IPython Shell:  

	 - Create an array called xs that contains the values of points[:,0] - that is, column 0 of points.
	 - Create an array called ys that contains the values of points[:,1] - that is, column 1 of points.
	 - Make a scatter plot by passing xs and ys to the plt.scatter() function.
	 - Call the plt.show() function to show your plot.
 
How many clusters do you see?    

### Possible Answers  => 2

 - 2
 - 3
 - 300

```python
In [1]: plt.scatter(x=points[:,0],y=points[:,1])
Out[1]: <matplotlib.collections.PathCollection at 0x7f3daf6efb38>

In [2]: plt.show()
```

### Results :  

see : img/graph1.
Correct! The scatter plot suggests that there are 3 distinct clusters.

---


## Clustering 2D points      

From the scatter plot of the previous exercise, you saw that the points seem to separate into 3 clusters. You'll now create a KMeans model to find 3 clusters, and fit it to the data points from the previous exercise. After the model has been fit, you'll obtain the cluster labels for some new points using the .predict() method.  

You are given the array points from the previous exercise, and also an array new_points.    

### Instructions

 - Import KMeans from sklearn.cluster.  
 - Using KMeans(), create a KMeans instance called model to find 3 clusters. To specify the number of clusters, use the n_clusters keyword argument.
 - Use the .fit() method of model to fit the model to the array of points points.
 - Use the .predict() method of model to predict the cluster labels of new_points, assigning the result to labels.
 - Hit 'Submit Answer' to see the cluster labels of new_points.  

```python
# Import KMeans
from sklearn.cluster import KMeans

# Create a KMeans instance with 3 clusters: model
model = KMeans(n_clusters=3)

# Fit model to points
model.fit(points)

# Determine the cluster labels of new_points: labels
labels = model.predict(new_points)

# Print cluster labels of new_points
print(labels)
```

### Results :  

	<script.py> output:
		[2 0 1 2 0 2 0 0 0 1 2 0 0 1 1 0 1 1 0 0 1 0 2 0 2 1 0 1 1 2 2 0 0 0 1 2 0
		 0 2 0 1 2 2 1 2 0 1 1 0 0 0 0 1 1 2 2 1 1 1 2 2 0 0 0 2 0 1 0 2 1 2 2 2 0
		 2 1 1 2 0 1 2 1 2 0 1 0 1 2 0 0 0 2 0 0 2 1 1 1 1 2 0 2 1 1 2 2 0 2 1 1 2
		 1 1 1 0 0 0 0 1 1 0 2 0 1 0 2 1 0 1 1 0 1 0 1 2 0 2 2 0 1 2 0 2 2 1 0 0 2
		 1 2 1 0 2 1 1 2 1 0 0 1 0 1 1 0 0 2 0 0 1 2 1 2 2 0 2 0 0 2 2 1 2 2 2 1 0
		 0 2 1 2 1 1 0 0 0 2 0 0 0 1 1 2 0 2 2 2 1 0 0 0 0 0 0 1 1 0 1 1 1 1 0 1 1
		 0 0 2 1 2 2 1 2 1 2 1 0 0 1 0 0 0 1 2 2 1 0 0 1 0 1 1 0 1 1 2 1 2 2 2 0 1
		 1 1 2 0 2 1 2 1 1 0 2 2 2 1 0 0 0 2 0 1 1 0 2 2 1 2 2 1 2 0 2 1 1 1 1 0 1
		 1 0 0 2]

Great work! You've successfully performed k-Means clustering and predicted the labels of new points. But it is not easy to inspect the clustering by just looking at the printed labels. A visualization would be far more useful. In the next exercise, you'll inspect your clustering with a scatter plot!  
		 
---


## What category of problem is this?    

 Import matplotlib.pyplot as plt.
Assign column 0 of new_points to xs, and column 1 of new_points to ys.
Make a scatter plot of xs and ys, specifying the c=labels keyword arguments to color the points by their cluster label. Also specify alpha=0.5.
Compute the coordinates of the centroids using the .cluster_centers_ attribute of model.
Assign column 0 of centroids to centroids_x, and column 1 of centroids to centroids_y.
Make a scatter plot of centroids_x and centroids_y, using 'D' (a diamond) as a marker by specifying the marker parameter. Set the size of the markers to be 50 using s=50.

### Instructions

 - Import matplotlib.pyplot as plt.
 - Assign column 0 of new_points to xs, and column 1 of new_points to ys.
 - Make a scatter plot of xs and ys, specifying the c=labels keyword arguments to color the points by their cluster label. Also specify alpha=0.5.
 - Compute the coordinates of the centroids using the .cluster_centers_ attribute of model.
 - Assign column 0 of centroids to centroids_x, and column 1 of centroids to centroids_y.
 - Make a scatter plot of centroids_x and centroids_y, using 'D' (a diamond) as a marker by specifying the marker parameter. Set the size of the markers to be 50 using s=50.

```python
# Import pyplot
import matplotlib.pyplot as plt

# Assign the columns of new_points: xs and ys
xs = new_points[:,0]
ys = new_points[:,1]

# Make a scatter plot of xs and ys, using labels to define the colors
plt.scatter(x=xs,y=ys,c=labels,alpha=0.5)

# Assign the cluster centers: centroids
centroids = model.cluster_centers_

# Assign the columns of centroids: centroids_x, centroids_y
centroids_x = centroids[:,0]
centroids_y = centroids[:,1]

# Make a scatter plot of centroids_x and centroids_y
plt.scatter(x=centroids_x,y=centroids_y,marker='D',s=50)
plt.show()
```

### Results :  

see img/graph2.svg  
Fantastic! The clustering looks great! But how can you be sure that 3 clusters is the correct choice? In other words, how can you evaluate the quality of a clustering? Tune into the next video in which Ben will explain how to evaluate a clustering!  

---



## How many clusters of grain?    

In the video, you learned how to choose a good number of clusters for a dataset using the k-means inertia graph. You are given an array samples containing the measurements (such as area, perimeter, length, and several others) of samples of grain. What's a good number of clusters in this case?  

KMeans and PyPlot (plt) have already been imported for you.  

This dataset was sourced from the UCI Machine Learning Repository.    

### Instructions

 - For each of the given values of k, perform the following steps:
 - Create a KMeans instance called model with k clusters.
 - Fit the model to the grain data samples.
 - Append the value of the inertia_ attribute of model to the list inertias.
 - The code to plot ks vs inertias has been written for you, so hit 'Submit Answer' to see the plot!

```python
ks = range(1, 6)
inertias = []

for k in ks:
    # Create a KMeans instance with k clusters: model
    model = KMeans(n_clusters=k)
    
    # Fit model to samples
    model.fit(samples)
    
    # Append the inertia to the list of inertias
    inertias.append(model.inertia_)
    
# Plot ks vs inertias
plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()
```

### Results :  

see img/graph3.svg  
Excellent job! The inertia decreases very slowly from 3 clusters to 4, so it looks like 3 clusters would be a good choice for this data.  

---



## Evaluating the grain clustering      

In the previous exercise, you observed from the inertia plot that 3 is a good number of clusters for the grain data. In fact, the grain samples come from a mix of 3 different grain varieties: "Kama", "Rosa" and "Canadian". In this exercise, cluster the grain samples into three clusters, and compare the clusters to the grain varieties using a cross-tabulation.  

You have the array samples of grain samples, and a list varieties giving the grain variety for each sample. Pandas (pd) and KMeans have already been imported for you.  

### Instructions

 - Create a KMeans model called model with 3 clusters.
 - Use the .fit_predict() method of model to fit it to samples and derive the cluster labels. Using .fit_predict() is the same as using .fit() followed by .predict().
 - Create a DataFrame df with two columns named 'labels' and 'varieties', using labels and varieties, respectively, for the column values. This has been done for you.
 - Use the pd.crosstab() function on df['labels'] and df['varieties'] to count the number of times each grain variety coincides with each cluster label. Assign the result to ct.
 - Hit 'Submit Answer' to see the cross-tabulation!

```python
# Create a KMeans model with 3 clusters: model
model = KMeans(n_clusters=3)

# Use fit_predict to fit model and obtain cluster labels: labels
labels = model.fit_predict(samples)

# Create a DataFrame with labels and varieties as columns: df
df = pd.DataFrame({'labels': labels, 'varieties': varieties})

# Create crosstab: ct
ct = pd.crosstab(df['labels'],df['varieties'])

# Display ct
print(ct)
```

### Results :  

	<script.py> output:
		varieties  Canadian wheat  Kama wheat  Rosa wheat
		labels                                           
		0                       2          60          10
		1                       0           1          60
		2                      68           9           0

Great work! The cross-tabulation shows that the 3 varieties of grain separate really well into 3 clusters. But depending on the type of data you are working with, the clustering may not always be this good. Is there anything you can do in such situations to improve your clustering? You'll find out in the next video!  		
		
---


## Scaling fish data for clustering   

You are given an array samples giving measurements of fish. Each row represents an individual fish. The measurements, such as weight in grams, length in centimeters, and the percentage ratio of height to length, have very different scales. In order to cluster this data effectively, you'll need to standardize these features first. In this exercise, you'll build a pipeline to standardize and cluster the data.  

These fish measurement data were sourced from the Journal of Statistics Education.  

### Instructions

 - Import:
	 - make_pipeline from sklearn.pipeline.
	 - StandardScaler from sklearn.preprocessing.
	 - KMeans from sklearn.cluster.
 - Create an instance of StandardScaler called scaler.
 - Create an instance of KMeans with 4 clusters called kmeans.
 - Create a pipeline called pipeline that chains scaler and kmeans. To do this, you just need to pass them in as arguments to make_pipeline().

```python
# Perform the necessary imports
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Create scaler: scaler
scaler = StandardScaler()

# Create KMeans instance: kmeans
kmeans = KMeans(n_clusters=4)

# Create pipeline: pipeline
pipeline = make_pipeline(scaler,kmeans)

```

### Results :  

Great work! Now that you've built the pipeline, you'll use it in the next exercise to cluster the fish by their measurements.  

---


## What category of problem is this?    

You'll now use your standardization and clustering pipeline from the previous exercise to cluster the fish by their measurements, and then create a cross-tabulation to compare the cluster labels with the fish species.  

As before, samples is the 2D array of fish measurements. Your pipeline is available as pipeline, and the species of every fish sample is given by the list species.    

### Instructions

 - Import pandas as pd.
 - Fit the pipeline to the fish measurements samples.
 - Obtain the cluster labels for samples by using the .predict() method of pipeline.
 - Using pd.DataFrame(), create a DataFrame df with two columns named 'labels' and 'species', using labels and species, respectively, for the column values.
 - Using pd.crosstab(), create a cross-tabulation ct of df['labels'] and df['species'].

```python
# Import pandas
import pandas as pd

print(samples[:5])
print('---------')
# Fit the pipeline to samples
pipeline.fit(samples)

# Calculate the cluster labels: labels
labels = pipeline.predict(samples)

print(species[:5])
print('---------')
# Create a DataFrame with labels and species as columns: df
df = pd.DataFrame({'labels': labels, 'species': species})

# Create crosstab: ct
ct = pd.crosstab(df['labels'],df['species'])

# Display ct
print(ct)
```

### Results :  

	<script.py> output:
		[[ 242.    23.2   25.4   30.    38.4   13.4]
		 [ 290.    24.    26.3   31.2   40.    13.8]
		 [ 340.    23.9   26.5   31.1   39.8   15.1]
		 [ 363.    26.3   29.    33.5   38.    13.3]
		 [ 430.    26.5   29.    34.    36.6   15.1]]
		---------
		['Bream', 'Bream', 'Bream', 'Bream', 'Bream']
		---------
		species  Bream  Pike  Roach  Smelt
		labels                            
		0            0    17      0      0
		1           33     0      1      0
		2            0     0      0     13
		3            1     0     19      1

		
Excellent! It looks like the fish data separates really well into 4 clusters!  
		
---



## Clustering stocks using KMeans    

In this exercise, you'll cluster companies using their daily stock price movements (i.e. the dollar difference between the closing and opening prices for each trading day). You are given a NumPy array movements of daily price movements from 2010 to 2015 (obtained from Yahoo! Finance), where each row corresponds to a company, and each column corresponds to a trading day.  

Some stocks are more expensive than others. To account for this, include a Normalizer at the beginning of your pipeline. The Normalizer will separately transform each company's stock price to a relative scale before the clustering begins.  

Note that Normalizer() is different to StandardScaler(), which you used in the previous exercise. While StandardScaler() standardizes features (such as the features of the fish data from the previous exercise) by removing the mean and scaling to unit variance, Normalizer() rescales each sample - here, each company's stock price - independently of the other.  

KMeans and make_pipeline have already been imported for you.    

### Instructions

 - Import Normalizer from sklearn.preprocessing.
 - Create an instance of Normalizer called normalizer.
 - Create an instance of KMeans called kmeans with 10 clusters.
 - Using make_pipeline(), create a pipeline called pipeline that chains normalizer and kmeans.
 - Fit the pipeline to the movements array.

```python
# Import Normalizer
from sklearn.preprocessing import Normalizer

# Create a normalizer: normalizer
normalizer = Normalizer()

# Create a KMeans model with 10 clusters: kmeans
kmeans = KMeans(n_clusters=10)

# Make a pipeline chaining normalizer and kmeans: pipeline
pipeline = make_pipeline(normalizer,kmeans)

# Fit pipeline to the daily price movements
pipeline.fit(movements)
```

### Results :  

Great work - you're really getting the hang of this. Now that your pipeline has been set up, you can find out which stocks move together in the next exercise!  

---



## Which stocks move together?      

In the previous exercise, you clustered companies by their daily stock price movements. So which company have stock prices that tend to change in the same way? You'll now inspect the cluster labels from your clustering to find out.  

Your solution to the previous exercise has already been run. Recall that you constructed a Pipeline pipeline containing a KMeans model and fit it to the NumPy array movements of daily stock movements. In addition, a list companies of the company names is available.    

### Instructions

 - Import pandas as pd.
 - Use the .predict() method of the pipeline to predict the labels for movements.
 - Align the cluster labels with the list of company names companies by creating a DataFrame df with labels and companies as columns. This has been done for you.
 - Use the .sort_values() method of df to sort the DataFrame by the 'labels' column, and print the result.
 - Hit 'Submit Answer' and take a moment to see which companies are together in each cluster!

```python
# Import pandas
import pandas as pd

# Predict the cluster labels: labels
labels = pipeline.predict(movements)

# Create a DataFrame aligning labels and companies: df
df = pd.DataFrame({'labels': labels, 'companies': companies})

# Display df sorted by cluster label
print(df.sort_values('labels'))
```

### Results :  

	<script.py> output:
									 companies  labels
		19                     GlaxoSmithKline       0
		37                            Novartis       0
		1                                  AIG       1
		55                         Wells Fargo       1
		3                     American express       1
		26                      JPMorgan Chase       1
		5                      Bank of America       1
		18                       Goldman Sachs       1
		16                   General Electrics       1
		0                                Apple       2
		33                           Microsoft       2
		24                               Intel       2
		23                                 IBM       2
		14                                Dell       2
		11                               Cisco       2
		47                            Symantec       2
		50  Taiwan Semiconductor Manufacturing       2
		51                   Texas instruments       2
		32                                  3M       3
		15                                Ford       3
		17                     Google/Alphabet       3
		45                                Sony       3
		34                          Mitsubishi       3
		21                               Honda       3
		22                                  HP       3
		48                              Toyota       3
		7                                Canon       3
		13                   DuPont de Nemours       3
		58                               Xerox       3
		59                               Yahoo       4
		2                               Amazon       4
		30                          MasterCard       5
		31                           McDonalds       5
		52                            Unilever       5
		20                          Home Depot       5
		6             British American Tobacco       5
		49                               Total       5
		46                      Sanofi-Aventis       5
		43                                 SAP       5
		42                   Royal Dutch Shell       5
		4                               Boeing       6
		29                     Lookheed Martin       6
		36                    Northrop Grumman       6
		56                            Wal-Mart       7
		27                      Kimberly-Clark       7
		54                            Walgreen       7
		25                   Johnson & Johnson       7
		40                      Procter Gamble       7
		38                               Pepsi       7
		39                              Pfizer       7
		9                    Colgate-Palmolive       7
		8                          Caterpillar       8
		12                             Chevron       8
		35                            Navistar       8
		53                       Valero Energy       8
		10                      ConocoPhillips       8
		57                               Exxon       8
		44                        Schlumberger       8
		41                       Philip Morris       9
		28                           Coca Cola       9

		
Fantastic job - you have completed Chapter 1! Take a look at the clusters. Are you surprised by any of the results? In the next chapter, you'll learn about how to communicate results such as this through visualizations.  

---


## What category of problem is this?    

  

### Instructions

 - 

```python

```

### Results :  



---


## What category of problem is this?    

  

### Instructions

 - 

```python

```

### Results :  



---



## What category of problem is this?    

  

### Instructions

 - 

```python

```

### Results :  



---



## What category of problem is this?    

  

### Instructions

 - 

```python

```

### Results :  



---


## What category of problem is this?    

  

### Instructions

 - 

```python

```

### Results :  



---


## What category of problem is this?    

  

### Instructions

 - 

```python

```

### Results :  



---



## What category of problem is this?    

  

### Instructions

 - 

```python

```

### Results :  



---


## What category of problem is this?    

  

### Instructions

 - 

```python

```

### Results :  



---


## What category of problem is this?    

  

### Instructions

 - 

```python

```

### Results :  



---


## What category of problem is this?    

  

### Instructions

 - 

```python

```

### Results :  



---



## What category of problem is this?    

  

### Instructions

 - 

```python

```

### Results :  



---


## What category of problem is this?    

  

### Instructions

 - 

```python

```

### Results :  



---


## What category of problem is this?    

  

### Instructions

 - 

```python

```

### Results :  



---


## What category of problem is this?    

  

### Instructions

 - 

```python

```

### Results :  



---



## What category of problem is this?    

  

### Instructions

 - 

```python

```

### Results :  



---