11/2017  
# Datacamp - Manipulating Time Series Data in Python 
[Manipulating Time Series Data in Python](https://www.datacamp.com/courses/manipulating-time-series-data-in-python)
---

***Course Description***  

In this course you'll learn the basics of manipulating time series data. Time series data are data that are indexed by a sequence of dates or times. You'll learn how to use methods built into Pandas to work with this index. You'll also learn how resample time series to change the frequency. This course will also show you how to calculate rolling and cumulative values for times series. Finally, you'll use all your new skills to build a value-weighted stock index from actual stock data.         

# Part 2 : Basic Time Series Metrics & Resampling     

This chapter dives deeper into the essential time series functionality made available through the pandas DataTimeIndex. It introduces resampling and how to compare different time series by normalizing their start points.     

## Compare the performance of several asset classes     

You have seen in the video how you can easily compare several time series by normalizing their starting points to 100, and plot the result.  

To broaden your perspective on financial markets, let's compare four key assets: stocks, bonds, gold, and oil.  

### Instructions

We have already imported pandas as pd and matplotlib.pyplot as plt.

 - Import 'asset_classes.csv', using .read_csv() to parse dates in the 'DATE' column and set this column as the index, then assign the result to prices.
 - Select the first price for each series using .iloc[0] on prices and assign the result to first_prices.
 - Divide prices by first_prices, multiply by 100 and assign the result to normalized.
 - Plot normalized.

```python
# Import data here
prices = pd.read_csv('asset_classes.csv',parse_dates=['DATE'],index_col='DATE')

# Inspect prices here
print(prices.info())
print('-------------')
print(prices.head())
print('-------------')
# Select first prices
first_prices = prices.iloc[0]
print(first_prices)
print('-------------')
# Create normalized
normalized = prices.div(first_prices).mul(100)
print(normalized.head())
print('-------------')
# Plot normalized
normalized.plot()
plt.show()
```

### Results :  

![graph7](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph7.svg)  

		<script.py> output:
			<class 'pandas.core.frame.DataFrame'>
			DatetimeIndex: 2469 entries, 2007-06-29 to 2017-06-26
			Data columns (total 4 columns):
			SP500    2469 non-null float64
			Bonds    2469 non-null float64
			Gold     2469 non-null float64
			Oil      2469 non-null float64
			dtypes: float64(4)
			memory usage: 96.4 KB
			None
			-------------
						  SP500   Bonds    Gold    Oil
			DATE                                      
			2007-06-29  1503.35  402.15  648.50  70.47
			2007-07-02  1519.43  402.96  650.50  71.11
			2007-07-03  1524.87  402.02  657.25  71.41
			2007-07-05  1525.40  400.15  655.90  71.81
			2007-07-06  1530.44  399.31  647.75  72.80
			-------------
			SP500    1503.35
			Bonds     402.15
			Gold      648.50
			Oil        70.47
			Name: 2007-06-29 00:00:00, dtype: float64
			-------------
							 SP500       Bonds        Gold         Oil
			DATE                                                      
			2007-06-29  100.000000  100.000000  100.000000  100.000000
			2007-07-02  101.069611  100.201417  100.308404  100.908188
			2007-07-03  101.431470   99.967674  101.349268  101.333901
			2007-07-05  101.466724   99.502673  101.141095  101.901518
			2007-07-06  101.801976   99.293796   99.884348  103.306372
			-------------

---


## Comparing stock prices with a benchmark  

You also learned in the video how to compare the performance of various stocks against a benchmark. Now you'll learn more about the stock market by comparing the three largest stocks on the NYSE to the Dow Jones Industrial Average, which contains the 30 largest US companies.  

The three largest companies on the NYSE are:  

Company	Stock  | Ticker
Johnson & Johnson  | JNJ
Exxon Mobil  | XOM
JP Morgan Chase  | JPM

### Instructions

We have already imported pandas as pd and matplotlib.pyplot as plt.  

 - Use pd.read_csv() to import 'nyse.csv' and 'dow_jones.csv', creating a DatetimeIndex for each from the 'date' column using parse_dates and index_col, and assign the result to stocks and dow_jones, respectively.
 - Use pd.concat() along axis=1 to combine stocks and dow_jones and assign the result to data. Inspect the .info() of data.
 - Divide data by the first value for each series, multiply by 100 and plot the result.

```python
# Import stock prices and index here
stocks = pd.read_csv('nyse.csv',parse_dates=['date'],index_col='date')
dow_jones = pd.read_csv('dow_jones.csv',parse_dates=['date'],index_col='date')

# Concatenate data and inspect result here
data = pd.concat([stocks,dow_jones],axis=1)
print(data.info())

# Normalize and plot your data here
data.div(data.iloc[0]).mul(100).plot()
plt.show()
```

### Results :  

![graph8](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph8.svg)  

		<script.py> output:
			<class 'pandas.core.frame.DataFrame'>
			DatetimeIndex: 1762 entries, 2010-01-04 to 2016-12-30
			Data columns (total 4 columns):
			JNJ     1762 non-null float64
			JPM     1762 non-null float64
			XOM     1762 non-null float64
			DJIA    1762 non-null float64
			dtypes: float64(4)
			memory usage: 68.8 KB
			None

---


## Plot performance difference vs benchmark index  

In the video, you learned how to calculate and plot the performance difference of a stock in percentage points relative to a benchmark index.  

Let's compare the performance of Microsoft (MSFT) and Apple (AAPL) to the S&P 500 over the last 10 years.  

### Instructions

We have already imported pandas as pd and matplotlib.pyplot as plt.

 - Create the list tickers containing the two stock symbols.
 - Use pd.read_csv() to import 'msft_aapl.csv' and 'sp500.csv', creating a DatetimeIndex for each from the 'date' column using parse_dates and index_col, and assign the result to stocks and sp500, respectively.
 - Use pd.concat() to concatenate stocks and sp500 along axis=1, apply .dropna() to drop all missing values, and assign the result to data.
 - Normalize data by dividing by the first price, multiply by 100 and assign the output to normalized.
 - Select tickers from normalized, and subtract normalized['SP500'] with keyword axis=0 to align the indexes, then plot the result.

```python
# Create tickers
tickers = ['MSFT','AAPL']

# Import stock data here
stocks = pd.read_csv('msft_aapl.csv',parse_dates=['date'],index_col='date')

# Import index here
sp500 = pd.read_csv('sp500.csv',parse_dates=['date'],index_col='date')

# Concatenate stocks and index here
data = pd.concat([stocks,sp500],axis=1).dropna()

# Normalize data
normalized = data.div(data.iloc[0]).mul(100)

# Subtract the normalized index from the normalized stock prices, and plot the result
normalized[tickers].sub(normalized['SP500'],axis=0).plot()
plt.show()
```

### Results :  

![graph9](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph9.svg)  

---


## Convert monthly to weekly data   

You have learned in the video how to use .reindex() to conform an existing time series to a DateTimeIndex at a different frequency.  

Let's practice this method by creating monthly data and then converting this data to weekly frequency while applying various fill logic options.  

### Instructions

We have already imported pandas as pd for you. We have also defined start and end dates.

 - Create monthly_dates using pd.date_range with start, end and frequency alias 'M'.
 - Create and print the pd.Series monthly, passing the list [1, 2] to data, and using monthly_dates as index.
 - Create weekly_dates using pd.date_range with start, end and frequency alias 'W'.
 - Apply .reindex() to monthly three times: first without additional options, then with ffill and then with bfill, print()-ing each result.

```python
# Set start and end dates
start = '2016-1-1'
end = '2016-2-29'

# Create monthly_dates here
monthly_dates = pd.date_range(start=start,end=end,freq='M')

# Create and print monthly here
monthly = pd.Series(data=[1, 2], index=monthly_dates)
print(monthly)
print('-------------------')
# Create weekly_dates here
weekly_dates = pd.date_range(start=start,end=end,freq='W')

# Print monthly, reindexed using weekly_dates
print(monthly.reindex(weekly_dates))
print('-------------------')
print(monthly.reindex(weekly_dates,method='ffill'))
print('-------------------')
print(monthly.reindex(weekly_dates,method='bfill'))
```

### Results :  

		<script.py> output:
			2016-01-31    1
			2016-02-29    2
			Freq: M, dtype: int64
			-------------------
			2016-01-03    NaN
			2016-01-10    NaN
			2016-01-17    NaN
			2016-01-24    NaN
			2016-01-31    1.0
			2016-02-07    NaN
			2016-02-14    NaN
			2016-02-21    NaN
			2016-02-28    NaN
			Freq: W-SUN, dtype: float64
			-------------------
			2016-01-03    NaN
			2016-01-10    NaN
			2016-01-17    NaN
			2016-01-24    NaN
			2016-01-31    1.0
			2016-02-07    1.0
			2016-02-14    1.0
			2016-02-21    1.0
			2016-02-28    1.0
			Freq: W-SUN, dtype: float64
			-------------------
			2016-01-03    1
			2016-01-10    1
			2016-01-17    1
			2016-01-24    1
			2016-01-31    1
			2016-02-07    2
			2016-02-14    2
			2016-02-21    2
			2016-02-28    2
			Freq: W-SUN, dtype: int64

---


## Create weekly from monthly unemployment data     

The civilian US unemployment rate is reported monthly. You may need more frequent data, but that's no problem because you just learned how to upsample a time series.  

You'll work with the time series data for the last 20 years, and apply a few options to fill in missing values before plotting the weekly series.  

### Instructions

We have already imported pandas as pd and matplotlib.pyplot as plt.

 - Use pd.read_csv() to import 'unemployment.csv', creating a DateTimeIndex from the 'date' column using parse_dates and index_col, and assign the result to data.
 - Convert data to weekly frequency using .asfreq() with the alias 'W' and show the first five rows.
 - Convert again to weekly frequency, adding the option 'bfill' and show the first five rows.
 - Create weekly series, now adding the option 'ffill', assign to weekly_ffill and show the first five rows.
 - Plot weekly_ffill starting in 2015.

```python
# Import data here
data = pd.read_csv('unemployment.csv', parse_dates=['date'], index_col='date')

# Show first five rows of weekly series
print(data.asfreq('W').head())

# Show first five rows of weekly series with bfill option
print(data.asfreq('W', method='bfill').head())

# Create weekly series with ffill option and show first five rows
weekly_ffill = data.asfreq('W', method='ffill')
print(weekly_ffill.head())

# Plot weekly_fill starting 2015 here 
weekly_ffill.loc['2015':].plot()
plt.show()

```

### Results :  

![graph10](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph10.svg)  

		<script.py> output:
						UNRATE
			date              
			2000-01-02     NaN
			2000-01-09     NaN
			2000-01-16     NaN
			2000-01-23     NaN
			2000-01-30     NaN
						UNRATE
			date              
			2000-01-02     4.1
			2000-01-09     4.1
			2000-01-16     4.1
			2000-01-23     4.1
			2000-01-30     4.1
						UNRATE
			date              
			2000-01-02     4.0
			2000-01-09     4.0
			2000-01-16     4.0
			2000-01-23     4.0
			2000-01-30     4.0

---


## Use interpolation to create weekly employment data    

You have recently used the civilian US unemployment rate, and converted it from monthly to weekly frequency using simple forward or backfill methods.  

Compare your previous approach to the new .interpolate() method that you learned about in this video.  

### Instructions

We have imported pandas as pd and matplotlib.pyplot as plt for you. We have also loaded the monthly unemployment rate from 2010 to 2016 into a variable monthly.

 - Inspect monthly using .info().
 - Create a pd.date_range() with weekly dates, using the .min() and .max() of the index of monthly as start and end, respectively, and assign the result to weekly_dates.
 - Apply .reindex() using weekly_dates to monthly and assign the output to weekly.
 - Create new columns 'ffill' and 'interpolated' by applying .ffill() and .interpolate() to weekly.UNRATE.
 - Show a plot of weekly.

```python
# Inspect data here
print(monthly.info())

# Create weekly dates
weekly_dates = pd.date_range(start=monthly.index.min(),end=monthly.index.max(),freq='W')

# Reindex monthly to weekly data
weekly = monthly.reindex(weekly_dates)

# Create ffill and interpolated columns
weekly['ffill'] = weekly.UNRATE.ffill()
weekly['interpolated'] = weekly.UNRATE.interpolate()

# Plot weekly
weekly.plot()
plt.show()
```

### Results :  

![graph11](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph11.svg)  

		<script.py> output:
			<class 'pandas.core.frame.DataFrame'>
			DatetimeIndex: 85 entries, 2010-01-01 to 2017-01-01
			Data columns (total 1 columns):
			UNRATE    85 non-null float64
			dtypes: float64(1)
			memory usage: 1.3 KB
			None

---



## Interpolate debt/GDP and compare to unemployment     

Since you have learned how to interpolate time series, you can now apply this new skill to the quarterly debt/GDP series, and compare the result to the monthly unemployment rate.  

### Instructions

We have imported pandas as pd and matplotlib.pyplot as plt for you.

 - Use pd.read_csv() to import 'debt_unemployment.csv', creating a DateTimeIndex from the 'date' column using parse_dates and index_col, and assign the result to data. print() the .info() of the data.
 - Apply .interpolate() to data and assign this to interpolated, then inspect the result.
 - Plot interpolated with 'Unemployment' on the secondary_y axis.

```python
# Import & inspect data here
data = pd.read_csv('debt_unemployment.csv',parse_dates=['date'],index_col='date')
print(data.info())
print('-----------------')
# Interpolate and inspect here
interpolated = data.interpolate()
print(interpolated.info())
print('-----------------')
# Plot interpolated data here
interpolated.plot(secondary_y='Unemployment')
plt.show()

```

### Results :  

![graph12](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph12.svg)  

		<script.py> output:
			<class 'pandas.core.frame.DataFrame'>
			DatetimeIndex: 89 entries, 2010-01-01 to 2017-05-01
			Data columns (total 2 columns):
			Debt/GDP        29 non-null float64
			Unemployment    89 non-null float64
			dtypes: float64(2)
			memory usage: 2.1 KB
			None
			-----------------
			<class 'pandas.core.frame.DataFrame'>
			DatetimeIndex: 89 entries, 2010-01-01 to 2017-05-01
			Data columns (total 2 columns):
			Debt/GDP        89 non-null float64
			Unemployment    89 non-null float64
			dtypes: float64(2)
			memory usage: 2.1 KB
			None
			-----------------

---


## Compare weekly, monthly and annual ozone trends for NYC & LA     

You have seen in the video how to downsample and aggregate time series on air quality.  

First, you'll apply this new skill to ozone data for both NYC and LA since 2000 to compare the air quality trend at weekly, monthly and annual frequencies and explore how different resampling periods impact the visualization.  

### Instructions

We have again imported pandas as pd and matplotlib.pyplot as plt for you.

 - Use pd.read_csv() to import 'ozone.csv' and set a DateTimeIndex based on the 'date' column using parse_dates and index_col, assign the result to ozone and inspect using .info().
 - Apply .resample() with weekly frequency ('W') to ozone, aggregate using .mean() and plot the result.
 - Repeat with monthly ('M') and annual ('A') frequencies, plotting each result.

```python
# Import and inspect data here
ozone = pd.read_csv('ozone.csv',parse_dates=['date'],index_col='date')
print(ozone.info())

# Calculate and plot the weekly average ozone trend
ozone.resample('W').mean().plot()
plt.show()

# Calculate and plot the monthly average ozone trend
ozone.resample('M').mean().plot()
plt.show()

# Calculate and plot the annual average ozone trend
ozone.resample('A').mean().plot()
plt.show()
```

### Results :  

![graph13](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph13.svg)  
![graph14](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph14.svg)  
![graph15](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph15.svg)  

		<script.py> output:
			<class 'pandas.core.frame.DataFrame'>
			DatetimeIndex: 6291 entries, 2000-01-01 to 2017-03-31
			Data columns (total 2 columns):
			Los Angeles    5488 non-null float64
			New York       6167 non-null float64
			dtypes: float64(2)
			memory usage: 147.4 KB
			None

---


## Compare monthly average stock prices for Facebook and Google   

Now, you'll apply your new resampling skills to daily stock price series for Facebook and Google for the 2015-2016 period to compare the trend of the monthly averages.  

### Instructions

We have again imported pandas as pd and matplotlib.pyplot as plt for you.

 - Use pd.read_csv() to import 'stocks.csv' and set a DateTimeIndex based on the 'date' column using parse_dates and index_col, assign the result to data and inspect using .info().
 - Create monthly_average by applying .resample() with monthly frequency to stocks, using .mean() to aggregate. Plot the result using subplots.

```python
# Import and inspect data here
stocks = pd.read_csv('stocks.csv',parse_dates=['date'],index_col='date')
print(stocks.info())

# Calculate and plot the monthly averages
monthly_average = stocks.resample('M').mean()
monthly_average.plot(subplots=True)
plt.show()
```

### Results :  

![graph16](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph16.svg)  

		<script.py> output:
			<class 'pandas.core.frame.DataFrame'>
			DatetimeIndex: 504 entries, 2015-01-02 to 2016-12-30
			Data columns (total 2 columns):
			FB      504 non-null float64
			GOOG    504 non-null float64
			dtypes: float64(2)
			memory usage: 11.8 KB
			None

---



## Compare quarterly GDP growth rate and stock returns     

With your new skill to downsample and aggregate time series, you can compare higher-frequency stock price series to lower-frequency economic time series.  

As a first example, let's compare the quarterly GDP growth rate to the quarterly rate of return on the (resampled) Dow Jones Industrial index of 30 large US stocks.  

GDP growth is reported at the beginning of each quarter for the previous quarter. To calculate matching stock returns, you'll resample the stock index to quarter start frequency using the alias 'QS', and aggregating using the .first() observations.  

### Instructions

As usual, we have imported pandas as pd and matplotlib.pyplot as plt for you.

 - Use pd.read_csv() to import 'gdp_growth.csv' and 'djia.csv', for both set a DatetimeIndex based on the 'date' column using parse_dates and index_col, and assign the results to gdp_growth and djia respectively, then inspect using .info().
 - Resample djia using frequency alias 'QS', aggregate using .first(), and assign to djia_quarterly.
 - Apply .pct_change() to djia_quarterly and .mul() by 100 to obtain djia_quarterly_return.
 - Use pd.concat() to concatenate gdp_growth and djia_quarterly_return along axis=1, and assign to data. Rename the columns using .columns and the new labels 'gdp' and 'djia', then .plot() the results.

```python
# Import and inspect gdp_growth here
gdp_growth = pd.read_csv('gdp_growth.csv',parse_dates=['date'],index_col='date')
print(gdp_growth.info())

# Import and inspect djia here
djia = pd.read_csv('djia.csv',parse_dates=['date'],index_col='date')
print(djia.info())

# Calculate djia quarterly returns here 
djia_quarterly = djia.resample('QS').first()
djia_quarterly_return = djia_quarterly.pct_change().mul(100)

# Concatenate, rename and plot djia_quarterly_return and gdp_growth here 
data = pd.concat([gdp_growth,djia_quarterly_return],axis=1)
data.columns = ['gdp','djia']
data.plot()
plt.show()
```

### Results :  

![graph17](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph17.svg)  

		<script.py> output:
			<class 'pandas.core.frame.DataFrame'>
			DatetimeIndex: 41 entries, 2007-01-01 to 2017-01-01
			Data columns (total 1 columns):
			gdp_growth    41 non-null float64
			dtypes: float64(1)
			memory usage: 656.0 bytes
			None
			<class 'pandas.core.frame.DataFrame'>
			DatetimeIndex: 2610 entries, 2007-06-29 to 2017-06-29
			Data columns (total 1 columns):
			djia    2519 non-null float64
			dtypes: float64(1)
			memory usage: 40.8 KB
			None

---


## Visualize monthly mean, median and standard deviation of S&P500 returns    

You have also learned how to calculate several aggregate statistics from upsampled data.  

Let's use this to explore how the monthly mean, median and standard deviation of daily S&P500 returns have trended over the last 10 years.  

### Instructions

As usual, we have imported pandas as pd and matplotlib.pyplot as plt for you.

 - Use pd.read_csv() to import 'sp500.csv', set a DateTimeIndex based on the 'date' column using parse_dates and index_col, assign the results to sp500, and inspect using .info().
 - Convert sp500 to a pd.Series() using .squeeze(), and apply .pct_change() to calculate daily_returns.
 - .resample() daily_returns to month-end frequency (alias: 'M'), and apply .agg() to calculate 'mean', 'median', and 'std'. Assign the result to stats.
 - .plot() stats.

```python
# Import data here
sp500 = pd.read_csv('sp500.csv',parse_dates=['date'],index_col='date')
print(sp500.info())
print('----------------')
# Calculate daily returns here
daily_returns = sp500.squeeze().pct_change()

# Resample and calculate statistics
stats = daily_returns.resample('M').agg(['mean','median','std'])

# Plot stats here
stats.plot()
plt.show()
```

### Results :  

![graph18](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph18.svg)  

		<script.py> output:
			<class 'pandas.core.frame.DataFrame'>
			DatetimeIndex: 2395 entries, 2007-06-29 to 2016-12-30
			Data columns (total 1 columns):
			SP500    2395 non-null float64
			dtypes: float64(1)
			memory usage: 37.4 KB
			None
			----------------

---
