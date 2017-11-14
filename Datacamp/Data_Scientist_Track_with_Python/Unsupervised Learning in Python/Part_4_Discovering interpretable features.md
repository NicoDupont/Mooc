11/2017  
# Datacamp - Unsupervised Learning in Python (Data Scientist Track with Python)  
[Unsupervised Learning in Python](https://www.datacamp.com/courses/unsupervised-learning-in-python)

---

***Course Description***  

Say you have a collection of customers with a variety of characteristics such as age, location, and financial history, and you wish to discover patterns and sort them into clusters. Or perhaps you have a set of texts, such as wikipedia pages, and you wish to segment them into categories based on their content. This is the world of unsupervised learning, called as such because you are not guiding, or supervising, the pattern discovery by some prediction task, but instead uncovering hidden structure from unlabeled data. Unsupervised learning encompasses a variety of techniques in machine learning, from clustering to dimension reduction to matrix factorization. In this course, you'll learn the fundamentals of unsupervised learning and implement the essential algorithms using scikit-learn and scipy. You will learn how to cluster, transform, visualize, and extract insights from unlabeled datasets, and end the course by building a recommender system to recommend popular musical artists.     

# Part 4 : Discovering interpretable features     

In this chapter, you'll learn about a dimension reduction technique called "Non-negative matrix factorization" ("NMF") that expresses samples as combinations of interpretable parts. For example, it expresses documents as combinations of topics, and images in terms of commonly occurring visual patterns. You'll also learn to use NMF to build recommender systems that can find you similar articles to read, or musical artists that match your listening history!      

## Non-negative data   

Which of the following 2-dimensional arrays are examples of non-negative data?  

 - A tf-idf word-frequency array.  
 - An array daily stock market price movements (up and down), where each row represents a company.  
 - An array where rows are customers, columns are products and entries are 0 or 1, indicating whether a customer has purchased a product.    

### Possible answers => 3

 - 1 only
 - 2 and 3
 - 1 and 3

```python

```

### Results :  

Well done! Stock prices can go down as well as up, so an array of daily stock market price movements is not an example of non-negative data.  

---


## NMF applied to Wikipedia articles      

In the video, you saw NMF applied to transform a toy word-frequency array. Now it's your turn to apply NMF, this time using the tf-idf word-frequency array of Wikipedia articles, given as a csr matrix articles. Here, fit the model and transform the articles. In the next exercise, you'll explore the result.    

### Instructions

 - Import NMF from sklearn.decomposition.
 - Create an NMF instance called model with 6 components.
 - Fit the model to the word count data articles.
 - Use the .transform() method of model to transform articles, and assign the result to nmf_features.
 - Print nmf_features to get a first idea what it looks like.

```python
# Import NMF
from sklearn.decomposition import NMF

# Create an NMF instance: model
model = NMF(n_components=6)

# Fit the model to articles
model.fit(articles)

# Transform the articles: nmf_features
nmf_features = model.transform(articles)

# Print the NMF features
print(nmf_features)
```

### Results :  

Fantastic - these NMF features don't make much sense at this point, but you will explore them in the next exercise!  

	<script.py> output:
		[[  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
			0.00000000e+00   4.40465961e-01]
		 [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
			0.00000000e+00   5.66606133e-01]
		 [  3.82036214e-03   0.00000000e+00   0.00000000e+00   0.00000000e+00
			0.00000000e+00   3.98647445e-01]
		 [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
			0.00000000e+00   3.81740425e-01]
		 [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
			0.00000000e+00   4.85518103e-01]
		 [  1.29284719e-02   1.37892330e-02   7.76348334e-03   3.34428961e-02
			0.00000000e+00   3.34523219e-01]
		 [  0.00000000e+00   0.00000000e+00   2.06750429e-02   0.00000000e+00
			6.04413529e-03   3.59061448e-01]
		 [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
			0.00000000e+00   4.90977760e-01]
		 [  1.54266533e-02   1.42819611e-02   3.76647536e-03   2.37072683e-02
			2.62586865e-02   4.80775547e-01]
		 [  1.11733445e-02   3.13683468e-02   3.09496996e-02   6.56889568e-02
			1.96651499e-02   3.38290095e-01]
		 [  0.00000000e+00   0.00000000e+00   5.30739618e-01   0.00000000e+00
			2.83644190e-02   0.00000000e+00]
		 [  0.00000000e+00   0.00000000e+00   3.56522859e-01   0.00000000e+00
			0.00000000e+00   0.00000000e+00]
		 [  1.20121639e-02   6.50047346e-03   3.12257123e-01   6.09671149e-02
			1.13847105e-02   1.92603386e-02]
		 [  3.93466960e-03   6.24444789e-03   3.42386270e-01   1.10750938e-02
			0.00000000e+00   0.00000000e+00]
		 [  4.63799563e-03   0.00000000e+00   4.34931593e-01   0.00000000e+00
			3.84227295e-02   3.08135802e-03]
		 [  0.00000000e+00   0.00000000e+00   4.83307476e-01   0.00000000e+00
			0.00000000e+00   0.00000000e+00]
		 [  5.64990349e-03   1.83536168e-02   3.76547303e-01   3.25407602e-02
			0.00000000e+00   1.13335489e-02]
		 [  0.00000000e+00   0.00000000e+00   4.80932052e-01   0.00000000e+00
			0.00000000e+00   0.00000000e+00]
		 [  0.00000000e+00   9.01867445e-03   5.51028873e-01   0.00000000e+00
			0.00000000e+00   0.00000000e+00]
		 [  0.00000000e+00   0.00000000e+00   4.65987338e-01   0.00000000e+00
			0.00000000e+00   0.00000000e+00]
		 [  0.00000000e+00   1.14081410e-02   2.08663739e-02   5.17682920e-01
			5.81336327e-02   1.37856003e-02]
		 [  0.00000000e+00   0.00000000e+00   0.00000000e+00   5.10392135e-01
			0.00000000e+00   0.00000000e+00]
		 [  0.00000000e+00   5.60107246e-03   0.00000000e+00   4.22311050e-01
			0.00000000e+00   0.00000000e+00]
		 [  0.00000000e+00   0.00000000e+00   0.00000000e+00   4.36680114e-01
			0.00000000e+00   0.00000000e+00]
		 [  0.00000000e+00   0.00000000e+00   0.00000000e+00   4.98010903e-01
			0.00000000e+00   0.00000000e+00]
		 [  9.88347371e-02   8.60046602e-02   3.91051202e-03   3.80955425e-01
			4.39184302e-04   5.22162073e-03]
		 [  0.00000000e+00   0.00000000e+00   0.00000000e+00   5.72076643e-01
			0.00000000e+00   7.13559643e-03]
		 [  1.31462589e-02   1.04853766e-02   0.00000000e+00   4.68829644e-01
			0.00000000e+00   1.16311185e-02]
		 [  3.84532670e-03   0.00000000e+00   0.00000000e+00   5.75616751e-01
			0.00000000e+00   0.00000000e+00]
		 [  2.25235731e-03   1.38738770e-03   0.00000000e+00   5.27859698e-01
			1.20249640e-02   1.49486186e-02]
		 [  0.00000000e+00   4.07549081e-01   1.85721533e-03   0.00000000e+00
			2.96574167e-03   4.52329596e-04]
		 [  1.53413933e-03   6.08174388e-01   5.22296028e-04   6.24750625e-03
			1.18429899e-03   4.40066303e-04]
		 [  5.38793914e-03   2.65017647e-01   5.38531521e-04   1.86895330e-02
			6.38571935e-03   2.90105966e-03]
		 [  0.00000000e+00   6.44917330e-01   0.00000000e+00   0.00000000e+00
			0.00000000e+00   0.00000000e+00]
		 [  0.00000000e+00   6.08908324e-01   0.00000000e+00   0.00000000e+00
			0.00000000e+00   0.00000000e+00]
		 [  0.00000000e+00   3.43686011e-01   0.00000000e+00   0.00000000e+00
			3.97745944e-03   0.00000000e+00]
		 [  6.10479873e-03   3.15313517e-01   1.54885857e-02   0.00000000e+00
			5.06182022e-03   4.74335820e-03]
		 [  6.47342385e-03   2.13329031e-01   9.49532071e-03   4.56906708e-02
			1.71893237e-02   9.52065946e-03]
		 [  7.99109463e-03   4.67596208e-01   0.00000000e+00   2.43385621e-02
			0.00000000e+00   0.00000000e+00]
		 [  0.00000000e+00   6.42821540e-01   0.00000000e+00   2.35815875e-03
			0.00000000e+00   0.00000000e+00]
		 [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
			4.77021221e-01   0.00000000e+00]
		 [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
			4.94192235e-01   0.00000000e+00]
		 [  0.00000000e+00   2.99073970e-04   2.14498143e-03   0.00000000e+00
			3.81729068e-01   5.83788462e-03]
		 [  0.00000000e+00   0.00000000e+00   0.00000000e+00   5.64604241e-03
			5.42171143e-01   0.00000000e+00]
		 [  1.78051606e-03   7.84417271e-04   1.41633578e-02   4.59757122e-04
			4.24247395e-01   0.00000000e+00]
		 [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
			5.11325712e-01   0.00000000e+00]
		 [  0.00000000e+00   0.00000000e+00   3.28401067e-03   0.00000000e+00
			3.72838407e-01   0.00000000e+00]
		 [  0.00000000e+00   2.62086340e-04   3.61118537e-02   2.32305055e-04
			2.30480837e-01   0.00000000e+00]
		 [  1.12512407e-02   2.12327860e-03   1.60978891e-02   1.02468154e-02
			3.25419278e-01   3.75882751e-02]
		 [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
			4.18903909e-01   3.57730354e-04]
		 [  3.08358864e-01   0.00000000e+00   0.00000000e+00   0.00000000e+00
			0.00000000e+00   0.00000000e+00]
		 [  3.68164151e-01   0.00000000e+00   0.00000000e+00   0.00000000e+00
			0.00000000e+00   0.00000000e+00]
		 [  3.97934378e-01   2.81703744e-02   3.67025815e-03   1.70038769e-02
			1.95941901e-03   2.11645135e-02]
		 [  3.75784707e-01   2.07521226e-03   0.00000000e+00   3.72093538e-02
			0.00000000e+00   5.85929861e-03]
		 [  4.38016661e-01   0.00000000e+00   0.00000000e+00   0.00000000e+00
			0.00000000e+00   0.00000000e+00]
		 [  4.57868953e-01   0.00000000e+00   0.00000000e+00   0.00000000e+00
			0.00000000e+00   0.00000000e+00]
		 [  2.75469972e-01   4.46957712e-03   0.00000000e+00   5.29568979e-02
			0.00000000e+00   1.90998282e-02]
		 [  4.45182195e-01   0.00000000e+00   0.00000000e+00   0.00000000e+00
			5.48627739e-03   0.00000000e+00]
		 [  2.92732682e-01   1.33665108e-02   1.14267879e-02   1.05182843e-02
			1.87672166e-01   9.23968567e-03]
		 [  3.78256534e-01   1.43970659e-02   0.00000000e+00   9.85078688e-02
			1.35882828e-02   0.00000000e+00]]

---


## NMF features of the Wikipedia articles      

Now you will explore the NMF features you created in the previous exercise. A solution to the previous exercise has been pre-loaded, so the array nmf_features is available. Also available is a list titles giving the title of each Wikipedia article.  

When investigating the features, notice that for both actors, the NMF feature 3 has by far the highest value. This means that both articles are reconstructed using mainly the 3rd NMF component. In the next video, you'll see why: NMF components represent topics (for instance, acting!).    

### Instructions

 - Import pandas as pd.
 - Create a DataFrame df from nmf_features using pd.DataFrame(). Set the index to titles using index=titles.
 - Use the .loc[] accessor of df to select the row with title 'Anne Hathaway', and print the result. These are the NMF features for the article about the actress Anne Hathaway.
 - Repeat the last step for 'Denzel Washington' (another actor).

```python
print( nmf_features[:5])
print('--------------')
print(titles)
print('--------------')

# Import pandas
import pandas as pd

# Create a pandas DataFrame: df
df = pd.DataFrame(nmf_features,index=titles)

print(df.head())
print('--------------')

# Print the row for 'Anne Hathaway'
print(df.loc['Anne Hathaway'])

# Print the row for 'Denzel Washington'
print(df.loc['Denzel Washington'])
```

### Results :  

Great work! Notice that for both actors, the NMF feature 3 has by far the highest value. This means that both articles are reconstructed using mainly the 3rd NMF component. In the next video, you'll see why: NMF components represent topics (for instance, acting!).  

	<script.py> output:
		[[ 0.          0.          0.          0.          0.          0.44046532]
		 [ 0.          0.          0.          0.          0.          0.56660476]
		 [ 0.00382058  0.          0.          0.          0.          0.39864643]
		 [ 0.          0.          0.          0.          0.          0.38173975]
		 [ 0.          0.          0.          0.          0.          0.48551712]]
		--------------
		['HTTP 404', 'Alexa Internet', 'Internet Explorer', 'HTTP cookie', 'Google Search', 'Tumblr', 'Hypertext Transfer Protocol', 'Social search', 'Firefox', 'LinkedIn', 'Global warming', 'Nationally Appropriate Mitigation Action', 'Nigel Lawson', 'Connie Hedegaard', 'Climate change', 'Kyoto Protocol', '350.org', 'Greenhouse gas emissions by the United States', '2010 United Nations Climate Change Conference', '2007 United Nations Climate Change Conference', 'Angelina Jolie', 'Michael Fassbender', 'Denzel Washington', 'Catherine Zeta-Jones', 'Jessica Biel', 'Russell Crowe', 'Mila Kunis', 'Dakota Fanning', 'Anne Hathaway', 'Jennifer Aniston', 'France national football team', 'Cristiano Ronaldo', 'Arsenal F.C.', 'Radamel Falcao', 'Zlatan Ibrahimović', 'Colombia national football team', '2014 FIFA World Cup qualification', 'Football', 'Neymar', 'Franck Ribéry', 'Tonsillitis', 'Hepatitis B', 'Doxycycline', 'Leukemia', 'Gout', 'Hepatitis C', 'Prednisone', 'Fever', 'Gabapentin', 'Lymphoma', 'Chad Kroeger', 'Nate Ruess', 'The Wanted', 'Stevie Nicks', 'Arctic Monkeys', 'Black Sabbath', 'Skrillex', 'Red Hot Chili Peppers', 'Sepsis', 'Adam Levine']
		--------------
								  0    1    2    3    4         5
		HTTP 404           0.000000  0.0  0.0  0.0  0.0  0.440465
		Alexa Internet     0.000000  0.0  0.0  0.0  0.0  0.566605
		Internet Explorer  0.003821  0.0  0.0  0.0  0.0  0.398646
		HTTP cookie        0.000000  0.0  0.0  0.0  0.0  0.381740
		Google Search      0.000000  0.0  0.0  0.0  0.0  0.485517
		--------------
		0    0.003845
		1    0.000000
		2    0.000000
		3    0.575711
		4    0.000000
		5    0.000000
		Name: Anne Hathaway, dtype: float64
		0    0.000000
		1    0.005601
		2    0.000000
		3    0.422380
		4    0.000000
		5    0.000000
		Name: Denzel Washington, dtype: float64

---



## NMF reconstructs samples      

In this exercise, you'll check your understanding of how NMF reconstructs samples from its components using the NMF feature values. On the right are the components of an NMF model. If the NMF feature values of a sample are [2, 1], then which of the following is most likely to represent the original sample? A pen and paper will help here! You have to apply the same technique Ben used in the video to reconstruct the sample [0.1203 0.1764 0.3195 0.141].    

### Possible answers => 1

 - [2.2, 1.0, 2.0].
 - [0.5, 1.6, 3.1].
 - [-4.0, 1.0, -2.0].

```python

```

### Results :  

Well done, you've got it!  

	[[ 1.   0.5  0. ]
	 [ 0.2  0.1  2.1]]


---



## NMF learns topics of documents      

In the video, you learned when NMF is applied to documents, the components correspond to topics of documents, and the NMF features reconstruct the documents from the topics. Verify this for yourself for the NMF model that you built earlier using the Wikipedia articles. Previously, you saw that the 3rd NMF feature value was high for the articles about actors Anne Hathaway and Denzel Washington. In this exercise, identify the topic of the corresponding NMF component.  

The NMF model you built earlier is available as model, while words is a list of the words that label the columns of the word-frequency array.  

After you are done, take a moment to recognise the topic that the articles about Anne Hathaway and Denzel Washington have in common!    

### Instructions

 - Import pandas as pd.
 - Create a DataFrame components_df from model.components_, setting columns=words so that columns are labeled by the words.
 - Print components_df.shape to check the dimensions of the DataFrame.
 - Use the .iloc[] accessor on the DataFrame components_df to select row 3. Assign the result to component.
 - Call the .nlargest() method of component, and print the result. This gives the five words with the highest values for that component.

```python
# Import pandas
import pandas as pd

# Create a DataFrame: components_df
components_df = pd.DataFrame(model.components_,columns=words)

# Print the shape of the DataFrame
print(components_df.shape)

# Select row 3: component
component = components_df.iloc[3]

# Print result of nlargest
print(component.nlargest())
```

### Results :  

Great work! Take a moment to recognise the topics that the articles about Anne Hathaway and Denzel Washington have in common!  

	<script.py> output:
		(6, 13125)
		film       0.627877
		award      0.253131
		starred    0.245284
		role       0.211451
		actress    0.186398
		Name: 3, dtype: float64

---


## Explore the LED digits dataset      

In the following exercises, you'll use NMF to decompose grayscale images into their commonly occurring patterns. Firstly, explore the image dataset and see how it is encoded as an array. You are given 100 images as a 2D array samples, where each row represents a single 13x8 image. The images in your dataset are pictures of a LED digital display.    

### Instructions

 - Import matplotlib.pyplot as plt.
 - Select row 0 of samples and assign the result to digit. For example, to select column 2 of an array a, you could use a[:,2]. Remember that since samples is a NumPy array, you can't use the .loc[] or iloc[] accessors to select specific rows or columns.
 - Print digit. This has been done for you. Notice that it is a 1D array of 0s and 1s.
 - Use the .reshape() method of digit to get a 2D array with shape (13, 8). Assign the result to bitmap.
 - Print bitmap, and notice that the 1s show the digit 7!
 - Use the plt.imshow() function to display bitmap as an image.

```python
# Import pyplot
from matplotlib import pyplot as plt

# Select the 0th row: digit
digit = samples[0,:]

# Print digit
print(digit)

# Reshape digit to a 13x8 array: bitmap
bitmap = digit.reshape((13,8))

# Print bitmap
print(bitmap)

# Use plt.imshow to display bitmap
plt.imshow(bitmap, cmap='gray', interpolation='nearest')
plt.colorbar()
plt.show()
```

### Results :  

Excellent job! You'll explore this dataset further in the next exercise and see for yourself how NMF can learn the parts of images.  

	<script.py> output:
		[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  1.  1.  1.  1.  0.  0.  0.  0.
		  0.  0.  0.  0.  1.  0.  0.  0.  0.  0.  0.  0.  1.  0.  0.  0.  0.  0.
		  0.  0.  1.  0.  0.  0.  0.  0.  0.  0.  1.  0.  0.  0.  0.  0.  0.  0.
		  0.  0.  0.  0.  0.  0.  0.  0.  1.  0.  0.  0.  0.  0.  0.  0.  1.  0.
		  0.  0.  0.  0.  0.  0.  1.  0.  0.  0.  0.  0.  0.  0.  1.  0.  0.  0.
		  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
		[[ 0.  0.  0.  0.  0.  0.  0.  0.]
		 [ 0.  0.  1.  1.  1.  1.  0.  0.]
		 [ 0.  0.  0.  0.  0.  0.  1.  0.]
		 [ 0.  0.  0.  0.  0.  0.  1.  0.]
		 [ 0.  0.  0.  0.  0.  0.  1.  0.]
		 [ 0.  0.  0.  0.  0.  0.  1.  0.]
		 [ 0.  0.  0.  0.  0.  0.  0.  0.]
		 [ 0.  0.  0.  0.  0.  0.  1.  0.]
		 [ 0.  0.  0.  0.  0.  0.  1.  0.]
		 [ 0.  0.  0.  0.  0.  0.  1.  0.]
		 [ 0.  0.  0.  0.  0.  0.  1.  0.]
		 [ 0.  0.  0.  0.  0.  0.  0.  0.]
		 [ 0.  0.  0.  0.  0.  0.  0.  0.]]

---


## NMF learns the parts of images      

Now use what you've learned about NMF to decompose the digits dataset. You are again given the digit images as a 2D array samples. This time, you are also provided with a function show_as_image() that displays the image encoded by any 1D array:  

```python
def show_as_image(sample):
    bitmap = sample.reshape((13, 8))
    plt.figure()
    plt.imshow(bitmap, cmap='gray', interpolation='nearest')
    plt.colorbar()
    plt.show()
```

After you are done, take a moment to look through the plots and notice how NMF has expressed the digit as a sum of the components!    

### Instructions

 - Import NMF from sklearn.decomposition.
 - Create an NMF instance called model with 7 components. (7 is the number of cells in an LED display).
 - Apply the .fit_transform() method of model to samples. Assign the result to features.
 - To each component of the model (accessed via model.components_), apply the show_as_image() function to that component inside the loop.
 - Assign the row 0 of features to digit_features.
 - Print digit_features.

```python
# Import NMF
from sklearn.decomposition import NMF

# Create an NMF model: model
model = NMF(n_components=7)

# Apply fit_transform to samples: features
features = model.fit_transform(samples)

# Call show_as_image on each component
for component in model.components_:
    show_as_image(component)

# Assign the 0th row of features: digit_features
digit_features = features[0,:]

# Print digit_features
print(digit_features)
```

### Results :  

see img/graph17.svg  
see img/graph18.svg  
see img/graph19.svg  
see img/graph20.svg  
see img/graph21.svg  
see img/graph22.svg  
see img/graph23.svg  

Great work! Take a moment to look through the plots and notice how NMF has expressed the digit as a sum of the components!  

	<script.py> output:
		[  4.76823559e-01   0.00000000e+00   0.00000000e+00   5.90605054e-01
		   4.81559442e-01   0.00000000e+00   7.37562716e-16]

---



## PCA doesn't learn parts    

Unlike NMF, PCA doesn't learn the parts of things. Its components do not correspond to topics (in the case of documents) or to parts of images, when trained on images. Verify this for yourself by inspecting the components of a PCA model fit to the dataset of LED digit images from the previous exercise. The images are available as a 2D array samples. Also available is a modified version of the show_as_image() function which colors a pixel red if the value is negative.  

After submitting the answer, notice that the components of PCA do not represent meaningful parts of images of LED digits!    

### Instructions

 - Import PCA from sklearn.decomposition.
 - Create a PCA instance called model with 7 components.
 - Apply the .fit_transform() method of model to samples. Assign the result to features.
 - To each component of the model (accessed via model.components_), apply the show_as_image() function to that component inside the loop.

```python
# Import PCA
from sklearn.decomposition import PCA

# Create a PCA instance: model
model = PCA(n_components=7)

# Apply fit_transform to samples: features
features = model.fit_transform(samples)

# Call show_as_image on each component
for component in model.components_:
    show_as_image(component)
```

### Results :  

see img/graph25.svg  
see img/graph26.svg  
see img/graph27.svg  
see img/graph28.svg  
see img/graph29.svg  
see img/graph30.svg  
see img/graph31.svg  

Great work! Notice that the components of PCA do not represent meaningful parts of images of LED digits!

---



## Which articles are similar to 'Cristiano Ronaldo'?  

In the video, you learned how to use NMF features and the cosine similarity to find similar articles. Apply this to your NMF model for popular Wikipedia articles, by finding the articles most similar to the article about the footballer Cristiano Ronaldo. The NMF features you obtained earlier are available as nmf_features, while titles is a list of the article titles.  

### Instructions

 - Import normalize from sklearn.preprocessing.
 - Apply the normalize() function to nmf_features. Store the result as norm_features.
 - Create a DataFrame df from norm_features, using titles as an index.
 - Use the .loc[] accessor of df to select the row of 'Cristiano Ronaldo'. Assign the result to article.
 - Apply the .dot() method of df to article to calculate the cosine similarity of every row with article.
 - Print the result of the .nlargest() method of similarities to display the most similiar articles. This has been done for you, so hit 'Submit Answer' to see the result!

```python
# Perform the necessary imports
import pandas as pd
from sklearn.preprocessing import normalize

# Normalize the NMF features: norm_features
norm_features = normalize(nmf_features)

# Create a DataFrame: df
df = pd.DataFrame(norm_features,index=titles)

# Select the row corresponding to 'Cristiano Ronaldo': article
article = df.loc['Cristiano Ronaldo']

# Compute the dot products: similarities
similarities = df.dot(article)

# Display those with the largest cosine similarity
print(similarities.nlargest())
```

### Results :  

Great work - although you may need to know a little about football (or soccer, depending on where you're from!) to be able to evaluate for yourself the quality of the computed similarities!  


    <script.py> output:
        Cristiano Ronaldo                1.000000
        Franck Ribéry                    0.999972
        Radamel Falcao                   0.999942
        Zlatan Ibrahimović               0.999942
        France national football team    0.999923
        dtype: float64

---


## Recommend musical artists part I   

In this exercise and the next, you'll use what you've learned about NMF to recommend popular music artists! You are given a sparse array artists whose rows correspond to artists and whose column correspond to users. The entries give the number of times each artist was listened to by each user.  

In this exercise, build a pipeline and transform the array into normalized NMF features. The first step in the pipeline, MaxAbsScaler, transforms the data so that all users have the same influence on the model, regardless of how many different artists they've listened to. In the next exercise, you'll use the resulting normalized NMF features for recommendation!  

This data is part of a larger dataset available [here](http://www-etud.iro.umontreal.ca/~bergstrj/audioscrobbler_data.html).
### Instructions

 - Import:
   - NMF from sklearn.decomposition.
   - Normalizer and MaxAbsScaler from sklearn.preprocessing.
   - make_pipeline from sklearn.pipeline.
 - Create an instance of MaxAbsScaler called scaler.
 - Create an NMF instance with 20 components called nmf.
 - Create an instance of Normalizer called normalizer.
 - Create a pipeline called pipeline that chains together scaler, nmf, and normalizer.
 - Apply the .fit_transform() method of pipeline to artists. Assign the result to norm_features.

```python
# Perform the necessary imports
from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline

# Create a MaxAbsScaler: scaler
scaler = MaxAbsScaler()

# Create an NMF model: nmf
nmf = NMF(n_components=20)

# Create a Normalizer: normalizer
normalizer = Normalizer()

# Create a pipeline: pipeline
pipeline = make_pipeline(scaler,nmf,normalizer)

# Apply fit_transform to artists: norm_features
norm_features = pipeline.fit_transform(artists)
```

### Results :  

Excellent work - now that you've computed the normalized NMF features, you'll use them in the next exercise to recommend musical artists!  

---


## Recommend musical artists part II      

Suppose you were a big fan of Bruce Springsteen - which other musicial artists might you like? Use your NMF features from the previous exercise and the cosine similarity to find similar musical artists. A solution to the previous exercise has been run, so norm_features is an array containing the normalized NMF features as rows. The names of the musical artists are available as the list artist_names.  

### Instructions

 - Import pandas as pd.
 - Create a DataFrame df from norm_features, using artist_names as an index.
 - Use the .loc[] accessor of df to select the row of 'Bruce Springsteen'. Assign the result to artist.
 - Apply the .dot() method of df to artist to calculate the dot product of every row with artist. Save the result as similarities.
 - Print the result of the .nlargest() method of similarities to display the artists most similar to 'Bruce Springsteen'.

```python
# Import pandas
import pandas as pd

# Create a DataFrame: df
df = pd.DataFrame(norm_features,index=artist_names)

# Select row of 'Bruce Springsteen': artist
artist = df.loc['Bruce Springsteen']

# Compute cosine similarities: similarities
similarities = df.dot(artist)

# Display those with highest cosine similarity
print(similarities.nlargest())
```

### Results :  

Well done, and congratulations on reaching the end of the course!   

    <script.py> output:
        Bruce Springsteen    1.000000
        Neil Young           0.958466
        Leonard Cohen        0.917837
        Van Morrison         0.874352
        Bob Dylan            0.865219
        dtype: float64

---
