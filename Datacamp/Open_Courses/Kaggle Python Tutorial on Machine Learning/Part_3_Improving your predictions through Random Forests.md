11/2017  
# Datacamp - Kaggle Python Tutorial on Machine Learning  
[Kaggle Python Tutorial on Machine Learning](https://www.datacamp.com/community/open-courses/kaggle-python-tutorial-on-machine-learning)

---

## Course description :

Always wanted to compete in a Kaggle competition but not sure you have the right skillset? This interactive tutorial by Kaggle and DataCamp on Machine Learning offers the solution. Step-by-step you will learn through fun coding exercises how to predict survival rate for Kaggle's Titanic competition using Machine Learning techniques. Upload your results and see your ranking go up!   

New to Python? Give our Introduction to Python for Data Science course a try.  

# Part 3 : Improving your predictions through Random Forests  

What techniques can you use to improve your predictions even more? One possible way is by making use of the machine learning method Random Forest. Namely, a forest is just a collection of trees...    

## A Random Forest analysis in Python      

A detailed study of Random Forests would take this tutorial a bit too far. However, since it's an often used machine learning technique, gaining a general understanding in Python won't hurt.  

In layman's terms, the Random Forest technique handles the overfitting problem you faced with decision trees. It grows multiple (very deep) classification trees using the training set. At the time of prediction, each tree is used to come up with a prediction and every outcome is counted as a vote. For example, if you have trained 3 trees with 2 saying a passenger in the test set will survive and 1 says he will not, the passenger will be classified as a survivor. This approach of overtraining trees, but having the majority's vote count as the actual classification decision, avoids overfitting.  

Building a random forest in Python looks almost the same as building a decision tree; so we can jump right to it. There are two key differences, however. Firstly, a different class is used. And second, a new argument is necessary. Also, we need to import the necessary library from scikit-learn.  

Use RandomForestClassifier() class instead of the DecisionTreeClassifier() class.
n_estimators needs to be set when using the RandomForestClassifier() class. This argument allows you to set the number of trees you wish to plant and average over.
The latest training and testing data are preloaded for you.  

### Instructions  

 - Build the random forest with n_estimators set to 100.
 - Fit your random forest model with inputs features_forest and target.
 - Compute the classifier predictions on the selected test set features.

```python
# Import the `RandomForestClassifier`
from sklearn.ensemble import RandomForestClassifier

# We want the Pclass, Age, Sex, Fare,SibSp, Parch, and Embarked variables
features_forest = train[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"]].values

# Building and fitting my_forest
forest = RandomForestClassifier(max_depth = 10, min_samples_split=2, n_estimators = 100, random_state = 1)
my_forest = forest.fit(features_forest, target)

# Print the score of the fitted random forest
print(my_forest.score(features_forest, target))

# Compute predictions on our test set features then print the length of the prediction vector
test_features = test[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"]].values
pred_forest = my_forest.predict(test_features)
print(len(pred_forest))

```

### Results :  

	<script.py> output:
		0.939393939394
		418

---



## Interpreting and Comparing    

Remember how we looked at .feature_importances_ attribute for the decision trees? Well, you can request the same attribute from your random forest as well and interpret the relevance of the included variables. You might also want to compare the models in some quick and easy way. For this, we can use the .score() method. The .score() method takes the features data and the target vector and computes mean accuracy of your model. You can apply this method to both the forest and individual trees. Remember, this measure should be high but not extreme because that would be a sign of overfitting.  

For this exercise, you have my_forest and my_tree_two available to you. The features and target arrays are also ready for use.  

### Instructions  

 - Explore the feature importance for both models
 - Compare the mean accuracy score of the two models

```python
#Request and print the `.feature_importances_` attribute
print(my_tree_two.feature_importances_)
print(my_forest.feature_importances_)

#Compute and print the mean accuracy score for both models
print(my_tree_two.score(features_two, target))
print(my_forest.score(features_two, target))
```

### Results :  

	<script.py> output:
		[ 0.14130255  0.17906027  0.41616727  0.17938711  0.05039699  0.01923751
		  0.0144483 ]
		[ 0.10384741  0.20139027  0.31989322  0.24602858  0.05272693  0.04159232
		  0.03452128]
		0.905723905724
		0.939393939394		
		
---


## Conclude and Submit     

Based on your finding in the previous exercise determine which feature was of most importance, and for which model. After this final exercise, you will be able to submit your random forest model to Kaggle! Use my_forest, my_tree_two, and feature_importances_ to answer the question.   

### Instructions  

 - The most important feature was "Age", but it was more significant for "my_tree_two"
 - The most important feature was "Sex", but it was more significant for "my_tree_two"
 - The most important feature was "Sex", but it was more significant for "my_forest"
 - The most important feature was "Age", but it was more significant for "my_forest"

```python
my_forest.feature_importances_
my_tree_two.feature_importances_
```

### Results :  

	In [1]: my_forest.feature_importances_
	Out[1]: 
	array([ 0.11283434,  0.20208835,  0.3239109 ,  0.23224813,  0.05627229,
			0.03899841,  0.03364757])

	In [2]: my_tree_two.feature_importances_
	Out[2]: 
	array([ 0.13961747,  0.18226803,  0.41120433,  0.17444813,  0.05357815,
			0.02262501,  0.01625888])

Wonderful! You are now at the end of this tutorial and ready to start improving the results yourself  		
		
---
