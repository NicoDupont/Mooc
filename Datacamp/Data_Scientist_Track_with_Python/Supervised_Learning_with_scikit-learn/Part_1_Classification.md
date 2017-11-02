10/2017  
Datcamp - Supervised Learning with scikit-learn  

---

***Course Description***  

At the end of day, the value of Data Scientists rests on their ability to describe the world and to make predictions. Machine Learning is the field of teaching machines and computers to learn from existing data to make predictions on new data - will a given tumor be benign or malignant? Which of your customers will take their business elsewhere? Is a particular email spam or not? In this course, you'll learn how to use Python to perform supervised learning, an essential component of Machine Learning. You'll learn how to build predictive models, how to tune their parameters and how to tell how well they will perform on unseen data, all the while using real world datasets. You'll do so using scikit-learn, one of the most popular and user-friendly machine learning libraries for Python.  
 
# Part 1 : Classification   

In this chapter, you will be introduced to classification problems and learn how to solve them using supervised learning techniques. Classification problems are prevalent in a variety of domains, ranging from finance to healthcare. Here, you will have the chance to apply what you are learning to a political dataset, where you classify the party affiliation of United States Congressmen based on their voting records.  

## Which of these is a classification problem?  

Once you decide to leverage supervised machine learning to solve a new problem, you need to identify whether your problem is better suited to classification or regression. This exercise will help you develop your intuition for distinguishing between the two.  

Provided below are 4 example applications of machine learning. Which of them is a supervised classification problem?  

### Possible Answers :  => 1

 - Using labeled financial data to predict whether the value of a stock will go up or go down next week.
 - Using labeled housing price data to predict the price of a new house based on various features.
 - Using unlabeled data to cluster the students of an online education company into different categories based on their learning styles.
 - Using labeled financial data to predict what the value of a stock will be next week.

```python

```

### Results :  

Exactly! In this example, there are two discrete, qualitative outcomes: the stock market going up, and the stock market going down. This can be represented using a binary variable, and is an application perfectly suited for classification.  

---

## Numerical EDA  

In this chapter, you'll be working with a dataset obtained from the UCI Machine Learning Repository consisting of votes made by US House of Representatives Congressmen. Your goal will be to predict their party affiliation ('Democrat' or 'Republican') based on how they voted on certain key issues. Here, it's worth noting that we have preprocessed this dataset to deal with missing values. This is so that your focus can be directed towards understanding how to train and evaluate supervised learning models. Once you have mastered these fundamentals, you will be introduced to preprocessing techniques in Chapter 4 and have the chance to apply them there yourself - including on this very same dataset!  

Before thinking about what supervised learning models you can apply to this, however, you need to perform Exploratory data analysis (EDA) in order to understand the structure of the data. For a refresher on the importance of EDA, check out the first two chapters of Statistical Thinking in Python (Part 1).  

Get started with your EDA now by exploring this voting records dataset numerically. It has been pre-loaded for you into a DataFrame called df. Use pandas' .head(), .info(), and .describe() methods in the IPython Shell to explore the DataFrame, and select the statement below that is not true.  

### Possible Answers :  => 4

 - The DataFrame has a total of 435 rows and 17 columns.
 - Except for 'party', all of the columns are of type int64.
 - The first two rows of the DataFrame consist of votes made by Republicans and the next three rows consist of votes made by Democrats.
 - There are 17 predictor variables, or features, in this DataFrame.
 - The target variable in this DataFrame is 'party'. 

```python

```

### Results :  

	In [1]: df.head()
	Out[1]: 
			party  infants  water  budget  physician  salvador  religious  \
	0  republican        0      1       0          1         1          1   
	1  republican        0      1       0          1         1          1   
	2    democrat        0      1       1          0         1          1   
	3    democrat        0      1       1          0         1          1   
	4    democrat        1      1       1          0         1          1   

	   satellite  aid  missile  immigration  synfuels  education  superfund  \
	0          0    0        0            1         0          1          1   
	1          0    0        0            0         0          1          1   
	2          0    0        0            0         1          0          1   
	3          0    0        0            0         1          0          1   
	4          0    0        0            0         1          0          1   

	   crime  duty_free_exports  eaa_rsa  
	0      1                  0        1  
	1      1                  0        1  
	2      1                  0        0  
	3      0                  0        1  
	4      1                  1        1

	In [2]: df.info()
	<class 'pandas.core.frame.DataFrame'>
	RangeIndex: 435 entries, 0 to 434
	Data columns (total 17 columns):
	party                435 non-null object
	infants              435 non-null int64
	water                435 non-null int64
	budget               435 non-null int64
	physician            435 non-null int64
	salvador             435 non-null int64
	religious            435 non-null int64
	satellite            435 non-null int64
	aid                  435 non-null int64
	missile              435 non-null int64
	immigration          435 non-null int64
	synfuels             435 non-null int64
	education            435 non-null int64
	superfund            435 non-null int64
	crime                435 non-null int64
	duty_free_exports    435 non-null int64
	eaa_rsa              435 non-null int64
	dtypes: int64(16), object(1)
	memory usage: 57.9+ KB

	In [3]: df.shape
	Out[3]: (435, 17)

Great work! The number of columns in the DataFrame is not equal to the number of features. One of the columns - 'party' is the target variable.  	
	
---

## Visual EDA  

The Numerical EDA you did in the previous exercise gave you some very important information, such as the names and data types of the columns, and the dimensions of the DataFrame. Following this with some visual EDA will give you an even better understanding of the data. In the video, Hugo used the scatter_matrix() function on the Iris data for this purpose. However, you may have noticed in the previous exercise that all the features in this dataset are binary; that is, they are either 0 or 1. So a different type of plot would be more useful here, such as Seaborn's countplot.  

Given on the right is a countplot of the 'education' bill, generated from the following code:  

see : img/graph1.svg  

```python
plt.figure()
sns.countplot(x='education', hue='party', data=df, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()
```

In sns.countplot(), we specify the x-axis data to be 'education', and hue to be 'party'. Recall that 'party' is also our target variable. So the resulting plot shows the difference in voting behavior between the two parties for the 'education' bill, with each party colored differently. We manually specified the color to be 'RdBu', as the Republican party has been traditionally associated with red, and the Democratic party with blue.  

It seems like Democrats voted resoundingly against this bill, compared to Republicans. This is the kind of information that our machine learning model will seek to learn when we try to predict party affiliation solely based on voting behavior. An expert in U.S politics may be able to predict this without machine learning, but probably not instantaneously - and certainly not if we are dealing with hundreds of samples!  

In the IPython Shell, explore the voting behavior further by generating countplots for the 'satellite' and 'missile' bills, and answer the following question: Of these two bills, for which ones do Democrats vote resoundingly in favor of, compared to Republicans? Be sure to begin your plotting statements for each figure with plt.figure() so that a new figure will be set up. Otherwise, your plots will be overlayed onto the same figure.  

### Possible Answers : => 3

 - 'satellite'.
 - 'missile'.
 - Both 'satellite' and 'missile'.
 - Neither 'satellite' nor 'missile'.

```python

```

### Results :  

	In [2]: plt.figure()
	... sns.countplot(x='education', hue='party', data=df, palette='RdBu')
	... plt.xticks([0,1], ['No', 'Yes'])
	... plt.show()

	In [3]: plt.figure()
	Out[3]: <matplotlib.figure.Figure at 0x7f789c512ac8>

	In [4]: sns.countplot(x='satellite', hue='party', data=df, palette='RdBu')
	Out[4]: <matplotlib.axes._subplots.AxesSubplot at 0x7f787f530c88>

	In [5]: plt.xticks([0,1], ['No', 'Yes'])
	Out[5]: 
	([<matplotlib.axis.XTick at 0x7f787f527b00>,
	  <matplotlib.axis.XTick at 0x7f787f5274a8>],
	 <a list of 2 Text xticklabel objects>)

	In [6]: plt.show()

	In [7]: plt.figure()
	Out[7]: <matplotlib.figure.Figure at 0x7f787f4c03c8>

	In [8]: sns.countplot(x='missile', hue='party', data=df, palette='RdBu')
	Out[8]: <matplotlib.axes._subplots.AxesSubplot at 0x7f787f4deba8>

	In [9]: plt.xticks([0,1], ['No', 'Yes'])
	Out[9]: 
	([<matplotlib.axis.XTick at 0x7f787f527ac8>,
	  <matplotlib.axis.XTick at 0x7f787f51e080>],
	 <a list of 2 Text xticklabel objects>)

	In [10]: plt.show()

see : img/graph2.svg 
see : img/graph3.svg   
Correct! Democrats voted in favor of both 'satellite' and 'missile'  	
	
---

## k-Nearest Neighbors: Fit  

Having explored the Congressional voting records dataset, it is time now to build your first classifier. In this exercise, you will fit a k-Nearest Neighbors classifier to the voting dataset, which has once again been pre-loaded for you into a DataFrame df.  
 
In the video, Hugo discussed the importance of ensuring your data adheres to the format required by the scikit-learn API. The features need to be in an array where each column is a feature and each row a different observation or data point - in this case, a Congressman's voting record. The target needs to be a single column with the same number of observations as the feature data. We have done this for you in this exercise. Notice we named the feature array X and response variable y: This is in accordance with the common scikit-learn practice.  

Your job is to create an instance of a k-NN classifier with 6 neighbors (by specifying the n_neighbors parameter) and then fit it to the data. The data has been pre-loaded into a DataFrame called df.  

### Instructions :

 - Import KNeighborsClassifier from sklearn.neighbors.
 - Create arrays X and y for the features and the target variable. Here this has been done for you. Note the use of .drop() to drop the target variable 'party' from the feature array X as well as the use of the .values attribute to ensure X and y are NumPy arrays. Without using .values, X and y are a DataFrame and Series respectively; the scikit-learn API will accept them in this form also as long as they are of the right shape.
 - Instantiate a KNeighborsClassifier called knn with 6 neighbors by specifying the n_neighbors parameter.
 - Fit the classifier to the data using the .fit() method.

```python
# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier

# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
res = knn.fit(X,y)
print(res)
```

### Results :  

	<script.py> output:
		KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
				   metric_params=None, n_jobs=1, n_neighbors=6, p=2,
				   weights='uniform')

Excellent! Now that your k-NN classifier with 6 neighbors has been fit to the data, it can be used to predict the labels of new data points.  

---

## k-Nearest Neighbors: Predict  

Having fit a k-NN classifier, you can now use it to predict the label of a new data point. However, there is no unlabeled data available since all of it was used to fit the model! You can still use the .predict() method on the X that was used to fit the model, but it is not a good indicator of the model's ability to generalize to new, unseen data.  

In the next video, Hugo will discuss a solution to this problem. For now, a random unlabeled data point has been generated and is available to you as X_new. You will use your classifier to predict the label for this new data point, as well as on the training data X that the model has already seen. Using .predict() on X_new will generate 1 prediction, while using it on X will generate 435 predictions: 1 for each sample.  

The DataFrame has been pre-loaded as df. This time, you will create the feature array X and target variable array y yourself.  

### Instructions :

 - Create arrays for the features and the target variable from df. As a reminder, the target variable is 'party'.
 - Instantiate a KNeighborsClassifier with 6 neighbors.
 - Fit the classifier to the data.
 - Predict the labels of the training data, X.
 - Predict the label of the new data point X_new.

```python
# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier 

print(df.head())
print('----------------')
# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X,y)


print(X_new.shape)
print('----------------')
print(X_new.head())
print('----------------')
# Predict the labels for the training data X
y_pred = knn.predict(X)

# Predict and print the label for the new data point X_new
new_prediction = knn.predict(X_new)
print("Prediction: {}".format(new_prediction))
```

### Results :  

	<script.py> output:
				party  infants  water  budget  physician  salvador  religious  \
		0  republican        0      1       0          1         1          1   
		1  republican        0      1       0          1         1          1   
		2    democrat        0      1       1          0         1          1   
		3    democrat        0      1       1          0         1          1   
		4    democrat        1      1       1          0         1          1   
		
		   satellite  aid  missile  immigration  synfuels  education  superfund  \
		0          0    0        0            1         0          1          1   
		1          0    0        0            0         0          1          1   
		2          0    0        0            0         1          0          1   
		3          0    0        0            0         1          0          1   
		4          0    0        0            0         1          0          1   
		
		   crime  duty_free_exports  eaa_rsa  
		0      1                  0        1  
		1      1                  0        1  
		2      1                  0        0  
		3      0                  0        1  
		4      1                  1        1  
		----------------
		(1, 16)
		----------------
				 0         1         2         3         4         5         6   \
		0  0.429078  0.220849  0.004436  0.600394  0.850926  0.358138  0.629755   
		
				 7         8         9        10        11        12        13  \
		0  0.234159  0.825512  0.167959  0.69006  0.871226  0.052972  0.450923   
		
				 14        15  
		0  0.698306  0.666329  
		----------------
		Prediction: ['republican']

Great work! Did your model predict 'democrat' or 'republican'? How sure can you be of its predictions? In other words, how can you measure its performance? This is what you will learn in the next video.  		
		
---

## The digits recognition dataset  

Up until now, you have been performing binary classification, since the target variable had two possible outcomes. Hugo, however, got to perform multi-class classification in the videos, where the target variable could take on three possible outcomes. Why does he get to have all the fun?! In the following exercises, you'll be working with the MNIST digits recognition dataset, which has 10 classes, the digits 0 through 9! A reduced version of the MNIST dataset is one of scikit-learn's included datasets, and that is the one we will use in this exercise.  

Each sample in this scikit-learn dataset is an 8x8 image representing a handwritten digit. Each pixel is represented by an integer in the range 0 to 16, indicating varying levels of black. Recall that scikit-learn's built-in datasets are of type Bunch, which are dictionary-like objects. Helpfully for the MNIST dataset, scikit-learn provides an 'images' key in addition to the 'data' and 'target' keys that you have seen with the Iris data. Because it is a 2D array of the images corresponding to each sample, this 'images' key is useful for visualizing the images, as you'll see in this exercise (for more on plotting 2D arrays, see Chapter 2 of DataCamp's course on Data Visualization with Python). On the other hand, the 'data' key contains the feature array - that is, the images as a flattened array of 64 pixels.  

Notice that you can access the keys of these Bunch objects in two different ways: By using the . notation, as in digits.images, or the [] notation, as in digits['images'].  

For more on the MNIST data, check out this exercise in Part 1 of DataCamp's Importing Data in Python course. There, the full version of the MNIST dataset is used, in which the images are 28x28. It is a famous dataset in machine learning and computer vision, and frequently used as a benchmark to evaluate the performance of a new model.  

### Instructions :

 - Import datasets from sklearn and matplotlib.pyplot as plt.
 - Load the digits dataset using the .load_digits() method on datasets.
 - Print the keys and DESCR of digits.
 - Print the shape of images and data keys using the . notation.
 - Display the 1010th image using plt.imshow(). This has been done for you, so hit 'Submit Answer' to see which handwritten digit this happens to be!

```python
# Import necessary modules
from sklearn import datasets
import matplotlib.pyplot as plt

# Load the digits dataset: digits
digits = datasets.load_digits()

# Print the keys and DESCR of the dataset
print(digits.keys())
print(digits.DESCR)

# Print the shape of the images and data keys
print(digits.images.shape)
print(digits.data.shape)

# Display digit 1010
plt.imshow(digits.images[1010], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
```

### Results :  

see : img/graph4.svg  

Good job! It looks like the image in question corresponds to the digit '5'. Now, can you build a classifier that can make this prediction not only for this image, but for all the other ones in the dataset? You'll do so in the next exercise!  

---

## Train/Test Split + Fit/Predict/Accuracy  

Now that you have learned about the importance of splitting your data into training and test sets, it's time to practice doing this on the digits dataset! After creating arrays for the features and target variable, you will split them into training and test sets, fit a k-NN classifier to the training data, and then compute its accuracy using the .score() method.  

### Instructions :

 - Import KNeighborsClassifier from sklearn.neighbors and train_test_split from sklearn.model_selection.
 - Create an array for the features using digits.data and an array for the target using digits.target.
 - Create stratified training and test sets using 0.2 for the size of the test set. Use a random state of 42. Stratify the split according to the labels so that they are distributed in the training and test sets as they are in the original dataset.
 - Create a k-NN classifier with 7 neighbors and fit it to the training data.
 - Compute and print the accuracy of the classifier's predictions using the .score() method.

```python
# Import necessary modules
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Create feature and target arrays
X = digits.data
y = digits.target

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42, stratify=y)

# Create a k-NN classifier with 7 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=7)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Print the accuracy
print(knn.score(X_test, y_test))
```

### Results :  

	<script.py> output:
		0.983333333333

Excellent work! Incredibly, this out of the box k-NN classifier with 7 neighbors has learned from the training data and predicted the labels of the images in the test set with 98% accuracy, and it did so in less than a second! This is one illustration of how incredibly useful machine learning techniques can be.  
		
---

## Overfitting and underfitting  

Remember the model complexity curve that Hugo showed in the video? You will now construct such a curve for the digits dataset! In this exercise, you will compute and plot the training and testing accuracy scores for a variety of different neighbor values. By observing how the accuracy scores differ for the training and testing sets with different values of k, you will develop your intuition for overfitting and underfitting.  

The training and testing sets are available to you in the workspace as X_train, X_test, y_train, y_test. In addition, KNeighborsClassifier has been imported from sklearn.neighbors.  

### Instructions :

- Inside the for loop:
	- Setup a k-NN classifier with the number of neighbors equal to k.
	- Fit the classifier with k neighbors to the training data.
	- Compute accuracy scores the training set and test set separately using the .score() method and assign the results to the train_accuracy and test_accuracy arrays respectively.

```python
# Setup arrays to store train and test accuracies
neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

# Loop over different values of k
for i, k in enumerate(neighbors):
    # Setup a k-NN Classifier with k neighbors: knn
    knn = KNeighborsClassifier(n_neighbors=k)

    # Fit the classifier to the training data
    knn.fit(X_train, y_train)
    
    #Compute accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)

    #Compute accuracy on the testing set
    test_accuracy[i] = knn.score(X_test, y_test)

# Generate plot
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label = 'Testing Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()
```

### Results :  

see : img/graph5.svg

Great work! It looks like the test accuracy is highest when using 3 and 5 neighbors. Using 8 neighbors or more seems to result in a simple model that underfits the data. Now that you've grasped the fundamentals of classification, you will learn about regression in the next chapter!  

---