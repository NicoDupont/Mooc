11/2017  
# Datacamp - Deep Learning in Python (Data Scientist Track with Python)  
[Deep Learning in Python](https://www.datacamp.com/courses/deep-learning-in-python)

---

***Course Description***  

Deep learning is the machine learning technique behind the most exciting capabilities in diverse areas like robotics, natural language processing, image recognition and artificial intelligence (including the famous AlphaGo). In this course, you'll gain hands-on, practical knowledge of how to use deep learning with Keras 2.0, the latest version of a cutting edge library for deep learning in Python.      

# Part 1 : Basics of deep learning and neural networks   

In this chapter, you'll become familiar with the fundamental concepts and terminology used in deep learning, and understand why deep learning techniques are so powerful today. You'll build simple neural networks yourself and generate predictions with them.      

## How many clusters?    

Which of the models in the diagrams has greater ability to account for interactions?  

![ch1ex2](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Deep%Learning%in%Python/img/ch1ex2.png)

### Possible Answers  => 2

 - Model 1.
 - Model 2.
 - They are both the same.

```python
```

### Results :  

Correct! Model 2 has more nodes in the hidden layer, and therefore, greater ability to capture interactions.  

---


## How many clusters?    

In this exercise, you'll write code to do forward propagation (prediction) for your first neural network:

![Ch1Ex4](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Deep%Learning%in%Python/img/1_4.png)

Each data point is a customer. The first input is how many accounts they have, and the second input is how many children they have. The model will predict how many transactions the user makes in the next year. You will use this data throughout the first 2 chapters of this course.  

The input data has been pre-loaded as input_data, and the weights are available in a dictionary called weights. The array of weights for the first node in the hidden layer are in weights['node_0'], and the array of weights for the second node in the hidden layer are in weights['node_1'].  

The weights feeding into the output node are available in weights['output'].  

NumPy will be pre-imported for you as np in all exercises.  

### Instructions

 - Calculate the value in node 0 by multiplying input_data by its weights weights['node_0'] and computing their sum. This is the 1st node in the hidden layer.
 - Calculate the value in node 1 using input_data and weights['node_1']. This is the 2nd node in the hidden layer.
 - Put the hidden layer values into an array. This has been done for you.
 - Generate the prediction by multiplying hidden_layer_outputs by weights['output'] and computing their sum.
 - Hit 'Submit Answer' to print the output!

```python
print(input_data)
print('------------------')
print(weights['node_0'])
print('------------------')
print(weights['node_1'])
print('------------------')
print(weights['output'])
print('------------------')
# Calculate node 0 value: node_0_value
node_0_value = (input_data * weights['node_0']).sum()

# Calculate node 1 value: node_1_value
node_1_value = (input_data * weights['node_1']).sum()

# Put node values into array: hidden_layer_outputs
hidden_layer_outputs = np.array([node_0_value, node_1_value])

# Calculate output: output
output = (hidden_layer_outputs * weights['output']).sum()

# Print output
print(output)
```

### Results :  

Wonderful work! It looks like the network generated a prediction of -39.  

	<script.py> output:
		[3 5]
		------------------
		[2 4]
		------------------
		[ 4 -5]
		------------------
		[2 7]
		------------------
		-39

---


## The Rectified Linear Activation Function      

As Dan explained to you in the video, an "activation function" is a function applied at each node. It converts the node's input into some output.  

The rectified linear activation function (called ReLU) has been shown to lead to very high-performance networks. This function takes a single number as an input, returning 0 if the input is negative, and the input if the input is positive.  

Here are some examples:  
relu(3) = 3   
relu(-3) = 0    

### Instructions

 - Fill in the definition of the relu() function:
 - Use the max() function to calculate the value for the output of relu().
 - Apply the relu() function to node_0_input to calculate node_0_output.
 - Apply the relu() function to node_1_input to calculate node_1_output.

```python
def relu(input):
    '''Define your relu activation function here'''
    # Calculate the value for the output of the relu function: output
    output = max(0, input)
    
    # Return the value just calculated
    return(output)

# Calculate node 0 value: node_0_output
node_0_input = (input_data * weights['node_0']).sum()
node_0_output = relu(node_0_input)

# Calculate node 1 value: node_1_output
node_1_input = (input_data * weights['node_1']).sum()
node_1_output = relu(node_1_input)

# Put node values into array: hidden_layer_outputs
hidden_layer_outputs = np.array([node_0_output, node_1_output])

# Calculate model output (do not apply relu)
model_output = (hidden_layer_outputs * weights['output']).sum()

# Print model output
print(model_output)
```

### Results :  

Great work! You predicted 52 transactions. Without this activation function, you would have predicted a negative number! The real power of activation functions will come soon when you start tuning model weights.  

	<script.py> output:
		52

---


## Applying the network to many observations/rows of data      

You'll now define a function called predict_with_network() which will generate predictions for multiple data observations, which are pre-loaded as input_data. As before, weights are also pre-loaded. In addition, the relu() function you defined in the previous exercise has been pre-loaded.  

### Instructions

 - Define a function called predict_with_network() that accepts two arguments - input_data_row and weights - and returns a prediction from the network as the output.
 - Calculate the input and output values for each node, storing them as: node_0_input, node_0_output, node_1_input, and node_1_output.
	- To calculate the input value of a node, multiply the relevant arrays together and compute their sum.
	- To calculate the output value of a node, apply the relu() function to the input value of the node.
 - Use a for loop to iterate over input_data:
	- Use your predict_with_network() to generate predictions for each row of the input_data - input_data_row. Append each prediction to results.

```python
# Define predict_with_network()
def predict_with_network(input_data_row, weights):

    # Calculate node 0 value
    node_0_input = (input_data_row * weights['node_0']).sum()
    node_0_output = relu(node_0_input)

    # Calculate node 1 value
    node_1_input = (input_data_row * weights['node_1']).sum()
    node_1_output = relu(node_1_input)

    # Put node values into array: hidden_layer_outputs
    hidden_layer_outputs = np.array([node_0_output, node_1_output])
    
    # Calculate model output
    input_to_final_layer = (hidden_layer_outputs * weights['output']).sum()
    model_output = relu(input_to_final_layer)
    
    # Return model output
    return(model_output)


# Create empty list to store prediction results
results = []
for input_data_row in input_data:
    # Append prediction to results
    results.append(predict_with_network(input_data_row, weights))

# Print results
print(results)
```

### Results :  

	<script.py> output:
		[52, 63, 0, 148]

---


## Forward propagation in a deeper network    

You now have a model with 2 hidden layers. The values for an input data point are shown inside the input nodes. The weights are shown on the edges/lines. What prediction would this model make on this data point?  

Assume the activation function at each node is the identity function. That is, each node's output will be the same as its input. So the value of the bottom node in the first hidden layer is -1, and not 0, as it would be if the ReLU activation function was used.  

![ch1ex9](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Deep%Learning%in%Python/img/ch1ex9.png)

### Possible Answers  => 1 (0)

 - 0.
 - 7.
 - 9.

```python
```

### Results :  


---


## Multi-layer neural networks      

In this exercise, you'll write code to do forward propagation for a neural network with 2 hidden layers. Each hidden layer has two nodes. The input data has been preloaded as input_data. The nodes in the first hidden layer are called node_0_0 and node_0_1. Their weights are pre-loaded as weights['node_0_0'] and weights['node_0_1'] respectively.  

The nodes in the second hidden layer are called node_1_0 and node_1_1. Their weights are pre-loaded as weights['node_1_0'] and weights['node_1_1'] respectively.  

We then create a model output from the hidden nodes using weights pre-loaded as weights['output'].  

![ch1ex10](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Data_Scientist_Track_with_Python/Deep%Learning%in%Python/img/ch1ex10.png)

### Instructions

 - Calculate node_0_0_input using its weights weights['node_0_0'] and the given input_data. Then apply the relu() function to get node_0_0_output.
 - Do the same as above for node_0_1_input to get node_0_1_output.
 - Calculate node_1_0_input using its weights weights['node_1_0'] and the outputs from the first hidden layer - hidden_0_outputs. Then apply the relu() function to get node_1_0_output.
 - Do the same as above for node_1_1_input to get node_1_1_output.
 - Calculate model_output using its weights weights['output'] and the outputs from the second hidden layer hidden_1_outputs array. Do not apply the relu() function to this output.

```python
def predict_with_network(input_data):
    # Calculate node 0 in the first hidden layer
    node_0_0_input = (input_data * weights['node_0_0']).sum()
    node_0_0_output = relu(node_0_0_input)

    # Calculate node 1 in the first hidden layer
    node_0_1_input = (input_data * weights['node_0_1']).sum()
    node_0_1_output = relu(node_0_1_input)

    # Put node values into array: hidden_0_outputs
    hidden_0_outputs = np.array([node_0_0_output, node_0_1_output])
    
    # Calculate node 0 in the second hidden layer
    node_1_0_input = (hidden_0_outputs * weights['node_1_0']).sum()
    node_1_0_output = relu(node_1_0_input)

    # Calculate node 1 in the second hidden layer
    node_1_1_input = (hidden_0_outputs * weights['node_1_1']).sum()
    node_1_1_output = relu(node_1_1_input)

    # Put node values into array: hidden_1_outputs
    hidden_1_outputs = np.array([node_1_0_output, node_1_1_output])

    # Calculate model output: model_output
    model_output = (hidden_1_outputs * weights['output']).sum()
    
    # Return model_output
    return(model_output)
```

### Results :  

Wonderful work! The network generated a prediction of 182.  

	<script.py> output:
		182

---


## Representations are learned   

How are the weights that determine the features/interactions in Neural Networks created?  

### Possible Answers => 2

 - A user chooses them when creating the model.
 - The model training process sets them to optimize predictive accuracy.
 - The weights are random numbers.

```python
```

### Results :  

Exactly! You will learn more about how Neural Networks optimize their weights in the next chapter!  

---


## Levels of representation   

Which layers of a model capture more complex or "higher level" interactions?  

### Possible Answers  => 2

 - The first layers capture the most complex interactions.
 - The last layers capture the most complex interactions.
 - All layers capture interactions of similar complexity.

```python
```

### Results :  

Exactly! The last layers capture the most complex interactions.  

---
