10/2017  
Datcamp - Supervised Learning with scikit-learn  

---

***Course Description***  

At the end of day, the value of Data Scientists rests on their ability to describe the world and to make predictions. Machine Learning is the field of teaching machines and computers to learn from existing data to make predictions on new data - will a given tumor be benign or malignant? Which of your customers will take their business elsewhere? Is a particular email spam or not? In this course, you'll learn how to use Python to perform supervised learning, an essential component of Machine Learning. You'll learn how to build predictive models, how to tune their parameters and how to tell how well they will perform on unseen data, all the while using real world datasets. You'll do so using scikit-learn, one of the most popular and user-friendly machine learning libraries for Python.  
 
# Part 2 : Regression  

In the previous chapter, you made use of image and political datasets to predict binary as well as multiclass outcomes. But what if your problem requires a continuous outcome? Regression, which is the focus of this chapter, is best suited to solving such problems. You will learn about fundamental concepts in regression and apply them to predict the life expectancy in a given country using Gapminder data.  

## Which of the following is a regression problem?  

Andy introduced regression to you using the Boston housing dataset. But regression models can be used in a variety of contexts to solve a variety of different problems.  

Given below are four example applications of machine learning. Your job is to pick the one that is best framed as a regression problem.  

### Possible Answers :  => 4

1. An e-commerce company using labeled customer data to predict whether or not a customer will purchase a particular item.
2. A healthcare company using data about cancer tumors (such as their geometric measurements) to predict whether a new tumor is benign or malignant.
3. A restaurant using review data to ascribe positive or negative sentiment to a given review.
4. A bike share company using time and weather data to predict the number of bikes being rented at any given hour.

```python

```

### Results :  

Great work! The target variable here - the number of bike rentals at any given hour - is quantitative, so this is best framed as a regression problem.  

---

## Loading and viewing your data

In this chapter, you will work with Gapminder data that we have consolidated into one CSV file available in the workspace as 'gapminder.csv'. Specifically, your goal will be to use this data to predict the life expectancy in a given country based on features such as the country's GDP, fertility rate, and population. As in Chapter 1, the dataset has been preprocessed.  

Since the target variable here is quantitative, this is a regression problem. To begin, you will fit a linear regression with just one feature: 'fertility', which is the average number of children a woman in a given country gives birth to. In later exercises, you will use all the features to build regression models.  

Before that, however, you need to import the data and get it into the form needed by scikit-learn. This involves creating feature and target variable arrays. Furthermore, since you are going to use only one feature to begin with, you need to do some reshaping using NumPy's .reshape() method. Don't worry too much about this reshaping right now, but it is something you will have to do occasionally when working with scikit-learn so it is useful to practice.  

### Instructions :

1. Import numpy and pandas as their standard aliases.
2. Read the file 'gapminder.csv' into a DataFrame df using the read_csv() function.
3. Create array X for the 'fertility' feature and array y for the 'life' target variable.
4. Reshape the arrays by using the .reshape() method and passing in (-1, 1).

```python
# Import numpy and pandas
import numpy as np
import pandas as pd

# Read the CSV file into a DataFrame: df
df = pd.read_csv('gapminder.csv')
print(df.head())
print('-----------')

# Create arrays for features and target variable
y = df.life.values
print(type(y))
print(y[:5])
print('-----------')
X = df.fertility.values

# Print the dimensions of X and y before reshaping
print("Dimensions of y before reshaping: {}".format(y.shape))
print("Dimensions of X before reshaping: {}".format(X.shape))

# Reshape X and y
y = y.reshape(-1, 1)
print(y[:5])
print('-----------')
X = X.reshape(-1, 1)

# Print the dimensions of X and y after reshaping
print("Dimensions of y after reshaping: {}".format(y.shape))
print("Dimensions of X after reshaping: {}".format(X.shape))
```

### Results :  

	<script.py> output:
	       population  fertility  HIV        CO2  BMI_male      GDP  BMI_female  life  \
	    0  34811059.0       2.73  0.1   3.328945  24.59620  12314.0    129.9049  75.3   
	    1  19842251.0       6.43  2.0   1.474353  22.25083   7103.0    130.1247  58.3   
	    2  40381860.0       2.24  0.5   4.785170  27.50170  14646.0    118.8915  75.5   
	    3   2975029.0       1.40  0.1   1.804106  25.35542   7383.0    132.8108  72.5   
	    4  21370348.0       1.96  0.1  18.016313  27.56373  41312.0    117.3755  81.5   
	    
	       child_mortality  
	    0             29.5  
	    1            192.0  
	    2             15.4  
	    3             20.0  
	    4              5.2  
	    -----------
	    <class 'numpy.ndarray'>
	    [ 75.3  58.3  75.5  72.5  81.5]
	    -----------
	    Dimensions of y before reshaping: (139,)
	    Dimensions of X before reshaping: (139,)
	    [[ 75.3]
	     [ 58.3]
	     [ 75.5]
	     [ 72.5]
	     [ 81.5]]
	    -----------
	    Dimensions of y after reshaping: (139, 1)
	    Dimensions of X after reshaping: (139, 1)

Great work! Notice the differences in shape before and after applying the .reshape() method. Getting the feature and target variable arrays into the right format for scikit-learn is an important precursor to model building.  

---

## Exploring the Gapminder data  

As always, it is important to explore your data before building models. On the right, we have constructed a heatmap showing the correlation between the different features of the Gapminder dataset, which has been pre-loaded into a DataFrame as df and is available for exploration in the IPython Shell. Cells that are in green show positive correlation, while cells that are in red show negative correlation. Take a moment to explore this: Which features are positively correlated with life, and which ones are negatively correlated? Does this match your intuition?  

Then, in the IPython Shell, explore the DataFrame using pandas methods such as .info(), .describe(), .head().  

In case you are curious, the heatmap was generated using Seaborn's heatmap function and the following line of code, where df.corr() computes the pairwise correlation between columns:  

```python
sns.heatmap(df.corr(), square=True, cmap='RdYlGn')
```

Once you have a feel for the data, consider the statements below and select the one that is not true. After this, Hugo will explain the mechanics of linear regression in the next video and you will be on your way building regression models!  

### Possible Answers : => 4

1. The DataFrame has 139 samples (or rows) and 9 columns.
2. life and fertility are negatively correlated.
3. The mean of life is 69.602878.
4. fertility is of type int64.
5. GDP and life are positively correlated.

```python

```

### Results :  

	In [1]: df.shape
	Out[1]: (139, 9)

	In [2]: df.describe
	Out[2]: 
	<bound method NDFrame.describe of       population  fertility    HIV        CO2  BMI_male      GDP  BMI_female  \
	0     34811059.0       2.73   0.10   3.328945  24.59620  12314.0    129.9049   
	1     19842251.0       6.43   2.00   1.474353  22.25083   7103.0    130.1247   
	2     40381860.0       2.24   0.50   4.785170  27.50170  14646.0    118.8915   
	3      2975029.0       1.40   0.10   1.804106  25.35542   7383.0    132.8108   
	4     21370348.0       1.96   0.10  18.016313  27.56373  41312.0    117.3755   
	5      8331465.0       1.41   0.30   8.183160  26.46741  43952.0    124.1394   
	6      8868713.0       1.99   0.10   5.109538  25.65117  14365.0    128.6024   
	7       348587.0       1.89   3.10   3.131921  27.24594  24373.0    124.3862   
	8    148252473.0       2.38   0.06   0.319161  20.39742   2265.0    125.0307   
	9       277315.0       1.83   1.30   6.008279  26.38439  16075.0    126.3940   
	10     9526453.0       1.42   0.20   6.488174  26.16443  14488.0    129.7968   
	11    10779155.0       1.82   0.20   9.797337  26.75915  41641.0    121.8227   
	12      306165.0       2.91   2.40   1.360126  27.02255   8293.0    120.9224   
	13     8973525.0       5.27   1.20   0.537539  22.41835   1646.0    130.2723   
	14      694990.0       2.51   0.20   0.601210  22.82180   5663.0    125.1258   
	15     9599916.0       3.48   0.20   1.431829  24.43335   5066.0    122.4155   
	16     1967866.0       2.86  24.90   2.547205  22.12984  13858.0    133.1307   
	17   194769696.0       1.90   0.45   2.023773  25.78623  13906.0    124.8745   
	18     7513646.0       1.43   0.10   6.690139  26.54286  15368.0    128.4721   
	19    14709011.0       6.04   1.20   0.109419  21.27157   1358.0    130.6651   
	20     8821795.0       6.48   3.50   0.031389  21.50291    723.0    134.1955   
	21    13933660.0       3.05   0.60   0.287547  20.80496   2442.0    117.5528   
	22    19570418.0       5.17   5.30   0.295542  23.68173   2571.0    127.2823   
	23    33363256.0       1.68   0.20  16.350399  27.45210  41468.0    118.0571   
	24    11139740.0       6.81   3.40   0.047839  21.48569   1753.0    127.8640   
	25    16645940.0       1.89   0.40   4.240259  27.01542  18698.0    125.5417   
	26    44901660.0       2.43   0.50   1.476092  24.94041  10489.0    124.0235   
	27      665414.0       5.05   0.06   0.178853  22.06131   1440.0    132.1354   
	28     3832771.0       5.10   3.50   0.384220  21.87134   5022.0    131.6935   
	29     4429506.0       1.91   0.30   1.911933  26.47897  12219.0    121.3500   
	..           ...        ...    ...        ...       ...      ...         ...   
	109    9109535.0       1.41   0.10   5.271223  26.51495  12522.0    130.3755   
	110    5521838.0       5.13   1.60   0.118256  22.53139   1289.0    134.7160   
	111    4849641.0       1.28   0.10   4.114441  23.83996  65991.0    121.1736   
	112    5396710.0       1.31   0.06   6.901654  26.92717  24670.0    129.5280   
	113    2030599.0       1.43   0.06   8.511828  27.43983  30816.0    129.9231   
	114    9132589.0       7.06   0.60   0.068219  21.96917    615.0    131.5318   
	115   50348811.0       2.54  17.90   9.427960  26.85538  12263.0    130.9949   
	116   45817016.0       1.42   0.40   7.293089  27.49975  34676.0    122.0453   
	117   19949553.0       2.32   0.06   0.580791  21.96671   6907.0    124.8615   
	118   34470138.0       4.79   1.00   0.382118  22.40484   3246.0    129.7199   
	119     506657.0       2.41   1.00   4.741140  25.49887  13470.0    124.6358   
	120    1153750.0       3.70  25.90   0.949861  23.16969   5887.0    131.8793   
	121    9226333.0       1.92   0.10   5.315688  26.37629  43421.0    122.9473   
	122    7646542.0       1.47   0.40   5.333058  26.20195  55020.0    119.6465   
	123    7254072.0       3.70   0.20   0.453168  23.77966   2001.0    129.9657   
	124   42844744.0       5.54   5.80   0.154673  22.47792   2030.0    130.8328   
	125   66453255.0       1.48   1.30   3.835102  23.00803  12216.0    120.4969   
	126    6052937.0       4.88   3.20   0.251983  21.87875   1219.0    131.0248   
	127    1315372.0       1.80   1.50  31.957717  26.39669  30875.0    124.9939   
	128   10408091.0       2.04   0.06   2.440669  25.15699   9938.0    128.6291   
	129   70344357.0       2.15   0.06   4.021903  26.70371  16454.0    124.0675   
	130   31014427.0       6.34   6.40   0.100853  22.35833   1437.0    134.5204   
	131   46028476.0       1.38   1.10   7.032359  25.42379   8762.0    131.4962   
	132   61689620.0       1.87   0.20   8.526467  27.39249  37739.0    124.0845   
	133  304473143.0       2.07   0.60  18.545992  28.45698  50384.0    118.4777   
	134    3350832.0       2.11   0.50   2.489764  26.39123  15317.0    124.2604   
	135   26952719.0       2.46   0.10   4.476669  25.32054   3733.0    124.3462   
	136   86589342.0       1.86   0.40   1.479347  20.91630   4085.0    121.9367   
	137   13114579.0       5.88  13.60   0.148982  20.68321   3039.0    132.4493   
	138   13495462.0       3.85  15.10   0.654323  22.02660   1286.0    131.9745   

	     life  child_mortality  
	0    75.3             29.5  
	1    58.3            192.0  
	2    75.5             15.4  
	3    72.5             20.0  
	4    81.5              5.2  
	5    80.4              4.6  
	6    70.6             43.3  
	7    72.2             14.5  
	8    68.4             55.9  
	9    75.3             15.4  
	10   70.1              7.2  
	11   79.4              4.7  
	12   70.7             20.1  
	13   63.2            116.3  
	14   67.6             48.1  
	15   70.9             52.0  
	16   61.2             63.8  
	17   73.9             18.6  
	18   73.2             13.7  
	19   59.4            130.4  
	20   57.4            108.6  
	21   66.2             51.5  
	22   56.6            113.8  
	23   80.7              5.8  
	24   54.8            168.0  
	25   78.9              8.9  
	26   75.1             19.7  
	27   62.6             91.2  
	28   58.6             72.6  
	29   79.7             10.3  
	..    ...              ...  
	109  76.4              8.0  
	110  55.9            179.1  
	111  80.9              2.8  
	112  74.8              8.8  
	113  78.5              3.7  
	114  56.7            168.5  
	115  55.0             66.1  
	116  81.1              5.0  
	117  74.3             11.7  
	118  67.4             84.7  
	119  69.1             26.4  
	120  46.1            112.2  
	121  81.1              3.2  
	122  81.9              4.7  
	123  69.5             56.2  
	124  59.7             72.4  
	125  74.1             15.6  
	126  60.0             96.4  
	127  71.3             24.9  
	128  76.5             19.4  
	129  75.1             22.2  
	130  57.2             89.3  
	131  68.2             12.9  
	132  79.5              5.6  
	133  78.2              7.7  
	134  76.0             13.0  
	135  68.7             49.2  
	136  75.4             26.2  
	137  52.0             94.9  
	138  49.0             98.3  

	[139 rows x 9 columns]>

	In [3]: df.describe()
	Out[3]: 
		 population   fertility         HIV         CO2    BMI_male  \
	count  1.390000e+02  139.000000  139.000000  139.000000  139.000000   
	mean   3.549977e+07    3.005108    1.915612    4.459874   24.623054   
	std    1.095121e+08    1.615354    4.408974    6.268349    2.209368   
	min    2.773150e+05    1.280000    0.060000    0.008618   20.397420   
	25%    3.752776e+06    1.810000    0.100000    0.496190   22.448135   
	50%    9.705130e+06    2.410000    0.400000    2.223796   25.156990   
	75%    2.791973e+07    4.095000    1.300000    6.589156   26.497575   
	max    1.197070e+09    7.590000   25.900000   48.702062   28.456980   

		         GDP  BMI_female        life  child_mortality  
	count     139.000000  139.000000  139.000000       139.000000  
	mean    16638.784173  126.701914   69.602878        45.097122  
	std     19207.299083    4.471997    9.122189        45.724667  
	min       588.000000  117.375500   45.200000         2.700000  
	25%      2899.000000  123.232200   62.200000         8.100000  
	50%      9938.000000  126.519600   72.000000        24.000000  
	75%     23278.500000  130.275900   76.850000        74.200000  
	max    126076.000000  135.492000   82.600000       192.000000

	In [4]: df.info()
	<class 'pandas.core.frame.DataFrame'>
	RangeIndex: 139 entries, 0 to 138
	Data columns (total 9 columns):
	population         139 non-null float64
	fertility          139 non-null float64
	HIV                139 non-null float64
	CO2                139 non-null float64
	BMI_male           139 non-null float64
	GDP                139 non-null float64
	BMI_female         139 non-null float64
	life               139 non-null float64
	child_mortality    139 non-null float64
	dtypes: float64(9)
	memory usage: 9.9 KB

Good job! As seen by using df.info(), fertility, along with all the other columns, is of type float64, not int64.  

---

## Fit & predict for regression  

Now, you will fit a linear regression and predict life expectancy using just one feature. You saw Andy do this earlier using the 'RM' feature of the Boston housing dataset. In this exercise, you will use the 'fertility' feature of the Gapminder dataset. Since the goal is to predict life expectancy, the target variable here is 'life'. The array for the target variable has been pre-loaded as y and the array for 'fertility' has been pre-loaded as X_fertility.  

A scatter plot with 'fertility' on the x-axis and 'life' on the y-axis has been generated. As you can see, there is a strongly negative correlation, so a linear regression should be able to capture this trend. Your job is to fit a linear regression and then predict the life expectancy, overlaying these predicted values on the plot to generate a regression line. You will also compute and print the R2R2 score using sckit-learn's .score() method.  

### Instructions :

- Import LinearRegression from sklearn.linear_model.
- Create a LinearRegression regressor called reg.
- Set up the prediction space to range from the minimum to the maximum of X_fertility. This has been done for you.
- Fit the regressor to the data (X_fertility and y) and compute its predictions using the .predict() method and the prediction_space array.
- Compute and print the R2R2 score using the .score() method.
- Overlay the plot with your linear regression line. This has been done for you, so hit 'Submit Answer' to see the result!

```python
# Import LinearRegression
from sklearn.linear_model import LinearRegression

# Create the regressor: reg
reg = LinearRegression()

# Create the prediction space
prediction_space = np.linspace(min(X_fertility), max(X_fertility)).reshape(-1,1)

# Fit the model to the data
reg.fit(X_fertility, y)

# Compute predictions over the prediction space: y_pred
y_pred = reg.predict(prediction_space)

# Print R^2 
print(reg.score(X_fertility, y))

# Plot regression line
plt.plot(prediction_space, y_pred, color='black', linewidth=3)
plt.show()
```

### Results :  

see img/graph6.svg and graph7.svg

	<script.py> output:
	    0.619244216774

Fantastic! Notice how the line captures the underlying trend in the data. And the performance is quite decent for this basic regression model with only one feature!  

---

## Train/test split for regression  

As you learned in Chapter 1, train and test sets are vital to ensure that your supervised learning model is able to generalize well to new data. This was true for classification models, and is equally true for linear regression models.  

In this exercise, you will split the Gapminder dataset into training and testing sets, and then fit and predict a linear regression over all features. In addition to computing the R2R2 score, you will also compute the Root Mean Squared Error (RMSE), which is another commonly used metric to evaluate regression models. The feature array X and target variable array y have been pre-loaded for you from the DataFrame df.  

### Instructions :

- Import LinearRegression from sklearn.linear_model, mean_squared_error from sklearn.metrics, and train_test_split from sklearn.model_selection.
- Using X and y, create training and test sets such that 30% is used for testing and 70% for training. Use a random state of 42.
- Create a linear regression regressor called reg_all, fit it to the training set, and evaluate it on the test set.
- Compute and print the R2R2 score using the .score() method on the test set.
- Compute and print the RMSE. To do this, first compute the Mean Squared Error using the mean_squared_error() function with the arguments y_test and y_pred, and then take its square root using np.sqrt().

```python
# Import necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)

# Create the regressor: reg_all
reg_all = LinearRegression()

# Fit the regressor to the training data
reg_all.fit(X_train, y_train)

# Predict on the test data: y_pred
y_pred = reg_all.predict(X_test)

# Compute and print R^2 and RMSE
print("R^2: {}".format(reg_all.score(X_test, y_test)))
rmse = np.sqrt(mean_squared_error(y_test,y_pred))
print("Root Mean Squared Error: {}".format(rmse))
```

### Results :  

	<script.py> output:
	    R^2: 0.838046873142936
	    Root Mean Squared Error: 3.2476010800377213

Excellent! Using all features has improved the model score. This makes sense, as the model has more information to learn from. However, there is one potential pitfall to this process. Can you spot it? You'll learn about this as well how to better validate your models in the next video!  

---

## 5-fold cross-validation  

Cross-validation is a vital step in evaluating a model. It maximizes the amount of data that is used to train the model, as during the course of training, the model is not only trained, but also tested on all of the available data.  

In this exercise, you will practice 5-fold cross validation on the Gapminder data. By default, scikit-learn's cross_val_score() function uses R2R2 as the metric of choice for regression. Since you are performing 5-fold cross-validation, the function will return 5 scores. Your job is to compute these 5 scores and then take their average.  

The DataFrame has been loaded as df and split into the feature/target variable arrays X and y. The modules pandas and numpy have been imported as pd and np, respectively.  

### Instructions :

 - Import LinearRegression from sklearn.linear_model and cross_val_score from sklearn.model_selection.
 - Create a linear regression regressor called reg.
 - Use the cross_val_score() function to perform 5-fold cross-validation on X and y.
 - Compute and print the average cross-validation score. You can use NumPy's mean() function to compute the average.

```python
# Import the necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# Create a linear regression object: reg
reg = LinearRegression()

# Compute 5-fold cross-validation scores: cv_scores
cv_scores = cross_val_score(reg,X,y,cv=5)

# Print the 5-fold cross-validation scores
print(df.head())
print('----------------')
print(X[:5])
print('----------------')
print(y[:5])
print('----------------')
print(cv_scores)
print('----------------')
print("Average 5-Fold CV Score: {}".format(np.mean(cv_scores)))
```

### Results :  

	script.py> output:
		   population  fertility  HIV        CO2  BMI_male      GDP  BMI_female  life  \
		0  34811059.0       2.73  0.1   3.328945  24.59620  12314.0    129.9049  75.3   
		1  19842251.0       6.43  2.0   1.474353  22.25083   7103.0    130.1247  58.3   
		2  40381860.0       2.24  0.5   4.785170  27.50170  14646.0    118.8915  75.5   
		3   2975029.0       1.40  0.1   1.804106  25.35542   7383.0    132.8108  72.5   
		4  21370348.0       1.96  0.1  18.016313  27.56373  41312.0    117.3755  81.5   
		
		   child_mortality  
		0             29.5  
		1            192.0  
		2             15.4  
		3             20.0  
		4              5.2  
		----------------
		[[  3.48110590e+07   2.73000000e+00   1.00000000e-01   3.32894466e+00
			2.45962000e+01   1.23140000e+04   1.29904900e+02   2.95000000e+01]
		 [  1.98422510e+07   6.43000000e+00   2.00000000e+00   1.47435339e+00
			2.22508300e+01   7.10300000e+03   1.30124700e+02   1.92000000e+02]
		 [  4.03818600e+07   2.24000000e+00   5.00000000e-01   4.78516998e+00
			2.75017000e+01   1.46460000e+04   1.18891500e+02   1.54000000e+01]
		 [  2.97502900e+06   1.40000000e+00   1.00000000e-01   1.80410622e+00
			2.53554200e+01   7.38300000e+03   1.32810800e+02   2.00000000e+01]
		 [  2.13703480e+07   1.96000000e+00   1.00000000e-01   1.80163133e+01
			2.75637300e+01   4.13120000e+04   1.17375500e+02   5.20000000e+00]]
		----------------
		[ 75.3  58.3  75.5  72.5  81.5]
		----------------
		[ 0.81720569  0.82917058  0.90214134  0.80633989  0.94495637]
		----------------
		Average 5-Fold CV Score: 0.8599627722793232

Great work! Now that you have cross-validated your model, you can more confidently evaluate its predictions.  
		
---

## K-Fold CV comparison

Cross validation is essential but do not forget that the more folds you use, the more computationally expensive cross-validation becomes. In this exercise, you will explore this for yourself. Your job is to perform 3-fold cross-validation and then 10-fold cross-validation on the Gapminder dataset.  

In the IPython Shell, you can use %timeit to see how long each 3-fold CV takes compared to 10-fold CV by executing the following cv=3 and cv=10:  

```python
%timeit cross_val_score(reg, X, y, cv = ____)
```

pandas and numpy are available in the workspace as pd and np. The DataFrame has been loaded as df and the feature/target variable arrays X and y have been created.  

### Instructions :

 - Import LinearRegression from sklearn.linear_model and cross_val_score from sklearn.model_selection.
 - Create a linear regression regressor called reg.
 - Perform 3-fold CV and then 10-fold CV. Compare the resulting mean scores.

```python
# Import necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# Create a linear regression object: reg
reg = LinearRegression()

# Perform 3-fold CV
cvscores_3 = cross_val_score(reg,X,y,cv=3)
print(np.mean(cvscores_3))

# Perform 10-fold CV
cvscores_10 = cross_val_score(reg,X,y,cv=10)
print(np.mean(cvscores_10))
```

### Results :  

	In [4]: %timeit cvscores_3 = cross_val_score(reg,X,y,cv=3)
	100 loops, best of 3: 11.4 ms per loop

	In [5]: %timeit cvscores_10 = cross_val_score(reg,X,y,cv=10)
	10 loops, best of 3: 36.3 ms per loop

	<script.py> output:
		0.871871278262
		0.843612862013


---

## Regularization I: Lasso  

In the video, you saw how Lasso selected out the 'RM' feature as being the most important for predicting Boston house prices, while shrinking the coefficients of certain other features to 0. Its ability to perform feature selection in this way becomes even more useful when you are dealing with data involving thousands of features.  

In this exercise, you will fit a lasso regression to the Gapminder data you have been working with and plot the coefficients. Just as with the Boston data, you will find that the coefficients of some features are shrunk to 0, with only the most important ones remaining.  

The feature and target variable arrays have been pre-loaded as X and y.  

### Instructions :

 - Import Lasso from sklearn.linear_model.
 - Instantiate a Lasso regressor with an alpha of 0.4 and specify normalize=True.
 - Fit the regressor to the data and compute the coefficients using the coef_ attribute.
 - Plot the coefficients on the y-axis and column names on the x-axis. This has been done for you, so hit 'Submit Answer' to view the plot!

```python
# Import Lasso
from sklearn.linear_model import Lasso

# Instantiate a lasso regressor: lasso
lasso = Lasso(alpha=0.4,normalize=True)

# Fit the regressor to the data
lasso = lasso.fit(X, y)

# Compute and print the coefficients
lasso_coef = lasso.coef_
print(lasso_coef)

# Plot the coefficients
plt.plot(range(len(df_columns)), lasso_coef)
plt.xticks(range(len(df_columns)), df_columns.values, rotation=60)
plt.margins(0.02)
plt.show()
```

### Results :  

see : img/graph8.svg

	<script.py> output:
		[-0.         -0.         -0.          0.          0.          0.         -0.
		 -0.07087587]

Great work! According to the lasso algorithm, it seems like 'child_mortality' is the most important feature when predicting life expectancy.  		 
		 
---

## Regularization II: Ridge  

Lasso is great for feature selection, but when building regression models, Ridge regression should be your first choice.  

Recall that lasso performs regularization by adding to the loss function a penalty term of the absolute value of each coefficient multiplied by some alpha. This is also known as L1L1 regularization because the regularization term is the L1L1 norm of the coefficients. This is not the only way to regularize, however.  

If instead you took the sum of the squared values of the coefficients multiplied by some alpha - like in Ridge regression - you would be computing the L2L2 norm. In this exercise, you will practice fitting ridge regression models over a range of different alphas, and plot cross-validated R2R2 scores for each, using this function that we have defined for you, which plots the R2R2 score as well as standard error for each alpha:  

```python
def display_plot(cv_scores, cv_scores_std):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(alpha_space, cv_scores)

    std_error = cv_scores_std / np.sqrt(10)

    ax.fill_between(alpha_space, cv_scores + std_error, cv_scores - std_error, alpha=0.2)
    ax.set_ylabel('CV Score +/- Std Error')
    ax.set_xlabel('Alpha')
    ax.axhline(np.max(cv_scores), linestyle='--', color='.5')
    ax.set_xlim([alpha_space[0], alpha_space[-1]])
    ax.set_xscale('log')
    plt.show()
```
	
Don't worry about the specifics of the above function works. The motivation behind this exercise is for you to see how the R2R2 score varies with different alphas, and to understand the importance of selecting the right value for alpha. You'll learn how to tune alpha in the next chapter.  

### Instructions :

 - Instantiate a Ridge regressor and specify normalize=True.
 - Inside the for loop:
	 - Specify the alpha value for the regressor to use.
	 - Perform 10-fold cross-validation on the regressor with the specified alpha. The data is available in the arrays X and y.
	 - Append the average and the standard deviation of the computed cross-validated scores. NumPy has been pre-imported for you as np.
 - Use the display_plot() function to visualize the scores and standard deviations.

```python
# Import necessary modules
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

# Setup the array of alphas and lists to store scores
alpha_space = np.logspace(-4, 0, 50)
ridge_scores = []
ridge_scores_std = []

# Create a ridge regressor: ridge
ridge = Ridge(normalize=True)

# Compute scores over range of alphas
for alpha in alpha_space:

    # Specify the alpha value to use: ridge.alpha
    ridge.alpha = alpha
    
    # Perform 10-fold CV: ridge_cv_scores
    ridge_cv_scores = cross_val_score(ridge,X,y,cv=10)
    
    # Append the mean of ridge_cv_scores to ridge_scores
    ridge_scores.append(np.mean(ridge_cv_scores))
    
    # Append the std of ridge_cv_scores to ridge_scores_std
    ridge_scores_std.append(np.std(ridge_cv_scores))

# Display the plot
display_plot(ridge_scores, ridge_scores_std)
```

### Results :  

see : img/graph9.svg  

Great work! Notice how the cross-validation scores change with different alphas. Which alpha should you pick? How can you fine-tune your model? You'll learn all about this in the next chapter!  

---

## Loading and viewing your data



### Instructions :

- 

```python

```

### Results :  



---

## Loading and viewing your data



### Instructions :

- 

```python

```

### Results :  



---

## Loading and viewing your data



### Instructions :

- 

```python

```

### Results :  



---

## Loading and viewing your data



### Instructions :

- 

```python

```

### Results :  



---

## Loading and viewing your data



### Instructions :

- 

```python

```

### Results :  



---

## Loading and viewing your data



### Instructions :

- 

```python

```

### Results :  



---

## Loading and viewing your data



### Instructions :

- 

```python

```

### Results :  



---

## Loading and viewing your data



### Instructions :

- 

```python

```

### Results :  



---

## Loading and viewing your data



### Instructions :

- 

```python

```

### Results :  



---

## Loading and viewing your data



### Instructions :

- 

```python

```

### Results :  



---

## Loading and viewing your data



### Instructions :

- 

```python

```

### Results :  



---

## Loading and viewing your data



### Instructions :

- 

```python

```

### Results :  



---

## Loading and viewing your data



### Instructions :

- 

```python

```

### Results :  



---

