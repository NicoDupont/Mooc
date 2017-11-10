11/2017  
# Datacamp - Kaggle Python Tutorial on Machine Learning  
[Kaggle Python Tutorial on Machine Learning](https://www.datacamp.com/community/open-courses/kaggle-python-tutorial-on-machine-learning)

---

## Course description :

Always wanted to compete in a Kaggle competition but not sure you have the right skillset? This interactive tutorial by Kaggle and DataCamp on Machine Learning offers the solution. Step-by-step you will learn through fun coding exercises how to predict survival rate for Kaggle's Titanic competition using Machine Learning techniques. Upload your results and see your ranking go up!   

New to Python? Give our Introduction to Python for Data Science course a try.  


# Part 2 : Predicting with Decision Trees  

After making your first predictions in the previous chapter, it's time to bring you to the next level. In chapter 2 you   


## How it works    

 In the previous chapter, you did all the slicing and dicing yourself to find subsets that have a higher chance of surviving. A decision tree automates this process for you and outputs a classification model or classifier.

Conceptually, the decision tree algorithm starts with all the data at the root node and scans all the variables for the best one to split on. Once a variable is chosen, you do the split and go down one level (or one node) and repeat. The final nodes at the bottom of the decision tree are known as terminal nodes, and the majority vote of the observations in that node determine how to predict for new observations that end up in that terminal node.

First, let's import the necessary libraries:

### Instructions  

 - Import the numpy library as np
 - From sklearn import the tree

```python
# Import the Numpy library
import numpy as np

# Import 'tree' from scikit-learn library
from sklearn import tree
```

### Results :  

		
		
---


## Cleaning and Formatting your Data   

Before you can begin constructing your trees you need to get your hands dirty and clean the data so that you can use all the features available to you. In the first chapter, we saw that the Age variable had some missing value. Missingness is a whole subject with and in itself, but we will use a simple imputation technique where we substitute each missing value with the median of the all present values.    

```python
train["Age"] = train["Age"].fillna(train["Age"].median())
```

Another problem is that the Sex and Embarked variables are categorical but in a non-numeric format. Thus, we will need to assign each class a unique integer so that Python can handle the information. Embarked also has some missing values which you should impute witht the most common class of embarkation, which is "S".      

### Instructions  

 - Assign the integer 1 to all females
 - Impute missing values in Embarked with class S. Use .fillna() method.
 - Replace each class of Embarked with a uniques integer. 0 for S, 1 for C, and 2 for Q.
 - Print the Sex and Embarked columns

```python
# Convert the male and female groups to integer form
train["Sex"][train["Sex"] == 'female'] = 1
train["Sex"][train["Sex"] == 'male'] = 0

# Impute the Embarked variable
train["Embarked"] = train["Embarked"].fillna("S")

# Convert the Embarked classes to integer form
train["Embarked"][train["Embarked"] == "S"] = 0
train["Embarked"][train["Embarked"] == "C"] = 1
train["Embarked"][train["Embarked"] == "Q"] = 2

#Print the Sex and Embarked columns
print(train["Sex"])
print(train["Embarked"])
```

### Results :  

Geat! Now that the data is cleaned up a bit you are ready to begin building your first decision tree.  		
		
---


## Creating your first decision tree      

You will use the scikit-learn and numpy libraries to build your first decision tree. scikit-learn can be used to create tree objects from the DecisionTreeClassifier class. The methods that we will use take numpy arrays as inputs and therefore we will need to create those from the DataFrame that we already have. We will need the following to build a decision tree  

target: A one-dimensional numpy array containing the target/response from the train data. (Survival in your case)  
features: A multidimensional numpy array containing the features/predictors from the train data. (ex. Sex, Age)  
Take a look at the sample code below to see what this would look like:  

```python
target = train["Survived"].values

features = train[["Sex", "Age"]].values

my_tree = tree.DecisionTreeClassifier()

my_tree = my_tree.fit(features, target)
```

One way to quickly see the result of your decision tree is to see the importance of the features that are included. This is done by requesting the .feature_importances_ attribute of your tree object. Another quick metric is the mean accuracy that you can compute using the .score() function with features_one and target as arguments.  

Ok, time for you to build your first decision tree in Python! The train and testing data from chapter 1 are available in your workspace.   

### Instructions  

 - Build the target and features_one numpy arrays. The target will be based on the Survived column in train. The features array will be based on the variables Passenger, Class, Sex, Age, and Passenger Fare
 - Build a decision tree my_tree_one to predict survival using features_one and target
 - Look at the importance of features in your tree and compute the score

```python
# Print the train data to see the available features
print(train)

# Create the target and features numpy arrays: target, features_one
target = train["Survived"].values
features_one = train[["Pclass", "Sex", "Age", "Fare"]].values

# Fit your first decision tree: my_tree_one
my_tree_one = tree.DecisionTreeClassifier()
my_tree_one = my_tree_one.fit(features_one, target)

# Look at the importance and score of the included features
print(my_tree_one.feature_importances_)
print(my_tree_one.score(features_one, target))
```

### Results :  

	<script.py> output:
			 PassengerId  Survived  Pclass  \
		0              1         0       3   
		1              2         1       1   
		2              3         1       3   
		3              4         1       1   
		4              5         0       3   
		5              6         0       3   
		6              7         0       1   
		7              8         0       3   
		8              9         1       3   
		9             10         1       2   
		10            11         1       3   
		11            12         1       1   
		12            13         0       3   
		13            14         0       3   
		14            15         0       3   
		15            16         1       2   
		16            17         0       3   
		17            18         1       2   
		18            19         0       3   
		19            20         1       3   
		20            21         0       2   
		21            22         1       2   
		22            23         1       3   
		23            24         1       1   
		24            25         0       3   
		25            26         1       3   
		26            27         0       3   
		27            28         0       1   
		28            29         1       3   
		29            30         0       3   
		..           ...       ...     ...   
		861          862         0       2   
		862          863         1       1   
		863          864         0       3   
		864          865         0       2   
		865          866         1       2   
		866          867         1       2   
		867          868         0       1   
		868          869         0       3   
		869          870         1       3   
		870          871         0       3   
		871          872         1       1   
		872          873         0       1   
		873          874         0       3   
		874          875         1       2   
		875          876         1       3   
		876          877         0       3   
		877          878         0       3   
		878          879         0       3   
		879          880         1       1   
		880          881         1       2   
		881          882         0       3   
		882          883         0       3   
		883          884         0       2   
		884          885         0       3   
		885          886         0       3   
		886          887         0       2   
		887          888         1       1   
		888          889         0       3   
		889          890         1       1   
		890          891         0       3   
		
														  Name Sex   Age  SibSp  \
		0                              Braund, Mr. Owen Harris   0  22.0      1   
		1    Cumings, Mrs. John Bradley (Florence Briggs Th...   1  38.0      1   
		2                               Heikkinen, Miss. Laina   1  26.0      0   
		3         Futrelle, Mrs. Jacques Heath (Lily May Peel)   1  35.0      1   
		4                             Allen, Mr. William Henry   0  35.0      0   
		5                                     Moran, Mr. James   0  28.0      0   
		6                              McCarthy, Mr. Timothy J   0  54.0      0   
		7                       Palsson, Master. Gosta Leonard   0   2.0      3   
		8    Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)   1  27.0      0   
		9                  Nasser, Mrs. Nicholas (Adele Achem)   1  14.0      1   
		10                     Sandstrom, Miss. Marguerite Rut   1   4.0      1   
		11                            Bonnell, Miss. Elizabeth   1  58.0      0   
		12                      Saundercock, Mr. William Henry   0  20.0      0   
		13                         Andersson, Mr. Anders Johan   0  39.0      1   
		14                Vestrom, Miss. Hulda Amanda Adolfina   1  14.0      0   
		15                    Hewlett, Mrs. (Mary D Kingcome)    1  55.0      0   
		16                                Rice, Master. Eugene   0   2.0      4   
		17                        Williams, Mr. Charles Eugene   0  28.0      0   
		18   Vander Planke, Mrs. Julius (Emelia Maria Vande...   1  31.0      1   
		19                             Masselmani, Mrs. Fatima   1  28.0      0   
		20                                Fynney, Mr. Joseph J   0  35.0      0   
		21                               Beesley, Mr. Lawrence   0  34.0      0   
		22                         McGowan, Miss. Anna "Annie"   1  15.0      0   
		23                        Sloper, Mr. William Thompson   0  28.0      0   
		24                       Palsson, Miss. Torborg Danira   1   8.0      3   
		25   Asplund, Mrs. Carl Oscar (Selma Augusta Emilia...   1  38.0      1   
		26                             Emir, Mr. Farred Chehab   0  28.0      0   
		27                      Fortune, Mr. Charles Alexander   0  19.0      3   
		28                       O'Dwyer, Miss. Ellen "Nellie"   1  28.0      0   
		29                                 Todoroff, Mr. Lalio   0  28.0      0   
		..                                                 ...  ..   ...    ...   
		861                        Giles, Mr. Frederick Edward   0  21.0      1   
		862  Swift, Mrs. Frederick Joel (Margaret Welles Ba...   1  48.0      0   
		863                  Sage, Miss. Dorothy Edith "Dolly"   1  28.0      8   
		864                             Gill, Mr. John William   0  24.0      0   
		865                           Bystrom, Mrs. (Karolina)   1  42.0      0   
		866                       Duran y More, Miss. Asuncion   1  27.0      1   
		867               Roebling, Mr. Washington Augustus II   0  31.0      0   
		868                        van Melkebeke, Mr. Philemon   0  28.0      0   
		869                    Johnson, Master. Harold Theodor   0   4.0      1   
		870                                  Balkic, Mr. Cerin   0  26.0      0   
		871   Beckwith, Mrs. Richard Leonard (Sallie Monypeny)   1  47.0      1   
		872                           Carlsson, Mr. Frans Olof   0  33.0      0   
		873                        Vander Cruyssen, Mr. Victor   0  47.0      0   
		874              Abelson, Mrs. Samuel (Hannah Wizosky)   1  28.0      1   
		875                   Najib, Miss. Adele Kiamie "Jane"   1  15.0      0   
		876                      Gustafsson, Mr. Alfred Ossian   0  20.0      0   
		877                               Petroff, Mr. Nedelio   0  19.0      0   
		878                                 Laleff, Mr. Kristo   0  28.0      0   
		879      Potter, Mrs. Thomas Jr (Lily Alexenia Wilson)   1  56.0      0   
		880       Shelley, Mrs. William (Imanita Parrish Hall)   1  25.0      0   
		881                                 Markun, Mr. Johann   0  33.0      0   
		882                       Dahlberg, Miss. Gerda Ulrika   1  22.0      0   
		883                      Banfield, Mr. Frederick James   0  28.0      0   
		884                             Sutehall, Mr. Henry Jr   0  25.0      0   
		885               Rice, Mrs. William (Margaret Norton)   1  39.0      0   
		886                              Montvila, Rev. Juozas   0  27.0      0   
		887                       Graham, Miss. Margaret Edith   1  19.0      0   
		888           Johnston, Miss. Catherine Helen "Carrie"   1  28.0      1   
		889                              Behr, Mr. Karl Howell   0  26.0      0   
		890                                Dooley, Mr. Patrick   0  32.0      0   
		
			 Parch            Ticket      Fare        Cabin Embarked  
		0        0         A/5 21171    7.2500          NaN        S  
		1        0          PC 17599   71.2833          C85        C  
		2        0  STON/O2. 3101282    7.9250          NaN        S  
		3        0            113803   53.1000         C123        S  
		4        0            373450    8.0500          NaN        S  
		5        0            330877    8.4583          NaN        Q  
		6        0             17463   51.8625          E46        S  
		7        1            349909   21.0750          NaN        S  
		8        2            347742   11.1333          NaN        S  
		9        0            237736   30.0708          NaN        C  
		10       1           PP 9549   16.7000           G6        S  
		11       0            113783   26.5500         C103        S  
		12       0         A/5. 2151    8.0500          NaN        S  
		13       5            347082   31.2750          NaN        S  
		14       0            350406    7.8542          NaN        S  
		15       0            248706   16.0000          NaN        S  
		16       1            382652   29.1250          NaN        Q  
		17       0            244373   13.0000          NaN        S  
		18       0            345763   18.0000          NaN        S  
		19       0              2649    7.2250          NaN        C  
		20       0            239865   26.0000          NaN        S  
		21       0            248698   13.0000          D56        S  
		22       0            330923    8.0292          NaN        Q  
		23       0            113788   35.5000           A6        S  
		24       1            349909   21.0750          NaN        S  
		25       5            347077   31.3875          NaN        S  
		26       0              2631    7.2250          NaN        C  
		27       2             19950  263.0000  C23 C25 C27        S  
		28       0            330959    7.8792          NaN        Q  
		29       0            349216    7.8958          NaN        S  
		..     ...               ...       ...          ...      ...  
		861      0             28134   11.5000          NaN        S  
		862      0             17466   25.9292          D17        S  
		863      2          CA. 2343   69.5500          NaN        S  
		864      0            233866   13.0000          NaN        S  
		865      0            236852   13.0000          NaN        S  
		866      0     SC/PARIS 2149   13.8583          NaN        C  
		867      0          PC 17590   50.4958          A24        S  
		868      0            345777    9.5000          NaN        S  
		869      1            347742   11.1333          NaN        S  
		870      0            349248    7.8958          NaN        S  
		871      1             11751   52.5542          D35        S  
		872      0               695    5.0000  B51 B53 B55        S  
		873      0            345765    9.0000          NaN        S  
		874      0         P/PP 3381   24.0000          NaN        C  
		875      0              2667    7.2250          NaN        C  
		876      0              7534    9.8458          NaN        S  
		877      0            349212    7.8958          NaN        S  
		878      0            349217    7.8958          NaN        S  
		879      1             11767   83.1583          C50        C  
		880      1            230433   26.0000          NaN        S  
		881      0            349257    7.8958          NaN        S  
		882      0              7552   10.5167          NaN        S  
		883      0  C.A./SOTON 34068   10.5000          NaN        S  
		884      0   SOTON/OQ 392076    7.0500          NaN        S  
		885      5            382652   29.1250          NaN        Q  
		886      0            211536   13.0000          NaN        S  
		887      0            112053   30.0000          B42        S  
		888      2        W./C. 6607   23.4500          NaN        S  
		889      0            111369   30.0000         C148        C  
		890      0            370376    7.7500          NaN        Q  
		
		[891 rows x 12 columns]
		[ 0.12818034  0.31274009  0.21690585  0.34217372]
		0.977553310887
		
Well done! Time to investigate your decision tree a bit more.  
		
---


## Interpreting your decision tree   

The feature_importances_ attribute make it simple to interpret the significance of the predictors you include. Based on your decision tree, what variable plays the most important role in determining whether or not a passenger survived? Your model (my_tree_one) is available in the console.  

### Possible answers => 3  

 - Passenger Class
 - Sex/Gender
 - Passenger Fare
 - Age

```python
my_tree_one.feature_importances_
```

### Results :  

	In [1]: my_tree_one.feature_importances_
	Out[1]: array([ 0.1269655 ,  0.31274009,  0.23147703,  0.32881738])

Bellissimo! Time to make a prediction and submit it to Kaggle!  		
		
---


## Predict and submit to Kaggle     

To send a submission to Kaggle you need to predict the survival rates for the observations in the test set. In the last exercise of the previous chapter, we created simple predictions based on a single subset. Luckily, with our decision tree, we can make use of some simple functions to "generate" our answer without having to manually perform subsetting.  

First, you make use of the .predict() method. You provide it the model (my_tree_one), the values of features from the dataset for which predictions need to be made (test). To extract the features we will need to create a numpy array in the same way as we did when training the model. However, we need to take care of a small but important problem first. There is a missing value in the Fare feature that needs to be imputed.  

Next, you need to make sure your output is in line with the submission requirements of Kaggle: a csv file with exactly 418 entries and two columns: PassengerId and Survived. Then use the code provided to make a new data frame using DataFrame(), and create a csv file using to_csv() method from Pandas.   

### Instructions  

 - Impute the missing value for Fare in row 153 with the median of the column.
 - Make a prediction on the test set using the .predict() method and my_tree_one. Assign the result to my_prediction.
 - Create a data frame my_solution containing the solution and the passenger ids from the test set. Make sure the solution is in line with the standards set forth by Kaggle by naming the column appropriately.

```python
# Impute the missing value with the median
test.Fare[152] = test.Fare.median()

# Extract the features from the test set: Pclass, Sex, Age, and Fare.
test_features = test[["Pclass","Sex","Age","Fare"]].values

# Make your prediction using the test set
my_prediction = my_tree_one.predict(test_features)
print(my_prediction)

# Create a data frame with two columns: PassengerId & Survived. Survived contains your predictions
PassengerId =np.array(test["PassengerId"]).astype(int)
my_solution = pd.DataFrame(my_prediction, PassengerId, columns = ["Survived"])
print(my_solution)

# Check that your data frame has 418 entries
print(my_solution.shape)

# Write your solution to a csv file with the name my_solution.csv
my_solution.to_csv("my_solution_one.csv", index_label = ["PassengerId"])
```

### Results :  

	<script.py> output:
		[0 1 1 0 1 0 0 1 1 0 0 0 0 1 0 1 1 1 0 1 0 0 0 0 0 0 0 1 0 1 1 1 1 0 0 1 0
		 0 0 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0
		 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 1 1
		 0 0 1 0 0 0 1 0 1 1 0 0 1 0 1 0 1 1 0 0 0 0 0 0 0 1 1 0 0 0 0 0 1 0 0 0 0
		 0 1 0 0 0 1 1 0 0 0 0 1 0 0 1 1 1 1 0 0 0 0 0 1 1 1 1 1 1 0 1 0 1 0 0 0 0
		 1 1 0 0 1 1 0 0 1 1 0 0 0 1 0 1 1 0 1 1 0 0 1 0 0 1 1 1 1 0 0 0 0 0 0 1 0
		 1 0 0 0 0 0 0 1 1 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 1 1 1 0 1 0 0 0 0 0 0 0 1
		 0 1 0 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 0 1 0 0 1 1 1 0 1 0 0 0 1 0 0 0
		 1 1 0 0 0 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 1 0 1 1 0 0 1 1 0 1 1 1 0 1
		 1 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 0 1 1 1 1 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1
		 1 0 0 1 0 0 0 1 0 1 0 0 0 1 1 1 0 1 0 0 0 0 1 1 1 0 1 0 0 0 0 1 0 0 0 1 1
		 0 0 1 0 0 0 0 0 1 0 1]
			  Survived
		892          0
		893          1
		894          1
		895          0
		896          1
		897          0
		898          0
		899          1
		900          1
		901          0
		902          0
		903          0
		904          0
		905          1
		906          0
		907          1
		908          1
		909          1
		910          0
		911          1
		912          0
		913          0
		914          0
		915          0
		916          0
		917          0
		918          0
		919          1
		920          0
		921          1
		...        ...
		1280         0
		1281         0
		1282         0
		1283         0
		1284         1
		1285         1
		1286         1
		1287         0
		1288         1
		1289         0
		1290         0
		1291         0
		1292         0
		1293         1
		1294         0
		1295         0
		1296         0
		1297         1
		1298         1
		1299         0
		1300         0
		1301         1
		1302         0
		1303         0
		1304         0
		1305         0
		1306         0
		1307         1
		1308         0
		1309         1
		
		[418 rows x 1 columns]
		(418, 1)

	<script.py> output:
		[0 0 1 1 1 0 0 0 1 0 0 0 1 1 1 1 0 1 1 0 0 1 1 1 1 0 1 1 1 0 0 0 1 0 1 0 0
		 0 0 1 0 1 0 1 1 0 0 0 1 1 1 0 1 1 1 0 0 0 1 1 0 0 0 1 0 0 1 0 0 1 1 0 1 0
		 1 0 0 1 0 1 1 0 0 0 0 0 1 1 1 1 1 1 1 0 0 0 1 1 1 0 1 0 0 0 1 0 0 0 0 0 0
		 0 1 1 1 0 1 1 0 1 1 0 1 0 0 1 0 1 0 0 1 0 0 1 0 0 1 0 0 0 0 0 0 0 0 1 1 0
		 1 0 1 0 0 1 0 0 1 1 0 1 1 1 1 1 0 1 1 0 0 0 0 1 0 1 0 1 1 0 1 1 0 0 1 0 1
		 0 1 0 0 0 0 0 1 0 1 0 1 0 0 0 0 1 0 1 0 0 0 0 1 0 1 1 0 1 0 0 1 0 1 0 1 0
		 1 1 1 0 0 1 0 0 0 1 0 0 1 0 0 1 1 1 1 1 1 0 0 0 1 0 1 0 1 0 0 0 0 0 0 0 1
		 0 0 0 1 1 0 0 0 0 0 0 0 0 1 0 1 1 0 0 0 0 0 1 1 0 1 0 0 0 1 0 1 0 1 0 0 0
		 1 0 0 0 0 0 0 0 1 1 0 1 1 0 0 1 0 0 1 1 0 0 0 0 0 0 0 1 1 0 1 0 0 0 1 0 1
		 1 0 0 0 0 0 1 0 0 0 1 0 1 0 0 0 1 1 0 0 0 1 0 1 0 0 1 0 1 1 1 1 0 0 0 1 0
		 0 1 0 0 1 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 1 1 0 0 1 0 1 0 0 1 0 1 1 0 0 0
		 0 1 1 1 1 0 0 1 0 0 0]
			  Survived
		892          0
		893          0
		894          1
		895          1
		896          1
		897          0
		898          0
		899          0
		900          1
		901          0
		902          0
		903          0
		904          1
		905          1
		906          1
		907          1
		908          0
		909          1
		910          1
		911          0
		912          0
		913          1
		914          1
		915          1
		916          1
		917          0
		918          1
		919          1
		920          1
		921          0
		...        ...
		1280         0
		1281         0
		1282         0
		1283         1
		1284         1
		1285         0
		1286         0
		1287         1
		1288         0
		1289         1
		1290         0
		1291         0
		1292         1
		1293         0
		1294         1
		1295         1
		1296         0
		1297         0
		1298         0
		1299         0
		1300         1
		1301         1
		1302         1
		1303         1
		1304         0
		1305         0
		1306         1
		1307         0
		1308         0
		1309         0
		
		[418 rows x 1 columns]
		(418, 1)		

Great! You just created your first decision tree. Download your csv file, and submit the created csv to Kaggle to see the result of your effort.  
		
---


## Overfitting and how to control it    

When you created your first decision tree the default arguments for max_depth and min_samples_split were set to None. This means that no limit on the depth of your tree was set. That's a good thing right? Not so fast. We are likely overfitting. This means that while your model describes the training data extremely well, it doesn't generalize to new data, which is frankly the point of prediction. Just look at the Kaggle submission results for the simple model based on Gender and the complex decision tree. Which one does better?  

Maybe we can improve the overfit model by making a less complex model? In DecisionTreeRegressor, the depth of our model is defined by two parameters: - the max_depth parameter determines when the splitting up of the decision tree stops. - the min_samples_split parameter monitors the amount of observations in a bucket. If a certain threshold is not reached (e.g minimum 10 passengers) no further splitting can be done.  

By limiting the complexity of your decision tree you will increase its generality and thus its usefulness for prediction!    

### Instructions  

 - Include the Siblings/Spouses Aboard, Parents/Children Aboard, and Embarked features in a new set of features.
 - Fit your second tree my_tree_two with the new features, and control for the model compelexity by toggling the max_depth and min_samples_split arguments.

```python
# Create a new array with the added features: features_two
features_two = train[["Pclass","Age","Sex","Fare", 'SibSp', 'Parch', 'Embarked']].values

#Control overfitting by setting "max_depth" to 10 and "min_samples_split" to 5 : my_tree_two
max_depth = 10
min_samples_split = 5
my_tree_two = tree.DecisionTreeClassifier(max_depth = max_depth, min_samples_split = min_samples_split, random_state = 1)
my_tree_two = my_tree_two.fit(features_two,target)

#Print the score of the new decison tree
print(my_tree_two.score(features_two, target))
```

### Results :  

	<script.py> output:
		0.905723905724		

Great! You just created your second and possibly improved decision tree. Download your csv file .Submit your updated solution to Kaggle to see how despite a lower .score you predict better.  
		
---


## Feature-engineering for our Titanic data set   

Data Science is an art that benefits from a human element. Enter feature engineering: creatively engineering your own features by combining the different existing variables.  

While feature engineering is a discipline in itself, too broad to be covered here in detail, you will have a look at a simple example by creating your own new predictive attribute: family_size.  

A valid assumption is that larger families need more time to get together on a sinking ship, and hence have lower probability of surviving. Family size is determined by the variables SibSp and Parch, which indicate the number of family members a certain passenger is traveling with. So when doing feature engineering, you add a new variable family_size, which is the sum of SibSp and Parch plus one (the observation itself), to the test and train set.  

### Instructions  

 - Create a new train set train_two that differs from train only by having an extra column with your feature engineered variable family_size.
 - Add your feature engineered variable family_size in addition to Pclass, Sex, Age, Fare, SibSp and Parch to features_three.
 - Create a new decision tree as my_tree_three and fit the decision tree with your new feature set features_three. Then check out the score of the decision tree.

```python
# Create train_two with the newly defined feature
train_two = train.copy()
train_two["family_size"] = train_two["SibSp"] + train_two["Parch"] +1

# Create a new feature set and add the new feature
features_three = train_two[["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch", "family_size"]].values

# Define the tree classifier, then fit the model
my_tree_three = tree.DecisionTreeClassifier()
my_tree_three = my_tree_three.fit(features_three,target)

# Print the score of this decision tree
print(my_tree_three.score(features_three, target))

```

### Results :  

	<script.py> output:
		0.979797979798

Great! Notice that this time the newly created variable is included in the model. Download your csv file, and submit the created csv to Kaggle to see the result of the updated model.  
(solution three)

		
---