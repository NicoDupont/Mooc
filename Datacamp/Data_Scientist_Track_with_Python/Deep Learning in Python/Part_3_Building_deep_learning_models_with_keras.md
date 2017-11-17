11/2017  
# Datacamp - Deep Learning in Python (Data Scientist Track with Python)  
[Deep Learning in Python](https://www.datacamp.com/courses/deep-learning-in-python)

---

***Course Description***  

Deep learning is the machine learning technique behind the most exciting capabilities in diverse areas like robotics, natural language processing, image recognition and artificial intelligence (including the famous AlphaGo). In this course, you'll gain hands-on, practical knowledge of how to use deep learning with Keras 2.0, the latest version of a cutting edge library for deep learning in Python.      

# Part 3 : Building deep learning models with keras   

In this chapter, you'll use the keras library to build deep learning models for both regression as well as classification! You'll learn about the Specify-Compile-Fit workflow that you can use to make predictions and by the end of this chapter, you'll have all the tools necessary to build deep neural networks!  

## Understanding your data      

You will soon start building models in Keras to predict wages based on various professional and demographic factors. Before you start building a model, it's good to understand your data by performing some exploratory analysis.  

The data is pre-loaded into a pandas DataFrame called df. Use the .head() and .describe() methods in the IPython Shell for a quick overview of the DataFrame.  

The target variable you'll be predicting is wage_per_hour. Some of the predictor variables are binary indicators, where a value of 1 represents True, and 0 represents False.  

Of the 9 predictor variables in the DataFrame, how many are binary indicators? The min and max values as shown by .describe() will be informative here. How many binary indicator predictors are there?  

### Possible answers => 6

 - 0.
 - 5.
 - 6.

```python
```

### Results :  

Exactly! There are 6 binary indicators.  

	In [1]: df.columns
	Out[1]: 
	Index(['wage_per_hour', 'union', 'education_yrs', 'experience_yrs', 'age',
		   'female', 'marr', 'south', 'manufacturing', 'construction'],
		  dtype='object')

	In [2]: df.describe()
	Out[2]: 
		   wage_per_hour       union  education_yrs  experience_yrs         age  \
	count     534.000000  534.000000     534.000000      534.000000  534.000000   
	mean        9.024064    0.179775      13.018727       17.822097   36.833333   
	std         5.139097    0.384360       2.615373       12.379710   11.726573   
	min         1.000000    0.000000       2.000000        0.000000   18.000000   
	25%         5.250000    0.000000      12.000000        8.000000   28.000000   
	50%         7.780000    0.000000      12.000000       15.000000   35.000000   
	75%        11.250000    0.000000      15.000000       26.000000   44.000000   
	max        44.500000    1.000000      18.000000       55.000000   64.000000   

			   female        marr       south  manufacturing  construction  
	count  534.000000  534.000000  534.000000     534.000000    534.000000  
	mean     0.458801    0.655431    0.292135       0.185393      0.044944  
	std      0.498767    0.475673    0.455170       0.388981      0.207375  
	min      0.000000    0.000000    0.000000       0.000000      0.000000  
	25%      0.000000    0.000000    0.000000       0.000000      0.000000  
	50%      0.000000    1.000000    0.000000       0.000000      0.000000  
	75%      1.000000    1.000000    1.000000       0.000000      0.000000  
	max      1.000000    1.000000    1.000000       1.000000      1.000000

---


## Specifying a model      

Now you'll get to work with your first model in Keras, and will immediately be able to run more complex neural network models on larger datasets compared to the first two chapters.  

To start, you'll take the skeleton of a neural network and add a hidden layer and an output layer. You'll then fit that model and see Keras do the optimization so your model continually gets better.  

As a start, you'll predict workers wages based on characteristics like their industry, education and level of experience. You can find the dataset in a pandas dataframe called df. For convenience, everything in df except for the target has been converted to a NumPy matrix called predictors. The target, wage_per_hour, is available as a NumPy matrix called target.  

For all exercises in this chapter, we've imported the Sequential model constructor, the Dense layer constructor, and pandas.  

### Instructions

 - Store the number of columns in the predictors data to n_cols. This has been done for you.
 - Start by creating a Sequential model called model.
 - Use the .add() method on model to add a Dense layer.
	- Add 50 units, specify activation='relu', and the input_shape parameter to be the tuple (n_cols,) which means it has n_cols items in each row of data, and any number of rows of data are acceptable as inputs.
 - Add another Dense layer. This should have 32 units and a 'relu' activation.
 - Finally, add an output layer, which is a Dense layer with a single node. Don't use any activation function here.

```python
# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential

# Save the number of columns in predictors: n_cols
n_cols = predictors.shape[1]

# Set up the model: model
model = Sequential()

# Add the first layer
model.add(Dense(50, activation='relu', input_shape = (n_cols,)))

# Add the second layer
model.add(Dense(32, activation='relu'))

# Add the output layer
model.add(Dense(1))

```

### Results :  

Well done! Now that you've specified the model, the next step is to compile it.  

---


## Compiling the model      

You're now going to compile the model you specified earlier. To compile the model, you need to specify the optimizer and loss function to use. In the video, Dan mentioned that the Adam optimizer is an excellent choice. You can read more about it as well as other keras optimizers [here](https://keras.io/optimizers/#adam), and if you are really curious to learn more, you can read the [original paper](https://arxiv.org/abs/1412.6980v8) that introduced the Adam optimizer.  

In this exercise, you'll use the Adam optimizer and the mean squared error loss function. Go for it!  

### Instructions

 - Compile the model using model.compile(). Your optimizer should be 'adam' and the loss should be 'mean_squared_error'.

```python
# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential

# Specify the model
n_cols = predictors.shape[1]
model = Sequential()
model.add(Dense(50, activation='relu', input_shape = (n_cols,)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam',loss='mean_squared_error')

# Verify that model contains information from compiling
print("Loss function: " + model.loss)
```

### Results :  

Fantastic work - all that's left now is to fit the model!  

	<script.py> output:
		Loss function: mean_squared_error

---


## Fitting the model     

You're at the most fun part. You'll now fit the model. Recall that the data to be used as predictive features is loaded in a NumPy matrix called predictors and the data to be predicted is stored in a NumPy matrix called target. Your model is pre-written and it has been compiled with the code from the previous exercise.

### Instructions

 - Fit the model. Remember that the first argument is the predictive features (predictors), and the data to be predicted (target) is the second argument.

```python
# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential

# Specify the model
n_cols = predictors.shape[1]
model = Sequential()
model.add(Dense(50, activation='relu', input_shape = (n_cols,)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

print(type(predictors))
print(predictors[:5])
print('--------------')
print(type(target))
print('--------------')
print(target[:5])
print('--------------')
print('--------------')

# Fit the model
model.fit(predictors,target)

```

### Results :  

Superb! You now know how to specify, compile, and fit a deep learning model using keras!  

		<script.py> output:
			<class 'numpy.ndarray'>
			[[ 0  8 21 35  1  1  0  1  0]
			 [ 0  9 42 57  1  1  0  1  0]
			 [ 0 12  1 19  0  0  0  1  0]
			 [ 0 12  4 22  0  0  0  0  0]
			 [ 0 12 17 35  0  1  0  0  0]]
			--------------
			<class 'numpy.ndarray'>
			--------------
			[ 5.1   4.95  6.67  4.    7.5 ]
			--------------
			--------------
			Epoch 1/10
			
		 32/534 [>.............................] - ETA: 1s - loss: 41.5956
		416/534 [======================>.......] - ETA: 0s - loss: 27.0530
		534/534 [==============================] - 0s - loss: 23.4728     
			Epoch 2/10
			
		 32/534 [>.............................] - ETA: 0s - loss: 18.3311
		534/534 [==============================] - 0s - loss: 21.7812     
			Epoch 3/10
			
		 32/534 [>.............................] - ETA: 0s - loss: 11.4606
		534/534 [==============================] - 0s - loss: 21.4489     
			Epoch 4/10
			
		 32/534 [>.............................] - ETA: 0s - loss: 15.5029
		534/534 [==============================] - 0s - loss: 21.2887     
			Epoch 5/10
			
		 32/534 [>.............................] - ETA: 0s - loss: 27.5338
		534/534 [==============================] - 0s - loss: 21.0044     
			Epoch 6/10
			
		 32/534 [>.............................] - ETA: 0s - loss: 33.5741
		534/534 [==============================] - 0s - loss: 21.0345     
			Epoch 7/10
			
		 32/534 [>.............................] - ETA: 0s - loss: 20.7167
		416/534 [======================>.......] - ETA: 0s - loss: 22.9046
		534/534 [==============================] - 0s - loss: 21.1434     
			Epoch 8/10
			
		 32/534 [>.............................] - ETA: 0s - loss: 15.1037
		352/534 [==================>...........] - ETA: 0s - loss: 21.2749
		534/534 [==============================] - 0s - loss: 20.7704     
			Epoch 9/10
			
		 32/534 [>.............................] - ETA: 0s - loss: 21.4615
		416/534 [======================>.......] - ETA: 0s - loss: 22.8094
		534/534 [==============================] - 0s - loss: 20.9418     
			Epoch 10/10
			
		 32/534 [>.............................] - ETA: 0s - loss: 32.0192
		416/534 [======================>.......] - ETA: 0s - loss: 21.7339
		534/534 [==============================] - 0s - loss: 20.8199

---


## Understanding your classification data    

Now you will start modeling with a new dataset for a classification problem. This data includes information about passengers on the Titanic. You will use predictors such as age, fare and where each passenger embarked from to predict who will survive. This data is from [a tutorial on data science competitions](https://www.kaggle.com/c/titanic). Look [here](https://www.kaggle.com/c/titanic/data) for descriptions of the features.  

The data is pre-loaded in a pandas DataFrame called df.  

It's smart to review the maximum and minimum values of each variable to ensure the data isn't misformatted or corrupted. What was the maximum age of passengers on the Titanic? Use the .describe() method in the IPython Shell to answer this question.  

### Possible Answers => 2

 - 29.699.
 - 80.
 - 891.
 - It is not listed.

```python
print(df.describe())
```

### Results :  

Exactly! The maximum age in the data is 80.  

		In [2]: df.describe()
		Out[2]: 
				 survived      pclass         age       sibsp       parch        fare  \
		count  891.000000  891.000000  891.000000  891.000000  891.000000  891.000000   
		mean     0.383838    2.308642   29.699118    0.523008    0.381594   32.204208   
		std      0.486592    0.836071   13.002015    1.102743    0.806057   49.693429   
		min      0.000000    1.000000    0.420000    0.000000    0.000000    0.000000   
		25%      0.000000    2.000000   22.000000    0.000000    0.000000    7.910400   
		50%      0.000000    3.000000   29.699118    0.000000    0.000000   14.454200   
		75%      1.000000    3.000000   35.000000    1.000000    0.000000   31.000000   
		max      1.000000    3.000000   80.000000    8.000000    6.000000  512.329200   

					 male  embarked_from_cherbourg  embarked_from_queenstown  \
		count  891.000000               891.000000                891.000000   
		mean     0.647587                 0.188552                  0.086420   
		std      0.477990                 0.391372                  0.281141   
		min      0.000000                 0.000000                  0.000000   
		25%      0.000000                 0.000000                  0.000000   
		50%      1.000000                 0.000000                  0.000000   
		75%      1.000000                 0.000000                  0.000000   
		max      1.000000                 1.000000                  1.000000   

			   embarked_from_southampton  
		count                 891.000000  
		mean                    0.722783  
		std                     0.447876  
		min                     0.000000  
		25%                     0.000000  
		50%                     1.000000  
		75%                     1.000000  
		max                     1.000000

---


## Last steps in classification models      

You'll now create a classification model using the titanic dataset, which has been pre-loaded into a DataFrame called df. You'll take information about the passengers and predict which ones survived.  

The predictive variables are stored in a NumPy array predictors. The target to predict is in df.survived, though you'll have to manipulate it for keras. The number of predictive features is stored in n_cols.  

Here, you'll use the 'sgd' optimizer, which stands for Stochastic Gradient Descent. You'll learn more about this in the next chapter!  

### Instructions

 - Convert df.survived to a categorical variable using the to_categorical() function.
 - Specify a Sequential model called model.
 - Add a Dense layer with 32 nodes. Use 'relu' as the activation and (n_cols,) as the input_shape.
 - Add the Dense output layer. Because there are two outcomes, it should have 2 units, and because it is a classification model, the activation should be 'softmax'.
 - Compile the model, using 'sgd' as the optimizer, 'categorical_crossentropy' as the loss function, and metrics=['accuracy'] to see the accuracy (what fraction of predictions were correct) at the end of each epoch.
 - Fit the model using the predictors and the target.

```python
# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical

# Convert the target to categorical: target
target = to_categorical(df.survived)

# Set up the model
model = Sequential()

# Add the first layer
model.add(Dense(32, activation='relu', input_shape = (n_cols,)))

# Add the output layer
model.add(Dense(2,activation='softmax'))

# Compile the model
model.compile(optimizer='sgd',metrics=['accuracy'],loss='categorical_crossentropy')

# Fit the model
model.fit(predictors, target)
```

### Results :  

Fantastic! This simple model is generating an accuracy of 68!  

	<script.py> output:
		Epoch 1/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 0.7098 - acc: 0.5312
	672/891 [=====================>........] - ETA: 0s - loss: 0.6405 - acc: 0.3408
	891/891 [==============================] - 0s - loss: 0.6357 - acc: 0.3401     
		Epoch 2/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 0.6296 - acc: 0.3125
	704/891 [======================>.......] - ETA: 0s - loss: 0.6156 - acc: 0.3224
	891/891 [==============================] - 0s - loss: 0.6203 - acc: 0.3311     
		Epoch 3/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 0.6161 - acc: 0.3750
	704/891 [======================>.......] - ETA: 0s - loss: 0.6132 - acc: 0.3253
	891/891 [==============================] - 0s - loss: 0.6098 - acc: 0.3221     
		Epoch 4/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 0.5954 - acc: 0.3125
	672/891 [=====================>........] - ETA: 0s - loss: 0.6107 - acc: 0.3095
	891/891 [==============================] - 0s - loss: 0.6037 - acc: 0.3064     
		Epoch 5/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 0.7103 - acc: 0.4062
	704/891 [======================>.......] - ETA: 0s - loss: 0.5933 - acc: 0.3097
	891/891 [==============================] - 0s - loss: 0.6016 - acc: 0.3165     
		Epoch 6/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 0.6260 - acc: 0.3438
	256/891 [=======>......................] - ETA: 0s - loss: 0.6124 - acc: 0.3320
	704/891 [======================>.......] - ETA: 0s - loss: 0.5980 - acc: 0.3139
	891/891 [==============================] - 0s - loss: 0.6029 - acc: 0.3120     
		Epoch 7/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 0.5249 - acc: 0.1875
	704/891 [======================>.......] - ETA: 0s - loss: 0.6132 - acc: 0.3324
	891/891 [==============================] - 0s - loss: 0.6010 - acc: 0.3120     
		Epoch 8/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 0.5883 - acc: 0.2500
	704/891 [======================>.......] - ETA: 0s - loss: 0.6015 - acc: 0.3097
	891/891 [==============================] - 0s - loss: 0.6021 - acc: 0.3131     
		Epoch 9/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 0.5991 - acc: 0.2500
	704/891 [======================>.......] - ETA: 0s - loss: 0.6056 - acc: 0.3196
	891/891 [==============================] - 0s - loss: 0.5993 - acc: 0.3154     
		Epoch 10/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 0.5668 - acc: 0.3438
	704/891 [======================>.......] - ETA: 0s - loss: 0.6011 - acc: 0.3097
	891/891 [==============================] - 0s - loss: 0.5997 - acc: 0.3086

	<script.py> output:
		Epoch 1/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 3.5722 - acc: 0.5312
	704/891 [======================>.......] - ETA: 0s - loss: 2.6803 - acc: 0.5767
	891/891 [==============================] - 0s - loss: 2.4013 - acc: 0.5960     
		Epoch 2/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 0.9370 - acc: 0.5312
	512/891 [================>.............] - ETA: 0s - loss: 1.4351 - acc: 0.5859
	891/891 [==============================] - 0s - loss: 1.2383 - acc: 0.6038     
		Epoch 3/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 0.8090 - acc: 0.6250
	384/891 [===========>..................] - ETA: 0s - loss: 0.7825 - acc: 0.6823
	800/891 [=========================>....] - ETA: 0s - loss: 0.7250 - acc: 0.6713
	891/891 [==============================] - 0s - loss: 0.7108 - acc: 0.6745     
		Epoch 4/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 1.4971 - acc: 0.6875
	416/891 [=============>................] - ETA: 0s - loss: 0.7176 - acc: 0.6538
	800/891 [=========================>....] - ETA: 0s - loss: 0.7064 - acc: 0.6262
	891/891 [==============================] - 0s - loss: 0.7111 - acc: 0.6308     
		Epoch 5/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 0.6705 - acc: 0.6250
	448/891 [==============>...............] - ETA: 0s - loss: 0.6321 - acc: 0.6786
	891/891 [==============================] - 0s - loss: 0.6337 - acc: 0.6756     
		Epoch 6/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 0.7427 - acc: 0.4375
	608/891 [===================>..........] - ETA: 0s - loss: 0.7017 - acc: 0.6184
	891/891 [==============================] - 0s - loss: 0.7040 - acc: 0.6128     
		Epoch 7/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 0.5564 - acc: 0.7812
	448/891 [==============>...............] - ETA: 0s - loss: 0.6894 - acc: 0.6272
	832/891 [===========================>..] - ETA: 0s - loss: 0.6859 - acc: 0.6418
	891/891 [==============================] - 0s - loss: 0.6804 - acc: 0.6498     
		Epoch 8/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 0.6320 - acc: 0.5625
	480/891 [===============>..............] - ETA: 0s - loss: 0.7803 - acc: 0.6271
	891/891 [==============================] - 0s - loss: 0.8069 - acc: 0.6453     
		Epoch 9/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 1.4920 - acc: 0.6875
	512/891 [================>.............] - ETA: 0s - loss: 0.9280 - acc: 0.6152
	891/891 [==============================] - 0s - loss: 0.9810 - acc: 0.6375     
		Epoch 10/10
		
	 32/891 [>.............................] - ETA: 0s - loss: 1.1045 - acc: 0.7500
	480/891 [===============>..............] - ETA: 0s - loss: 0.8716 - acc: 0.6521
	832/891 [===========================>..] - ETA: 0s - loss: 0.9843 - acc: 0.6298
	891/891 [==============================] - 0s - loss: 1.0252 - acc: 0.6251
---


## Making predictions   

The trained network from your previous coding exercise is now stored as model. New data to make predictions is stored in a NumPy array as pred_data. Use model to make predictions on your new data.  

In this exercise, your predictions will be probabilities, which is the most common way for data scientists to communicate their predictions to colleagues.  

### Instructions

 - Create your predictions using the model's .predict() method on pred_data.
 - Use NumPy indexing to find the column corresponding to predicted probabilities of survival being True. This is the second column (index 1) of predictions. Store the result in predicted_prob_true and print it.

```python
# Specify, compile, and fit the model
model = Sequential()
model.add(Dense(32, activation='relu', input_shape = (n_cols,)))
model.add(Dense(2, activation='softmax'))
model.compile(optimizer='sgd', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])
model.fit(predictors, target)

# Calculate predictions: predictions
predictions = model.predict(pred_data)

# Calculate predicted probability of survival: predicted_prob_true
predicted_prob_true = predictions[:,1]

# print predicted_prob_true
print(predicted_prob_true)
```

### Results :  

Excellent work! You're now ready to begin learning how to fine-tune your models.  

		[ 0.14106742  0.2939837   0.72041941  0.39310485  0.1339099   0.11239728
		  0.0201272   0.26580003  0.10781743  0.43063962  0.14763513  0.15907367
		  0.11807266  0.3595095   0.1171111   0.06142054  0.21177891  0.28925496
		  0.04514197  0.31768849  0.41884002  0.14550553  0.02201079  0.22162883
		  0.43071264  0.12394029  0.43177718  0.49504554  0.12899502  0.33571559
		  0.35291895  0.46181589  0.1124588   0.17205848  0.22821167  0.44502205
		  0.19747329  0.13315323  0.41307583  0.32690102  0.20052902  0.30727428
		  0.3623943   0.075498    0.24654301  0.05593342  0.23268615  0.07939808
		  0.3439281   0.63931042  0.34171996  0.00416652  0.38117304  0.50451887
		  0.15513846  0.28557676  0.80085188  0.10889684  0.25668025  0.1124588
		  0.0709618   0.23254065  0.15516447  0.25735936  0.22568662  0.11461174
		  0.20787722  0.42714414  0.14302108  0.39431939  0.14769486  0.29740661
		  0.09204852  0.04489262  0.30585635  0.28220907  0.22144032  0.2102688
		  0.13213845  0.36239544  0.36822239  0.10135249  0.24887271  0.17060868
		  0.14933577  0.18280807  0.19581646  0.47341907  0.26113832  0.3583014
		  0.10446005]
		  
---