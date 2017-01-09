"""
Datacamp - Pandas Fundations
https://www.datacamp.com/courses/pandas-foundations
Part 4 : Case Study - Sunlight in Austin
Python 3.X
"""



"""
Working with real-world weather and climate data, in this chapter you will bring together and apply all of the skills you have acquired in this course.
You will use pandas to manipulate the data into a form usable for analysis, and then systematically explore it using the techniques you learned in the prior chapters. Enjoy!
"""



""" question answer : 1
What method should we use to read the data?
50xp

The first step in our analysis is to read in the data. Upon inspection with a certain system tool, we find that the data appears to be ASCII encoded with comma delimited columns, but has no header and no column labels. Which of the following is the best method to start with to read the data files?
Possible Answers

    pd.read_csv()
    1
    pd.to_csv()
    2
    pd.read_hdf()
    3
    np.load()
    4
"""





"""
Reading in a data file
100xp

Now that you have identified the method to use to read the data, let's try to read one file. The problem with real data such as this is that the files are almost never formatted in a convenient way. In this exercise, there are several problems to overcome in reading the file. First, there is no header, and thus the columns don't have labels. There is also no obvious index column, since none of the data columns contain a full date or time.

Your job is to read the file into a DataFrame using the default arguments. After inspecting it, you will re-read the file specifying that there are no headers supplied.

The file name has been provided for you as file_name.
Instructions

    Import pandas as pd.
    Read in the data file file_name with pd.read_csv() and assign it to df.
    Print the output of df.head(). This has been done for you. Notice the formatting problems in df.
    Re-read the data using specifying the keyword argument header=None and assign it to df_headers.
    Print the output of df_headers.head(). This has already been done for you. Hit 'Submit Answer' and see how this resolves the formatting issues.

"""
# Import pandas
import pandas as pd

# Read in the data file: df
df = pd.read_csv(file_name)

# Print the output of df.head()
print(df.head())

# Read in the data file with header=None: df_headers
df_headers = pd.read_csv(file_name, header=None)

# Print the output of df_headers.head()
print(df_headers.head())
""" results or consol output
<script.py> output:
       13904  20110101  0053  12  OVC045     10.00  .1  .2  .3 ...   .18  .19  \
    0  13904  20110101   153  12  OVC049     10.00             ...
    1  13904  20110101   253  12  OVC060     10.00             ...   030
    2  13904  20110101   353  12  OVC065     10.00             ...
    3  13904  20110101   453  12  BKN070     10.00             ...
    4  13904  20110101   553  12  BKN065     10.00             ...   015

       29.95  .20  AA  .21  .22  .23 29.95.1  .24
    0  30.01       AA                  30.02
    1  30.01       AA                  30.02
    2  30.03       AA                  30.04
    3  30.04       AA                  30.04
    4  30.06       AA                  30.06

    [5 rows x 44 columns]
          0         1    2   3       4  5      6  7  8  9  ...   34 35     36 37  \
    0  13904  20110101   53  12  OVC045     10.00          ...          29.95
    1  13904  20110101  153  12  OVC049     10.00          ...          30.01
    2  13904  20110101  253  12  OVC060     10.00          ...  030     30.01
    3  13904  20110101  353  12  OVC065     10.00          ...          30.03
    4  13904  20110101  453  12  BKN070     10.00          ...          30.04

       38 39 40 41     42 43
    0  AA           29.95
    1  AA           30.02
    2  AA           30.02
    3  AA           30.04
    4  AA           30.04

    [5 rows x 44 columns]
"""




"""
Re-assigning column names
100xp

After the initial step of reading in the data, the next step is to clean and tidy it so that it is easier to work with.

In this exercise, you will begin this cleaning process by re-assigning column names and dropping unnecessary columns.

pandas has been imported in the workspace as pd, and the file NOAA_QCLCD_2011_hourly_13904.txt has been parsed and loaded into a DataFrame df. The comma separated string of column names, column_labels, and list of columns to drop, list_to_drop, have also been loaded for you.
Instructions

    Convert the comma separated string column_labels to a list of strings using .split(','). Assign the result to column_labels_list.
    Reassign df.columns using the list of strings column_labels_list.
    Call df.drop() with list_to_drop and axis='columns'. Assign the result to df_dropped.
    Print df_dropped.head() to examine the result. This has already been done for you.

"""
# Split on the comma to create a list: column_labels_list
column_labels_list = column_labels.split(',')

# Assign the new column labels to the DataFrame: df.columns
df.columns = column_labels_list

# Remove the appropriate columns: df_dropped
df_dropped = df.drop(list_to_drop,axis='columns')

# Print the output of df_dropped.head()
print(df_dropped.head())
print('-------')
print(df_dropped.columns)
""" results or consol output
<script.py> output:
        Wban      date  Time  StationType sky_condition visibility dry_bulb_faren  \
    0  13904  20110101    53           12        OVC045      10.00             51
    1  13904  20110101   153           12        OVC049      10.00             51
    2  13904  20110101   253           12        OVC060      10.00             51
    3  13904  20110101   353           12        OVC065      10.00             50
    4  13904  20110101   453           12        BKN070      10.00             50

      dry_bulb_cel wet_bulb_faren wet_bulb_cel dew_point_faren dew_point_cel  \
    0         10.6             38          3.1              15          -9.4
    1         10.6             37          3.0              14         -10.0
    2         10.6             37          2.9              13         -10.6
    3         10.0             38          3.1              17          -8.3
    4         10.0             37          2.8              15          -9.4

      relative_humidity wind_speed wind_direction station_pressure  \
    0                24         15            360            29.42
    1                23         10            340            29.49
    2                22         15            010            29.49
    3                27          7            350            29.51
    4                25         11            020            29.51

      sea_level_pressure
    0              29.95
    1              30.01
    2              30.01
    3              30.03
    4              30.04
    -------
    Index(['Wban', 'date', 'Time', 'StationType', 'sky_condition', 'visibility',
           'dry_bulb_faren', 'dry_bulb_cel', 'wet_bulb_faren', 'wet_bulb_cel',
           'dew_point_faren', 'dew_point_cel', 'relative_humidity', 'wind_speed',
           'wind_direction', 'station_pressure', 'sea_level_pressure'],
          dtype='object')
"""




"""
Cleaning and tidying datetime data
100xp

In order to use the full power of pandas time series, you must construct a DatetimeIndex. To do so, it is necessary to clean and transform the date and time columns.

The DataFrame df_dropped you created in the last exercise is provided for you and pandas has been imported as pd.

Your job is to clean up the date and Time columns and combine them into a datetime collection to be used as the Index.
Instructions

    Convert the 'date' column to a string with .astype(str) and assign to df_dropped['date'].
    Add leading zeros to the 'Time' column. This has been done for you.
    Concatenate the new 'date' and 'Time' columns together. Assign to date_string.
    Convert the date_string Series to datetime values with pd.to_datetime(). Specify the format parameter.
    Set the index of the df_dropped DataFrame to to be date_times. Assign the result to df_clean.

"""
# Convert the date column to string: df_dropped['date']
df_dropped['date'] = df_dropped['date'].astype(str)

# Pad leading zeros to the Time column: df_dropped['Time']
df_dropped['Time'] = df_dropped['Time'].apply(lambda x:'{:0>4}'.format(x))

# Concatenate the new date and Time columns: date_string
date_string = df_dropped['date']+df_dropped['Time']

# Convert the date_string Series to datetime: date_times
date_times = pd.to_datetime(date_string, format='%Y%m%d%H%M')

# Set the index to be the new date_times container: df_clean
df_clean = df_dropped.set_index(date_times)

# Print the output of df_clean.head()
print(df_clean.head())
""" results or consol output
<script.py> output:
                          Wban      date  Time  StationType sky_condition  \
    2011-01-01 00:53:00  13904  20110101  0053           12        OVC045
    2011-01-01 01:53:00  13904  20110101  0153           12        OVC049
    2011-01-01 02:53:00  13904  20110101  0253           12        OVC060
    2011-01-01 03:53:00  13904  20110101  0353           12        OVC065
    2011-01-01 04:53:00  13904  20110101  0453           12        BKN070

                        visibility dry_bulb_faren dry_bulb_cel wet_bulb_faren  \
    2011-01-01 00:53:00      10.00             51         10.6             38
    2011-01-01 01:53:00      10.00             51         10.6             37
    2011-01-01 02:53:00      10.00             51         10.6             37
    2011-01-01 03:53:00      10.00             50         10.0             38
    2011-01-01 04:53:00      10.00             50         10.0             37

                        wet_bulb_cel dew_point_faren dew_point_cel  \
    2011-01-01 00:53:00          3.1              15          -9.4
    2011-01-01 01:53:00          3.0              14         -10.0
    2011-01-01 02:53:00          2.9              13         -10.6
    2011-01-01 03:53:00          3.1              17          -8.3
    2011-01-01 04:53:00          2.8              15          -9.4

                        relative_humidity wind_speed wind_direction  \
    2011-01-01 00:53:00                24         15            360
    2011-01-01 01:53:00                23         10            340
    2011-01-01 02:53:00                22         15            010
    2011-01-01 03:53:00                27          7            350
    2011-01-01 04:53:00                25         11            020

                        station_pressure sea_level_pressure
    2011-01-01 00:53:00            29.42              29.95
    2011-01-01 01:53:00            29.49              30.01
    2011-01-01 02:53:00            29.49              30.01
    2011-01-01 03:53:00            29.51              30.03
    2011-01-01 04:53:00            29.51              30.04

"""




"""
Cleaning the numeric columns
100xp

The numeric columns contain missing values labeled as 'M'. In this exercise, your job is to transform these columns such that they contain only numeric values and interpret missing data as NaN.

The pandas function pd.to_numeric() is ideal for this purpose: It converts a Series of values to floating-point values. Furthermore, by specifying the keyword argument errors='coerce', you can force strings like 'M' to be interpreted as NaN.

A DataFrame df_clean is provided for you at the start of the exercise, and as usual, pandas has been imported as pd.
Instructions

    Print the 'dry_bulb_faren' temperature between 8 AM and 9 AM on June 20, 2011.
    Convert the 'dry_bulb_faren' column to numeric values with pd.to_numeric(). Specify errors='coerce'.
    Print the transformed dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011.
    Convert the 'visibility' and 'dew_point_faren' columns to numeric values with pd.to_numeric(). Again, specify errors='coerce'.

"""
# Print the dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011
print(df_clean.loc['2011-6-20 8:00:00':'2011-6-20 9:00:00', 'dry_bulb_faren'])
print('---------------')
# Convert the dry_bulb_faren column to numeric values: df_clean['dry_bulb_faren']
df_clean['dry_bulb_faren'] = pd.to_numeric(df_clean['dry_bulb_faren'], errors='coerce')

# Print the transformed dry_bulb_faren temperature between 8 AM and 9 AM on June 20, 2011
print(df_clean.loc['2011-6-20 8:00:00':'2011-6-20 9:00:00', 'dry_bulb_faren'])

# Convert the wind_speed and dew_point_faren columns to numeric values
df_clean['wind_speed'] = pd.to_numeric(df_clean['wind_speed'], errors='coerce')
df_clean['dew_point_faren'] = pd.to_numeric(df_clean['dew_point_faren'], errors='coerce')
""" results or consol output
<script.py> output:
    2011-06-20 08:27:00     M
    2011-06-20 08:28:00     M
    2011-06-20 08:29:00     M
    2011-06-20 08:30:00     M
    2011-06-20 08:31:00     M
    2011-06-20 08:32:00     M
    2011-06-20 08:33:00     M
    2011-06-20 08:34:00     M
    2011-06-20 08:35:00     M
    2011-06-20 08:53:00    83
    Name: dry_bulb_faren, dtype: object
    ---------------
    2011-06-20 08:27:00     NaN
    2011-06-20 08:28:00     NaN
    2011-06-20 08:29:00     NaN
    2011-06-20 08:30:00     NaN
    2011-06-20 08:31:00     NaN
    2011-06-20 08:32:00     NaN
    2011-06-20 08:33:00     NaN
    2011-06-20 08:34:00     NaN
    2011-06-20 08:35:00     NaN
    2011-06-20 08:53:00    83.0
    Name: dry_bulb_faren, dtype: float64

"""




"""
Signal min, max, median
100xp

Now that you have the data read and cleaned, you can begin with statistical EDA. First, you will analyze the 2011 Austin weather data.

Your job in this exercise is to analyze the 'dry_bulb_faren' column and print the median temperatures for specific time ranges. You can do this using partial datetime string selection.

The cleaned dataframe is provided in the workspace as df_clean.
Instructions

    Select the 'dry_bulb_faren' column and print the output of .median().
    Use .loc[] to select the range '2011-Apr':'2011-Jun' from dry_bulb_faren' and print the output of .median().
    Use .loc[] to select the month '2011-Jan' from dry_bulb_faren' and print the output of .median().

"""
# Print the median of the dry_bulb_faren column
print(df_clean['dry_bulb_faren'].median())

# Print the median of the dry_bulb_faren column for the time range '2011-Apr':'2011-Jun'
print(df_clean.loc['2011-Apr':'2011-Jun', 'dry_bulb_faren'].median())

# Print the median of the dry_bulb_faren column for the month of January
print(df_clean.loc['2011-1':'2011-1', 'dry_bulb_faren'].median())
""" results or consol output
<script.py> output:
    72.0
    78.0
    48.0
"""





"""
Signal variance
100xp

You're now ready to compare the 2011 weather data with the 30-year normals reported in 2010. You can ask questions such as, on average, how much hotter was every day in 2011 than expected from the 30-year average?

The DataFrames df_clean and df_climate from previous exercises are available in the workspace.

Your job is to first resample df_clean and df_climate by day and aggregate the mean temperatures. You will then extract the temperature related columns from each - 'dry_bulb_faren' in df_clean, and 'Temperature' in df_climate - as NumPy arrays and compute the difference.

Notice that the indexes of df_clean and df_climate are not aligned - df_clean has dates in 2011, while df_climate has dates in 2010. This is why you extract the temperature columns as NumPy arrays. An alternative approach is to use the pandas .reset_index() method to make sure the Series align properly. You will practice this approach as well.
Instructions

    Downsample df_clean with daily frequency and aggregate by the mean. Store the result as daily_mean_2011.
    Extract the 'dry_bulb_faren' column from daily_mean_2011 as a NumPy array using .values. Store the result as daily_temp_2011.
    Downsample df_climate with daily frequency and aggregate by the mean. Store the result as daily_climate.
    Extract the 'Temperature' column from daily_climate using the .reset_index() method. To do this, first reset the index of daily_climate, and then use bracket slicing to access 'Temperature'. Store the result as daily_temp_climate.

"""
# Downsample df_clean by day and aggregate by mean: daily_mean_2011
daily_mean_2011 = df_clean.resample('D').mean()
print(daily_mean_2011.head())
print('---------------')

# Extract the dry_bulb_faren column from daily_mean_2011 using .values: daily_temp_2011
daily_temp_2011 = daily_mean_2011['dry_bulb_faren'].values
print(daily_temp_2011[0:5])
print('---------------')

# Downsample df_climate by day and aggregate by mean: daily_mean_2011
daily_climate = df_climate.resample('D').mean()
print(daily_climate.head())
print('---------------')

# Extract the Temperature column from daily_climate using .reset_index(): daily_temp_climate
daily_temp_climate = daily_climate['Temperature'].reset_index(drop=True)

# Compute the difference between the two arrays and print the mean difference
difference = daily_temp_2011 - daily_temp_climate
print(difference.mean())
""" results or consol output
<script.py> output:
                 Wban  StationType  dry_bulb_faren  dew_point_faren  wind_speed
    2011-01-01  13904           12       50.166667        20.500000   11.083333
    2011-01-02  13904           12       39.416667        19.708333    4.166667
    2011-01-03  13904           12       46.846154        35.500000    2.653846
    2011-01-04  13904           12       53.367347        50.408163    2.510204
    2011-01-05  13904           12       57.965517        40.068966    4.689655
    ---------------
    [ 50.16666667  39.41666667  46.84615385  53.36734694  57.96551724]
    ---------------
                Temperature   DewPoint  Pressure
    Date
    2010-01-01    49.337500  37.716667       1.0
    2010-01-02    49.795833  38.370833       1.0
    2010-01-03    49.900000  38.279167       1.0
    2010-01-04    49.729167  38.008333       1.0
    2010-01-05    49.841667  38.087500       1.0
    ---------------
    1.3301831870056482
"""




"""
Sunny or cloudy
100xp

On average, how much hotter is it when the sun is shining? In this exercise, you will compare temperatures on sunny days against temperatures on overcast days.

Your job is to use Boolean selection to filter out sunny and overcast days, and then compute the difference of the mean daily maximum temperatures between each type of day.

The DataFrame df_clean from previous exercises has been provided for you. The column 'sky_condition' provides information about whether the day was sunny ('CLR') or overcast ('OVC').
Instructions

    Use .loc[] to select sunny days and assign to sunny. If 'sky_condition' equals 'CLR', then the day is sunny.
    Use .loc[] to select overcast days and assign to overcast. If 'sky_condition' contains 'OVC', then the day is overcast.
    Resample sunny and overcast and aggregate by the maximum daily temperature. Assign to sunny_daily_max and overcast_daily_max.
    Print the difference between the mean of sunny_daily_max and overcast_daily_max. This has already been done for you, so click 'Submit Answer' to view the result!

"""
# Select days that are sunny: sunny
sunny = df_clean.loc[df_clean['sky_condition'].str.contains('CLR')]

# Select days that are overcast: overcast
overcast = df_clean.loc[df_clean['sky_condition'].str.contains('OVC')]

# Resample sunny and overcast, aggregating by maximum daily temperature
sunny_daily_max = sunny.resample('D').max()
overcast_daily_max = overcast.resample('D').max()

# Print the difference between the mean of sunny_daily_max and overcast_daily_max
print(sunny_daily_max.mean() - overcast_daily_max.mean())
""" results or consol output
<script.py> output:
    Wban               0.000000
    StationType        0.000000
    dry_bulb_faren     6.504304
    dew_point_faren   -4.339286
    wind_speed        -3.246062
    dtype: float64
"""




"""
Weekly average temperature and visibility
100xp

Is there a correlation between temperature and visibility? Let's find out.

In this exercise, your job is to plot the weekly average temperature and visibility as subplots. To do this, you need to first select the appropriate columns and then resample by week, aggregating the mean.

In addition to creating the subplots, you will compute the Pearson correlation coefficient using .corr(). The Pearson correlation coefficient, known also as Pearson's r, ranges from -1 (indicating total negative linear correlation) to 1 (indicating total positive linear correlation). A value close to 1 here would indicate that there is a strong correlation between temperature and visibility.

The DataFrame df_clean has been pre-loaded for you.
Instructions

    Import matplotlib.pyplot as plt.
    Select the 'visibility' and 'dry_bulb_faren' columns and resample them by week, aggregating the mean. Assign the result to weekly_mean.
    Print the output of weekly_mean.corr().
    Plot the weekly_mean dataframe with .plot(), specifying subplots=True.

"""
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Select the visibility and dry_bulb_faren columns and resample them: weekly_mean
weekly_mean = df_clean[['visibility','dry_bulb_faren']].resample('W').mean()

# Print the output of weekly_mean.corr()
print(weekly_mean.corr())

# Plot weekly_mean with subplots=True
weekly_mean.plot(subplots=True)
plt.show()
""" results or consol output
<script.py> output:
                    visibility  dry_bulb_faren
    visibility        1.000000        0.490328
    dry_bulb_faren    0.490328        1.000000
"""




"""
Daily hours of clear sky
100xp

In a previous exercise, you analyzed the 'sky_condition' column to explore the difference in temperature on sunny days compared to overcast days. Recall that a 'sky_condition' of 'CLR' represents a sunny day. In this exercise, you will explore sunny days in greater detail. Specifically, you will use a box plot to visualize the fraction of days that are sunny.

The 'sky_condition' column is recorded hourly. Your job is to resample this column appropriately such that you can extract the number of sunny hours in a day and the number of total hours. Then, you can divide the number of sunny hours by the number of total hours, and generate a box plot of the resulting fraction.

As before, df_clean is available for you in the workspace.
Instructions

    Create a Boolean Series for sunny days. Assign the result to sunny.
    Resample sunny by day and compute the sum. Assign the result to sunny_hours.
    Resample sunny by day and compute the count. Assign the result to total_hours.
    Divide sunny_hours by total_hours. Assign to sunny_fraction.
    Make a box plot of sunny_fraction.

"""
# Create a Boolean Series for sunny days: sunny
sunny = df_clean['sky_condition'] == 'CLR'

# Resample the Boolean Series by day and compute the sum: sunny_hours
sunny_hours = sunny.resample('D').sum()

# Resample the Boolean Series by day and compute the count: total_hours
total_hours = sunny.resample('D').count()

# Divide sunny_hours by total_hours: sunny_fraction
sunny_fraction = sunny_hours / total_hours

# Make a box plot of sunny_fraction
sunny_fraction.plot(kind='box')
plt.show()
""" results or consol output

"""




"""
Heat or humidity
100xp

Dew point is a measure of relative humidity based on pressure and temperature. A dew point above 65 is considered uncomfortable while a temperature above 90 is also considered uncomfortable.

In this exercise, you will explore the maximum temperature and dew point of each month. The columns of interest are 'dry_bulb_faren' and 'dew_point_faren'. After resampling them appropriately to get the maximum temperature and dew point in each month, generate a histogram of these values as subplots. Uncomfortably, you will notice that the maximum dew point is above 65 every month!

df_clean has been pre-loaded for you.
Instructions

    Select the 'dew_point_faren' and 'dry_bulb_faren' columns. Resample by month and aggregate the maximum monthly temperatures. Assign the result to monthly_max.
    Plot a histogram of the resampled data with bins=8, alpha=0.5, and subplots=True.

"""
# Resample dew_point_faren and dry_bulb_faren by Month, aggregating the maximum values: monthly_max
monthly_max = df_clean[['dew_point_faren','dry_bulb_faren']].resample('M').max()

# Generate a histogram with bins=8, alpha=0.5, subplots=True
monthly_max.plot(kind='hist',bins=8,alpha=0.5,subplots=True)

# Show the plot
plt.show()
""" results or consol output

"""




"""
Probability of high temperatures
100xp

We already know that 2011 was hotter than the climate normals for the previous thirty years. In this final exercise, you will compare the maximum temperature in August 2011 against that of the August 2010 climate normals. More specifically, you will use a CDF plot to determine the probability of the 2011 daily maximum temperature in August being above the 2010 climate normal value. To do this, you will leverage the data manipulation, filtering, resampling, and visualization skills you have acquired throughout this course.

The two DataFrames df_clean and df_climate are available in the workspace. Your job is to select the maximum temperature in August in df_climate, and then maximum daily temperatures in August 2011. You will then filter out the days in August 2011 that were above the August 2010 maximum, and use this to construct a CDF plot.

Once you've generated the CDF, notice how it shows that there was a 50% probability of the 2011 daily maximum temperature in August being 5 degrees above the 2010 climate normal value!
Instructions

    From df_climate, extract the maximum temperature observed in August 2010. The relevant column here is 'Temperature'. Store the result in august_max.
    From df_clean, select the August 2011 temperature data from the 'dry_bulb_faren'. Resample this data by day and aggregate the maximum value. Store the result in august_2011.
    Filter out days in august_2011 where the value exceeded august_max. Store the result in august_2011_high.
    Construct a CDF of august_2011_high using 25 bins.

"""
# Extract the maximum temperature in August 2010 from df_climate: august_max
august_max = df_climate.loc['2010-Aug','Temperature'].max()
print(august_max)

# Resample the August 2011 temperatures in df_clean by day and aggregate the maximum value: august_2011
august_2011 = df_clean.loc['2011-Aug','dry_bulb_faren'].resample('D').max()

# Filter out days in august_2011 where the value exceeded august_max: august_2011_high
august_2011_high = august_2011.loc[august_2011 > august_max]

# Construct a CDF of august_2011_high
august_2011_high.plot(kind='hist', normed=True, cumulative=True, bins=25)

# Display the plot
plt.show()
""" results or consol output
In [2]: august_2011
Out[2]:
2011-08-01    103.0
2011-08-02    103.0
2011-08-03    103.0
2011-08-04    104.0
2011-08-05    103.0
2011-08-06    102.0
2011-08-07    102.0
2011-08-08    103.0
2011-08-09    103.0
2011-08-10    102.0
2011-08-11    101.0
2011-08-12    100.0
2011-08-13     96.0
2011-08-14    101.0
2011-08-15    103.0
2011-08-16    102.0
2011-08-17    100.0
2011-08-18    104.0
2011-08-19    103.0
2011-08-20    104.0
2011-08-21    102.0
2011-08-22    103.0
2011-08-23    102.0
2011-08-24    102.0
2011-08-25     93.0
2011-08-26    101.0
2011-08-27    107.0
2011-08-28    110.0
2011-08-29    107.0
2011-08-30    103.0
2011-08-31    100.0
Freq: D, Name: dry_bulb_faren, dtype: float64

<script.py> output:
    95.3
"""
