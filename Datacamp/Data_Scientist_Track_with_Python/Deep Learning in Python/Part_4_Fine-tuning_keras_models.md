11/2017  
# Datacamp - Deep Learning in Python (Data Scientist Track with Python)  
[Deep Learning in Python](https://www.datacamp.com/courses/deep-learning-in-python)

---

***Course Description***  

Deep learning is the machine learning technique behind the most exciting capabilities in diverse areas like robotics, natural language processing, image recognition and artificial intelligence (including the famous AlphaGo). In this course, you'll gain hands-on, practical knowledge of how to use deep learning with Keras 2.0, the latest version of a cutting edge library for deep learning in Python.      

# Part 4 : Fine-tuning keras models  

Here, you'll learn how to optimize your deep learning models in keras. You'll learn how to validate your models, understand the concept of model capacity, and experiment with wider and deeper networks. Enjoy!      

## Diagnosing optimization problems   

Which of the following could prevent a model from showing an improved loss in its first few epochs?  

### Possible answers => 4

 - Learning rate too low.
 - Learning rate too high.
 - Poor choice of activation function.
 - All of the above.

```python
```

### Results :  

Well done! All the options listed could prevent a model from showing an improved loss in its first few epochs.  

---


## Changing optimization parameters   

It's time to get your hands dirty with optimization. You'll now try optimizing a model at a very low learning rate, a very high learning rate, and a "just right" learning rate. You'll want to look at the results after running this exercise, remembering that a low value for the loss function is good.  

For these exercises, we've pre-loaded the predictors and target values from your previous classification models (predicting who would survive on the Titanic). You'll want the optimization to start from scratch every time you change the learning rate, to give a fair comparison of how each learning rate did in your results. So we have created a function get_new_model() that creates an unoptimized model to optimize.  

### Instructions

 - Import SGD from keras.optimizers.
 - Create a list of learning rates to try optimizing with called lr_to_test. The learning rates in it should be .000001, 0.01, and 1.
 - Using a for loop to iterate over lr_to_test:
	- Use the get_new_model() function to build a new, unoptimized model.
	- Create an optimizer called my_optimizer using the SGD() constructor with keyword argument lr=lr.
	- Compile your model. Set the optimizer parameter to be the SGD object you created above, and because this is a classification problem, use 'categorical_crossentropy' for the loss parameter.
	- Fit your model using the predictors and target.

```python
# Import the SGD optimizer
from keras.optimizers import SGD

# Create list of learning rates: lr_to_test
lr_to_test = [0.000001,0.01,1]

# Loop over learning rates
for lr in lr_to_test:
    print('\n\nTesting model with learning rate: %f\n'%lr )

    # Build new model to test, unaffected by previous models
    model = get_new_model()

    # Create SGD optimizer with specified learning rate: my_optimizer
    my_optimizer = SGD(lr=lr)

    # Compile the model
    model.compile(optimizer=my_optimizer,loss='categorical_crossentropy')

    # Fit the model
    model.fit(predictors,target)
```

### Results :  


---


## Evaluating model accuracy on validation dataset   

Now it's your turn to monitor model accuracy with a validation data set. A model definition has been provided as model. Your job is to add the code to compile it and then fit it. You'll check the validation score in each epoch.   

### Instructions

 - Compile your model using 'adam' as the optimizer and 'categorical_crossentropy' for the loss. To see what fraction of predictions are correct (the accuracy) in each epoch, specify the additional keyword argument metrics=['accuracy'] in model.compile().
 - Fit the model using the predictors and target. Create a validation split of 30% (or 0.3). This will be reported in each epoch.

```python
# Save the number of columns in predictors: n_cols
n_cols = predictors.shape[1]
input_shape = (n_cols,)

# Specify the model
model = Sequential()
model.add(Dense(100, activation='relu', input_shape = input_shape))
model.add(Dense(100, activation='relu'))
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

# Fit the model
hist = model.fit(predictors,target,validation_split=0.3)
```

### Results :  

Great work!  

    <script.py> output:
        Train on 623 samples, validate on 268 samples
        Epoch 1/10

     32/623 [>.............................] - ETA: 1s - loss: 3.3028 - acc: 0.4062
    608/623 [============================>.] - ETA: 0s - loss: 1.3322 - acc: 0.5987
    623/623 [==============================] - 0s - loss: 1.3098 - acc: 0.6051 - val_loss: 0.6893 - val_acc: 0.7239
        Epoch 2/10

     32/623 [>.............................] - ETA: 0s - loss: 0.6948 - acc: 0.7188
    608/623 [============================>.] - ETA: 0s - loss: 0.8885 - acc: 0.5691
    623/623 [==============================] - 0s - loss: 0.8881 - acc: 0.5698 - val_loss: 1.1191 - val_acc: 0.6418
        Epoch 3/10

     32/623 [>.............................] - ETA: 0s - loss: 1.0483 - acc: 0.5938
    608/623 [============================>.] - ETA: 0s - loss: 0.8072 - acc: 0.6168
    623/623 [==============================] - 0s - loss: 0.8026 - acc: 0.6228 - val_loss: 0.8656 - val_acc: 0.6231
        Epoch 4/10

     32/623 [>.............................] - ETA: 0s - loss: 0.6488 - acc: 0.6875
    608/623 [============================>.] - ETA: 0s - loss: 0.7612 - acc: 0.6464
    623/623 [==============================] - 0s - loss: 0.7569 - acc: 0.6469 - val_loss: 0.6980 - val_acc: 0.7015
        Epoch 5/10

     32/623 [>.............................] - ETA: 0s - loss: 0.6978 - acc: 0.6250
    608/623 [============================>.] - ETA: 0s - loss: 0.6840 - acc: 0.6414
    623/623 [==============================] - 0s - loss: 0.6838 - acc: 0.6388 - val_loss: 0.5718 - val_acc: 0.7201
        Epoch 6/10

     32/623 [>.............................] - ETA: 0s - loss: 0.5621 - acc: 0.6875
    608/623 [============================>.] - ETA: 0s - loss: 0.6589 - acc: 0.6562
    623/623 [==============================] - 0s - loss: 0.6572 - acc: 0.6533 - val_loss: 0.5273 - val_acc: 0.7463
        Epoch 7/10

     32/623 [>.............................] - ETA: 0s - loss: 0.5634 - acc: 0.7500
    608/623 [============================>.] - ETA: 0s - loss: 0.5996 - acc: 0.6826
    623/623 [==============================] - 0s - loss: 0.5999 - acc: 0.6806 - val_loss: 0.5108 - val_acc: 0.7239
        Epoch 8/10

     32/623 [>.............................] - ETA: 0s - loss: 0.5904 - acc: 0.7500
    608/623 [============================>.] - ETA: 0s - loss: 0.5912 - acc: 0.6859
    623/623 [==============================] - 0s - loss: 0.5911 - acc: 0.6854 - val_loss: 0.5274 - val_acc: 0.7463
        Epoch 9/10

     32/623 [>.............................] - ETA: 0s - loss: 0.5605 - acc: 0.7500
    608/623 [============================>.] - ETA: 0s - loss: 0.6663 - acc: 0.6546
    623/623 [==============================] - 0s - loss: 0.6634 - acc: 0.6581 - val_loss: 0.5686 - val_acc: 0.6978
        Epoch 10/10

     32/623 [>.............................] - ETA: 0s - loss: 0.4844 - acc: 0.7812
    608/623 [============================>.] - ETA: 0s - loss: 0.6183 - acc: 0.6859
    623/623 [==============================] - 0s - loss: 0.6150 - acc: 0.6886 - val_loss: 0.5335 - val_acc: 0.7313

---


## Early stopping: Optimizing the optimization    

Now that you know how to monitor your model performance throughout optimization, you can use early stopping to stop optimization when it isn't helping any more. Since the optimization stops automatically when it isn't helping, you can also set a high value for epochs in your call to .fit(), as Dan showed in the video.  

The model you'll optimize has been specified as model. As before, the data is pre-loaded as predictors and target.  

### Instructions

 - Import EarlyStopping from keras.callbacks.
 - Compile the model, once again using 'adam' as the optimizer, 'categorical_crossentropy' as the loss function, and metrics=['accuracy'] to see the accuracy at each epoch.
 - Create an EarlyStopping object called early_stopping_monitor. Stop optimization when the validation loss hasn't improved for 2 epochs by specifying the patience parameter of EarlyStopping() to be 2.
 - Fit the model using the predictors and target. Specify the number of epochs to be 30 and use a validation split of 0.3. In addition, pass [early_stopping_monitor] to the callbacks parameter.

```python
# Import EarlyStopping
from keras.callbacks import EarlyStopping

# Save the number of columns in predictors: n_cols
n_cols = predictors.shape[1]
input_shape = (n_cols,)

# Specify the model
model = Sequential()
model.add(Dense(100, activation='relu', input_shape = input_shape))
model.add(Dense(100, activation='relu'))
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

# Define early_stopping_monitor
early_stopping_monitor = EarlyStopping(patience=2)

# Fit the model
model.fit(predictors, target, validation_split=0.3, epochs=30, callbacks = [early_stopping_monitor])
```

### Results :  

Wonderful work! Because optimization will automatically stop when it is no longer helpful, it is okay to specify the maximum number of epochs as 30 rather than using the default of 10 that you've used so far. Here, it seems like the optimization stopped after 7 epochs.  


    <script.py> output:
        Train on 623 samples, validate on 268 samples
        Epoch 1/20

     32/623 [>.............................] - ETA: 1s - loss: 5.6563 - acc: 0.4688
    384/623 [=================>............] - ETA: 0s - loss: 1.8169 - acc: 0.5078
    623/623 [==============================] - 0s - loss: 1.6362 - acc: 0.5682 - val_loss: 1.0867 - val_acc: 0.6530
        Epoch 2/20

     32/623 [>.............................] - ETA: 0s - loss: 1.8369 - acc: 0.4688
    352/623 [===============>..............] - ETA: 0s - loss: 0.9372 - acc: 0.6023
    623/623 [==============================] - 0s - loss: 0.8345 - acc: 0.6083 - val_loss: 0.5688 - val_acc: 0.7276
        Epoch 3/20

     32/623 [>.............................] - ETA: 0s - loss: 0.8420 - acc: 0.6562
    608/623 [============================>.] - ETA: 0s - loss: 0.7040 - acc: 0.6546
    623/623 [==============================] - 0s - loss: 0.7147 - acc: 0.6533 - val_loss: 0.5283 - val_acc: 0.7537
        Epoch 4/20

     32/623 [>.............................] - ETA: 0s - loss: 1.0064 - acc: 0.6562
    608/623 [============================>.] - ETA: 0s - loss: 0.6689 - acc: 0.6760
    623/623 [==============================] - 0s - loss: 0.6717 - acc: 0.6758 - val_loss: 0.5189 - val_acc: 0.7239
        Epoch 5/20

     32/623 [>.............................] - ETA: 0s - loss: 0.5421 - acc: 0.7188
    608/623 [============================>.] - ETA: 0s - loss: 0.6737 - acc: 0.6431
    623/623 [==============================] - 0s - loss: 0.6814 - acc: 0.6421 - val_loss: 0.6336 - val_acc: 0.6903
        Epoch 6/20

     32/623 [>.............................] - ETA: 0s - loss: 0.4556 - acc: 0.8438
    608/623 [============================>.] - ETA: 0s - loss: 0.6241 - acc: 0.7089
    623/623 [==============================] - 0s - loss: 0.6263 - acc: 0.7063 - val_loss: 0.5628 - val_acc: 0.7239
        Epoch 7/20

     32/623 [>.............................] - ETA: 0s - loss: 0.6456 - acc: 0.6250
    384/623 [=================>............] - ETA: 0s - loss: 0.6034 - acc: 0.6901
    623/623 [==============================] - 0s - loss: 0.6595 - acc: 0.6998 - val_loss: 0.6633 - val_acc: 0.6679

    <script.py> output:
        Train on 623 samples, validate on 268 samples
        Epoch 1/30

     32/623 [>.............................] - ETA: 1s - loss: 5.6563 - acc: 0.4688
    352/623 [===============>..............] - ETA: 0s - loss: 1.9240 - acc: 0.4972
    576/623 [==========================>...] - ETA: 0s - loss: 1.7013 - acc: 0.5556
    623/623 [==============================] - 0s - loss: 1.6543 - acc: 0.5666 - val_loss: 1.0126 - val_acc: 0.6791
        Epoch 2/30

     32/623 [>.............................] - ETA: 0s - loss: 1.7841 - acc: 0.4688
    352/623 [===============>..............] - ETA: 0s - loss: 0.9541 - acc: 0.5767
    623/623 [==============================] - 0s - loss: 0.8363 - acc: 0.6035 - val_loss: 0.5825 - val_acc: 0.7351
        Epoch 3/30

     32/623 [>.............................] - ETA: 0s - loss: 0.9322 - acc: 0.6250
    512/623 [=======================>......] - ETA: 0s - loss: 0.7563 - acc: 0.6055
    623/623 [==============================] - 0s - loss: 0.7952 - acc: 0.6228 - val_loss: 0.6661 - val_acc: 0.7276
        Epoch 4/30

     32/623 [>.............................] - ETA: 0s - loss: 1.4005 - acc: 0.5625
    576/623 [==========================>...] - ETA: 0s - loss: 0.7300 - acc: 0.6337
    623/623 [==============================] - 0s - loss: 0.7310 - acc: 0.6340 - val_loss: 0.5365 - val_acc: 0.7313
        Epoch 5/30

     32/623 [>.............................] - ETA: 0s - loss: 0.5660 - acc: 0.7188
    512/623 [=======================>......] - ETA: 0s - loss: 0.6489 - acc: 0.6641
    623/623 [==============================] - 0s - loss: 0.6461 - acc: 0.6661 - val_loss: 0.5830 - val_acc: 0.6903
        Epoch 6/30

     32/623 [>.............................] - ETA: 0s - loss: 0.4329 - acc: 0.8750
    576/623 [==========================>...] - ETA: 0s - loss: 0.5990 - acc: 0.6910
    623/623 [==============================] - 0s - loss: 0.5970 - acc: 0.6870 - val_loss: 0.5750 - val_acc: 0.7015
        Epoch 7/30

     32/623 [>.............................] - ETA: 0s - loss: 0.6180 - acc: 0.6562
    480/623 [======================>.......] - ETA: 0s - loss: 0.6086 - acc: 0.6979
    623/623 [==============================] - 0s - loss: 0.6389 - acc: 0.7030 - val_loss: 0.7115 - val_acc: 0.6455

---


## Experimenting with wider networks      

Now you know everything you need to begin experimenting with different models!  

A model called model_1 has been pre-loaded. You can see a summary of this model printed in the IPython Shell. This is a relatively small network, with only 10 units in each hidden layer.  

In this exercise you'll create a new model called model_2 which is similar to model_1, except it has 100 units in each hidden layer.  

After you create model_2, both models will be fitted, and a graph showing both models loss score at each epoch will be shown. We added the argument verbose=False in the fitting commands to print out fewer updates, since you will look at these graphically instead of as text.  

Because you are fitting two models, it will take a moment to see the outputs after you hit run, so be patient.  

### Instructions

 - Create model_2 to replicate model_1, but use 100 nodes instead of 10 for the first two Dense layers you add with the 'relu' activation. Use 2 nodes for the Dense output layer with 'softmax' as the activation.
 - Compile model_2 as you have done with previous models: Using 'adam' as the optimizer, 'categorical_crossentropy' for the loss, and metrics=['accuracy'].
 - Hit 'Submit Answer' to fit both the models and visualize which one gives better results! Notice the keyword argument verbose=False in model.fit(): This prints out fewer updates, since you'll be evaluating the models graphically instead of through text.

```python
# Define early_stopping_monitor
early_stopping_monitor = EarlyStopping(patience=2)

# Create the new model: model_2
model_2 = Sequential()

# Add the first and second layers
model_2.add(Dense(100, activation='relu', input_shape = input_shape))
model_2.add(Dense(100, activation='relu'))

# Add the output layer
model_2.add(Dense(2, activation='softmax'))

# Compile model_2
model_2.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

# Fit model_1
model_1_training = model_1.fit(predictors, target, epochs=15, validation_split=0.2, callbacks=[early_stopping_monitor], verbose=False)

# Fit model_2
model_2_training = model_2.fit(predictors, target, epochs=15, validation_split=0.2, callbacks=[early_stopping_monitor], verbose=False)

# Create the plot
plt.plot(model_1_training.history['val_loss'], 'r', model_2_training.history['val_loss'], 'b')
plt.xlabel('Epochs')
plt.ylabel('Validation score')
plt.show()
```

### Results :  

![graph2](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Deep%20Learning%20in%20Python/img/graph2.svg)

The blue model is the one you made, the red is the original model. Your model had a lower loss value, so it is the better model. Nice job!  

    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    dense_1 (Dense)              (None, 10)                110       
    _________________________________________________________________
    dense_2 (Dense)              (None, 10)                110       
    _________________________________________________________________
    dense_3 (Dense)              (None, 2)                 22        
    =================================================================
    Total params: 242.0
    Trainable params: 242
    Non-trainable params: 0.0
    _________________________________________________________________
    None

---


## Adding layers to a network     

You've seen how to experiment with wider networks. In this exercise, you'll try a deeper network (more hidden layers).  

Once again, you have a baseline model called model_1 as a starting point. It has 1 hidden layer, with 50 units. You can see a summary of that model's structure printed out. You will create a similar network with 3 hidden layers (still keeping 50 units in each layer).  

This will again take a moment to fit both models, so you'll need to wait a few seconds to see the results after you run your code.  

### Instructions

 - Specify a model called model_2 that is like model_1, but which has 3 hidden layers of 50 units instead of only 1 hidden layer.
 - Use input_shape to specify the input shape in the first hidden layer.
 - Use 'relu' activation for the 3 hidden layers and 'softmax' for the output layer, which should have 2 units.
 - Compile model_2 as you have done with previous models: Using 'adam' as the optimizer, 'categorical_crossentropy' for the loss, and metrics=['accuracy'].
 - Hit 'Submit Answer' to fit both the models and visualize which one gives better results! For both models, you should look for the best val_loss and val_acc, which won't be the last epoch for that model.

```python
# The input shape to use in the first hidden layer
input_shape = (n_cols,)

# Create the new model: model_2
model_2 = Sequential()

# Add the first, second, and third hidden layers
model_2.add(Dense(50, activation='relu', input_shape = input_shape))
model_2.add(Dense(50, activation='relu'))
model_2.add(Dense(50, activation='relu'))

# Add the output layer
model_2.add(Dense(2, activation='softmax'))

# Compile model_2
model_2.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

# Fit model 1
model_1_training = model_1.fit(predictors, target, epochs=20, validation_split=0.4, callbacks=[early_stopping_monitor], verbose=False)

# Fit model 2
model_2_training = model_2.fit(predictors, target, epochs=20, validation_split=0.4, callbacks=[early_stopping_monitor], verbose=False)

# Create the plot
plt.plot(model_1_training.history['val_loss'], 'r', model_2_training.history['val_loss'], 'b')
plt.xlabel('Epochs')
plt.ylabel('Validation score')
plt.show()

```

### Results :  

![graph3](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Deep%20Learning%20in%20Python/img/graph3.svg)

Great work! The blue model is the one you made and the red is the original model. The model with the lower loss value is the better model.  

    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    dense_1 (Dense)              (None, 50)                550       
    _________________________________________________________________
    dense_2 (Dense)              (None, 2)                 102       
    =================================================================
    Total params: 652.0
    Trainable params: 652
    Non-trainable params: 0.0
    _________________________________________________________________
    None


---


## Experimenting with model structures    

You've just run an experiment where you compared two networks that were identical except that the 2nd network had an extra hidden layer. You see that this 2nd network (the deeper network) had better performance. Given that, which of the following would be a good experiment to run next for even better performance?  

### Possible Answers => 2

 - Try a new network with fewer layers than anything you have tried yet.
 - Use more units in each hidden layer.
 - Use fewer units in each hidden layer.

```python
```

### Results :  

Well done! Increasing the number of units in each hidden layer would be a good next step to try achieving even better performance.  

---


## Building your own digit recognition model   

You've reached the final exercise of the course - you now know everything you need to build an accurate model to recognize handwritten digits!  

We've already done the basic manipulation of the MNIST dataset shown in the video, so you have X and y loaded and ready to model with. Sequential and Dense from keras are also pre-imported.  

To add an extra challenge, we've loaded only 2500 images, rather than 60000 which you will see in some published results. Deep learning models perform better with more data, however, they also take longer to train, especially when they start becoming more complex.  

If you have a computer with a CUDA compatible GPU, you can take advantage of it to improve computation time. If you don't have a GPU, no problem! You can set up a deep learning environment in the cloud that can run your models on a GPU. Here is a [blog post](https://www.datacamp.com/community/tutorials/deep-learning-jupyter-aws) by Dan that explains how to do this - check it out after completing this exercise! It is a great next step as you continue your deep learning journey.  

### Instructions

 - Create a Sequential object to start your model. Call this model.
 - Add the first Dense hidden layer of 50 units to your model with 'relu' activation. For this data, the input_shape is (784,).
 - Add a second Dense hidden layer with 50 units and a 'relu' activation function.
 - Add the output layer. Your activation function should be 'softmax', and the number of nodes in this layer should be the same as the number of possible outputs in this case: 10.
 - Compile model as you have done with previous models: Using 'adam' as the optimizer, 'categorical_crossentropy' for the loss, and metrics=['accuracy'].
 - Fit the model using X and y using a validation_split of 0.3.

```python
# Create the model: model
model = Sequential()

# Add the first hidden layer
model.add(Dense(50, activation='relu', input_shape = (784,)))

# Add the second hidden layer
model.add(Dense(50, activation='relu'))

# Add the output layer
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

# Fit the model
model.fit(X, y, validation_split=0.3)
```

### Results :  

Congrats! You've done something pretty amazing. You should see better than 90% accuracy recognizing handwritten digits, even while using a small training set of only 1750 images!  

    <script.py> output:
        Train on 1750 samples, validate on 750 samples
        Epoch 1/10

      32/1750 [..............................] - ETA: 2s - loss: 2.2931 - acc: 0.1875
     448/1750 [======>.......................] - ETA: 0s - loss: 2.1553 - acc: 0.2879
     832/1750 [=============>................] - ETA: 0s - loss: 2.0242 - acc: 0.3774
    1248/1750 [====================>.........] - ETA: 0s - loss: 1.8353 - acc: 0.4647
    1664/1750 [===========================>..] - ETA: 0s - loss: 1.6496 - acc: 0.5343
    1750/1750 [==============================] - 0s - loss: 1.6094 - acc: 0.5474 - val_loss: 0.8862 - val_acc: 0.7933
        Epoch 2/10

      32/1750 [..............................] - ETA: 0s - loss: 0.9038 - acc: 0.7500
     512/1750 [=======>......................] - ETA: 0s - loss: 0.7189 - acc: 0.8320
     992/1750 [================>.............] - ETA: 0s - loss: 0.6684 - acc: 0.8306
    1472/1750 [========================>.....] - ETA: 0s - loss: 0.6408 - acc: 0.8295
    1750/1750 [==============================] - 0s - loss: 0.6380 - acc: 0.8303 - val_loss: 0.5199 - val_acc: 0.8533
        Epoch 3/10

      32/1750 [..............................] - ETA: 0s - loss: 0.5629 - acc: 0.7188
     512/1750 [=======>......................] - ETA: 0s - loss: 0.4147 - acc: 0.8867
     992/1750 [================>.............] - ETA: 0s - loss: 0.4136 - acc: 0.8881
    1472/1750 [========================>.....] - ETA: 0s - loss: 0.4137 - acc: 0.8818
    1750/1750 [==============================] - 0s - loss: 0.4155 - acc: 0.8817 - val_loss: 0.4270 - val_acc: 0.8800
        Epoch 4/10

      32/1750 [..............................] - ETA: 0s - loss: 0.3230 - acc: 0.9375
     512/1750 [=======>......................] - ETA: 0s - loss: 0.3645 - acc: 0.9043
     896/1750 [==============>...............] - ETA: 0s - loss: 0.3239 - acc: 0.9141
    1312/1750 [=====================>........] - ETA: 0s - loss: 0.3239 - acc: 0.9085
    1750/1750 [==============================] - 0s - loss: 0.3297 - acc: 0.9029 - val_loss: 0.3774 - val_acc: 0.8893
        Epoch 5/10

      32/1750 [..............................] - ETA: 0s - loss: 0.1501 - acc: 0.9688
     480/1750 [=======>......................] - ETA: 0s - loss: 0.2319 - acc: 0.9375
     736/1750 [===========>..................] - ETA: 0s - loss: 0.2316 - acc: 0.9334
     864/1750 [=============>................] - ETA: 0s - loss: 0.2367 - acc: 0.9352
     992/1750 [================>.............] - ETA: 0s - loss: 0.2430 - acc: 0.9325
    1248/1750 [====================>.........] - ETA: 0s - loss: 0.2614 - acc: 0.9271
    1408/1750 [=======================>......] - ETA: 0s - loss: 0.2596 - acc: 0.9290
    1600/1750 [==========================>...] - ETA: 0s - loss: 0.2661 - acc: 0.9263
    1750/1750 [==============================] - 0s - loss: 0.2627 - acc: 0.9263 - val_loss: 0.3697 - val_acc: 0.8840
        Epoch 6/10

      32/1750 [..............................] - ETA: 0s - loss: 0.2564 - acc: 0.8750
     416/1750 [======>.......................] - ETA: 0s - loss: 0.1997 - acc: 0.9375
     896/1750 [==============>...............] - ETA: 0s - loss: 0.1824 - acc: 0.9487
    1376/1750 [======================>.......] - ETA: 0s - loss: 0.2088 - acc: 0.9426
    1750/1750 [==============================] - 0s - loss: 0.2217 - acc: 0.9354 - val_loss: 0.3512 - val_acc: 0.8920
        Epoch 7/10

      32/1750 [..............................] - ETA: 0s - loss: 0.1012 - acc: 0.9688
     288/1750 [===>..........................] - ETA: 0s - loss: 0.1429 - acc: 0.9688
     672/1750 [==========>...................] - ETA: 0s - loss: 0.1605 - acc: 0.9583
    1152/1750 [==================>...........] - ETA: 0s - loss: 0.1664 - acc: 0.9549
    1632/1750 [==========================>...] - ETA: 0s - loss: 0.1791 - acc: 0.9516
    1750/1750 [==============================] - 0s - loss: 0.1817 - acc: 0.9514 - val_loss: 0.3509 - val_acc: 0.8973
        Epoch 8/10

      32/1750 [..............................] - ETA: 0s - loss: 0.1694 - acc: 0.9062
     416/1750 [======>.......................] - ETA: 0s - loss: 0.1598 - acc: 0.9639
     864/1750 [=============>................] - ETA: 0s - loss: 0.1679 - acc: 0.9595
    1344/1750 [======================>.......] - ETA: 0s - loss: 0.1577 - acc: 0.9576
    1750/1750 [==============================] - 0s - loss: 0.1608 - acc: 0.9589 - val_loss: 0.3322 - val_acc: 0.9067
        Epoch 9/10

      32/1750 [..............................] - ETA: 0s - loss: 0.1261 - acc: 1.0000
     512/1750 [=======>......................] - ETA: 0s - loss: 0.0992 - acc: 0.9844
     928/1750 [==============>...............] - ETA: 0s - loss: 0.1197 - acc: 0.9806
    1376/1750 [======================>.......] - ETA: 0s - loss: 0.1254 - acc: 0.9731
    1750/1750 [==============================] - 0s - loss: 0.1322 - acc: 0.9709 - val_loss: 0.3393 - val_acc: 0.8960
        Epoch 10/10

      32/1750 [..............................] - ETA: 0s - loss: 0.0458 - acc: 1.0000
     224/1750 [==>...........................] - ETA: 0s - loss: 0.1191 - acc: 0.9821
     384/1750 [=====>........................] - ETA: 0s - loss: 0.1161 - acc: 0.9818
     544/1750 [========>.....................] - ETA: 0s - loss: 0.1109 - acc: 0.9835
     864/1750 [=============>................] - ETA: 0s - loss: 0.1088 - acc: 0.9826
    1280/1750 [====================>.........] - ETA: 0s - loss: 0.1084 - acc: 0.9812
    1504/1750 [========================>.....] - ETA: 0s - loss: 0.1150 - acc: 0.9801
    1750/1750 [==============================] - 0s - loss: 0.1156 - acc: 0.9806 - val_loss: 0.3376 - val_acc: 0.9000


---
