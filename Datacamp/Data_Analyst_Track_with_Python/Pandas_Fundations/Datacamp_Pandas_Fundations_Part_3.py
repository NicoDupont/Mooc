"""
Datacamp - Pandas Fundations
https://www.datacamp.com/courses/pandas-foundations
Part 3 : Time series in pandas
Python 3.X
"""



"""
In this chapter, you will learn how to manipulate and visualize time series data using pandas.
You will become familiar with concepts such as upsampling, downsampling, and interpolation.
You will practice using pandas' method chaining to efficiently filter your data and perform time series analyses.
From stock prices to flight timings, time series data are found in a wide variety of domains and being able to effectively work with such data can be an invaluable skill.
"""



""" QUESTION ANSWER: 5
Reading and slicing times
50xp

For this exercise, we have read in the same data file using three different approaches:

    df1 = pd.read_csv(filename)
    df2 = pd.read_csv(filename, parse_dates=['Date'])
    df3 = pd.read_csv(filename, index_col='Date', parse_dates=True)

Use df.head() and df.info() in the IPython Shell to inspect the data. Then, try to index with a datetime string. Which of the resulting DataFrames allows you to easily index and slice data by dates using, for example, df.loc['2010-Aug-01']?
Possible Answers

    df1
    1
    df1 and df2
    2
    df2
    3
    df2 and df3
    4
    df3
    5
"""

""" consol ouput or results
In [1]: df1.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8759 entries, 0 to 8758
Data columns (total 4 columns):
Temperature    8759 non-null float64
DewPoint       8759 non-null float64
Pressure       8759 non-null float64
Date           8759 non-null object
dtypes: float64(3), object(1)
memory usage: 273.8+ KB

In [2]: df2.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8759 entries, 0 to 8758
Data columns (total 4 columns):
Temperature    8759 non-null float64
DewPoint       8759 non-null float64
Pressure       8759 non-null float64
Date           8759 non-null datetime64[ns]
dtypes: datetime64[ns](1), float64(3)
memory usage: 273.8 KB

In [3]: df3.info()
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 8759 entries, 2010-01-01 00:00:00 to 2010-12-31 23:00:00
Data columns (total 3 columns):
Temperature    8759 non-null float64
DewPoint       8759 non-null float64
Pressure       8759 non-null float64
dtypes: float64(3)
memory usage: 273.7 KB
"""





"""
Creating and using a DatetimeIndex
50xp

The pandas Index is a powerful way to handle time series data, so it is valuable to know how to build one yourself. Pandas provides the pd.to_datetime() function for just this task. For example, if passed the list of strings ['2015-01-01 091234','2015-01-01 091234'] and a format specification variable, such as format='%Y-%m-%d %H%M%S, pandas will parse the string into the proper datetime elements and build the datetime objects.

In this exercise, a list of temperature data and a list of date strings has been pre-loaded for you as temperature_list and date_list respectively. Your job is to use the .to_datetime() method to build a DatetimeIndex out of the list of date strings, and to then use it along with the list of temperature data to build a pandas Series.
Instructions

    Prepare a format string, time_format, using '%Y-%m-%d %H:%M' as the desired format.
    Convert date_list into a datetime object by using the pd.to_datetime() function. Specify the format string you defined above and assign the result to my_datetimes.
    Construct a pandas Series called time_series using pd.Series() with temperature_list and my_datetimes. Set the index of the Series to be my_datetimes.

"""
# Prepare a format string: time_format
time_format = '%Y-%m-%d %H:%M'

# Convert date_list into a datetime object: my_datetimes
my_datetimes = pd.to_datetime(date_list, format=time_format)

# Construct a pandas Series using temperature_list and my_datetimes: time_series
time_series = pd.Series(temperature_list, index=my_datetimes)
""" results or consol output

"""




"""
Partial string indexing and slicing
100xp

Pandas time series support "partial string" indexing. What this means is that even when passed only a portion of the datetime, such as the date but not the time, pandas is remarkably good at doing what one would expect. Pandas datetime indexing also supports a wide variety of commonly used datetime string formats, even when mixed.

In this exercise, a time series that contains hourly weather data has been pre-loaded for you. This data was read using the parse_dates=True option in read_csv() with index_col="Dates" so that the Index is indeed a DatetimeIndex.

All data from the 'Temperature' column has been extracted into the variable ts0. Your job is to use a variety of natural date strings to extract one or more values from ts0.

After you are done, you will have three new variables - ts1, ts2, and ts3. You can slice these further to extract only the first and last entries of each. Try doing this after your submission for more practice.
Instructions

    Extract data from ts0 for a single hour - the hour from 9pm to 10pm on 2010-10-11. Assign it to ts1.
    Extract data from ts0 for a single day - July 4th, 2010 - and assign it to ts2.
    Extract data from ts0 for the second half of December 2010 - 12/15/2010 to 12/31/2010. Assign it to ts3.

"""
# Extract the hour from 9pm to 10pm on '2010-10-11': ts1
ts1 = ts0.loc['2010-10-11 21:00:00']

# Extract '2010-07-04' from ts0: ts2
ts2 = ts0.loc['2010-07-04']

# Extract data from '2010-12-15' to '2010-12-31': ts3
ts3 = ts0.loc['2010-12-15':'2010-12-31']
""" results or consol output

"""





"""
Reindexing the Index
100xp

Reindexing is useful in preparation for adding or otherwise combining two time series data sets. To reindex the data, we provide a new index and ask pandas to try and match the old data to the new index. If data is unavailble for one of the new index dates or times, you must tell pandas how to fill it in. Otherwise, pandas will fill with NaN by default.

In this exercise, two time series data sets containing daily data have been pre-loaded for you, each indexed by dates. The first, ts1, includes weekends, but the second, ts2, does not. The goal is to combine the two data sets in a sensible way. Your job is to reindex the second data set so that it has weekends as well, and then add it to the first. When you are done, it would be informative to inspect your results.
Instructions

    Create a new time series ts3 by reindexing ts2 with the index of ts1. To do this, call .reindex() on ts2 and pass in the index of ts1 (ts1.index).
    Create another new time series, ts4, by calling the same .reindex() as above, but also specifiying a fill method, using the keyword argument method="ffill" to forward-fill values.
    Add ts1 + ts2. Assign the result to sum12.
    Add ts1 + ts3. Assign the result to sum13.
    Add ts1 + ts4, Assign the result to sum14.

"""
# Reindex without fill method: ts3
ts3 = ts2.reindex(ts1.index)

# Reindex with fill method, using forward fill: ts4
ts4 = ts2.reindex(ts1.index,method='ffill')

# Combine ts1 + ts2: sum12
sum12 = ts1 + ts2

# Combine ts1 + ts3: sum13
sum13 = ts1 + ts3

# Combine ts1 + ts4: sum14
sum14 = ts1 + ts4
""" results or consol output

"""





"""
Resampling and frequency
100xp

Pandas provides methods for resampling time series data. When downsampling or upsampling, the syntax is similar, but the methods called are different. Both use the concept of 'method chaining' - df.method1().method2().method3() - to direct the output from one method call to the input of the next, and so on, as a sequence of operations, one feeding into the next.

For example, if you have hourly data, and just need daily data, pandas will not guess how to throw out the 23 of 24 points. You must specify this in the method. One approach, for instance, could be to take the mean, as in df.resample('D').mean().

In this exercise, a data set containing hourly temperature data has been pre-loaded for you. Your job is to resample the data using a variety of aggregation methods to answer a few questions.
Instructions

    Downsample df['Temperature'] to 6 hour data using .resample('6h') and .mean(). Assign the result to df1.
    Downsample df['Temperature'] to daily data using .resample('D') and then count the number of data points in each day with .count(). Assign the result df2.

"""
# Downsample to 6 hour data and aggregate by mean: df1
df1 = df['Temperature'].resample('6h').mean()

# Downsample to daily data and count the number of data points: df2
df2 = df['Temperature'].resample('D').count()
""" results or consol output

"""



"""
Separating and resampling
100xp

With pandas, you can resample in different ways on different subsets of your data. For example, resampling different months of data with different aggregations. In this exercise, the data set containing hourly temperature data from the last exercise has been pre-loaded.

Your job is to resample the data using a variety of aggregation methods. The DataFrame is available in the workspace as df. You will be working with the 'Temperature' column.
Instructions

    Use partial string indexing to extract temperature data for August 2010 into august.
    Use the temperature data for August and downsample to find the daily maximum temperatures. Store the result in august_highs.
    Use partial string indexing to extract temperature data for February 2010 into february.
    Use the temperature data for February and downsample to find the daily minimum temperatures. Store the result in february_lows.

"""
# Extract temperature data for August: august
august = df['Temperature'].loc['2010-8']

# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('D').max()

# Extract temperature data for February: february
february = df['Temperature'].loc['2010-2']

# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('D').min()
""" results or consol output

"""




"""
Rolling mean and frequency
100xp

In this exercise, some hourly weather data is pre-loaded for you. You will continue to practice resampling, this time using rolling means.

Rolling means (or moving averages) are generally used to smooth out short-term fluctuations in time series data and highlight long-term trends. You can read more about them here.

To use the .rolling() method, you must always use method chaining, first calling .rolling() and then chaining an aggregation method after it. For example, with a Series hourly_data, hourly_data.rolling(window=24).mean() would compute new values for each hourly point, based on a 24-hour window stretching out behind each point. The frequency of the output data is the same: it is still hourly. Such an operation is useful for smoothing time series data.

Your job is to resample the data using the combination of .rolling() and .mean(). You will work with the same DataFrame df from the previous exercise.
Instructions

    Use partial string indexing to extract temperature data from August 1 2010 to August 15 2010. Assign to unsmoothed.
    Use .rolling() with a 24 hour window to smooth the mean temperature data. Assign the result to smoothed.
    Use a dictionary to create a new DataFrame august with the time series smoothed and unsmoothed as columns.
    Plot both the columns of august as line plots using the .plot() method.

"""
# Extract data from 2010-Aug-01 to 2010-Aug-15: unsmoothed
unsmoothed = df['Temperature']['2010-Aug-01':'2010-Aug-15']

# Apply a rolling mean with a 24 hour window: smoothed
smoothed = unsmoothed.rolling(window=24).mean()

# Create a new DataFrame with columns smoothed and unsmoothed: august
august = pd.DataFrame({'smoothed':smoothed, 'unsmoothed':unsmoothed})

# Plot both smoothed and unsmoothed data using august.plot().
august.plot()
plt.show()
""" results or consol output

"""





"""
Resample and roll with it
100xp

As of pandas version 0.18.0, the interface for applying rolling transformations to time series has become more consistent and flexible, and feels somewhat like a groupby (If you do not know what a groupby is, don't worry, you will learn about it in the next course!).

You can now more flexibly chain together both resampling as well as rolling operations. In this exercise, the same weather data from the previous exercises has been pre-loaded for you. Your job is to extract one month of data, resample to find the daily high temperatures, and then use a rolling and aggregation operation to smooth the data.
Instructions

    Use partial string indexing to extract August 2010 temperature data, and assign to august.
    Resample to daily frequency, saving the maximum daily temperatures, and assign the result to daily_highs.
    As part of one long method chain, repeat the above resampling (do not re-use daily_highs) and then combine it with .rolling() to apply a 7 day .mean() (with window=7 inside .rolling()) so as to smooth the daily highs. Assign the result to daily_highs_smoothed and print the result.

"""
# Extract the August 2010 data: august
august = df['Temperature']['2010-8']

# Resample to daily data, aggregating by max: daily_highs
daily_highs = august.resample('D').max()

# Use a rolling 7-day window with method chaining to smooth the daily high temperatures in August
daily_highs_smoothed = august.resample('D').max().rolling(window=7).mean()
print(daily_highs_smoothed)
""" results or consol output
<script.py> output:
    Date
    2010-08-01          NaN
    2010-08-02          NaN
    2010-08-03          NaN
    2010-08-04          NaN
    2010-08-05          NaN
    2010-08-06          NaN
    2010-08-07    95.114286
    2010-08-08    95.142857
    2010-08-09    95.171429
    2010-08-10    95.171429
    2010-08-11    95.157143
    2010-08-12    95.128571
    2010-08-13    95.100000
    2010-08-14    95.042857
    2010-08-15    94.971429
    2010-08-16    94.900000
    2010-08-17    94.857143
    2010-08-18    94.828571
    2010-08-19    94.814286
    2010-08-20    94.785714
    2010-08-21    94.757143
    2010-08-22    94.742857
    2010-08-23    94.714286
    2010-08-24    94.642857
    2010-08-25    94.542857
    2010-08-26    94.428571
    2010-08-27    94.271429
    2010-08-28    94.100000
    2010-08-29    93.914286
    2010-08-30    93.742857
    2010-08-31    93.571429
    Freq: D, Name: Temperature, dtype: float64
"""





"""
Method chaining and filtering
100xp

We've seen that pandas supports method chaining. This technique can be very powerful when cleaning and filtering data.

In this exercise, a DataFrame containing flight departure data for a single airline and a single airport for the month of July 2015 has been pre-loaded. Your job is to use .str() filtering and method chaining to generate summary statistics on flight delays each day to Dallas.
Instructions

    Use .str.strip() to strip extra whitespace from df.columns. Assign the result back to df.columns.
    In the 'Destination Airport' column, extract all entries where Dallas ('DAL') is the destination airport. Use .str.contains('DAL') for this and store the result in dallas.
    Resample dallas such that you get the total number of departures each day. Store the result in daily_departures.
    Generate summary statistics for daily Dallas departures using .describe(). Store the result in stats.

"""
# Strip extra whitespace from the column names: df.columns
df.columns = df.columns.str.strip()

# Extract data for which the destination airport is Dallas: dallas
dallas = df['Destination Airport'].str.contains('DAL')

# Compute the total number of Dallas departures each day: daily_departures
daily_departures = dallas.resample('D').sum()

# Generate the summary statistics for daily Dallas departures: stats
stats = daily_departures.describe()
print(daily_departures)
print('----------------------------')
print(stats)
""" results or consol output
<script.py> output:
    Date (MM/DD/YYYY)
    2015-07-01    10
    2015-07-02    10
    2015-07-03    11
    2015-07-04     3
    2015-07-05     9
    2015-07-06    10
    2015-07-07    10
    2015-07-08    10
    2015-07-09    10
    2015-07-10    11
    2015-07-11     5
    2015-07-12     9
    2015-07-13    10
    2015-07-14    10
    2015-07-15    10
    2015-07-16    10
    2015-07-17    11
    2015-07-18     5
    2015-07-19     9
    2015-07-20    10
    2015-07-21    10
    2015-07-22    10
    2015-07-23    10
    2015-07-24    11
    2015-07-25     5
    2015-07-26     9
    2015-07-27    10
    2015-07-28    10
    2015-07-29    10
    2015-07-30    10
    2015-07-31    11
    dtype: int64
    ----------------------------
    count    31.000000
    mean      9.322581
    std       1.989759
    min       3.000000
    25%       9.500000
    50%      10.000000
    75%      10.000000
    max      11.000000
    dtype: float64
"""




"""
Missing values and interpolation
100xp

One common application of interpolation in data analysis is to fill in missing data.

In this exercise, noisy measured data that has some dropped or otherwise missing values has been loaded. The goal is to compare two time series, and then look at summary statistics of the differences. The problem is that one of the data sets is missing data at some of the times. The pre-loaded data ts1 has value for all times, yet the data set ts2 does not: it is missing data for the weekends.

Your job is to first interpolate to fill in the data for all days. Then, compute the differences between the two data sets, now that they both have full support for all times. Finally, generate the summary statistics that describe the distribution of differences.
Instructions

    Replace the index of ts2 with that of ts1, and then fill in the missing values of ts2 by using .interpolate(how='linear'). Save the result as ts2_interp.
    Compute the difference between ts1 and ts2_interp. Take the absolute value of the difference with np.abs(), and assign the result to differences.
    Generate and print summary statistics of the differences with .describe() and print().

"""
# Reset the index of ts2 to ts1, and then use linear interpolation to fill in the NaNs: ts2_interp
ts2_interp = ts2.reindex(ts1.index).interpolate(how='linear')

# Compute the absolute difference of ts1 and ts2_interp: differences
differences = np.abs(ts1-ts2_interp)

# Generate and print summary statistics of the differences
print(differences.describe())
""" results or consol output
<script.py> output:
    count    17.000000
    mean      2.882353
    std       1.585267
    min       0.000000
    25%       2.000000
    50%       2.666667
    75%       4.000000
    max       6.000000
        dtype: float64
"""




"""
Time zones and conversion
100xp

Time zone handling with pandas typically assumes that you are handling the Index of the Series. In this exercise, you will learn how to handle timezones that are associated with datetimes in the column data, and not just the Index.

You will work with the flight departure dataset again, and this time you will select Los Angeles ('LAX') as the destination airport.
Instructions

    Create a Boolean mask, mask, such that if the 'Destination Airport' column of df equals 'LAX', the result is True, and otherwise, it is False.
    Use the mask to extract only the LAX rows. Assign the result to la.
    Concatenate the two columns la['Date (MM/DD/YYYY)'] and la['Wheels-off Time'] with a ' ' space in between. Pass this to pd.to_datetime() to create a datetime array of all the times the LAX-bound flights left the ground.
    Use the Series.dt.tz_localize() interface to localize the time to 'US/Central'.
    Use the .dt.tz_convert() method to convert datetimes from 'US/Central' to 'US/Pacific'.

"""
# Buid a Boolean mask to filter out all the 'LAX' departure flights: mask
mask = df['Destination Airport'] == 'LAX'

# Use the mask to subset the data: la
la = df[mask]

# Combine two columns of data to create a datetime series: times_tz_none
times_tz_none = pd.to_datetime(la['Date (MM/DD/YYYY)']+ ' ' +la['Wheels-off Time'])

# Localize the time to US/Central: times_tz_central
times_tz_central = times_tz_none.dt.tz_localize('US/Central')

# Convert the datetimes from US/Central to US/Pacific
times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')

print(times_tz_none.head())
print('------------------')
print(times_tz_central.head())
print('------------------')
""" results or consol output
<script.py> output:
    33    2015-07-01 05:43:00
    55    2015-07-01 16:27:00
    91    2015-07-02 05:47:00
    113   2015-07-02 16:23:00
    134   2015-07-03 05:30:00
    dtype: datetime64[ns]
    ------------------
    33    2015-07-01 05:43:00-05:00
    55    2015-07-01 16:27:00-05:00
    91    2015-07-02 05:47:00-05:00
    113   2015-07-02 16:23:00-05:00
    134   2015-07-03 05:30:00-05:00
    dtype: datetime64[ns, US/Central]
    ------------------
    33    2015-07-01 03:43:00-07:00
    55    2015-07-01 14:27:00-07:00
    91    2015-07-02 03:47:00-07:00
    113   2015-07-02 14:23:00-07:00
    134   2015-07-03 03:30:00-07:00
    dtype: datetime64[ns, US/Pacific]
"""





"""
Plotting time series, datetime indexing
100xp

Pandas handles datetimes not only in your data, but also in your plotting.

In this exercise, some time series data has been pre-loaded. However, we have not parsed the date-like columns nor set the index, as we have done for you in the past!

The plot displayed is how pandas renders data with the default integer/positional index. Your job is to convert the 'Date' column from a collection of strings into a collection of datetime objects. Then, you will use this converted 'Date' column as your new index, and re-plot the data, noting the improved datetime awareness. After you are done, you can cycle between the two plots you generated by clicking on the 'Previous Plot' and 'Next Plot' buttons.

Before proceeding, look at the plot shown and observe how pandas handles data with the default integer index. Then, inspect the DataFrame df using the .head() method in the IPython Shell to get a feel for its structure.
Instructions

    Use pd.to_datetime() to convert the 'Date' column to a collection of datetime objects, and assign back to df.Date.
    Set the index to this updated 'Date' column, using df.set_index() with the optional keyword argument inplace=True.
    Re-plot the DataFrame to see that the axis is now datetime aware. This code has been written for you.

"""
# Plot the raw data before setting the datetime index
df.plot()
plt.show()
print(df.head())
print('---------')
print(df.columns)
print('---------')
# Convert the 'Date' column into a collection of datetime objects: df.Date
df.Date = pd.to_datetime(df.Date, format='%Y-%m-%d %H:%M')
print(df.head())
print('---------')
print(df.columns)
print('---------')
# Set the index to be the converted 'Date' columndf.head()
df.set_index('Date',inplace=True)
print(df.head())
print('---------')
print(df.columns)
print('---------')
# Re-plot the DataFrame to see that the axis is now datetime aware!
df.plot()
plt.show()
print(df.head())
print('---------')
print(df.columns)
""" results or consol output
<script.py> output:
                         Temperature
    Date
    2010-01-01 00:00:00         46.2
    2010-01-01 01:00:00         44.6
    2010-01-01 02:00:00         44.1
    2010-01-01 03:00:00         43.8
    2010-01-01 04:00:00         43.5
    ---------
    Index(['Temperature'], dtype='object')

<script.py> output:
       Temperature            Date
    0         46.2  20100101 00:00
    1         44.6  20100101 01:00
    2         44.1  20100101 02:00
    3         43.8  20100101 03:00
    4         43.5  20100101 04:00
    ---------
    Index(['Temperature', 'Date'], dtype='object')
    ---------
       Temperature                Date
    0         46.2 2010-01-01 00:00:00
    1         44.6 2010-01-01 01:00:00
    2         44.1 2010-01-01 02:00:00
    3         43.8 2010-01-01 03:00:00
    4         43.5 2010-01-01 04:00:00
    ---------
    Index(['Temperature', 'Date'], dtype='object')
    ---------
                         Temperature
    Date
    2010-01-01 00:00:00         46.2
    2010-01-01 01:00:00         44.6
    2010-01-01 02:00:00         44.1
    2010-01-01 03:00:00         43.8
    2010-01-01 04:00:00         43.5
    ---------
    Index(['Temperature'], dtype='object')
    ---------
                         Temperature
    Date
    2010-01-01 00:00:00         46.2
    2010-01-01 01:00:00         44.6
    2010-01-01 02:00:00         44.1
    2010-01-01 03:00:00         43.8
    2010-01-01 04:00:00         43.5
    ---------
    Index(['Temperature'], dtype='object')
"""





"""
Plotting date ranges, partial indexing
100xp

Now that you have set the DatetimeIndex in your DataFrame, you have a much more powerful and flexible set of tools to use when plotting your time series data. Of these, one of the most convenient is partial string indexing and slicing. In this exercise, we've pre-loaded a full year of Austin 2010 weather data, with the index set to be the datetime parsed 'Date' column as shown in the previous exercise.

Your job is to use partial string indexing of the dates, in a variety of datetime string formats, to plot all the summer data and just one week of data together. After you are done, you can cycle between the two plots by clicking on the 'Previous Plot' and 'Next Plot' buttons.

First, remind yourself how to extract one month of temperature data using 'May 2010' as a key into df.Temperature[], and call head() to inspect the result: df.Temperature['May 2010'].head().
Instructions

    Plot the summer temperatures using method chaining. The summer ranges from the months '2010-Jun' to '2010-Aug'.
    Plot the temperatures for one week in June using the same method chaining, but this time indexing with '2010-06-10':'2010-06-17' before you follow up with .plot().

"""
# Plot the summer data
df.Temperature['2010-Jun':'2010-Aug'].plot()
plt.show()
plt.clf()

# Plot the one week data
df.Temperature['2010-06-10':'2010-06-17'].plot()
plt.show()
plt.clf()
