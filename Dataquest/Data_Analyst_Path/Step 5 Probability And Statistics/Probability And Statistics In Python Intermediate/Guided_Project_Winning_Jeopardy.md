03/2017  
Dataquest : Data Analyst Path  
Step 5: Probability and Statistics  
SubStep : Probability and Statistics in Python: Intermediate : Guided Project: Winning Jeopardy    
dimanche, 26. mars 2017 01:01 

---
# 1: Jeopardy Questions  

Jeopardy is a popular TV show in the US where participants answer questions to win money. It's been running for a few decades, and is a major force in popular culture. If you need help at any point, you can consult our solution notebook here.  

Let's say you want to compete on Jeopardy, and you're looking for any edge you can get to win. In this project, you'll work with a dataset of Jeopardy questions to figure out some patterns in the questions that could help you win.  

The dataset is named jeopardy.csv, and contains 20000 rows from the beginning of a full dataset of Jeopardy questions, which you can download here. Here's the beginning of the file:  

![](https://dq-content.s3.amazonaws.com/Nlfu13A.png) 

As you can see, each row in the dataset represents a single question on a single episode of Jeopardy. Here are explanations of each column:

- Show Number -- the Jeopardy episode number of the show this question was in.
- Air Date -- the date the episode aired.
- Round -- the round of Jeopardy that the question was asked in. Jeopardy has several rounds as each episode progresses.
- Category -- the category of the question.
- Value -- the number of dollars answering the question correctly is worth.
- Question -- the text of the question.
- Answer -- the text of the answer.

#### Instructions :

- Read the dataset into a Dataframe called jeopardy using Pandas.
- Print out the first 5 rows of jeopardy.
- Print out the columns of jeopardy using jeopardy.columns.
- Some of the column names have spaces in front.
- Remove the spaces in each item in jeopardy.columns.
- Assign the result back to jeopardy.columns to fix the column names in jeopardy.
- Make sure you pay close attention to the format of each column.
 
```python
#1: Jeopardy Questions
import pandas as pd
jeopardy = pd.read_csv("jeopardy.csv")
jeopardy.head()
jeopardy.columns
jeopardy.columns = ['Show Number', 'Air Date', 'Round', 'Category', 'Value', 'Question', 'Answer']
```  

#### Results :  


---
# 2: Normalizing Text

Before you can start doing analysis on the Jeopardy questions, you need to normalize all of the text columns (the Question and Answer columns). We covered normalization before, but the idea is to ensure that you lowercase words and remove punctuation so Don't and don't aren't considered to be different words when you compare them.   


#### Instructions :

- Write a function to normalize questions and answers. It should:
	- Take in a string.
	- Convert the string to lowercase.
	- Remove all punctuation in the string.
	- Return the string.
- Normalize the Question column.
	- Use the Pandas apply method to apply the function to each item in the Question column.
	- Assign the result to the clean_question column.
- Normalize the Answer column.
	- Use the Pandas apply method to apply the function to each item in the Answer column.
	- Assign the result to the clean_answer column.

```python
#2: Normalizing Text
import re

def normalize_text(text):
    text = text.lower()
    text = re.sub("[^A-Za-z0-9\s]", "", text)
    return text

def normalize_values(text):
    text = re.sub("[^A-Za-z0-9\s]", "", text)
    try:
        text = int(text)
    except Exception:
        text = 0
    return text
jeopardy["clean_question"] = jeopardy["Question"].apply(normalize_text)
jeopardy["clean_answer"] = jeopardy["Answer"].apply(normalize_text)
jeopardy.head()
```  


---
# 3: Normalizing Columns  

Now that you've normalized the text columns, there are also some other columns to normalize.  

The Value column should also be numeric, to allow you to manipulate it more easily. You'll need to remove the dollar sign from the beginning of each value and convert the column from text to numeric.  

The Air Date column should also be a datetime, not a string, to enable you to work with it more easily.   


#### Instructions :

- Write a function to normalize dollar values. It should:
	- Take in a string.
	- Remove any punctuation in the string.
	- Convert the string to an integer.
	- If the conversion has an error, assign 0 instead.
	- Return the integer.
- Normalize the Value column.
	- Use the Pandas apply method to apply the function to each item in the Value column.
	- Assign the result to the clean_value column.
- Use the pandas.to_datetime function to convert the Air Date column to a datetime column.
 
```python
#3: Normalizing Columns
jeopardy["clean_value"] = jeopardy["Value"].apply(normalize_values)
jeopardy["Air Date"] = pd.to_datetime(jeopardy["Air Date"])
jeopardy.dtypes
jeopardy.head()
```  



---
# 4: Answers In Questions  

In order to figure out whether to study past questions, study general knowledge, or not study it all, it would be helpful to figure out two things:  

- How often the answer is deducible from the question.  
- How often new questions are repeats of older questions.  

You can answer the second question by seeing how often complex words (> 6 characters) reoccur. You can answer the first question by seeing how many times words in the answer also occur in the question. We'll work on the first question now, and come back to the second.   


#### Instructions :

- Write a function that takes in a row in jeopardy, as a Series. It should:
	- Split the clean_answer column on the space character (), and assign to the variable split_answer.
		- Split the clean_question column on the space character (), and assign to the variable split_question.
	- Create a variable called match_count, and set it to 0.
	- If the is in split_answer, remove it using the remove method on lists. The is commonly found in answers and questions, but doesn't have any meaningful use in finding the answer.
	- If the length of split_answer is 0, return 0. This prevents a division by zero error later.
	- Loop through each item in split_answer, and see if it occurs in split_question. If it does, add 1 to match_count.
	- Divide match_count by the length of split_answer, and return the result.
- Count how many times terms in clean_answer occur in clean_question.
	- Use the Pandas apply method on Dataframes to apply the function to each row in jeopardy.
	- Pass the axis=1 argument to apply the function across each row.
	- Assign the result to the answer_in_question column.
- Find the mean of the answer_in_question column using the mean method on Series.
- Write up a markdown cell with a short explanation of how finding this mean might influence your studying strategy for Jeopardy.
 
```python
#4: Answers In Questions
def count_matches(row):
    split_answer = row["clean_answer"].split(" ")
    split_question = row["clean_question"].split(" ")
    if "the" in split_answer:
        split_answer.remove("the")
    if len(split_answer) == 0:
        return 0
    match_count = 0
    for item in split_answer:
        if item in split_question:
            match_count += 1
    return match_count / len(split_answer)

jeopardy["answer_in_question"] = jeopardy.apply(count_matches, axis=1)
jeopardy["answer_in_question"].mean()
```  

#### Results :  

	0.060493257069335872

---
# 5: Recycled Questions  

Let's say you want to investigate how often new questions are repeats of older ones. You can't completely answer this, because you only have about 10% of the full Jeopardy question dataset, but you can investigate it at least.  

To do this, you can:  

- Sort jeopardy in order of ascending air date.
- Maintain a set called terms_used that will be empty initially.
- Iterate through each row of jeopardy.
- Split clean_question into words, remove any word shorter than 6 characters, and check if each word occurs in terms_used.
	- If it does, increment a counter.
	- Add each word to terms_used.

This will enable you to check if the terms in questions have been used previously or not. Only looking at words greater than 6 characters enables you to filter out words like the and than, which are commonly used, but don't tell you a lot about a question.  


#### Instructions :

- Create an empty list called question_overlap.
- Create an empty set called terms_used.
- Use the iterrows Dataframe method to loop through each row of jeopardy.
	- Split the clean_question column of the row on the space character (), and assign to split_question.
	- Remove any words in split_question that are less than 6 characters long.
	- Set match_count to 0.
	- Loop through each word in split_question.
		- If the term occurs in terms_used, add 1 to match_count.
	- Add each word in split_question to terms_used using the add method on sets.
	- If the length of split_question is greater than 0, divide match_count by the length of split_question.
	- Append match_count to question_overlap.
- Assign question_overlap to the question_overlap column of jeopardy.
- Find the mean of the question_overlap column and print it.
- Look at the value, and think about what this might mean for questions being recycled. Write up your thoughts in a markdown cell.
 
```python
#5: Recycled Questions

question_overlap = []
terms_used = set()
for i, row in jeopardy.iterrows():
        split_question = row["clean_question"].split(" ")
        split_question = [q for q in split_question if len(q) > 5]
        match_count = 0
        for word in split_question:
            if word in terms_used:
                match_count += 1
        for word in split_question:
            terms_used.add(word)
        if len(split_question) > 0:
            match_count /= len(split_question)
        question_overlap.append(match_count)
jeopardy["question_overlap"] = question_overlap
jeopardy["question_overlap"].mean()
```  

#### Results :  

	0.69087373156719623

---
# 6: Low Value Vs High Value Questions  

Let's say you only want to study questions that pertain to high value questions instead of low value questions. This will help you earn more money when you're on Jeopardy.  

You can actually figure out which terms correspond to high-value questions using a chi-squared test. You'll first need to narrow down the questions into two categories:  

- Low value -- Any row where Value is less than 800.
- High value -- Any row where Value is greater than 800.

You'll then be able to loop through each of the terms from the last screen, terms_used, and:  

- Find the number of low value questions the word occurs in.
- Find the number of high value questions the word occurs in.
- Find the percentage of questions the word occurs in.
- Based on the percentage of questions the word occurs in, find expected counts.
- Compute the chi squared value based on the expected counts and the observed counts for high and low value questions.

You can then find the words with the biggest differences in usage between high and low value questions, by selecting the words with the highest associated chi-squared values. Doing this for all of the words would take a very long time, so we'll just do it for a small sample now.   


#### Instructions :

- Create a function that takes in a row from a Dataframe, and:
	- If the clean_value column is greater than 800, assign 1 to value.
	- Otherwise, assign 0 to value.
	- Return value.
- Determine which questions are high and low value.
	- Use the Pandas apply method on Dataframes to apply the function to each row in jeopardy.
	- Pass the axis=1 argument to apply the function across each row.
	- Assign the result to the high_value column.
- Create a function that takes in a word, and:
	- Assigns 0 to low_count.
	- Assigns 0 to high_count.
	- Loops through each row in jeopardy using the iterrows method.
		- Split the clean_question column on the space character ().
		- If the word is in the split question:
			- If the high_value column is 1, add 1 to high_count.
			- Else, add 1 to low_count.
	- Returns high_count and low_count. You can return multiple values by separating them with a comma.
- Create an empty list called observed_expected.
- Convert terms_used into a list using the list function, and assign the first 5 elements to comparison_terms.
- Loop through each term in comparison_terms, and:
	- Run the function on the term to get the high value and low value counts.
	- Append the result of running the function (which will be a list) to observed_expected.
 
```python
#6: Low Value Vs High Value Questions
def determine_value(row):
    value = 0
    if row["clean_value"] > 800:
        value = 1
    return value

jeopardy["high_value"] = jeopardy.apply(determine_value, axis=1)
def count_usage(term):
    low_count = 0
    high_count = 0
    for i, row in jeopardy.iterrows():
        if term in row["clean_question"].split(" "):
            if row["high_value"] == 1:
                high_count += 1
            else:
                low_count += 1
    return high_count, low_count

comparison_terms = list(terms_used)[:5]
observed_expected = []
for term in comparison_terms:
    observed_expected.append(count_usage(term))

observed_expected
```  

#### Results :  

	[(4, 5), (0, 1), (3, 5), (2, 0), (6, 15)]

---
# 7: Applying The Chi-Squared Test  

Now that you've found the observed counts for a few terms, you can compute the expected counts and the chi-squared value.  


#### Instructions :

- Find the number of rows in jeopardy where high_value is 1, and assign to high_value_count.
- Find the number of rows in jeopardy where high_value is 0, and assign to low_value_count.
- Create an empty list called chi_squared.
- Loop through each list in observed_expected.
	- Add up both items in the list (high and low counts) to get the total count, and assign to total.
	- Divide total by the number of rows in jeopardy to get the proportion across the dataset. Assign to total_prop.
	- Multiply total_prop by high_value_count to get the expected term count for high value rows.
	- Multiply total_prop by low_value_count to get the expected term count for low value rows.
	- Use the scipy.stats.chisquare function to compute the chi-squared value and p-value given the expected and observed counts.
	- Append the results to chi_squared.
- Look over the chi-squared values and the associated p-values. Are there any statistically significant results? Write up your thoughts in a markdown cell.
 
```python

from scipy.stats import chisquare
import numpy as np

high_value_count = jeopardy[jeopardy["high_value"] == 1].shape[0]
low_value_count = jeopardy[jeopardy["high_value"] == 0].shape[0]

chi_squared = []
for obs in observed_expected:
    total = sum(obs)
    total_prop = total / jeopardy.shape[0]
    high_value_exp = total_prop * high_value_count
    low_value_exp = total_prop * low_value_count
    
    observed = np.array([obs[0], obs[1]])
    expected = np.array([high_value_exp, low_value_exp])
    chi_squared.append(chisquare(observed, expected))

chi_squared
```  

	not good actually (26/03/2017) ?

---
# 8: Next Steps  

That's it for the guided steps! We recommend exploring the data more on your own.  

Here are some potential next steps:  

- Find a better way to eliminate non-informative words than just removing words that are less than 6 characters long. Some ideas:
	- Manually create a list of words to remove, like the, than, etc.
	- Find a list of stopwords to remove.
	- Remove words that occur in more than a certain percentage (like 5%) of questions.
- Perform the chi-squared test across more terms to see what terms have larger differences. This is hard to do currently because the code is slow, but here are some ideas:
	- Use the apply method to make the code that calculates frequencies more efficient.
	- Only select terms that have high frequencies across the dataset, and ignore the others.
- Look more into the Category column and see if any interesting analysis can be done with it. Some ideas:
	- See which categories appear the most often.
	- Find the probability of each category appearing in each round.
- Use the whole Jeopardy dataset (available here) instead of the subset we used in this mission.
- Use phrases instead of single words when seeing if there's overlap between questions. Single words don't capture the whole context of the question well.

We recommend creating a Github repository and placing this project there. It will help other people, including employers, see your work. As you start to put multiple projects on Github, you'll have the beginnings of a strong portfolio.  

You're welcome to keep working on the project here, but we recommend downloading it to your computer using the download icon above and working on it there.  

We hope this guided project has been a good experience, and please email us at hello@dataquest.io if you want to share your work!   
