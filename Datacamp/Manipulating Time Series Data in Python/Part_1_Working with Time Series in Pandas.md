11/2017  
# Datacamp - Manipulating Time Series Data in Python 
[Manipulating Time Series Data in Python](https://www.datacamp.com/courses/manipulating-time-series-data-in-python)
---

***Course Description***  

In this course you'll learn the basics of manipulating time series data. Time series data are data that are indexed by a sequence of dates or times. You'll learn how to use methods built into Pandas to work with this index. You'll also learn how resample time series to change the frequency. This course will also show you how to calculate rolling and cumulative values for times series. Finally, you'll use all your new skills to build a value-weighted stock index from actual stock data.         

# Part 1 : Working with Time Series in Pandas   

This chapter lays the foundations to leverage the powerful time series functionality made available by how Pandas represents dates, in particular by the DateTimeIndex. You will learn how to create and manipulate date information and time series, and how to do calculations with time-aware DataFrames to shift your data in time or create period-specific returns.    

## Your first time series   

You have learned in the video how to create a sequence of dates using pd.date_range(). You have also seen that each date in the resulting pd.DatetimeIndex is a pd.Timestamp with various attributes that you can access to obtain information about the date.  

Now, you'll create a week of data, iterate over the result, and obtain the dayofweek and weekday_name for each date.  

### Instructions

We have already imported pandas as pd for you.  

 - Use pd.date_range to create seven dates starting from '2017-1-1' at (default) daily frequency. Use the arguments start and periods. Assign the result to seven_days.
 - Iterate over each date in seven_days and in each iteration, print the .dayofweek and .weekday_name attributes.

```python
# Create the range of dates here
seven_days = pd.date_range(start='2017-1-1',periods=7)

# Iterate over the dates and print the number and name of the weekday
for day in seven_days:
    print(day.dayofweek, day.weekday_name)
```

### Results :  

		<script.py> output:
			6 Sunday
			0 Monday
			1 Tuesday
			2 Wednesday
			3 Thursday
			4 Friday
			5 Saturday

---


## Create a time series of air quality data     

You have seen in the video how to deal with dates that are not in the correct format, but instead are provided as string types, represented as dtype object in pandas.  

We have prepared a data set with air quality data (ozone, pm25, and carbon monoxide for NYC, 2000-2017) for you to practice the use of pd.to_datetime().  

### Instructions

We have already imported pandas as pd and matplotlib.pyplot as plt for you, and loaded the air quality DataFrame into the variable data.  

 - Inspect data using .info().
 - Use pd.to_datetime to convert the column 'date' to dtype datetime64.
 - Set the 'Date' column as index.
 - Validate the changes by inspecting data using .info() again.
 - Plot data using subplots=True.

```python
# Inspect data
print(data.info())

# Convert the date column to datetime64
data.date = pd.to_datetime(data.date)

# Set date column as index
data.set_index('date', inplace=True)

# Inspect data 
print(data.info())

# Plot data
data.plot(subplots=True)
plt.show()

```

### Results :  

![graph1](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph1.svg)  

		<script.py> output:
			<class 'pandas.core.frame.DataFrame'>
			RangeIndex: 6317 entries, 0 to 6316
			Data columns (total 4 columns):
			date     6317 non-null object
			ozone    6317 non-null float64
			pm25     6317 non-null float64
			co       6317 non-null float64
			dtypes: float64(3), object(1)
			memory usage: 197.5+ KB
			None
			<class 'pandas.core.frame.DataFrame'>
			DatetimeIndex: 6317 entries, 1999-07-01 to 2017-03-31
			Data columns (total 3 columns):
			ozone    6317 non-null float64
			pm25     6317 non-null float64
			co       6317 non-null float64
			dtypes: float64(3)
			memory usage: 197.4 KB
			None

---


## Compare annual stock price trends     

In the video, you have seen how to select sub-periods from a time series.  

You'll use this to compare the performance for three years of Yahoo stock prices.  

### Instructions

We have already imported pandas as pd and matplotlib.pyplot as plt and we have already loaded the 'yahoo.csv' file in a variable yahoo with DateTimeIndex and a single column price.

 - Create an empty pd.DataFrame() called prices.
 - Iterate over a list containing the three years, 2013, 2014, and 2015, as string, and in each loop:
 - Use the iteration variable to select the data for this year and the column price.
 - Use .reset_index() with drop=True to remove the DatetimeIndex.
 - Rename the column price' column to the appropriate year.
 - Use pd.concat() to combine the yearly data with the data in prices along axis=1.
 - Plot prices.

```python
# Create dataframe prices here
prices = pd.DataFrame()

# Select data for each year and concatenate with prices here 
for year in ['2013', '2014', '2015']:
    price_per_year = yahoo.loc[year, ['price']].reset_index(drop=True)
    price_per_year.rename(columns={'price': year}, inplace=True)
    prices = pd.concat([prices, price_per_year], axis=1)

# Plot prices
prices.plot()
plt.show()

```

### Results :  

![graph2](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph2.svg)  

---


## What is a network?   

In the video, you have seen how to assign a frequency to a DateTimeIndex, and then change this frequency.

Now, you'll use data on the daily carbon monoxide concentration in NYC, LA and Chicago from 2005-17.

You'll set the frequency to calendar daily and then resample to monthly frequency, and visualize both series to see how the different frequencies affect the data.

### Instructions

We have already imported pandas as pd and matplotlib.pyplot as plt and we have already loaded the co_cities.csv file in a variable co.

 - Inspect co using .info().
 - Use .asfreq() to set the frequency to calendar daily.
 - Show a plot of 'co' using subplots=True.
 - Change the the frequency to monthly using the alias 'M'.
 - Show another plot of co using subplots=True.

```python
# Inspect data
print(co.info())

# Set the frequency to calendar daily
co = co.asfreq('D')

# Plot the data
co.plot(subplots=True)
plt.show()

# Set frequency to monthly
co = co.asfreq('M')

# Plot the data
co.plot(subplots=True)
plt.show()
```

### Results :  

		<script.py> output:
			<class 'pandas.core.frame.DataFrame'>
			DatetimeIndex: 1898 entries, 2005-01-01 to 2010-12-31
			Data columns (total 3 columns):
			Chicago        1898 non-null float64
			Los Angeles    1898 non-null float64
			New York       1898 non-null float64
			dtypes: float64(3)
			memory usage: 59.3 KB
			None

![graph3](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph3.svg)  	
![graph4](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph4.svg)  		
			
---


## Shifting stock prices across time   

The first method to manipulate time series that you saw in the video was .shift(), which allows you shift all values in a Series or DataFrame by a number of periods to a different time along the DateTimeIndex.  

Let's use this to visually compare a stock price series for Google shifted 90 business days into both past and future.  

### Instructions

We have already imported pandas as pd and matplotlib.pyplot as plt.  

 - Use pd.read_csv() to import 'google.csv', parsing the 'Date' as dates, setting the result as index and assigning to google.
 - Use .asfreq() to set the frequency of google to business daily.
 - Add new columns lagged and shifted to google that contain the Close shifted by 90 business days into past and future, respectively.
 - Plot the three columns of google.

```python
# Import data here
google = pd.read_csv('google.csv',parse_dates=['Date'],index_col='Date')

# Set data frequency to business daily
google = google.asfreq('B')

# Create 'lagged' and 'shifted'
google['shifted'] = google.Close.shift(periods=90)
google['lagged'] = google.Close.shift(periods=-90)

# Plot the google price series
google.plot()
plt.show()
```

### Results :  

![graph5](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph5.svg)  

---


## Calculating stock price changes 

You have learned in the video how to calculate returns using current and shifted prices as input. Now you'll practice a similar calculation to calculate absolute changes from current and shifted prices, and compare the result to the function .diff().  

### Instructions

We have already imported pandas as pd and matplotlib.pyplot as plt. We have also loaded Yahoo stock prices for the years 2015 and 2016, set the frequency to business daily, and assigned the result to yahoo.  

 - Create a new column called shifted_30 that contains the 'price' shifted by 30 business days into the future.
 - Subtract 'shifted_30' from 'price', and assign the result to a new column, 'change_30'.
 - Apply .diff(), setting periods to 30, and assign the result to a new column, 'diff_30'.
 - Inspect the last five rows of google to verify the calculation.
 - Subtract diff_30 from change_30 and print the .value_counts() of the result to show both columns are equal.

```python
# Created shifted_30 here
yahoo['shifted_30'] = yahoo.price.shift(periods=30)

# Subtract shifted_30 from price
yahoo['change_30'] = yahoo.price - yahoo.shifted_30

# Get the 30-day price difference
yahoo['diff_30'] = yahoo.price.diff(periods=30)

# Inspect the last five rows of price
print(yahoo.tail())
print('---------------------------')
# Show the value_counts of the difference between abs_change_30 and difference_30
print(yahoo.change_30.sub(yahoo.diff_30).value_counts())
```

### Results :  

		<script.py> output:
						price  shifted_30  change_30  diff_30
			date                                             
			2015-12-25    NaN       32.19        NaN      NaN
			2015-12-28  33.60       32.94       0.66     0.66
			2015-12-29  34.04       32.86       1.18     1.18
			2015-12-30  33.37       32.98       0.39     0.39
			2015-12-31  33.26       32.62       0.64     0.64
			---------------------------
			0.0    703
			dtype: int64

---



## Plotting multi-period returns    

The last time series method you have learned about in the video was .pct_change(). Let's use this function to calculate returns for various calendar day periods, and plot the result to compare the different patterns.  

We'll be using Google stock prices from 2014-2016.  

### Instructions

We have already imported pandas as pd, and matplotlib.pyplot as plt. We have also loaded 'GOOG' stock prices for the years 2014-2016, set the frequency to calendar daily, and assigned the result to google.  

 - Create the columns 'daily_return', 'monthly_return', and 'annual_return' that contain the pct_change() of 'Close' for 1, 30 and 360 calendar days, respectively, and multiply each by 100.
 - Plot the result using subplots=True.

```python
# Create daily_return
google['daily_return'] = google.Close.pct_change().mul(100)

# Create monthly_return
google['monthly_return'] = google.Close.pct_change(30).mul(100)

# Create annual_return
google['annual_return'] = google.Close.pct_change(360).mul(100)

# Plot the result
google.plot(subplots=True)
plt.show()
```

### Results :  

![graph6](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph6.svg)  

---
