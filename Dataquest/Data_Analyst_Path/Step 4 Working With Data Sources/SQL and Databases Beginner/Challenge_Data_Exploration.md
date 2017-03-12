03/2017  
Dataquest : Data Analyst Path  
Step 4: Working With Data Sources  
SubStep :  SQL and Databases: Beginner : Challenge: Data Exploration  
samedi, 11. mars 2017 03:14 


---
# 1: Introduction  

In this challenge, you'll practice calculating summary statistics in SQL while exploring data from factbook.db. Recall that factbook.db contains information about each country in the world. You'll work with the facts table, where each row represents a single country. Here's the descriptions of some of the columns:  

- name -- the name of the country.
- area -- the total land and sea area of the country.
- population -- the population of the country.
- birth_rate -- the birth rate of the country.
- created_at -- the date the record was created.
- updated_at -- the date the record was updated.

Here are the first few rows of facts:  

see img/img6.png

In this challenge, you'll focus on the population values for each country and predicting the next year's population using the data. First, you'll need to explore the data and look for any data quality issues.  

#### Instructions :

 - Calculate the means in SQL for the population, population_growth, birth_rate, and death_rate columns.
 - Assign the mean of the population column to pop_avg.
 - Assign the mean of the population_growth column to pop_growth_avg.
 - Assign the mean of the birth_rate column to birth_rate_avg.
 - Assign the mean of the death_rate column to death_rate_avg.
 

```python
 import sqlite3
conn = sqlite3.connect("factbook.db")
res_tuple = conn.execute("SELECT avg(population),avg(population_growth),avg(birth_rate),avg(death_rate) FROM facts;").fetchall()
pop_avg = res_tuple[0][0]
print(pop_avg)
print("---------")
pop_growth_avg = res_tuple[0][1]
print(pop_growth_avg)
print("---------")
birth_rate_avg = res_tuple[0][2]
print(birth_rate_avg)
print("---------")
death_rate_avg = res_tuple[0][3]
print(death_rate_avg)
print("---------")
```  

#### Results :  


	Output
	62094928.32231405
	---------
	1.2009745762711865
	---------
	19.32855263157894
	---------
	7.8212719298245625
	---------


---
# 2: Ranges  

While the averages give you some sense of the values in these columns, let's calculate the ranges as well to better understand the lower and upper bounds for these columns. This way, you can also look for the presence of any outliers.   

#### Instructions :

Calculate the minimum and maximum values for the columns from the previous screen:  

- Assign the minimum of the population column to pop_min.
- Assign the maximum of the population column to pop_max.
- Assign the minimum of the population_growth column to pop_growth_min.
- Assign the maximum of the population_growth column to pop_growth_max.
- Assign the minimum of the birth_rate column to birth_rate_min.
- Assign the maximum of the birth_rate column to birth_rate_max.
- Assign the minimum of the death_rate column to death_rate_min.
- Assign the maximum of the death_rate column to death_rate_max.

Use print statements or the variables display below the output box to o
bserve these values.  
 
```python
 conn = sqlite3.connect("factbook.db")

averages = "select avg(population), avg(population_growth), avg(birth_rate), avg(death_rate), avg(migration_rate) from facts;"
avg_results = conn.execute(averages).fetchall()
pop_avg = avg_results[0][0]
pop_growth_avg = avg_results[0][1]
birth_rate_avg = avg_results[0][2]
death_rate_avg = avg_results[0][3]
mig_rate_avg = avg_results[0][4]

ranges = "select min(population),max(population), min(population_growth),max(population_growth), min(birth_rate),max(birth_rate), min(death_rate), max(death_rate) from facts;"
ranges_results = conn.execute(ranges).fetchall()

pop_min = ranges_results[0][0]
pop_max = ranges_results[0][1]
pop_growth_min = ranges_results[0][2]
pop_growth_max = ranges_results[0][3]
birth_rate_min = ranges_results[0][4]
birth_rate_max = ranges_results[0][5]
death_rate_min = ranges_results[0][6]
death_rate_max = ranges_results[0][7]

print(pop_min)
print(pop_max)
print(pop_growth_min)
print(pop_growth_max)
print(birth_rate_min)
print(birth_rate_max)
print(death_rate_min)
print(death_rate_max)
```  

#### Results : 

	Output
	0
	7256490011
	0.0
	4.02
	6.65
	45.45
	1.53
	14.89

---
# 3: Filtering  

If you observed the values in the previous screen, you may have noticed the outlier values. The max value for population is 7,256,490,011 while the minimum is 0. We know that China, the most populated country in the world, doesn't even have 2 billion people but the max value for the population column is over 7 billion. The minimum value for the population column is also problematic, since no country has 0 people.  

These quirks exist because the database contains rows for entities that aren't countries. For example, there's a row representing the entire world (hence the 7 billion population) and some rows representing oceanic areas (hence the population of 0).  

#### Instructions :

Write a single query that returns the following minimum and maximum values for countries where population is less than 2 billion and population is greater than 0:  

- Assign the minimum of the population column to pop_min.
- Assign the maximum of the population column to pop_max.
- Assign the minimum of the population_growth column to pop_growth_min.
- Assign the maximum of the population_growth column to pop_growth_max.
- Assign the minimum of the birth_rate column to birth_rate_min.
- Assign the maximum of the birth_rate column to birth_rate_max.
- Assign the minimum of the death_rate column to death_rate_min.
- Assign the maximum of the death_rate column to death_rate_max.
 
```python
 conn = sqlite3.connect("factbook.db")

ranges = "select min(population),max(population), min(population_growth),max(population_growth), min(birth_rate),max(birth_rate), min(death_rate), max(death_rate) from facts where population < 2000000000 and population > 0;"
ranges_results = conn.execute(ranges).fetchall()

pop_min = ranges_results[0][0]
pop_max = ranges_results[0][1]
pop_growth_min = ranges_results[0][2]
pop_growth_max = ranges_results[0][3]
birth_rate_min = ranges_results[0][4]
birth_rate_max = ranges_results[0][5]
death_rate_min = ranges_results[0][6]
death_rate_max = ranges_results[0][7]

print(pop_min)
print(pop_max)
print(pop_growth_min)
print(pop_growth_max)
print(birth_rate_min)
print(birth_rate_max)
print(death_rate_min)
print(death_rate_max)
```  

#### Results : 

	Output
	48
	1367485388
	0.0
	4.02
	6.65
	45.45
	1.53
	14.89


---
# 4: Predicting Future Population Growth  

These measures seem to align more with reality. Let's now predict next year's population for each country using the following formula:  

>projected_population = population + (population * (population_growth/100))

We need to divide by 100 since the values in population_growth are percentage values (e.g. 2.32) instead of proportional values (e.g. 0.0232).  

#### Instructions :

Use SQL arithmetic to return the projected population values using the above formula and the following parameters:

 - Round the values to the nearest whole number, since population values can't contain fractional values.
 - Filter out any rows with NULL as the value for either population or population_growth.
 - Restrict to only countries with a population of less than 7 billion and greater than 0.
 - Assign the resulting projected population values to projected_population.

 
```python
 import sqlite3
conn = sqlite3.connect("factbook.db")
projection = "select round(population + (population * (population_growth/100)),0) as projected_population from facts where population is not null and population_growth is not null and population < 7000000000 and population > 0"
projected_population = conn.execute(projection).fetchall()
```  

#### Results : 




---
# 5: Exploring Projected Population  

To understand how the population would shift under the projected population values, calculate the min, max, and avg values.  

#### Instructions :

Write a single query that returns:  

 - the minimum of the projected population values, assign to pop_proj_min.
 - the maximum of the projected population values, assign to pop_proj_max.
 - the average of the projected population values, assign to pop_proj_avg.

Make sure to:  

- Round all fractional values to the nearest whole number.
- Filter out any rows with NULL as the value for either population or population_growth.
- Restrict to only countries with a population of less than 7 billion and greater than 0.
- Use print statements or the variables display below the output box to observe these values.
 
```python
 import sqlite3
conn = sqlite3.connect("factbook.db")
projection = "select round(min(projected_population),0),round(max(projected_population),0),round(avg(projected_population),0) from (select round(population + (population * (population_growth/100)),0) as projected_population from facts where population is not null and population_growth is not null and population < 7000000000 and population > 0)"
projected_population = conn.execute(projection).fetchall()

pop_proj_min = projected_population[0][0]
pop_proj_max = projected_population[0][1]
pop_proj_avg = projected_population[0][2]

print(pop_proj_min)
print(pop_proj_max)
print(pop_proj_avg)


#or

import sqlite3
conn = sqlite3.connect("factbook.db")
proj_pop_query = '''
select round(min(population + population * (population_growth/100)), 0), 
round(max(population + population * (population_growth/100)), 0), 
round(avg(population + population * (population_growth/100)), 0)
from facts 
where population > 0 and population < 7000000000 and 
population is not null and population_growth is not null;
'''

proj_results = conn.execute(proj_pop_query).fetchall()

pop_proj_min = proj_results[0][0]
pop_proj_max = proj_results[0][1]
pop_proj_avg = proj_results[0][2]

print("Projected Population,", "Minimum: ", pop_proj_min)
print("Projected Population,", "Maximum: ", pop_proj_max)
print("Projected Population,", "Average: ", pop_proj_avg)

```  

#### Results : 

	Output
	48.0
	1373639072.0
	33405469.0

---
# 6: Next Steps

In this challenge, you calculated summary statistics to better understand the data and then projected next year's population for each country using SQL arithmetic. In the next mission, you'll learn about group summary techniques for segmenting data in your queries.  