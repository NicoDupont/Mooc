03/2017  
Dataquest : Data Analyst Path  
Step 5: Probability and Statistics  
SubStep : Probability and Statistics in Python: Intermediate : Multi category chi-squared tests    
mercredi, 22. mars 2017 07:22 


---
# 1: Multiple Categories  

In the last mission, we looked at the gender frequencies of people included in a data set on US income. The dataset consists of 32561 rows, and here are the first few:  


	age,workclass,fnlwgt,education,education_num,marital_status,occupation,relationship,race,sex,capital_gain,capital_loss,hours_per_week,native_country,high_income
	39, State-gov, 77516, Bachelors, 13, Never-married, Adm-clerical, Not-in-family, White, Male, 2174, 0, 40, United-States, <=50K
	50, Self-emp-not-inc, 83311, Bachelors, 13, Married-civ-spouse, Exec-managerial, Husband, White, Male, 0, 0, 13, United-States, <=50K
	38, Private, 215646, HS-grad, 9, Divorced, Handlers-cleaners, Not-in-family, White, Male, 0, 0, 40, United-States, <=50K

Each row represents a single person who was counted in the 1990 US Census, and contains information about their income and demograpics. Here are some of the relevant columns:  

- age -- how old the person is
- workclass -- the type of sector the person is employed in.
- race -- the race of the person.
- sex -- the gender of the person, either Male or Female.
- high_income -- if the person makes more the 50k or not.

In the last mission, we calculated a chi-squared value indicating how the observed frequencies in a single categorical column, such as sex, varied from the US population as a whole.  

In this mission, we'll look how to make this same technique applicable to cross tables, that show how two categorical columns interact. For instance, here's a table showing the relationship between sex and high_income:  

see img/img36.png

On looking at this diagram, you might see a pattern between sex and high_income. But it's hard to immediately quantify that pattern, and tell if it's significant. We can apply the chi-squared test (also known as the chi-squared test of association) to figure out if there's a statistically significant correlation between two categorical columns.  

---
# 2: Calculating Expected Values  

In the single category chi-squared test, we find expected values from other data sets, and then compare with our own observed values. In a multiple category chi-squared test, we calculate expected values across our whole dataset. We'll illustrate this by converting our chart from last screen into proportions:  

see img/img37.png

Each cell represents the proportion of people in the data set that fall into the specified categories.

- 20.5% of Males in the whole data set earn >50k in income.
- 33.1% of the whole dataset is Female
- 75.9% of the whole dataset earns <=50k.

We can use our total proportions to calculate expected values. 24.1% of all people in income earn >50k, and 33.1% of all people in income are Female, so we'd expect the proportion of people who are female and earn >50k to be .241 * .331, which is .0799771. We have this expectation based on the proportions of Females and >50k earners across the whole dataset. Instead, we see that the observed proportion is .036, which indicates that there may be some correlation between the sex and high_income columns.  

We can convert our expected proportion to an expected value by multiplying by 32561, the total number of rows in the data set, which gives us 32561 * .0799771, or 2597.4.  


#### Instructions :

Using the expected proportions in the table above, calculate the expected values for each of the 4 cells in the table.
- Calculate the expected value for Males who earn >50k, and assign to males_over50k.
- Calculate the expected value for Males who earn <=50k, and assign to males_under50k.
- Calculate the expected value for Females who earn >50k, and assign to females_over50k.
- Calculate the expected value for Females who earn <=50k, and assign to females_under50k.
 
```python
males_over50k = .669 * .241 * 32561
males_under50k = .669 * .759 * 32561
females_over50k = .331 * .241 * 32561
females_under50k = .331 * .759 * 32561
```  

#### Results :  


	Variables
	 males_under50kfloat (<class 'float'>)
	16533.531531000004
	 males_over50kfloat (<class 'float'>)
	5249.777469000001
	 females_under50kfloat (<class 'float'>)
	8180.267469000001
	 females_over50kfloat (<class 'float'>)
	2597.423531

---
# 3: Calculating Chi-Squared  

In the last screen, you should have ended up with a table like this:   

see img/img38.png

Now that we have our expected values, we can calculate the chi-squared value by using the same principle from the previous mission. Here are the steps:  

- Subtract the expected value from the observed value.
- Square the difference.
- Divide the squared difference by the expected value.
- Repeat for all the observed and expected values and add up the values.

Here's the formula:  

see img/img39.png
∑(observed−expected)2expected∑(observed−expected)2expected  

Here's the table of our observed values for reference:  

see img/img40.png

#### Instructions :

 - Compute the chi-squared value for the observed values above and the expected values above.
	- Assign the result to chisq_gender_income.
 
```python
observed = [6662, 1179, 15128, 9592]
expected = [5249.8, 2597.4, 16533.5, 8180.3]
values = []

for i, obs in enumerate(observed):
    exp = expected[i]
    value = (obs - exp) ** 2 / exp
    values.append(value)

chisq_gender_income = sum(values)
```  

#### Results :  

	chisq_gender_incomefloat (<class 'float'>)
	1517.5510981525103


---
# 4: Finding Statistical Significance  

Now that we've found our chi-squared value, 1517.6, we can use the same technique with the chi-squared sampling distribution from the last mission to find a p-value associated with the chi-squared value. The p-value will tell us whether the difference between the observed and expected values is statistically significant or not.  

Rather than construct a sampling distribution again manually, we'll use the scipy.stats.chisquare function that we covered in the last mission.  

If we had a table of expected values that looked like this:  

see img/img41.png

And a table of observed values that looked like this:  

see img/img42.png

We could find the chi-squared value and the p-value using the scipy.stats.chisquare function like this:

```python
import numpy as np
from scipy.stats import chisquare
​
observed = np.array([10, 10, 5, 5])
expected = np.array([5, 5, 10, 10])
chisquare_value, pvalue = chisquare(observed, expected)
```

#### Instructions :

Here are our expected values from the last screen:  

see img/img43.png  

And here are our observed values:  

see img/img44.png   

 - Use the scipy.stats.chisquare function to find the chi-squared value and p-value for the above observed and expected counts.
	- Assign the p-value to pvalue_gender_income.
 
```python
import numpy as np
from scipy.stats import chisquare

observed = np.array([6662, 1179, 15128, 9592])
expected = np.array([5249.8, 2597.4, 16533.5, 8180.3])

chisq_value, pvalue_gender_income = chisquare(observed, expected)
```  

#### Results :  

	 pvalue_gender_incomefloat64 (<class 'numpy.float64'>)
	0.0
	 chisq_valuefloat64 (<class 'numpy.float64'>)
	1517.5510981525103


---
# 5: Cross Tables  

We can also scale up the chi-squared test to cases where each category contains more than two possibilities. We'll illustrate this with an example where we look at sex vs race.  

Before we can find the chi-squared value, we need to find the observed frequency counts. We can do this using the pandas.crosstab function. The crosstab function will print a table that shows frequency counts for two or more columns. Here's how you could use the pandas.crosstab function:  

```python
import pandas
​
table = pandas.crosstab(income["sex"], [income["high_income"]])
print(table)
```

The above code will print a table showing how many people from income fall into each category of sex and high_income.  

The second parameter passed into pandas.crosstab is actually a list -- this parameter can contain more than one item.  


#### Instructions :

Use the pandas.crosstab function to print out a table comparing the sex column of income to the race column of income.  
 
```python
import pandas
table = pandas.crosstab(income["sex"], [income["race"]])
print(table)
```  

#### Results :  

	Output
	race      Amer-Indian-Eskimo   Asian-Pac-Islander   Black   Other   White
	sex                                                                      
	 Female                  119                  346    1555     109    8642
	 Male                    192                  693    1569     162   19174

---
# 6: Finding Expected Values  

Now that we have the observed frequency counts, we can generate the expected values. We can use the scipy.stats.chi2_contingency function to do this. The function takes in a cross table of observed counts, and returns the chi-squared value, the p-value, the degrees of freedom, and the expected frequencies. Let's say we have the following observed counts:  

see img/img45.png  

Here's how we could use the scipy.stats.chi2_contingency function:  

```python
import numpy as np
from scipy.stats import chi2_contingency
observed = np.array([5, 5], [10, 10])
​
chisq_value, pvalue, df, expected = chi2_contingency(observed)
```

You can also directly pass the result of the pandas.crosstab function into the scipy.stats.chi2_contingency function, which makes it extremely easy to do perform a chi-squared test.  


#### Instructions :

 - Use the scipy.stats.chi2_contingency function to calculate the pvalue for the sex and race columns of income.
	- Assign the result to pvalue_gender_race.
 
```python
import pandas
from scipy.stats import chi2_contingency

table = pandas.crosstab(income["sex"], [income["race"]])
chisq_value, pvalue_gender_race, df, expected = chi2_contingency(table)
```  

#### Results :  

	pvalue_gender_racefloat64 (<class 'numpy.float64'>)
	5.1920613027604561e-97
	 chisq_valuefloat64 (<class 'numpy.float64'>)
	454.26710891310881


---
# 7: Caveats  

Now that we've learned the chi-squared test, you should be able to figure out if the association between two columns of categorical data is statistically significant or not. There are a few caveats to using the chi-squared test that are important to cover, though:

 - Finding that a result isn't significant doesn't mean that no association between the columns exists. For instance, if we found that the chi-squared test between the sex and race columns returned a p-value of .1, it wouldn't mean that there is no relationship between sex and race. It just means that there isn't a statistically significant relationship.
 - Finding a statistically significant result doesn't imply anything about what the correlation is. For instance, finding that a chi-squared test between sex and race results in a p-value of .01 doesn't mean that the dataset contains too many Females who are White (or too few). A statistically significant finding means that some evidence of a relationship between the variables exists, but needs to be investigated further.
 - Chi-squared tests can only be applied in the case where each possibility within a category is independent. For instance, the Census counts individuals as either Male or Female, not both.
 - Chi-squared tests are more valid when the numbers in each cell of the cross table are larger. So if each number is 100, great -- if each number is 1, you may need to gather more data. 

---
# 8: Next Steps  

In this mission, we covered chi-squared tests for multiple categories, and learned how to quickly perform chi-squared tests. We learned when to apply and when not to apply chi-squared tests. Chi-squared tests can be a powerful tool to discover correlations and figure out when anomalies in your data should be investigated further.  