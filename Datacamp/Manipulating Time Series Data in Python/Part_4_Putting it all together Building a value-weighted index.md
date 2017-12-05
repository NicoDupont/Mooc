12/2017  
# Datacamp - Manipulating Time Series Data in Python 
[Manipulating Time Series Data in Python](https://www.datacamp.com/courses/manipulating-time-series-data-in-python)
---

***Course Description***  

In this course you'll learn the basics of manipulating time series data. Time series data are data that are indexed by a sequence of dates or times. You'll learn how to use methods built into Pandas to work with this index. You'll also learn how resample time series to change the frequency. This course will also show you how to calculate rolling and cumulative values for times series. Finally, you'll use all your new skills to build a value-weighted stock index from actual stock data.         

# Part 4 : Putting it all together: Building a value-weighted index  

This chapter combines the previous concepts by teaching you how to create a value-weighted index. This index uses market-cap data contained in the stock exchange listings to calculate weights and 2016 stock price information. Index performance is then compared against benchmarks to evaluate the performance of the index you created.    

## Explore and clean company listing information     

To get started with the construction of a market-value based index, you'll work with the combined listing info for the three largest US stock exchanges, the NYSE, the NASDAQ and the AMEX.  

In this and the next exercise, you will calculate market-cap weights for these stocks.  

### Instructions

We have already imported pandas as pd, and loaded the listings data set with listings information from the NYSE, NASDAQ, and AMEX. The column `'Market Capitalization' is already measured in USD mn.

 - Inspect listings using .info().
 - Move the column 'Stock Symbol' into the index (inplace).
 - Drop all companies with missing 'Sector' information from listings.
 - Select companies with IPO Year before 2019.
 - Inspect the result of the changes you just made using .info().
 - Show the number of companies per 'Sector' using .groupby() and .size(). Sort the output in descending order.

```python
# Inspect listings
print(listings.info())
print('--------------')
print(listings.head())
print('--------------')

# Move 'stock symbol' into the index
listings.set_index('Stock Symbol',inplace=True)

# Drop rows with missing 'sector' data
listings.dropna(subset=['Sector'])

# Select companies with ipo year before 2019
listings = listings[listings['IPO Year'] < 2019]

# Inspect the new listings data
print(listings.info())

# Show the number of companies per sector
print(listings.groupby('Sector').size().sort_values(ascending=False))
```

### Results :  

![graph29](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph29.svg)	

		<script.py> output:
			<class 'pandas.core.frame.DataFrame'>
			RangeIndex: 6674 entries, 0 to 6673
			Data columns (total 8 columns):
			Exchange                 6674 non-null object
			Stock Symbol             6674 non-null object
			Company Name             6674 non-null object
			Last Sale                6590 non-null float64
			Market Capitalization    6674 non-null float64
			IPO Year                 2852 non-null float64
			Sector                   5182 non-null object
			Industry                 5182 non-null object
			dtypes: float64(3), object(5)
			memory usage: 417.2+ KB
			None
			--------------
			  Exchange Stock Symbol           Company Name  Last Sale  \
			0   nasdaq         AAPL             Apple Inc.     141.05   
			1   nasdaq        GOOGL          Alphabet Inc.     840.18   
			2   nasdaq         GOOG          Alphabet Inc.     823.56   
			3   nasdaq         MSFT  Microsoft Corporation      64.95   
			4   nasdaq         AMZN       Amazon.com, Inc.     884.67   
			
			   Market Capitalization  IPO Year             Sector  \
			0          740024.467000    1980.0         Technology   
			1          580917.530339       NaN         Technology   
			2          569426.124504    2004.0         Technology   
			3          501903.061809    1986.0         Technology   
			4          422138.530626    1997.0  Consumer Services   
			
													  Industry  
			0                           Computer Manufacturing  
			1  Computer Software: Programming, Data Processing  
			2  Computer Software: Programming, Data Processing  
			3          Computer Software: Prepackaged Software  
			4                   Catalog/Specialty Distribution  
			--------------
			<class 'pandas.core.frame.DataFrame'>
			Index: 2852 entries, AAPL to ZTO
			Data columns (total 7 columns):
			Exchange                 2852 non-null object
			Company Name             2852 non-null object
			Last Sale                2849 non-null float64
			Market Capitalization    2852 non-null float64
			IPO Year                 2852 non-null float64
			Sector                   2349 non-null object
			Industry                 2349 non-null object
			dtypes: float64(3), object(4)
			memory usage: 178.2+ KB
			None
			Sector
			Health Care              445
			Consumer Services        402
			Technology               386
			Finance                  351
			Energy                   144
			Capital Goods            143
			Public Utilities         104
			Basic Industries         104
			Consumer Non-Durables     89
			Miscellaneous             68
			Transportation            58
			Consumer Durables         55
			dtype: int64

---


## Select and inspect index components   

Now that you have imported and cleaned the listings data, you can proceed to select the index components as the largest company for each sector by market capitalization.  

You'll also have the opportunity to take a closer look at the components, their last market value, and last price.  

### Instructions

We have already imported pandas as pd, and loaded the listings data with the modifications you made during the last exercise.

 - Use .groupby() and .nlargest() to select the largest company by 'Market Capitalization' for each 'Sector', and assign the result to components.
 - Print components, sorted in descending order by market cap.
 - Select Stock Symbol from the index of components, assign it to tickers and print the result.
 - Use .loc[] with tickers and the columns Company Name, Market Capitalization, and Last Sale, (store these in info_cols) to print() more details about the listings sorted in descending order by Market Capitalization).

```python
# Select largest company for each sector
components = listings.groupby(['Sector'])['Market Capitalization'].nlargest(1)

# Print components, sorted by market cap
print(components.sort_values(ascending=False))

# Select stock symbols and print the result
tickers = components.index.get_level_values('Stock Symbol')
print(tickers)

# Print company name, market cap, and last price for each component 
info_cols = ['Company Name', 'Market Capitalization', 'Last Sale']
print(listings.loc[tickers, info_cols].sort_values('Market Capitalization', ascending=False))
```

### Results :  

		<script.py> output:
			Sector                 Stock Symbol
			Technology             AAPL           740,024.47
			Consumer Services      AMZN           422,138.53
			Miscellaneous          MA             123,330.09
			Health Care            AMGN           118,927.21
			Transportation         UPS             90,180.89
			Finance                GS              88,840.59
			Basic Industries       RIO             70,431.48
			Public Utilities       TEF             54,609.81
			Consumer Non-Durables  EL              31,122.51
			Capital Goods          ILMN            25,409.38
			Energy                 PAA             22,223.00
			Consumer Durables      CPRT            13,620.92
			Name: Market Capitalization, dtype: float64
			Index(['RIO', 'ILMN', 'CPRT', 'EL', 'AMZN', 'PAA', 'GS', 'AMGN', 'MA', 'TEF',
				   'AAPL', 'UPS'],
				  dtype='object', name='Stock Symbol')
												Company Name  Market Capitalization  \
			Stock Symbol                                                              
			AAPL                                  Apple Inc.             740,024.47   
			AMZN                            Amazon.com, Inc.             422,138.53   
			MA                       Mastercard Incorporated             123,330.09   
			AMGN                                  Amgen Inc.             118,927.21   
			UPS                  United Parcel Service, Inc.              90,180.89   
			GS               Goldman Sachs Group, Inc. (The)              88,840.59   
			RIO                                Rio Tinto Plc              70,431.48   
			TEF                                Telefonica SA              54,609.81   
			EL            Estee Lauder Companies, Inc. (The)              31,122.51   
			ILMN                              Illumina, Inc.              25,409.38   
			PAA           Plains All American Pipeline, L.P.              22,223.00   
			CPRT                                Copart, Inc.              13,620.92   
			
						  Last Sale  
			Stock Symbol             
			AAPL             141.05  
			AMZN             884.67  
			MA               111.22  
			AMGN             161.61  
			UPS              103.74  
			GS               223.32  
			RIO               38.94  
			TEF               10.84  
			EL                84.94  
			ILMN             173.68  
			PAA               30.72  
			CPRT              29.65

---


## Import index component price information   

Now you'll use the stock symbols for the companies you selected in the last exercise to calculate returns for each company.  

### Instructions

We have already imported pandas as pd and matplotlib.pyplot as plt for you. We have also made the variable tickers available to you, which contains the Stock Symbol for each index component as a list.

 - Print tickers to verify the content matches your result from the last exercise.
 - Use pd.read_csv() to import 'stock_prices.csv', parsing the 'Date' column and also setting the 'Date' column as index before assigning the result to stock_prices. Inspect the result using .info().
 - Calculate the price return for the index components by dividing the last row of stock_prices by the first, subtracting 1 and multiplying by 100. Assign the result to price_return.
 - Plot a horizontal bar chart of the sorted returns with the title Stock Price Returns.

```python
# Print tickers
print(tickers)
print('-------------------')

# Import prices and inspect result
stock_prices = pd.read_csv('stock_prices.csv',parse_dates=['Date'],index_col='Date')
print(stock_prices.info())
print('-------------------')
print(stock_prices.head())
print('-------------------')

# Calculate the returns    
price_return = stock_prices.iloc[-1].div(stock_prices.iloc[0]).sub(1).mul(100)

print(price_return.head())
print('-------------------')

# Plot horizontal bar chart of sorted price_return   
price_return.sort_values().plot(kind='barh',title='Stock Price Returns')
plt.show()
```

### Results :  

			<script.py> output:
				['RIO', 'ILMN', 'CPRT', 'EL', 'AMZN', 'PAA', 'GS', 'AMGN', 'MA', 'TEF', 'AAPL', 'UPS']
				-------------------
				<class 'pandas.core.frame.DataFrame'>
				DatetimeIndex: 1762 entries, 2010-01-04 to 2016-12-30
				Data columns (total 12 columns):
				AAPL    1761 non-null float64
				AMGN    1761 non-null float64
				AMZN    1761 non-null float64
				CPRT    1761 non-null float64
				EL      1762 non-null float64
				GS      1762 non-null float64
				ILMN    1761 non-null float64
				MA      1762 non-null float64
				PAA     1762 non-null float64
				RIO     1762 non-null float64
				TEF     1762 non-null float64
				UPS     1762 non-null float64
				dtypes: float64(12)
				memory usage: 179.0 KB
				None
				-------------------
							 AAPL   AMGN    AMZN  CPRT     EL      GS   ILMN     MA    PAA  \
				Date                                                                         
				2010-01-04  30.57  57.72  133.90  4.55  24.27  173.08  30.55  25.68  27.00   
				2010-01-05  30.63  57.22  134.69  4.55  24.18  176.14  30.35  25.61  27.30   
				2010-01-06  30.14  56.79  132.25  4.53  24.25  174.26  32.22  25.56  27.29   
				2010-01-07  30.08  56.27  130.00  4.50  24.56  177.67  32.77  25.39  26.96   
				2010-01-08  30.28  56.77  133.52  4.52  24.66  174.31  33.15  25.40  27.05   
				
							  RIO    TEF    UPS  
				Date                             
				2010-01-04  56.03  28.55  58.18  
				2010-01-05  56.90  28.53  58.28  
				2010-01-06  58.64  28.23  57.85  
				2010-01-07  58.65  27.75  57.41  
				2010-01-08  59.30  27.57  60.17  
				-------------------
				AAPL    278.868171
				AMGN    153.309078
				AMZN    460.022405
				CPRT    204.395604
				EL      215.162752
				dtype: float64
				-------------------

---


## Calculate number of shares outstanding  

The next step towards building a value-weighted index is to calculate the number of shares for each index component.  

The number of shares will allow you to calculate the total market capitalization for each component given the historical price series in the next exercise.  

### Instructions

We have already imported pandas as pd, tickers and listings as in the previous exercises.

 - Inspect listings and print tickers.
 - Use .loc[] with the list of tickers to select the index components and the columns 'Market Capitalization' and 'Last Sale'; assign this to components.
 - Print the first five rows of components.
 - Create a new column 'Number of Shares' by dividing Market Capitalization by 'Last Sale'.
 - Print no_shares in descending order.

```python
# Inspect listings and print tickers
print(listings.info())
print(listings.head())
print('--------------')
print(tickers)
print('--------------')

# Select components and relevant columns from listings
components = listings.loc[tickers,['Market Capitalization','Last Sale']]

# Print the first rows of components
print(components.head())
print('--------------')

# Calculate the number of shares here
no_shares = components['Market Capitalization'].div(components['Last Sale'])

# Print the sorted no_shares
print(no_shares.sort_values(ascending=False))
```

### Results :  

	<script.py> output:
	    <class 'pandas.core.frame.DataFrame'>
	    Index: 1015 entries, ACU to YPF
	    Data columns (total 7 columns):
	    Exchange                 1015 non-null object
	    Company Name             1015 non-null object
	    Last Sale                1015 non-null float64
	    Market Capitalization    1015 non-null float64
	    IPO Year                 1015 non-null float64
	    Sector                   1015 non-null object
	    Industry                 1015 non-null object
	    dtypes: float64(3), object(4)
	    memory usage: 63.4+ KB
	    None
		         Exchange                  Company Name  Last Sale  \
	    Stock Symbol                                                     
	    ACU              amex      Acme United Corporation.      27.39   
	    ROX              amex           Castle Brands, Inc.       1.46   
	    CQP              amex  Cheniere Energy Partners, LP      32.70   
	    CIX              amex      CompX International Inc.      14.35   
	    GSAT             amex              Globalstar, Inc.       1.73   
	    
		          Market Capitalization  IPO Year                 Sector  \
	    Stock Symbol                                                           
	    ACU                       91.138992    1988.0          Capital Goods   
	    ROX                      237.644444    2006.0  Consumer Non-Durables   
	    CQP                    11046.922888    2007.0       Public Utilities   
	    CIX                      178.214185    1998.0          Capital Goods   
	    GSAT                    1931.550661    2006.0      Consumer Services   
	    
		                                     Industry  
	    Stock Symbol                                       
	    ACU               Industrial Machinery/Components  
	    ROX           Beverages (Production/Distribution)  
	    CQP                          Oil/Gas Transmission  
	    CIX               Industrial Machinery/Components  
	    GSAT                 Telecommunications Equipment  
	    --------------
	    ['RIO', 'ILMN', 'CPRT', 'EL', 'AMZN', 'PAA', 'GS', 'AMGN', 'MA', 'TEF', 'AAPL', 'UPS']
	    --------------
		          Market Capitalization  Last Sale
	    Stock Symbol                                  
	    RIO                    70431.476895      38.94
	    ILMN                   25409.384000     173.68
	    CPRT                   13620.922869      29.65
	    EL                     31122.510011      84.94
	    AMZN                  422138.530626     884.67
	    --------------
	    Stock Symbol
	    AAPL    5246.540000
	    TEF     5037.804990
	    RIO     1808.717948
	    MA      1108.884100
	    UPS      869.297154
	    AMGN     735.890171
	    PAA      723.404994
	    AMZN     477.170618
	    CPRT     459.390316
	    GS       397.817439
	    EL       366.405816
	    ILMN     146.300000
	    dtype: float64

---


## Create time series of market value   

You can now use the number of shares to calculate the total market capitalization for each component and trading date from the historical price series.  

The result will be the key input to construct the value-weighted stock index, which you will complete in the next exercise.  

### Instructions

We have already imported pandas as pd and matplotlib.pyplot as plt for you. We have also created the variables components and stock_prices that you worked with in the last exercises.

 - Select the 'Number of Shares' from components, assign to no_shares, and print the sorted result.
 - Multiply stock_prices by no_shares to create a time series of market cap per ticker, and assign it to market_cap.
 - Select the first and the last row of market_cap and assign these to first_value and last_value.
 - Use pd.concat() to concatenate first_value and last_value along axis=1 and plot the result as horizontal bar chart.

```python
# Select the number of shares
no_shares = components['Number of Shares']
print(no_shares.sort_values())

# Create the series of market cap per ticker
market_cap = stock_prices.mul(no_shares)

# Select first and last market cap here
first_value = market_cap.first('D')
last_value = market_cap.last('D')


# Concatenate and plot first and last market cap here
pd.concat([first_value,last_value],axis=1).plot(kind='barh')
plt.show()

```

### Results :  

![graph30](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph30.svg)	

---


## What is a network?   

By now you have all ingredients that you need to calculate the aggregate stock performance for your group of companies.

Use the time series of market capitalization that you created in the last exercise to aggregate the market value for each period, and then normalize this series to convert it to an index.

### Instructions

We have already imported pandas as pd and matplotlib.pyplot as plt for you. We have also loaded components and market_cap_series, which you worked with in the last exercise.

 - Aggregate the market cap per trading day by applying .sum() to market_cap_series with axis=1, assign to raw_index and print the result.
 - Normalize the aggregate market cap by dividing by the first value of raw_index and multiplying by 100. Assign this to index and print the result.
 - Plot the index with the title 'Market-Cap Weighted Index'.

```python
# Aggregate and print the market cap per trading day
raw_index = market_cap_series.sum(axis=1)
print(raw_index)

# Normalize the aggregate market cap here 
index = raw_index.div(raw_index.iloc[0]).mul(100)
print(index)

# Plot the index here
index.plot(title='Market-Cap Weighted Index')
plt.show()
```

### Results :  

![graph31](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph31.svg)	

	<script.py> output:
	    Date
	    2010-01-04    6.948176e+05
	    2010-01-05    6.979957e+05
	    2010-01-06    6.946857e+05
	    2010-01-07    6.912416e+05
	    2010-01-08    6.958476e+05
	    2010-01-11    6.900534e+05
	    2010-01-12    6.804604e+05
	    2010-01-13    6.891775e+05
	    2010-01-14    6.886516e+05
	    2010-01-15    6.803840e+05
	    2010-01-19    6.950413e+05
	    2010-01-20    6.808697e+05
	    2010-01-21    6.639949e+05
	    2010-01-22    6.444539e+05
	    2010-01-25    6.500961e+05
	    2010-01-26    6.484830e+05
	    2010-01-27    6.531749e+05
	    2010-01-28    6.403780e+05
	    2010-01-29    6.280382e+05
	    2010-02-01    6.370596e+05
	    2010-02-02    6.433044e+05
	    2010-02-03    6.418327e+05
	    2010-02-04    6.147855e+05
	    2010-02-05    6.182118e+05
	    2010-02-08    6.132701e+05
	    2010-02-09    6.251142e+05
	    2010-02-10    6.233165e+05
	    2010-02-11    6.297971e+05
	    2010-02-12    6.276746e+05
	    2010-02-16    6.390117e+05
		              ...     
	    2016-11-17    1.532619e+06
	    2016-11-18    1.531333e+06
	    2016-11-21    1.555436e+06
	    2016-11-22    1.559177e+06
	    2016-11-23    1.554286e+06
	    2016-11-25    1.558921e+06
	    2016-11-28    1.546420e+06
	    2016-11-29    1.544427e+06
	    2016-11-30    1.533752e+06
	    2016-12-01    1.523518e+06
	    2016-12-02    1.525650e+06
	    2016-12-05    1.537861e+06
	    2016-12-06    1.544385e+06
	    2016-12-07    1.561619e+06
	    2016-12-08    1.570176e+06
	    2016-12-09    1.581568e+06
	    2016-12-12    1.573771e+06
	    2016-12-13    1.593656e+06
	    2016-12-14    1.586068e+06
	    2016-12-15    1.589219e+06
	    2016-12-16    1.583155e+06
	    2016-12-19    1.589038e+06
	    2016-12-20    1.598892e+06
	    2016-12-21    1.595957e+06
	    2016-12-22    1.588010e+06
	    2016-12-23    1.588874e+06
	    2016-12-27    1.599280e+06
	    2016-12-28    1.593635e+06
	    2016-12-29    1.589422e+06
	    2016-12-30    1.574862e+06
	    dtype: float64
	    Date
	    2010-01-04    100.000000
	    2010-01-05    100.457394
	    2010-01-06     99.981005
	    2010-01-07     99.485328
	    2010-01-08    100.148231
	    2010-01-11     99.314312
	    2010-01-12     97.933674
	    2010-01-13     99.188260
	    2010-01-14     99.112560
	    2010-01-15     97.922676
	    2010-01-19    100.032195
	    2010-01-20     97.992574
	    2010-01-21     95.563903
	    2010-01-22     92.751512
	    2010-01-25     93.563557
	    2010-01-26     93.331393
	    2010-01-27     94.006661
	    2010-01-28     92.164906
	    2010-01-29     90.388923
	    2010-02-01     91.687303
	    2010-02-02     92.586084
	    2010-02-03     92.374271
	    2010-02-04     88.481564
	    2010-02-05     88.974681
	    2010-02-08     88.263454
	    2010-02-09     89.968095
	    2010-02-10     89.709363
	    2010-02-11     90.642074
	    2010-02-12     90.336595
	    2010-02-16     91.968254
		             ...    
	    2016-11-17    220.578541
	    2016-11-18    220.393503
	    2016-11-21    223.862427
	    2016-11-22    224.400891
	    2016-11-23    223.697023
	    2016-11-25    224.364017
	    2016-11-28    222.564865
	    2016-11-29    222.278065
	    2016-11-30    220.741687
	    2016-12-01    219.268716
	    2016-12-02    219.575595
	    2016-12-05    221.333049
	    2016-12-06    222.271924
	    2016-12-07    224.752373
	    2016-12-08    225.983842
	    2016-12-09    227.623470
	    2016-12-12    226.501355
	    2016-12-13    229.363186
	    2016-12-14    228.271048
	    2016-12-15    228.724629
	    2016-12-16    227.851940
	    2016-12-19    228.698597
	    2016-12-20    230.116769
	    2016-12-21    229.694351
	    2016-12-22    228.550649
	    2016-12-23    228.675001
	    2016-12-27    230.172669
	    2016-12-28    229.360223
	    2016-12-29    228.753821
	    2016-12-30    226.658267
	    dtype: float64

---



## Calculate the contribution of each stock to the index  

You have successfully built the value-weighted index. Let's now explore how it performed over the 2010-2016 period.  

Let's also determine how much each stock has contributed to the index return.  

### Instructions

We have already imported pandas as pd and matplotlib.pyplot as plt for you. We have also loaded components and the index you worked with in the last exercise.

 - Divide the last index value by the first, subtract 1 and multiply by 100. Assign the result to index_return and print it.
 - Select the 'Market Capitalization' column from components.
 - Calculate the total market cap for all components and assign this to total_market_cap.
 - Divide the components' market cap by total_market_cap to calculate the component weights, assign it to weights, and print the result.
 - Multiply weights by the index_return to calculate the contribution by component and plot the result as a horizontal bar chart.

```python
# Calculate and print the index return here
index_return = (index.iloc[-1] / index.iloc[0] - 1) * 100
print(index_return)

# Select the market capitalization
market_cap = components['Market Capitalization']

# Calculate the total market cap
total_market_cap = market_cap.sum()

# Calculate the component weights, and print the result
weights = market_cap.div(total_market_cap)
print(weights.sort_values())

# Calculate and plot the contribution by component
weights.mul(index_return).sort_values().plot(kind='barh')
plt.show()
```

### Results :  

Fantastic job! The next step is to take a look at how your index stacks up against a benchmark!  

![graph32](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph32.svg)	

	<script.py> output:
	    126.6582666
	    Stock Symbol
	    CPRT    0.007564
	    PAA     0.012340
	    ILMN    0.014110
	    EL      0.017282
	    TEF     0.030324
	    RIO     0.039110
	    GS      0.049332
	    UPS     0.050077
	    AMGN    0.066039
	    MA      0.068484
	    AMZN    0.234410
	    AAPL    0.410929
	    Name: Market Capitalization, dtype: float64

---


## Compare index performance against benchmark I  

The next step in analyzing the performance of your index is to compare it against a benchmark.  

In the video, we used the S&P 500 as benchmark. You can also use the Dow Jones Industrial Average, which contains the 30 largest stocks, and would also be a reasonable benchmark for the largest stocks from all sectors across the three exchanges.  

### Instructions

We have already imported pandas as pd, matplotlib.pyplot as plt for you. We have also loaded your index and the DJIA data into variables index and djia, respectively, both as a pd.Series().

 - Convert index to a pd.DataFrame with the column name 'Index' and assign the result to data.
 - Normalize djia to start at 100 and add it as new column to data.
 - Show the total return for both index and djia by dividing the last row of data by the first, subtracting 1 and multiplying by 100.
 - Show a plot of both of the series in data.

```python
# Convert index series to dataframe here
data = index.to_frame('Index')

# Normalize djia series and add as new column to data
djia = djia.div(djia.iloc[0]).mul(100)
data['DJIA'] = djia

# Show total return for both index and djia
print((data.iloc[-1] / data.iloc[0] - 1) * 100)

# Plot both series
data.plot()
plt.show()
```

### Results :  

![graph33](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph33.svg)	

Awesome! How do they compare?

	<script.py> output:
	    Index    126.658267
	    DJIA      86.722172
	    dtype: float64

---


## Compare index performance against benchmark II   

The next step in analyzing the performance of your index is to compare it against a benchmark.  

In the video, we have use the S&P 500 as benchmark. You can also use the Dow Jones Industrial Average, which contains the 30 largest stocks, and would also be a reasonable benchmark for the largest stocks from all sectors across the three exchanges.  

### Instructions

We have already imported numpy as np, pandas as pd, matplotlib.pyplot as plt for you. We have also loaded your Index and the Dow Jones Industrial Average (normalized) in a variable called data.

 - Inspect data and print the first five rows.
 - Define a function multi_period_return that takes a numpy array of period returns as input, and returns the total return for the period. Use the formula from the video - add 1 to the input, pass the result to np.prod(), subtract 1 and multiply by 100.
 - Create a .rolling() window of length '360D' from data, and apply multi_period_return. Assign to rolling_return_360.
 - Plot rolling_return_360 using the title 'Rolling 360D Return'.

```python
# Inspect data
print(data.info())
print(data.head())
print('-----------------')

# Create multi_period_return function here
def multi_period_return(r):
    return (np.prod(r + 1) - 1) * 100

# Calculate rolling_return_360
rolling_return_360 = data.pct_change().rolling('360D').apply(multi_period_return)

# Plot rolling_return_360 here
rolling_return_360.plot(title='Rolling 360D Return')
plt.show()
```

### Results :  

Great job! How do the returns of your index compare to the Dow Jones?  

![graph34](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph34.svg)	

	<script.py> output:
	    <class 'pandas.core.frame.DataFrame'>
	    DatetimeIndex: 1761 entries, 2010-01-04 to 2016-12-30
	    Data columns (total 2 columns):
	    Index    1761 non-null float64
	    DJIA     1761 non-null float64
	    dtypes: float64(2)
	    memory usage: 41.3 KB
	    None
		             Index        DJIA
	    Date                              
	    2010-01-04  100.000000  100.000000
	    2010-01-05  100.457394   99.887188
	    2010-01-06   99.981005   99.902872
	    2010-01-07   99.485328  100.216365
	    2010-01-08  100.148231  100.323414
	    -----------------

---



## Visualize your index constituent correlations  

To better understand the characteristics of your index constituents, you can calculate the return correlations.  

Use the daily stock prices or your index companies, and show a heatmap of the daily return correlations!  

### Instructions

We have already imported pandas as pd, matplotlib.pyplot as plt, and seaborn as sns. We have also loaded the historical price series of your index constituents into the variable stock_prices.

 - Inspect stock_prices using .info().
 - Calculate the daily returns for stock_prices and assign the result to returns.
 - Calculate the pairwise correlations for returns, assign them to correlations and print the result.
 - Plot a seaborn annotated heatmap of the daily return correlations with the title 'Daily Return Correlations'.

```python

```

### Results :  

![graph35](https://github.com/NicoDupont/Mooc/blob/master/Datacamp/Manipulating%20Time%20Series%20Data%20in%20Python/img/graph35.svg)	

	<script.py> output:
	    <class 'pandas.core.frame.DataFrame'>
	    DatetimeIndex: 1762 entries, 2010-01-04 to 2016-12-30
	    Data columns (total 12 columns):
	    AAPL    1761 non-null float64
	    AMGN    1761 non-null float64
	    AMZN    1761 non-null float64
	    CPRT    1761 non-null float64
	    EL      1762 non-null float64
	    GS      1762 non-null float64
	    ILMN    1761 non-null float64
	    MA      1762 non-null float64
	    PAA     1762 non-null float64
	    RIO     1762 non-null float64
	    TEF     1762 non-null float64
	    UPS     1762 non-null float64
	    dtypes: float64(12)
	    memory usage: 179.0 KB
	    None
		  AAPL  AMGN  AMZN  CPRT   EL   GS  ILMN   MA  PAA  RIO  TEF  UPS
	    AAPL  1.00  0.29  0.33  0.35 0.31 0.34  0.26 0.39 0.21 0.36 0.33 0.37
	    AMGN  0.29  1.00  0.32  0.36 0.35 0.39  0.34 0.40 0.23 0.31 0.37 0.43
	    AMZN  0.33  0.32  1.00  0.30 0.33 0.33  0.24 0.43 0.18 0.33 0.33 0.38
	    CPRT  0.35  0.36  0.30  1.00 0.37 0.42  0.27 0.40 0.22 0.39 0.38 0.46
	    EL    0.31  0.35  0.33  0.37 1.00 0.36  0.21 0.43 0.21 0.42 0.43 0.46
	    GS    0.34  0.39  0.33  0.42 0.36 1.00  0.27 0.47 0.27 0.53 0.50 0.51
	    ILMN  0.26  0.34  0.24  0.27 0.21 0.27  1.00 0.30 0.16 0.23 0.23 0.27
	    MA    0.39  0.40  0.43  0.40 0.43 0.47  0.30 1.00 0.24 0.44 0.45 0.49
	    PAA   0.21  0.23  0.18  0.22 0.21 0.27  0.16 0.24 1.00 0.34 0.25 0.22
	    RIO   0.36  0.31  0.33  0.39 0.42 0.53  0.23 0.44 0.34 1.00 0.56 0.51
	    TEF   0.33  0.37  0.33  0.38 0.43 0.50  0.23 0.45 0.25 0.56 1.00 0.52
	    UPS   0.37  0.43  0.38  0.46 0.46 0.51  0.27 0.49 0.22 0.51 0.52 1.00

---


## What is a network?   

Now that you have completed your analysis, you may want to save all results into a single Excel workbook.  

Let's practice exporting various DataFrame to multiple Excel worksheets.  

### Instructions

We have already imported pandas as pd for you. We have also loaded both the historical price series of your index constituents into the variable stock_prices, and the index as index.

 - Inspect both index and stock_prices using .info().
 - Use .join() to combine index with stock_prices, and assign to data.
 - Apply .pct_change() to data and assign to returns.
 - Create pd.ExcelWriter and use with to export data and returns to excel with sheet_names of the same name.

```python
# Inspect index and stock_prices
print(index.info())
print(index.head())
print('------------')
print(stock_prices.info())
print(stock_prices.head())
print('------------')

# Join index to stock_prices, and inspect the result
data = stock_prices.join(index)
print(data.info())
print(data.head())
print('------------')

# Create index & stock price returns
returns = data.pct_change()

# Export data and data as returns to excel
with pd.ExcelWriter('data.xls') as writer:
    data.to_excel(excel_writer=writer,sheet_name='data')
    returns.to_excel(excel_writer=writer,sheet_name='returns')
```

### Results :  

	<script.py> output:
	    <class 'pandas.core.frame.DataFrame'>
	    DatetimeIndex: 1761 entries, 2010-01-04 to 2016-12-30
	    Data columns (total 1 columns):
	    Index    1761 non-null float64
	    dtypes: float64(1)
	    memory usage: 27.5 KB
	    None
		             Index
	    Date                  
	    2010-01-04  100.000000
	    2010-01-05  100.457394
	    2010-01-06   99.981005
	    2010-01-07   99.485328
	    2010-01-08  100.148231
	    ------------
	    <class 'pandas.core.frame.DataFrame'>
	    DatetimeIndex: 1762 entries, 2010-01-04 to 2016-12-30
	    Data columns (total 12 columns):
	    AAPL    1761 non-null float64
	    AMGN    1761 non-null float64
	    AMZN    1761 non-null float64
	    CPRT    1761 non-null float64
	    EL      1762 non-null float64
	    GS      1762 non-null float64
	    ILMN    1761 non-null float64
	    MA      1762 non-null float64
	    PAA     1762 non-null float64
	    RIO     1762 non-null float64
	    TEF     1762 non-null float64
	    UPS     1762 non-null float64
	    dtypes: float64(12)
	    memory usage: 179.0 KB
	    None
		         AAPL   AMGN    AMZN  CPRT     EL      GS   ILMN     MA    PAA  \
	    Date                                                                         
	    2010-01-04  30.57  57.72  133.90  4.55  24.27  173.08  30.55  25.68  27.00   
	    2010-01-05  30.63  57.22  134.69  4.55  24.18  176.14  30.35  25.61  27.30   
	    2010-01-06  30.14  56.79  132.25  4.53  24.25  174.26  32.22  25.56  27.29   
	    2010-01-07  30.08  56.27  130.00  4.50  24.56  177.67  32.77  25.39  26.96   
	    2010-01-08  30.28  56.77  133.52  4.52  24.66  174.31  33.15  25.40  27.05   
	    
		          RIO    TEF    UPS  
	    Date                             
	    2010-01-04  56.03  28.55  58.18  
	    2010-01-05  56.90  28.53  58.28  
	    2010-01-06  58.64  28.23  57.85  
	    2010-01-07  58.65  27.75  57.41  
	    2010-01-08  59.30  27.57  60.17  
	    ------------
	    <class 'pandas.core.frame.DataFrame'>
	    DatetimeIndex: 1762 entries, 2010-01-04 to 2016-12-30
	    Data columns (total 13 columns):
	    AAPL     1761 non-null float64
	    AMGN     1761 non-null float64
	    AMZN     1761 non-null float64
	    CPRT     1761 non-null float64
	    EL       1762 non-null float64
	    GS       1762 non-null float64
	    ILMN     1761 non-null float64
	    MA       1762 non-null float64
	    PAA      1762 non-null float64
	    RIO      1762 non-null float64
	    TEF      1762 non-null float64
	    UPS      1762 non-null float64
	    Index    1761 non-null float64
	    dtypes: float64(13)
	    memory usage: 192.7 KB
	    None
		         AAPL   AMGN    AMZN  CPRT     EL      GS   ILMN     MA    PAA  \
	    Date                                                                         
	    2010-01-04  30.57  57.72  133.90  4.55  24.27  173.08  30.55  25.68  27.00   
	    2010-01-05  30.63  57.22  134.69  4.55  24.18  176.14  30.35  25.61  27.30   
	    2010-01-06  30.14  56.79  132.25  4.53  24.25  174.26  32.22  25.56  27.29   
	    2010-01-07  30.08  56.27  130.00  4.50  24.56  177.67  32.77  25.39  26.96   
	    2010-01-08  30.28  56.77  133.52  4.52  24.66  174.31  33.15  25.40  27.05   
	    
		          RIO    TEF    UPS       Index  
	    Date                                         
	    2010-01-04  56.03  28.55  58.18  100.000000  
	    2010-01-05  56.90  28.53  58.28  100.457394  
	    2010-01-06  58.64  28.23  57.85   99.981005  
	    2010-01-07  58.65  27.75  57.41   99.485328  
	    2010-01-08  59.30  27.57  60.17  100.148231  
	    ------------

---
