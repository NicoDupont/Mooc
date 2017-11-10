11/2017  
# Datacamp - Kaggle Python Tutorial on Machine Learning  
[Kaggle Python Tutorial on Machine Learning](https://www.datacamp.com/community/open-courses/kaggle-python-tutorial-on-machine-learning)

---

## Course description :

Always wanted to compete in a Kaggle competition but not sure you have the right skillset? This interactive tutorial by Kaggle and DataCamp on Machine Learning offers the solution. Step-by-step you will learn through fun coding exercises how to predict survival rate for Kaggle's Titanic competition using Machine Learning techniques. Upload your results and see your ranking go up!   

New to Python? Give our Introduction to Python for Data Science course a try.  


# Part 1 : Exploring the raw data   

In this chapter we will go trough the essential steps that you will need to take before beginning to build predictive models.   

## How it works    

Welcome to our Kaggle Machine Learning Tutorial. In this tutorial, you will explore how to tackle Kaggle Titanic competition using Python and Machine Learning. In case you're new to Python, it's recommended that you first take our free Introduction to Python for Data Science Tutorial. Furthermore, while not required, familiarity with machine learning techniques is a plus so you can get the maximum out of this tutorial.  

In the editor on the right, you should type Python code to solve the exercises. When you hit the 'Submit Answer' button, every line of code is interpreted and executed by Python and you get a message whether or not your code was correct. The output of your Python code is shown in the console in the lower right corner. Python makes use of the # sign to add comments; these lines are not run as Python code, so they will not influence your result.  

You can also execute Python commands straight in the console. This is a good way to experiment with Python code, as your submission is not checked for correctness.  

### Instructions  

 - In the editor to the right, you see some Python code and annotations. This is what a typical exercise will look like.
 - To complete the exercise and see how the interactive environment works add the code to compute y and hit the Submit Answer button. Don't forget to print the result.

```python
#Compute x = 4 * 3 and print the result
x = 4 * 3
print(x)

#Compute y = 6 * 9 and print the result
y = 6 * 9
print(y)
```

### Results :  

	<script.py> output:
		12
		54

Awesome! See how the console shows the result of the Python code you submitted? Now that you're familiar with the interface, let's get down to business!  		
		
---

## Get the Data with Pandas    

When the Titanic sank, 1502 of the 2224 passengers and crew were killed. One of the main reasons for this high level of casualties was the lack of lifeboats on this self-proclaimed "unsinkable" ship.  

Those that have seen the movie know that some individuals were more likely to survive the sinking (lucky Rose) than others (poor Jack). In this course, you will learn how to apply machine learning techniques to predict a passenger's chance of surviving using Python.  

Let's start with loading in the training and testing set into your Python environment. You will use the training set to build your model, and the test set to validate it. The data is stored on the web as csv files; their URLs are already available as character strings in the sample code. You can load this data with the read_csv() method from the Pandas library.  

### Instructions  

 - First, import the Pandas library as pd.
 - Load the test data similarly to how the train data is loaded.
 - Inspect the first couple rows of the loaded dataframes using the .head() method with the code provided.

```python
# Import the Pandas library
import pandas as pd

# Load the train and test datasets to create two DataFrames
train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train = pd.read_csv(train_url)

test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test = pd.read_csv(test_url)

#Print the `head` of the train and test dataframes
print(train.head())
print(test.head())
```

### Results :  

	<script.py> output:
		   PassengerId  Survived  Pclass  \
		0            1         0       3   
		1            2         1       1   
		2            3         1       3   
		3            4         1       1   
		4            5         0       3   
		
														Name     Sex   Age  SibSp  \
		0                            Braund, Mr. Owen Harris    male  22.0      1   
		1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
		2                             Heikkinen, Miss. Laina  female  26.0      0   
		3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   
		4                           Allen, Mr. William Henry    male  35.0      0   
		
		   Parch            Ticket     Fare Cabin Embarked  
		0      0         A/5 21171   7.2500   NaN        S  
		1      0          PC 17599  71.2833   C85        C  
		2      0  STON/O2. 3101282   7.9250   NaN        S  
		3      0            113803  53.1000  C123        S  
		4      0            373450   8.0500   NaN        S  
		   PassengerId  Pclass                                          Name     Sex  \
		0          892       3                              Kelly, Mr. James    male   
		1          893       3              Wilkes, Mrs. James (Ellen Needs)  female   
		2          894       2                     Myles, Mr. Thomas Francis    male   
		3          895       3                              Wirz, Mr. Albert    male   
		4          896       3  Hirvonen, Mrs. Alexander (Helga E Lindqvist)  female   
		
			Age  SibSp  Parch   Ticket     Fare Cabin Embarked  
		0  34.5      0      0   330911   7.8292   NaN        Q  
		1  47.0      1      0   363272   7.0000   NaN        S  
		2  62.0      0      0   240276   9.6875   NaN        Q  
		3  27.0      0      0   315154   8.6625   NaN        S  
		4  22.0      1      1  3101298  12.2875   NaN        S		

Well done! Now that your data is loaded in, let's see if you can understand it.  
		
---


## Understanding your data     

Before starting with the actual analysis, it's important to understand the structure of your data. Both test and train are DataFrame objects, the way pandas represent datasets. You can easily explore a DataFrame using the .describe() method. .describe() summarizes the columns/features of the DataFrame, including the count of observations, mean, max and so on. Another useful trick is to look at the dimensions of the DataFrame. This is done by requesting the .shape attribute of your DataFrame object. (ex. your_data.shape)  

The training and test set are already available in the workspace, as train and test. Apply .describe() method and print the .shape attribute of the training set. Which of the following statements is correct?  

### Possible Answers  => 1

 - The training set has 891 observations and 12 variables, count for Age is 714.
 - The training set has 418 observations and 11 variables, count for Age is 891.
 - The testing set has 891 observations and 11 variables, count for Age is 891.
 - The testing set has 418 observations and 12 variables, count for Age is 714.

```python

```

### Results :  
	
		
---


## Rose vs Jack, or Female vs Male   

How many people in your training set survived the disaster with the Titanic? To see this, you can use the value_counts() method in combination with standard bracket notation to select a single column of a DataFrame:  

```python
# absolute numbers
train["Survived"].value_counts()
```

```python
# percentages
train["Survived"].value_counts(normalize = True)
```

If you run these commands in the console, you'll see that 549 individuals died (62%) and 342 survived (38%). A simple way to predict heuristically could be: "majority wins". This would mean that you will predict every unseen observation to not survive.  

To dive in a little deeper we can perform similar counts and percentage calculations on subsets of the Survived column. For example, maybe gender could play a role as well? You can explore this using the .value_counts() method for a two-way comparison on the number of males and females that survived, with this syntax:  

```python
train["Survived"][train["Sex"] == 'male'].value_counts()
train["Survived"][train["Sex"] == 'female'].value_counts()
```

To get proportions, you can again pass in the argument normalize = True to the .value_counts() method.  

### Instructions  

 - Calculate and print the survival rates in absolute numbers using values_counts() method.
 - Calculate and print the survival rates as proportions by setting the normalize argument to True.
 - Repeat the same calculations but on subsets of survivals based on Sex.

```python
# Passengers that survived vs passengers that passed away
print(train["Survived"].value_counts())

# As proportions
print(train["Survived"].value_counts(normalize = True))

# Males that survived vs males that passed away
print(train["Survived"][train["Sex"] == 'male'].value_counts())

# Females that survived vs Females that passed away
print(train["Survived"][train["Sex"] != 'male'].value_counts())

# Normalized male survival
print(train["Survived"][train["Sex"] == 'male'].value_counts(normalize = True))

# Normalized female survival
print(train["Survived"][train["Sex"] != 'male'].value_counts(normalize = True))
```

### Results :  

	<script.py> output:
		0    549
		1    342
		Name: Survived, dtype: int64
		0    0.616162
		1    0.383838
		Name: Survived, dtype: float64
		0    468
		1    109
		Name: Survived, dtype: int64
		1    233
		0     81
		Name: Survived, dtype: int64
		0    0.811092
		1    0.188908
		Name: Survived, dtype: float64
		1    0.742038
		0    0.257962
		Name: Survived, dtype: float64		

Well done! It looks like it makes sense to predict that all females will survive, and all men will die.  
		
---


## Does age play a role?     

Another variable that could influence survival is age; since it's probable that children were saved first. You can test this by creating a new column with a categorical variable Child. Child will take the value 1 in cases where age is less than 18, and a value of 0 in cases where age is greater than or equal to 18.    

To add this new variable you need to do two things (i) create a new column, and (ii) provide the values for each observation (i.e., row) based on the age of the passenger.    

Adding a new column with Pandas in Python is easy and can be done via the following syntax:    

```python
your_data["new_var"] = 0
```

This code would create a new column in the train DataFrame titled new_var with 0 for each observation.    

To set the values based on the age of the passenger, you make use of a boolean test inside the square bracket operator. With the []-operator you create a subset of rows and assign a value to a certain variable of that subset of observations. For example,   
 
```python
train["new_var"][train["Fare"] > 10] = 1
```

would give a value of 1 to the variable new_var for the subset of passengers whose fares greater than 10. Remember that new_var has a value of 0 for all other values (including missing values).    

A new column called Child in the train data frame has been created for you that takes the value NaN for all observations.    

### Instructions  

 - Set the values of Child to 1 is the passenger's age is less than 18 years.
 - Then assign the value 0 to observations where the passenger is greater than or equal to 18 years in the new Child column.
 - Compare the normalized survival rates for those who are <18 and those who are older. Use code similar to what you had in the previous exercise.

```python
# Create the column Child and assign to 'NaN'
train["Child"] = float('NaN')

# Assign 1 to passengers under 18, 0 to those 18 or older. Print the new column.
train["Child"][train["Age"] < 18] = 1
train["Child"][train["Age"] >= 18] = 0
print(train["Child"])

# Print normalized Survival Rates for passengers under 18
print(train["Survived"][train["Child"] == 1].value_counts(normalize = True))

# Print normalized Survival Rates for passengers 18 or older
print(train["Survived"][train["Child"] == 0].value_counts(normalize = True))
```

### Results :  

	<script.py> output:
		0      0.0
		1      0.0
		2      0.0
		3      0.0
		4      0.0
		5      NaN
		6      0.0
		7      1.0
		8      0.0
		9      1.0
		10     1.0
		11     0.0
		12     0.0
		13     0.0
		14     1.0
		15     0.0
		16     1.0
		17     NaN
		18     0.0
		19     NaN
		20     0.0
		21     0.0
		22     1.0
		23     0.0
		24     1.0
		25     0.0
		26     NaN
		27     0.0
		28     NaN
		29     NaN
			  ... 
		861    0.0
		862    0.0
		863    NaN
		864    0.0
		865    0.0
		866    0.0
		867    0.0
		868    NaN
		869    1.0
		870    0.0
		871    0.0
		872    0.0
		873    0.0
		874    0.0
		875    1.0
		876    0.0
		877    0.0
		878    NaN
		879    0.0
		880    0.0
		881    0.0
		882    0.0
		883    0.0
		884    0.0
		885    0.0
		886    0.0
		887    0.0
		888    NaN
		889    0.0
		890    0.0
		Name: Child, dtype: float64
		1    0.539823
		0    0.460177
		Name: Survived, dtype: float64
		0    0.618968
		1    0.381032
		Name: Survived, dtype: float64		

Well done! As you can see from the survival proportions, age does certainly seem to play a role.  
		
---


## First Prediction    

In one of the previous exercises you discovered that in your training set, females had over a 50% chance of surviving and males had less than a 50% chance of surviving. Hence, you could use this information for your first prediction: all females in the test set survive and all males in the test set die.  

You use your test set for validating your predictions. You might have seen that contrary to the training set, the test set has no Survived column. You add such a column using your predicted values. Next, when uploading your results, Kaggle will use this variable (= your predictions) to score your performance.   

### Instructions  

 - Create a variable test_one, identical to dataset test
 - Add an additional column, Survived, that you initialize to zero.
 - Use vector subsetting like in the previous exercise to set the value of Survived to 1 for observations whose Sex equals "female".
 - Print the Survived column of predictions from the test_one dataset.

```python
# Create a copy of test: test_one
test_one = test

# Initialize a Survived column to 0
test_one["Survived"] = 0

# Set Survived to 1 if Sex equals "female" and print the `Survived` column from `test_one`
test_one["Survived"][test_one["Sex"] == 'female'] = 1
test_one["Survived"][test_one["Sex"] == 'male'] = 0
print(test_one["Survived"])
```

### Results :  

	<script.py> output:
		0      0
		1      1
		2      0
		3      0
		4      1
		5      0
		6      1
		7      0
		8      1
		9      0
		10     0
		11     0
		12     1
		13     0
		14     1
		15     1
		16     0
		17     0
		18     1
		19     1
		20     0
		21     0
		22     1
		23     0
		24     1
		25     0
		26     1
		27     0
		28     0
		29     0
			  ..
		388    0
		389    0
		390    0
		391    1
		392    0
		393    0
		394    0
		395    1
		396    0
		397    1
		398    0
		399    0
		400    1
		401    0
		402    1
		403    0
		404    0
		405    0
		406    0
		407    0
		408    1
		409    1
		410    1
		411    1
		412    1
		413    0
		414    1
		415    0
		416    0
		417    0
		Name: Survived, dtype: int64		

Well done! If you want, you can already submit these first predictions to Kaggle by uploading this csv file. In the next chapter, you will learn how to make more advanced predictions and create your own .csv file from Python.  
		
---