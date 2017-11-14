11/2017  
# Datacamp - Unsupervised Learning in Python (Data Scientist Track with Python)  
[Unsupervised Learning in Python](https://www.datacamp.com/courses/unsupervised-learning-in-python)

---

***Course Description***  

Say you have a collection of customers with a variety of characteristics such as age, location, and financial history, and you wish to discover patterns and sort them into clusters. Or perhaps you have a set of texts, such as wikipedia pages, and you wish to segment them into categories based on their content. This is the world of unsupervised learning, called as such because you are not guiding, or supervising, the pattern discovery by some prediction task, but instead uncovering hidden structure from unlabeled data. Unsupervised learning encompasses a variety of techniques in machine learning, from clustering to dimension reduction to matrix factorization. In this course, you'll learn the fundamentals of unsupervised learning and implement the essential algorithms using scikit-learn and scipy. You will learn how to cluster, transform, visualize, and extract insights from unlabeled datasets, and end the course by building a recommender system to recommend popular musical artists.     

# Part 3 : Decorrelating your data and dimension reduction     

Dimension reduction summarizes a dataset using its common occuring patterns. In this chapter, you'll learn about the most fundamental of dimension reduction techniques, "Principal Component Analysis" ("PCA"). PCA is often used before supervised learning to improve model performance and generalization. It can also be useful for unsupervised learning. For example, you'll employ a variant of PCA will allow you to cluster Wikipedia articles by their content!      

## Correlated data in nature   

You are given an array grains giving the width and length of samples of grain. You suspect that width and length will be correlated. To confirm this, make a scatter plot of width vs length and measure their Pearson correlation.    

### Instructions

 - Import:
   - matplotlib.pyplot as plt.
   - pearsonr from scipy.stats.
 - Assign column 0 of grains to width and column 1 of grains to length.
 - Make a scatter plot with width on the x-axis and length on the y-axis.
 - Use the pearsonr() function to calculate the Pearson correlation of width and length.

```python
# Perform the necessary imports
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Assign the 0th column of grains: width
width = grains[:,0]

# Assign the 1st column of grains: length
length = grains[:,1]

# Scatter plot width vs length
plt.scatter(width, length)
plt.axis('equal')
plt.show()

# Calculate the Pearson correlation
correlation, pvalue = pearsonr(width, length)

# Display the correlation
print(correlation)

```

### Results :  

    <script.py> output:
    0.860414937714

See: img/graph10.svg  
Great work! As you would expect, the width and length of the grain samples are highly correlated.  

---


## Decorrelating the grain measurements with PCA      

You observed in the previous exercise that the width and length measurements of the grain are correlated. Now, you'll use PCA to decorrelate these measurements, then plot the decorrelated points and measure their Pearson correlation.  

### Instructions

 - Import PCA from sklearn.decomposition.
 - Create an instance of PCA called model.
 - Use the .fit_transform() method of model to apply the PCA transformation to grains. Assign the result to pca_features.
 - The subsequent code to extract, plot, and compute the Pearson correlation of the first two columns pca_features has been written for you, so hit 'Submit Answer' to see the result!

```python
# Import PCA
from sklearn.decomposition import PCA

# Create PCA instance: model
model = PCA()

# Apply the fit_transform method of model to grains: pca_features
pca_features = model.fit_transform(grains)

# Assign 0th column of pca_features: xs
xs = pca_features[:,0]

# Assign 1st column of pca_features: ys
ys = pca_features[:,1]

# Scatter plot xs vs ys
plt.scatter(xs, ys)
plt.axis('equal')
plt.show()

# Calculate the Pearson correlation of xs and ys
correlation, pvalue = pearsonr(xs, ys)

# Display the correlation
print(correlation)
```

### Results :  

    <script.py> output:
        0.0

see img/graph11.svg  
Excellent! You've successfully decorrelated the grain measurements with PCA!  

---


## Principal components    

On the right are three scatter plots of the same point cloud. Each scatter plot shows a different set of axes (in red). In which of the plots could the axes represent the principal components of the point cloud?  

Recall that the principal components are the directions along which the the data varies.  

### Possible answers => 2 (Both plot 1 and plot 3)

 - None of them.
 - Both plot 1 and plot 3.
 - Plot 2.

```python

```

### Results :  

see: img/graph12.svg  
Well done! You've correctly inferred that the principal components have to align with the axes of the point cloud. This happens in both plot 1 and plot 3.  

---



## The first principal component      

The first principal component of the data is the direction in which the data varies the most. In this exercise, your job is to use PCA to find the first principal component of the length and width measurements of the grain samples, and represent it as an arrow on the scatter plot.  

The array grains gives the length and width of the grain samples. PyPlot (plt) and PCA have already been imported for you.  

### Instructions

 - Make a scatter plot of the grain measurements. This has been done for you.
 - Create a PCA instance called model.
 - Fit the model to the grains data.
 - Extract the coordinates of the mean of the data using the .mean_ attribute of model.
 - Get the first principal component of model using the .components_[0,:] attribute.
 - Plot the first principal component as an arrow on the scatter plot, using the plt.arrow() function. You have to specify the first two arguments - mean[0] and mean[1].

```python
# Make a scatter plot of the untransformed points
plt.scatter(grains[:,0], grains[:,1])

# Create a PCA instance: model
model = PCA()

# Fit model to points
model.fit(grains)

# Get the mean of the grain samples: mean
mean = model.mean_

# Get the first principal component: first_pc
first_pc = model.components_[0,:]

# Plot first_pc as an arrow, starting at mean
plt.arrow(mean[0], mean[1], first_pc[0], first_pc[1], color='red', width=0.01)

# Keep axes on same scale
plt.axis('equal')
plt.show()
```

### Results :  

See : img/graph13.svg  
Excellent job! This is the direction in which the grain data varies the most.  

---



## Variance of the PCA features      

The fish dataset is 6-dimensional. But what is its intrinsic dimension? Make a plot of the variances of the PCA features to find out. As before, samples is a 2D array, where each row represents a fish. You'll need to standardize the features first.  

### Instructions

 - Create an instance of StandardScaler called scaler.
 - Create a PCA instance called pca.
 - Use the make_pipeline() function to create a pipeline chaining scaler and pca.
 - Use the .fit() method of pipeline to fit it to the fish samples samples.
 - Extract the number of components used using the .n_components_ attribute of pca. Place this inside a range() function and store the result as features.
 - Use the plt.bar() function to plot the explained variances, with features on the x-axis and pca.explained_variance_ on the y-axis.

```python
# Perform the necessary imports
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

# Create scaler: scaler
scaler = StandardScaler()

# Create a PCA instance: pca
pca = PCA()

# Create pipeline: pipeline
pipeline = make_pipeline(scaler, pca)

print(samples[:5])
print('---------------')

# Fit the pipeline to 'samples'
pipeline.fit(samples)

# Plot the explained variances
features = range(pca.n_components_)
plt.bar(features, pca.explained_variance_)
plt.xlabel('PCA feature')
plt.ylabel('variance')
plt.xticks(features)
plt.show()
```

### Results :  

    <script.py> output:
        [[ 242.    23.2   25.4   30.    38.4   13.4]
         [ 290.    24.    26.3   31.2   40.    13.8]
         [ 340.    23.9   26.5   31.1   39.8   15.1]
         [ 363.    26.3   29.    33.5   38.    13.3]
         [ 430.    26.5   29.    34.    36.6   15.1]]
        ---------------

see img/graph14.svg  
Great work! It looks like PCA features 0 and 1 have significant variance.  

---


## Intrinsic dimension of the fish data    

In the previous exercise, you plotted the variance of the PCA features of the fish measurements. Looking again at your plot, what do you think would be a reasonable choice for the "intrinsic dimension" of the the fish measurements? Recall that the intrinsic dimension is the number of PCA features with significant variance.  

### Possible Answers  => 2

 - 1
 - 2
 - 5

```python

```

### Results :  

see img/graph15.svg  
Great job! Since PCA features 0 and 1 have significant variance, the intrinsic dimension of this dataset appears to be 2.  

---


## Dimension reduction of the fish measurements    

In a previous exercise, you saw that 2 was a reasonable choice for the "intrinsic dimension" of the fish measurements. Now use PCA for dimensionality reduction of the fish measurements, retaining only the 2 most important components.  

The fish measurements have already been scaled for you, and are available as scaled_samples.  

### Instructions

 - Import PCA from sklearn.decomposition.
 - Create a PCA instance called pca with n_components=2.
 - Use the .fit() method of pca to fit it to the scaled fish measurements scaled_samples.
 - Use the .transform() method of pca to transform the scaled_samples. Assign the result to pca_features.

```python
# Import PCA
from sklearn.decomposition import PCA

# Create a PCA model with 2 components: pca
pca = PCA(n_components=2)

# Fit the PCA instance to the scaled samples
pca.fit(scaled_samples)

# Transform the scaled samples: pca_features
pca_features = pca.transform(scaled_samples)

print(scaled_samples.shape)
print('--------------------')
# Print the shape of pca_features
print(pca_features.shape)
```

### Results :  

	<script.py> output:
		(85, 6)
		--------------------
		(85, 2)

Superb! You've successfully reduced the dimensionality from 6 to 2.  

---



## A tf-idf word-frequency array      

In this exercise, you'll create a tf-idf word frequency array for a toy collection of documents. For this, use the TfidfVectorizer from sklearn. It transforms a list of documents into a word frequency array, which it outputs as a csr_matrix. It has fit() and transform() methods like other sklearn objects.  

You are given a list documents of toy documents about pets. Its contents have been printed in the IPython Shell.  

### Instructions

 - Import TfidfVectorizer from sklearn.feature_extraction.text.
 - Create a TfidfVectorizer instance called tfidf.
 - Apply .fit_transform() method of tfidf to documents and assign the result to csr_mat. This is a word-frequency array in csr_matrix format.
 - Inspect csr_mat by calling its .toarray() method and printing the result. This has been done for you.
 - The columns of the array correspond to words. Get the list of words by calling the .get_feature_names() method of tfidf, and assign the result to words.

```python
# Import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Create a TfidfVectorizer: tfidf
tfidf = TfidfVectorizer() 

# Apply fit_transform to document: csr_mat
csr_mat = tfidf.fit_transform(documents)

# Print result of toarray() method
print(csr_mat.toarray())

# Get the words: words
words = tfidf.get_feature_names()

# Print words
print(words)
```

### Results :  

	['cats say meow', 'dogs say woof', 'dogs chase cats']

	<script.py> output:
		[[ 0.51785612  0.          0.          0.68091856  0.51785612  0.        ]
		 [ 0.          0.          0.51785612  0.          0.51785612  0.68091856]
		 [ 0.51785612  0.68091856  0.51785612  0.          0.          0.        ]]
		['cats', 'chase', 'dogs', 'meow', 'say', 'woof']

Great work! You'll now move to clustering Wikipedia articles!  		
		
---



## Clustering Wikipedia part I    

You saw in the video that TruncatedSVD is able to perform PCA on sparse arrays in csr_matrix format, such as word-frequency arrays. Combine your knowledge of TruncatedSVD and k-means to cluster some popular pages from Wikipedia. In this exercise, build the pipeline. In the next exercise, you'll apply it to the word-frequency array of some Wikipedia articles.  

Create a Pipeline object consisting of a TruncatedSVD followed by KMeans. (This time, we've precomputed the word-frequency matrix for you, so there's no need for a TfidfVectorizer).  

The Wikipedia dataset you will be working with was obtained from [here](https://blog.lateral.io/2015/06/the-unknown-perils-of-mining-wikipedia/).  

### Instructions

 - Import:
	 - TruncatedSVD from sklearn.decomposition.
	 - KMeans from sklearn.cluster.
	 - make_pipeline from sklearn.pipeline.
 - Create a TruncatedSVD instance called svd with n_components=50.
 - Create a KMeans instance called kmeans with n_clusters=6.
 - Create a pipeline called pipeline consisting of svd and kmeans.

```python
# Perform the necessary imports
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline

# Create a TruncatedSVD instance: svd
svd = TruncatedSVD(n_components=50)

# Create a KMeans instance: kmeans
kmeans = KMeans(n_clusters=6)

# Create a pipeline: pipeline
pipeline = make_pipeline(svd,kmeans)
```

### Results :  

Excellent! Now that you have set up your pipeline, you will use it in the next exercise to cluster the articles.  

---


## Clustering Wikipedia part II    

It is now time to put your pipeline from the previous exercise to work! You are given an array articles of tf-idf word-frequencies of some popular Wikipedia articles, and a list titles of their titles. Use your pipeline to cluster the Wikipedia articles.  	

A solution to the previous exercise has been pre-loaded for you, so a Pipeline pipeline chaining TruncatedSVD with KMeans is available.  

### Instructions

 - Import pandas as pd.
 - Fit the pipeline to the word-frequency array articles.
 - Predict the cluster labels.
 - Align the cluster labels with the list titles of article titles by creating a DataFrame df with labels and titles as columns. This has been done for you.
 - Use the .sort_values() method of df to sort the DataFrame by the 'label' column, and print the result.
 - Hit 'Submit Answer' and take a moment to investigate your amazing clustering of Wikipedia pages!

```python
# Import pandas
import pandas as pd
# Fit the pipeline to articles
pipeline.fit(articles)

# Calculate the cluster labels: labels
labels = pipeline.predict(articles)

# Create a DataFrame aligning labels and titles: df
df = pd.DataFrame({'label': labels, 'article': titles})

# Display df sorted by cluster label
print(df.sort_values('label'))
```

### Results :  

	<script.py> output:
												  article  label
		41                                    Hepatitis B      0
		49                                       Lymphoma      0
		48                                     Gabapentin      0
		47                                          Fever      0
		46                                     Prednisone      0
		40                                    Tonsillitis      0
		45                                    Hepatitis C      0
		44                                           Gout      0
		43                                       Leukemia      0
		42                                    Doxycycline      0
		22                              Denzel Washington      1
		23                           Catherine Zeta-Jones      1
		24                                   Jessica Biel      1
		25                                  Russell Crowe      1
		29                               Jennifer Aniston      1
		27                                 Dakota Fanning      1
		28                                  Anne Hathaway      1
		21                             Michael Fassbender      1
		26                                     Mila Kunis      1
		20                                 Angelina Jolie      1
		37                                       Football      1
		32                                   Arsenal F.C.      1
		18  2010 United Nations Climate Change Conference      2
		17  Greenhouse gas emissions by the United States      2
		15                                 Kyoto Protocol      2
		14                                 Climate change      2
		13                               Connie Hedegaard      2
		12                                   Nigel Lawson      2
		11       Nationally Appropriate Mitigation Action      2
		10                                 Global warming      2
		9                                        LinkedIn      2
		5                                          Tumblr      2
		19  2007 United Nations Climate Change Conference      2
		16                                        350.org      2
		0                                        HTTP 404      3
		3                                     HTTP cookie      3
		8                                         Firefox      3
		7                                   Social search      3
		6                     Hypertext Transfer Protocol      3
		4                                   Google Search      3
		2                               Internet Explorer      3
		1                                  Alexa Internet      3
		57                          Red Hot Chili Peppers      4
		56                                       Skrillex      4
		55                                  Black Sabbath      4
		54                                 Arctic Monkeys      4
		53                                   Stevie Nicks      4
		52                                     The Wanted      4
		51                                     Nate Ruess      4
		50                                   Chad Kroeger      4
		59                                    Adam Levine      4
		58                                         Sepsis      4
		30                  France national football team      5
		31                              Cristiano Ronaldo      5
		39                                  Franck Ribéry      5
		38                                         Neymar      5
		33                                 Radamel Falcao      5
		36              2014 FIFA World Cup qualification      5
		34                             Zlatan Ibrahimović      5
		35                Colombia national football team      5

Fantastic! Take a look at the cluster labels and see if you can identify any patterns!  

---