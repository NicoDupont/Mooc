10/2017  
Datcamp - Supervised Learning with scikit-learn  

---

***Course Description***  

At the end of day, the value of Data Scientists rests on their ability to describe the world and to make predictions. Machine Learning is the field of teaching machines and computers to learn from existing data to make predictions on new data - will a given tumor be benign or malignant? Which of your customers will take their business elsewhere? Is a particular email spam or not? In this course, you'll learn how to use Python to perform supervised learning, an essential component of Machine Learning. You'll learn how to build predictive models, how to tune their parameters and how to tell how well they will perform on unseen data, all the while using real world datasets. You'll do so using scikit-learn, one of the most popular and user-friendly machine learning libraries for Python.  
 
# Part 4 : Preprocessing and pipelines 

Having trained your model, your next task is to evaluate its performance. What metrics can you use to gauge how good your model is? So far, you have used accuracy for classification and R-squared for regression. In this chapter, you will learn about some of the other metrics available in scikit-learn that will allow you to assess your model's performance in a more nuanced manner. You will then learn to optimize both your classification as well as regression models using hyperparameter tuning.  

## Exploring categorical features  

The Gapminder dataset that you worked with in previous chapters also contained a categorical 'Region' feature, which we dropped in previous exercises since you did not have the tools to deal with it. Now however, you do, so we have added it back in!  

Your job in this exercise is to explore this feature. Boxplots are particularly useful for visualizing categorical features such as this.  

### Instructions :

- Import pandas as pd.
- Read the CSV file 'gapminder.csv' into a DataFrame called df.
- Use pandas to create a boxplot showing the variation of life expectancy ('life') by region ('Region'). To do so, pass the column names in to df.boxplot() (in that order).

```python
# Import pandas
import pandas as pd

# Read 'gapminder.csv' into a DataFrame: df
df = pd.read_csv('gapminder.csv')

# Create a boxplot of life expectancy per region
df.boxplot('life', 'Region', rot=60)

# Show the plot
plt.show()
```

### Results :  

see :  img/graph13.svg

Great work! Exploratory data analysis should always be the precursor to model building.  

---

## Creating dummy variables  

As Andy discussed in the video, scikit-learn does not accept non-numerical features. You saw in the previous exercise that the 'Region' feature contains very useful information that can predict life expectancy. For example, Sub-Saharan Africa has a lower life expectancy compared to Europe and Central Asia. Therefore, if you are trying to predict life expectancy, it would be preferable to retain the 'Region' feature. To do this, you need to binarize it by creating dummy variables, which is what you will do in this exercise.  

### Instructions :

- Use the pandas get_dummies() function to create dummy variables from the df DataFrame. Store the result as df_region.
- Print the columns of df_region. This has been done for you.
- Use the get_dummies() function again, this time specifying drop_first=True to drop the unneeded dummy variable (in this case, 'Region_America').
- Hit 'Submit Answer to print the new columns of df_region and take note of how one column was dropped!

```python
# Create dummy variables: df_region
df_region = pd.get_dummies(df)

# Print the columns of df_region
print(df_region.columns)

# Create dummy variables with drop_first=True: df_region
df_region = pd.get_dummies(df,drop_first=True)

# Print the new columns of df_region
print(df_region.columns)
```

### Results :  

	<script.py> output:
	    Index(['population', 'fertility', 'HIV', 'CO2', 'BMI_male', 'GDP',
		   'BMI_female', 'life', 'child_mortality', 'Region_America',
		   'Region_East Asia & Pacific', 'Region_Europe & Central Asia',
		   'Region_Middle East & North Africa', 'Region_South Asia',
		   'Region_Sub-Saharan Africa'],
		  dtype='object')
	    Index(['population', 'fertility', 'HIV', 'CO2', 'BMI_male', 'GDP',
		   'BMI_female', 'life', 'child_mortality', 'Region_East Asia & Pacific',
		   'Region_Europe & Central Asia', 'Region_Middle East & North Africa',
		   'Region_South Asia', 'Region_Sub-Saharan Africa'],
		  dtype='object')

Excellent! Now that you have created the dummy variables, you can use the 'Region' feature to predict life expectancy!  

---

## Regression with categorical features

Having created the dummy variables from the 'Region' feature, you can build regression models as you did before. Here, you'll use ridge regression to perform 5-fold cross-validation.  

The feature array X and target variable array y have been pre-loaded.  

### Instructions :

- Import Ridge from sklearn.linear_model and cross_val_score from sklearn.model_selection.
- Instantiate a ridge regressor called ridge with alpha=0.5 and normalize=True.
- Perform 5-fold cross-validation on X and y using the cross_val_score() function.
- Print the cross-validated scores.

```python
# Import necessary modules
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge

# Instantiate a ridge regressor: ridge
ridge = Ridge(alpha=0.5,normalize=True)

# Perform 5-fold cross-validation: ridge_cv
ridge_cv = cross_val_score(ridge, X, y, cv=5)

# Print the cross-validated scores
print(ridge_cv)
```

### Results :  

	<script.py> output:
	    [ 0.86808336  0.80623545  0.84004203  0.7754344   0.87503712]

Excellent! You now know how to build models using data that includes categorical features.  

---

## Dropping missing data

The voting dataset from Chapter 1 contained a bunch of missing values that we dealt with for you behind the scenes. Now, it's time for you to take care of these yourself!  

The unprocessed dataset has been loaded into a DataFrame df. Explore it in the IPython Shell with the .head() method. You will see that there are certain data points labeled with a '?'. These denote missing values. As you saw in the video, different datasets encode missing values in different ways. Sometimes it may be a '9999', other times a 0 - real-world data can be very messy! If you're lucky, the missing values will already be encoded as NaN. We use NaN because it is an efficient and simplified way of internally representing missing data, and it lets us take advantage of pandas methods such as .dropna() and .fillna(), as well as scikit-learn's Imputation transformer Imputer().  

In this exercise, your job is to convert the '?'s to NaNs, and then drop the rows that contain them from the DataFrame.  

### Instructions :

- Explore the DataFrame df in the IPython Shell. Notice how the missing value is represented.
- Convert all '?' data points to np.nan.
- Count the total number of NaNs using the .isnull() and .sum() methods. This has been done for you.
- Drop the rows with missing values from df using .dropna().
- Hit 'Submit Answer' to see how many rows were lost by dropping the missing values.

```python
# Convert '?' to NaN
df[df == '?'] = np.nan

# Print the number of NaNs
print(df.isnull().sum())

# Print shape of original DataFrame
print("Shape of Original DataFrame: {}".format(df.shape))

# Drop missing values and print shape of new DataFrame
df = df.dropna()

# Print shape of new DataFrame
print("Shape of DataFrame After Dropping All Rows with Missing Values: {}".format(df.shape))
```

### Results :  

	<script.py> output:
	    party                  0
	    infants               12
	    water                 48
	    budget                11
	    physician             11
	    salvador              15
	    religious             11
	    satellite             14
	    aid                   15
	    missile               22
	    immigration            7
	    synfuels              21
	    education             31
	    superfund             25
	    crime                 17
	    duty_free_exports     28
	    eaa_rsa              104
	    dtype: int64
	    Shape of Original DataFrame: (435, 17)
	    Shape of DataFrame After Dropping All Rows with Missing Values: (232, 17)

Great work! When many values in your dataset are missing, if you drop them, you may end up throwing away valuable information along with the missing data. It's better instead to develop an imputation strategy. This is where domain knowledge is useful, but in the absence of it, you can impute missing values with the mean or the median of the row or column that the missing value is in  

---

## Imputing missing data in a ML Pipeline I

As you've come to appreciate, there are many steps to building a model, from creating training and test sets, to fitting a classifier or regressor, to tuning its parameters, to evaluating its performance on new data. Imputation can be seen as the first step of this machine learning process, the entirety of which can be viewed within the context of a pipeline. Scikit-learn provides a pipeline constructor that allows you to piece together these steps into one process and thereby simplify your workflow.  

You'll now practice setting up a pipeline with two steps: the imputation step, followed by the instantiation of a classifier. You've seen three classifiers in this course so far: k-NN, logistic regression, and the decision tree. You will now be introduced to a fourth one - the Support Vector Machine, or SVM. For now, do not worry about how it works under the hood. It works exactly as you would expect of the scikit-learn estimators that you have worked with previously, in that it has the same .fit() and .predict() methods as before.  

### Instructions :

- Import Imputer from sklearn.preprocessing and SVC from sklearn.svm. SVC stands for Support Vector Classification, which is a type of SVM.
- Setup the Imputation transformer to impute missing data (represented as 'NaN') with the 'most_frequent' value in the column (axis=0).
- Instantiate a SVC classifier. Store the result in clf.
- Create the steps of the pipeline by creating a list of tuples:
	- The first tuple should consist of the imputation step, using imp.
	- The second should consist of the classifier.

```python
# Import the Imputer module
from sklearn.svm import SVC
from sklearn.preprocessing import Imputer

# Setup the Imputation transformer: imp
imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)

# Instantiate the SVC classifier: clf
clf = SVC()

# Setup the pipeline with the required steps: steps
steps = [('imputation', imp),
        ('SVM', clf)]
```

### Results :  

Fantastic! Having set up the pipeline steps, you can now use it for classification.  

---

## Imputing missing data in a ML Pipeline II  

Having setup the steps of the pipeline in the previous exercise, you will now use it on the voting dataset to classify a Congressman's party affiliation. What makes pipelines so incredibly useful is the simple interface that they provide. You can use the .fit() and .predict() methods on pipelines just as you did with your classifiers and regressors!  

Practice this for yourself now and generate a classification report of your predictions. The steps of the pipeline have been set up for you, and the feature array X and target variable array y have been pre-loaded. Additionally, train_test_split and classification_report have been imported from sklearn.model_selection and sklearn.metrics respectively.  

### Instructions :

- Import the following modules:
	- Imputer from sklearn.preprocessing and Pipeline from sklearn.pipeline.
	- SVC from sklearn.svm.
- Create the pipeline using Pipeline() and steps.
- Create training and test sets. Use 30% of the data for testing and a random state of 42.
- Fit the pipeline to the training set and predict the labels of the test set.
- Compute the classification report.


```python
# Import necessary modules
from sklearn.preprocessing import Imputer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

# Setup the pipeline steps: steps
steps = [('imputation', Imputer(missing_values='NaN', strategy='most_frequent', axis=0)),
        ('SVM', SVC())]

# Create the pipeline: pipeline
pipeline = Pipeline(steps)

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)

# Fit the pipeline to the train set
pipeline.fit(X_train,y_train)

# Predict the labels of the test set
y_pred = pipeline.predict(X_test)

# Compute metrics
print(classification_report(y_test, y_pred))
```

### Results :  

	<script.py> output:
		         precision    recall  f1-score   support
	    
	       democrat       0.99      0.96      0.98        85
	     republican       0.94      0.98      0.96        46
	    
	    avg / total       0.97      0.97      0.97       131

Great work! Your pipeline has performed imputation as well as classification!  

---

## Centering and scaling your data

In the video, Hugo demonstrated how significantly the performance of a model can improve if the features are scaled. Note that this is not always the case: In the Congressional voting records dataset, for example, all of the features are binary. In such a situation, scaling will have minimal impact.  

You will now explore scaling for yourself on a new dataset - White Wine Quality! Hugo used the Red Wine Quality dataset in the video. We have used the 'quality' feature of the wine to create a binary target variable: If 'quality' is less than 5, the target variable is 1, and otherwise, it is 0.  

The DataFrame has been pre-loaded as df, along with the feature and target variable arrays X and y. Explore it in the IPython Shell. Notice how some features seem to have different units of measurement. 'density', for instance, only takes values between 0 and 1, while 'total sulfur dioxide' has a maximum value of 289. As a result, it may be worth scaling the features here. Your job in this exercise is to scale the features and compute the mean and standard deviation of the unscaled features compared to the scaled features.  

### Instructions :

- Import scale from sklearn.preprocessing.
- Scale the features X using scale().
- Print the mean and standard deviation of the unscaled features X, and then the scaled features X_scaled. Use the numpy functions np.mean() and np.std() to compute the mean and standard deviations.

```python
# Import the necessary modules
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Setup the pipeline steps: steps
steps = [('scaler', StandardScaler()),
        ('knn', KNeighborsClassifier())]
        
# Create the pipeline: pipeline
pipeline = Pipeline(steps)

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)

# Fit the pipeline to the training set: knn_scaled
knn_scaled = pipeline.fit(X_train,y_train)

# Instantiate and fit a k-NN classifier to the unscaled data
knn_unscaled = KNeighborsClassifier().fit(X_train, y_train)

# Compute and print metrics
print('Accuracy with Scaling: {}'.format(knn_scaled.score(X_test, y_test)))
print('Accuracy without Scaling: {}'.format(knn_unscaled.score(X_test, y_test)))
```

### Results :  

	<script.py> output:
		Accuracy with Scaling: 0.7700680272108843
		Accuracy without Scaling: 0.6979591836734694

Fantastic! It looks like scaling has significantly improved model performance!  
		
---

## Bringing it all together I: Pipeline for classification  

It is time now to piece together everything you have learned so far into a pipeline for classification! Your job in this exercise is to build a pipeline that includes scaling and hyperparameter tuning to classify wine quality.  

You'll return to using the SVM classifier you were briefly introduced to earlier in this chapter. The hyperparameters you will tune are CC and gammagamma. CC controls the regularization strength. It is analogous to the CC you tuned for logistic regression in Chapter 3, while gammagamma controls the kernel coefficient: Do not worry about this now as it is beyond the scope of this course.  

The following modules have been pre-loaded: Pipeline, svm, train_test_split, GridSearchCV, classification_report, accuracy_score. The feature and target variable arrays X and y have also been pre-loaded.  

### Instructions :

- Setup the pipeline with the following steps:
	- Scaling, called 'scaler' with StandardScaler().
	- Classification, called 'SVM' with SVC().
- Specify the hyperparameter space using the following notation: 'step_name__parameter_name'. Here, the step_name is SVM, and the parameter_names are C and gamma.
- Create training and test sets, with 20% of the data used for the test set. Use a random state of 21.
- Instantiate GridSearchCV with the pipeline and hyperparameter space and fit it to the training set. Use 3-fold cross-validation (This is the default, so you don't have to specify it).
- Predict the labels of the test set and compute the metrics. The metrics have been computed for you.

```python
# Setup the pipeline
steps = [('scaler', StandardScaler()),
         ('SVM', SVC())]

pipeline = Pipeline(steps)

# Specify the hyperparameter space
parameters = {'SVM__C':[1, 10, 100],
              'SVM__gamma':[0.1, 0.01]}

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=21)

# Instantiate the GridSearchCV object: cv
cv = GridSearchCV(pipeline, param_grid=parameters)

# Fit to the training set
cv.fit(X_train,y_train)

# Predict the labels of the test set: y_pred
y_pred = cv.predict(X_test)

# Compute and print metrics
print("Accuracy: {}".format(cv.score(X_test, y_test)))
print(classification_report(y_test, y_pred))
print("Tuned Model Parameters: {}".format(cv.best_params_))
```

### Results :  

	<script.py> output:
		Accuracy: 0.7795918367346939
					 precision    recall  f1-score   support
		
			  False       0.83      0.85      0.84       662
			   True       0.67      0.63      0.65       318
		
		avg / total       0.78      0.78      0.78       980
		
		Tuned Model Parameters: {'SVM__C': 10, 'SVM__gamma': 0.1}

---

## Bringing it all together II: Pipeline for regression  

For this final exercise, you will return to the Gapminder dataset. Guess what? Even this dataset has missing values that we dealt with for you in earlier chapters! Now, you have all the tools to take care of them yourself!  

Your job is to build a pipeline that imputes the missing data, scales the features, and fits an ElasticNet to the Gapminder data. You will then tune the l1_ratio of your ElasticNet using GridSearchCV.  

All the necessary modules have been imported, and the feature and target variable arrays have been pre-loaded as X and y.  

### Instructions :

- Set up a pipeline with the following steps:
	- 'imputation', which uses the Imputer() transformer and the 'mean' strategy to impute missing data ('NaN') using the mean of the column.
	- 'scaler', which scales the features using StandardScaler().
	- 'elasticnet', which instantiates an ElasticNet regressor.
- Specify the hyperparameter space for the l1l1 ratio using the following notation: 'step_name__parameter_name'. Here, the step_name is elasticnet, and the parameter_name is l1_ratio.
- Create training and test sets, with 40% of the data used for the test set. Use a random state of 42.
- Instantiate GridSearchCV with the pipeline and hyperparameter space. Use 3-fold cross-validation (This is the default, so you don't have to specify it).
- Fit the GridSearchCV object to the training set.
- Compute R squarred and the best parameters. This has been done for you, so hit 'Submit Answer' to see the results!

```python
# Setup the pipeline steps: steps
steps = [('imputation', Imputer(missing_values='NaN', strategy='mean', axis=0)),
         ('scaler', StandardScaler()),
         ('elasticnet', ElasticNet())]

# Create the pipeline: pipeline 
pipeline = Pipeline(steps)

# Specify the hyperparameter space
parameters = {'elasticnet__l1_ratio':np.linspace(0,1,30)}

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=42)

# Create the GridSearchCV object: gm_cv
gm_cv = GridSearchCV(pipeline, param_grid=parameters)

# Fit to the training set
gm_cv.fit(X_train,y_train)

# Compute and print the metrics
r2 = gm_cv.score(X_test, y_test)
print("Tuned ElasticNet Alpha: {}".format(gm_cv.best_params_))
print("Tuned ElasticNet R squared: {}".format(r2))
```

### Results :  

	<script.py> output:
		Tuned ElasticNet Alpha: {'elasticnet__l1_ratio': 1.0}
		Tuned ElasticNet R squared: 0.8862016570888217

Fantastic work! You have now mastered the fundamentals of supervised learning with scikit-learn!  

---