"""
Datacamp - Manipulating DataFrames with pandas
https://www.datacamp.com/courses/manipulating-dataframes-with-pandas
Part 5 : Bringing it all together
Python 3.X
"""



"""
Here, you will bring together everything you have learned in this course while working with data recorded from the Summer Olympic games that goes as far back as 1896!
This is a rich dataset that will allow you to fully apply the data manipulation techniques you have learned.
You will pivot, unstack, group, slice, and reshape your data as you explore this dataset and uncover some truly fascinating insights. Enjoy!
"""



""" answer : 3
Grouping and aggregating
50xp

The Olympic medal data for the following exercises comes from The Guardian. It comprises records of all events held at the Olympic games between 1896 and 2012.

Suppose you have loaded the data into a DataFrame medals. You now want to find the total number of medals awarded to the USA per edition. To do this, filter the 'USA' rows and use the groupby() function to put the 'Edition' column on the index:

USA_edition_grouped = medals.loc[medals.NOC == 'USA'].groupby('Edition')

Given the goal of finding the total number of USA medals awarded per edition, what column should you select and which aggregation method should you use?
Possible Answers

    USA_edition_grouped['City'].mean()
    1
    USA_edition_grouped['Athlete'].sum()
    2
    USA_edition_grouped['Medal'].count()
    3
    USA_edition_grouped['Gender'].first()
    4
"""





"""
Using .value_counts() for ranking
100xp

For this exercise, you will use the pandas Series method .value_counts() to determine the top 15 countries ranked by total number of medals.

Notice that .value_counts() sorts by values by default. The result is returned as a Series of counts indexed by unique entries from the original Series with values (counts) ranked in descending order.

The DataFrame has been pre-loaded for you as medals.
Instructions

    Extract the 'NOC' column from the DataFrame medals and assign the result to country_names. Notice that this Series has repeated entries for every medal (of any type) a country has won in any Edition of the Olympics.
    Create a Series medal_counts by applying .value_counts() to the Series country_names.
    Print the top 15 countries ranked by total number of medals won. This has been done for you, so hit 'Submit Answer' to see the result.

"""
# Select the 'NOC' column of medals: country_names
country_names = medals['NOC']
print(type(country_names))
print('------------------------')
# Count the number of medals won by each country: medal_counts
medal_counts = country_names.value_counts()

# Print top 15 countries ranked by medals
print(medal_counts.head(15))
""" results or consol output
<script.py> output:
    <class 'pandas.core.series.Series'>
    ------------------------
    USA    4335
    URS    2049
    GBR    1594
    FRA    1314
    ITA    1228
    GER    1211
    AUS    1075
    HUN    1053
    SWE    1021
    GDR     825
    NED     782
    JPN     704
    CHN     679
    RUS     638
    ROU     624
    Name: NOC, dtype: int64

"""





"""
Using .pivot_table() to count medals by type
100xp

Rather than ranking countries by total medals won and showing that list, you may want to see a bit more detail. You can use a pivot table to compute how many separate bronze, silver and gold medals each country won. That pivot table can then be used to repeat the previous computation to rank by total medals won.

In this exercise, you will use .pivot_table() first to aggregate the total medals by type. Then, you can use .sum() along the columns of the pivot table to produce a new column. When the modified pivot table is sorted by the total medals column, you can display the results from the last exercise with a bit more detail.
Instructions

    Construct a pivot table counted from the DataFrame medals aggregating by count. Use 'NOC' as the index, 'Athlete' for the values, and 'Medal' for the columns.
    Modify the DataFrame counted by adding a column counted['totals']. The new column 'totals' should contain the result of taking the sum along the columns (i.e., use .sum(axis='columns')).
    Overwrite the DataFrame counted by sorting it with the .sort_values() method. Specify the keyword argument ascending=False.
    Print the first 15 rows of counted using .head(15). This has been done for you, so hit 'Submit Answer' to see the result.

"""
print(medals.head())
print('--------------------')
# Construct the pivot table: counted
counted = medals.pivot_table(index='NOC',columns='Medal',values='Athlete',aggfunc='count')
print(counted)
print('--------------------')
# Create the new column: counted['totals']
counted['totals'] = counted.sum(axis='columns')
print(counted['totals'][0:15])
print('--------------------')
# Sort counted by the 'totals' column
counted = counted.sort_values('totals', ascending=False)
print('--------------------')
# Print the top 15 rows of counted
print(counted.head(15))
""" results or consol output
<script.py> output:
         City  Edition     Sport Discipline             Athlete  NOC Gender  \
    0  Athens     1896  Aquatics   Swimming       HAJOS, Alfred  HUN    Men
    1  Athens     1896  Aquatics   Swimming    HERSCHMANN, Otto  AUT    Men
    2  Athens     1896  Aquatics   Swimming   DRIVAS, Dimitrios  GRE    Men
    3  Athens     1896  Aquatics   Swimming  MALOKINIS, Ioannis  GRE    Men
    4  Athens     1896  Aquatics   Swimming  CHASAPIS, Spiridon  GRE    Men

                            Event Event_gender   Medal
    0              100m freestyle            M    Gold
    1              100m freestyle            M  Silver
    2  100m freestyle for sailors            M  Bronze
    3  100m freestyle for sailors            M    Gold
    4  100m freestyle for sailors            M  Silver
    --------------------
    Medal  Bronze    Gold  Silver
    NOC
    AFG       1.0     NaN     NaN
    AHO       NaN     NaN     1.0
    ALG       8.0     4.0     2.0
    ANZ       5.0    20.0     4.0
    ARG      88.0    68.0    83.0
    ARM       7.0     1.0     1.0
    AUS     413.0   293.0   369.0
    AUT      44.0    21.0    81.0
    AZE       9.0     4.0     3.0
    BAH       5.0     9.0     9.0
    BAR       1.0     NaN     NaN
    BDI       NaN     1.0     NaN
    BEL     150.0    91.0   167.0
    BER       1.0     NaN     NaN
    BLR      53.0    14.0    25.0
    BOH       6.0     NaN     1.0
    BRA     174.0    59.0   139.0
    BUL     136.0    53.0   142.0
    BWI       5.0     NaN     NaN
    CAN     227.0   154.0   211.0
    CHI      21.0     3.0     9.0
    CHN     193.0   234.0   252.0
    CIV       NaN     NaN     1.0
    CMR       1.0    20.0     1.0
    COL       7.0     1.0     3.0
    CRC       2.0     1.0     1.0
    CRO      18.0    31.0    30.0
    CUB     109.0   160.0   126.0
    CZE      13.0    10.0    18.0
    DEN     152.0   147.0   192.0
    ..        ...     ...     ...
    SRI       NaN     NaN     2.0
    SUD       NaN     NaN     1.0
    SUI     138.0    73.0   165.0
    SUR       1.0     1.0     NaN
    SVK       8.0    10.0    11.0
    SWE     325.0   347.0   349.0
    SYR       1.0     1.0     1.0
    TAN       NaN     NaN     2.0
    TCH     105.0    80.0   144.0
    TGA       NaN     NaN     1.0
    THA      10.0     7.0     4.0
    TJK       1.0     NaN     1.0
    TOG       1.0     NaN     NaN
    TPE      13.0     2.0    27.0
    TRI      11.0     1.0     8.0
    TUN       3.0     2.0     2.0
    TUR      22.0    37.0    23.0
    UAE       NaN     1.0     NaN
    UGA       2.0     1.0     3.0
    UKR      78.0    32.0    38.0
    URS     584.0   838.0   627.0
    URU      30.0    44.0     2.0
    USA    1052.0  2088.0  1195.0
    UZB       8.0     4.0     5.0
    VEN       8.0     1.0     2.0
    VIE       NaN     NaN     2.0
    YUG     118.0   143.0   174.0
    ZAM       1.0     NaN     1.0
    ZIM       1.0    18.0     4.0
    ZZX      10.0    23.0    15.0

    [138 rows x 3 columns]
    --------------------
    NOC
    AFG       1.0
    AHO       1.0
    ALG      14.0
    ANZ      29.0
    ARG     239.0
    ARM       9.0
    AUS    1075.0
    AUT     146.0
    AZE      16.0
    BAH      23.0
    BAR       1.0
    BDI       1.0
    BEL     408.0
    BER       1.0
    BLR      92.0
    Name: totals, dtype: float64
    --------------------
    --------------------
    Medal  Bronze    Gold  Silver  totals
    NOC
    USA    1052.0  2088.0  1195.0  4335.0
    URS     584.0   838.0   627.0  2049.0
    GBR     505.0   498.0   591.0  1594.0
    FRA     475.0   378.0   461.0  1314.0
    ITA     374.0   460.0   394.0  1228.0
    GER     454.0   407.0   350.0  1211.0
    AUS     413.0   293.0   369.0  1075.0
    HUN     345.0   400.0   308.0  1053.0
    SWE     325.0   347.0   349.0  1021.0
    GDR     225.0   329.0   271.0   825.0
    NED     320.0   212.0   250.0   782.0
    JPN     270.0   206.0   228.0   704.0
    CHN     193.0   234.0   252.0   679.0
    RUS     240.0   192.0   206.0   638.0
    ROU     282.0   155.0   187.0   624.0
    --------------------
"""




"""
Applying .drop_duplicates()
100xp

What could be the difference between the 'Event_gender' and 'Gender' columns? You should be able to evaluate your guess by looking at the unique values of the pairs (Event_gender, Gender) in the data. In particular, you should not see something like (Event_gender='M', Gender='Women'). However, you will see that, strangely enough, there is an observation with (Event_gender='W', Gender='Men').

The duplicates can be dropped using the .drop_duplicates() method, leaving behind the unique observations. The DataFrame has been loaded as medals.
Instructions

    Select the columns 'Event_gender' and 'Gender'.
    Create a dataframe ev_gen_uniques containing the unique pairs contained in ev_gen.
    Print ev_gen_uniques. This has been done for you, so hit 'Submit Answer' to see the result.

"""
# Select columns: ev_gen
ev_gen = medals[['Event_gender','Gender']]

# Drop duplicate pairs: ev_gen_uniques
ev_gen_uniques = ev_gen.drop_duplicates()

# Print ev_gen_uniques
print(ev_gen_uniques)
""" results or consol output
<script.py> output:
          Event_gender Gender
    0                M    Men
    348              X    Men
    416              W  Women
    639              X  Women
    23675            W    Men
"""




"""
Finding possible errors with .groupby()
100xp

You will now use .groupby() to continue your exploration. Your job is to group by 'Event_gender' and 'Gender' and count the rows.

You will see that there is only one suspicious row: This is likely a data error.

The DataFrame is available to you as medals.
Instructions

    Group medals by 'Event_gender' and 'Gender'.
    Create a medal_count_by_gender DataFrame with a group count using the .count() method.
    Print medal_count_by_gender. This has been done for you, so hit 'Submit Answer' to view the result.

"""
# Group medals by the two columns: medals_by_gender
medals_by_gender = medals.groupby(['Event_gender','Gender'])

# Create a DataFrame with a group count: medal_count_by_gender
medal_count_by_gender = medals_by_gender.count()

# Print medal_count_by_gender
print(medal_count_by_gender)
""" results or consol output
<script.py> output:
                          City  Edition  Sport  Discipline  Athlete    NOC  Event  \
    Event_gender Gender
    M            Men     20067    20067  20067       20067    20067  20067  20067
    W            Men         1        1      1           1        1      1      1
                 Women    7277     7277   7277        7277     7277   7277   7277
    X            Men      1653     1653   1653        1653     1653   1653   1653
                 Women     218      218    218         218      218    218    218

                         Medal
    Event_gender Gender
    M            Men     20067
    W            Men         1
                 Women    7277
    X            Men      1653
                 Women     218
"""




"""
Locating suspicious data
100xp

You will now inspect the suspect record by locating the offending row.

You will see that, according to the data, Joyce Chepchumba was a man that won a medal in a women's event. That is a data error as you can confirm with a web search.
Instructions

    Create a Boolean Series with a condition that captures the only row that has medals.Event_gender == 'W' and medals.Gender == 'Men'. Be sure to use the & operator.
    Use the Boolean Series to create a DataFrame called suspect with the suspicious row.
    Print suspect. This has been done for you, so hit 'Submit Answer' to see the result.

"""
# Create the Boolean Series: sus
sus = (medals.Event_gender == 'W') & (medals.Gender == 'Men')

# Create a DataFrame with the suspicious row: suspect
suspect = medals[sus]

# Print suspect
print(suspect)
""" results or consol output
<script.py> output:
             City  Edition      Sport Discipline            Athlete  NOC Gender  \
    23675  Sydney     2000  Athletics  Athletics  CHEPCHUMBA, Joyce  KEN    Men

              Event Event_gender   Medal
    23675  marathon            W  Bronze
"""





"""
Using .nunique() to rank by distinct sports
100xp

You may want to know which countries won medals in the most distinct sports. The .nunique() method is the principal aggregation here. Given a categorical Series S, S.nunique() returns the number of distinct categories.
Instructions

    Group medals by 'NOC'.
    Compute the number of distinct sports in which each country won medals. To do this, select the 'Sport' column from country_grouped and apply .nunique().
    Sort Nsports in descending order with .sort_values() and ascending=False.
    Print the first 15 rows of Nsports. This has been done for you, so hit 'Submit Answer' to see the result.

"""
# Group medals by 'NOC': country_grouped
country_grouped = medals.groupby('NOC')

# Compute the number of distinct sports in which each country won medals: Nsports
Nsports = country_grouped['Sport'].nunique()

# Sort the values of Nsports in descending order
Nsports = Nsports.sort_values(ascending=False)

# Print the top 15 rows of Nsports
print(Nsports.head(15))

""" results or consol output
<script.py> output:
    NOC
    USA    34
    GBR    31
    FRA    28
    GER    26
    CHN    24
    AUS    22
    ESP    22
    CAN    22
    SWE    21
    URS    21
    ITA    21
    NED    20
    RUS    20
    JPN    20
    DEN    19
    Name: Sport, dtype: int64
"""




"""
Counting USA vs. USSR Cold War Olympic Sports
100xp

The Olympic competitions between 1952 and 1988 took place during the height of the Cold War between the United States of America (USA) & the Union of Soviet Socialist Republics (USSR). Your goal in this exercise is to aggregate the number of distinct sports in which the USA and the USSR won medals during the Cold War years.

The construction is mostly the same as in the preceding exercise. There is an additional filtering stage beforehand in which you reduce the original DataFrame medals by extracting data from the Cold War period that applies only to the US or to the USSR. The relevant country codes in the DataFrame, which has been pre-loaded as medals, are 'USA' & 'URS'.
Instructions

    Create a DataFrame cold_war_medals by filtering the DataFrame medals on two simultaneous conditions:
        Extract all rows for which the 'Edition' is >= 1952 & <= 1988;
        Extract rows for which 'NOC' is either 'USA' or 'URS'.
    Group cold_war_medals by 'NOC'.
    Create a Series Nsports from country_grouped using indexing & chained methods:
        Extract the column 'Sport';
        Use .nunique() to get the number of unique elements in each group;
        Apply .sort_values(ascending=False) to rearrange the Series.
    Print the final Series Nsports. This has been done for you, so hit 'Submit Answer' to see the result!

"""
# Extract all rows for which the 'Edition' is between 1952 & 1988: during_cold_war
during_cold_war = (medals.Edition >= 1952) & (medals.Edition <= 1988)
print(during_cold_war.head())
print('--------------------')

# Extract rows for which 'NOC' is either 'USA' or 'URS': is_usa_urs
is_usa_urs = medals.NOC.isin(['USA','URS'])
print(is_usa_urs.head())
print('--------------------')
# Use during_cold_war and is_usa_urs to create the DataFrame: cold_war_medals
cold_war_medals = medals.loc[(during_cold_war) & (is_usa_urs)]
print(cold_war_medals.head())
print('--------------------')
# Group cold_war_medals by 'NOC'
country_grouped = cold_war_medals.groupby('NOC')
print(country_grouped.head())
print('--------------------')
# Create Nsports
Nsports = country_grouped['Sport'].nunique().sort_values(ascending=False)

# Print Nsports
print(Nsports)
""" results or consol output
<script.py> output:
    0    False
    1    False
    2    False
    3    False
    4    False
    Name: Edition, dtype: bool
    --------------------
    0    False
    1    False
    2    False
    3    False
    4    False
    Name: NOC, dtype: bool
    --------------------
              City  Edition     Sport Discipline                     Athlete  NOC  \
    8019  Helsinki     1952  Aquatics     Diving                 LEE, Samuel  USA
    8021  Helsinki     1952  Aquatics     Diving  STOVER-IRWIN, Juno Roslays  USA
    8022  Helsinki     1952  Aquatics     Diving         MCCORMICK, Patricia  USA
    8023  Helsinki     1952  Aquatics     Diving      MYERS-POPE, Paula Jean  USA
    8024  Helsinki     1952  Aquatics     Diving     CLOTWORTHY, Robert Lynn  USA

         Gender           Event Event_gender   Medal
    8019    Men    10m platform            M    Gold
    8021  Women    10m platform            W  Bronze
    8022  Women    10m platform            W    Gold
    8023  Women    10m platform            W  Silver
    8024    Men  3m springboard            M  Bronze
    --------------------
              City  Edition      Sport Discipline                         Athlete  \
    8019  Helsinki     1952   Aquatics     Diving                     LEE, Samuel
    8021  Helsinki     1952   Aquatics     Diving      STOVER-IRWIN, Juno Roslays
    8022  Helsinki     1952   Aquatics     Diving             MCCORMICK, Patricia
    8023  Helsinki     1952   Aquatics     Diving          MYERS-POPE, Paula Jean
    8024  Helsinki     1952   Aquatics     Diving         CLOTWORTHY, Robert Lynn
    8114  Helsinki     1952  Athletics  Athletics            ANUFRIYEV, Aleksandr
    8117  Helsinki     1952  Athletics  Athletics                     JUNK, Bruno
    8135  Helsinki     1952  Athletics  Athletics  KHNYKINA-DVALISHVILI, Nadezhda
    8140  Helsinki     1952  Athletics  Athletics             KAZANTSEV, Vladimir
    8146  Helsinki     1952  Athletics  Athletics                    LITUEV, Yuri

          NOC Gender               Event Event_gender   Medal
    8019  USA    Men        10m platform            M    Gold
    8021  USA  Women        10m platform            W  Bronze
    8022  USA  Women        10m platform            W    Gold
    8023  USA  Women        10m platform            W  Silver
    8024  USA    Men      3m springboard            M  Bronze
    8114  URS    Men              10000m            M  Bronze
    8117  URS    Men         10000m walk            M  Bronze
    8135  URS  Women                200m            W  Bronze
    8140  URS    Men  3000m steeplechase            M  Silver
    8146  URS    Men        400m hurdles            M  Silver
    --------------------
    NOC
    URS    21
    USA    20
    Name: Sport, dtype: int64

"""




"""
Counting USA vs. USSR Cold War Olympic Medals
100xp

For this exercise, you want to see which country, the USA or the USSR, won the most medals consistently over the Cold War period.

There are several steps involved in carrying out this computation.

    You'll need a pivot table with years ('Edition') on the index and countries ('NOC') on the columns. The entries will be the total number of medals each country won that year. If the country won no medals in a given edition, expect a NaN in that entry of the pivot table.
    You'll need to slice the Cold War period and subset the 'USA' and 'URS' columns.
    You'll need to make a Series from this slice of the pivot table that tells which country won the most medals in that edition using .idxmax(axis='columns'). If .max() returns the maximum value of Series or 1D array, .idxmax() returns the index of the maximizing element. The argument axis=columns or axis=1 is required because, by default, this aggregation would be done along columns for a DataFrame.
    The final Series contains either 'USA' or 'URS' according to which country won the most medals in each Olympic edition. You can use .value_counts() to count the number of occurrences of each.

Instructions

    Construct medals_won_by_country using medals.pivot_table().
        The index should the years ('Edition') & the columns should be country ('NOC')
        the values should be 'Athlete' (which captures every medal regardless of kind) & the aggregation method should be 'count' (which captures the total number of medals won).
    Create cold_war_usa_usr_medals by slicing the pivot table medals_won_by_country. Your slice should contain the editions from years 1952:1988 and only the columns 'USA' & 'URS' from the pivot table.
    Create the Series most_medals by applying the .idxmax() method to cold_war_usa_usr_medals. Be sure to use axis='columns'.
    Print the result of applying .value_counts() to most_medals. The result reported gives the number of times each of the USA or the USSR won more Olympic medals in total than the other between 1952 and 1988.

"""
print(medals.head())
print('---------------------')
# Create the pivot table: medals_won_by_country
medals_won_by_country = medals.pivot_table(index='Edition',columns='NOC',values='Athlete',aggfunc='count')
print(medals_won_by_country.head())
print('---------------------')
# Slice medals_won_by_country: cold_war_usa_usr_medals
cold_war_usa_usr_medals = medals_won_by_country.loc[1952:1988, ['USA','URS']]
print(cold_war_usa_usr_medals.head())
print('---------------------')
# Create most_medals
most_medals = cold_war_usa_usr_medals.idxmax(axis='columns')
print(most_medals.head())
print('---------------------')
# Print most_medals.value_counts()
print(most_medals.value_counts())
""" results or consol output
<script.py> output:
         City  Edition     Sport Discipline             Athlete  NOC Gender  \
    0  Athens     1896  Aquatics   Swimming       HAJOS, Alfred  HUN    Men
    1  Athens     1896  Aquatics   Swimming    HERSCHMANN, Otto  AUT    Men
    2  Athens     1896  Aquatics   Swimming   DRIVAS, Dimitrios  GRE    Men
    3  Athens     1896  Aquatics   Swimming  MALOKINIS, Ioannis  GRE    Men
    4  Athens     1896  Aquatics   Swimming  CHASAPIS, Spiridon  GRE    Men

                            Event Event_gender   Medal
    0              100m freestyle            M    Gold
    1              100m freestyle            M  Silver
    2  100m freestyle for sailors            M  Bronze
    3  100m freestyle for sailors            M    Gold
    4  100m freestyle for sailors            M  Silver
    ---------------------
    NOC      AFG  AHO  ALG   ANZ  ARG  ARM  AUS   AUT  AZE  BAH  ...   URS  URU  \
    Edition                                                      ...
    1896     NaN  NaN  NaN   NaN  NaN  NaN  2.0   5.0  NaN  NaN  ...   NaN  NaN
    1900     NaN  NaN  NaN   NaN  NaN  NaN  5.0   6.0  NaN  NaN  ...   NaN  NaN
    1904     NaN  NaN  NaN   NaN  NaN  NaN  NaN   1.0  NaN  NaN  ...   NaN  NaN
    1908     NaN  NaN  NaN  19.0  NaN  NaN  NaN   1.0  NaN  NaN  ...   NaN  NaN
    1912     NaN  NaN  NaN  10.0  NaN  NaN  NaN  14.0  NaN  NaN  ...   NaN  NaN

    NOC        USA  UZB  VEN  VIE  YUG  ZAM  ZIM   ZZX
    Edition
    1896      20.0  NaN  NaN  NaN  NaN  NaN  NaN   6.0
    1900      55.0  NaN  NaN  NaN  NaN  NaN  NaN  34.0
    1904     394.0  NaN  NaN  NaN  NaN  NaN  NaN   8.0
    1908      63.0  NaN  NaN  NaN  NaN  NaN  NaN   NaN
    1912     101.0  NaN  NaN  NaN  NaN  NaN  NaN   NaN

    [5 rows x 138 columns]
    ---------------------
    NOC        USA    URS
    Edition
    1952     130.0  117.0
    1956     118.0  169.0
    1960     112.0  169.0
    1964     150.0  174.0
    1968     149.0  188.0
    ---------------------
    Edition
    1952    USA
    1956    URS
    1960    URS
    1964    URS
    1968    URS
    dtype: object
    ---------------------
    URS    8
    USA    2
    dtype: int64
"""




"""
Visualizing USA Medal Counts by Edition: Line Plot
100xp

Your job in this exercise is to visualize the medal counts by 'Edition' for the USA. The DataFrame has been pre-loaded for you as medals.
Instructions

    Create a DataFrame usa with data only for the USA.
    Group usa such that ['Edition', 'Medal'] is the index. Aggregate the count over 'Athlete'.
    Use .unstack() with level='Medal' to reshape the DataFrame usa_medals_by_year.
    Construct a line plot from the final DataFrame usa_medals_by_year. This has been done for you, so hit 'Submit Answer' to see the plot!

"""
print(medals.head())
print('---------------')
# Create the DataFrame: usa
usa = medals[medals['NOC'] == 'USA']
print(usa.head())
print('---------------')
# Group usa by 'Edition', 'Medal', and 'Athlete'
usa_medals_by_year = usa.groupby(['Edition','Medal'])['Athlete'].count()
print(usa_medals_by_year.head())
print('---------------')
# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')
print(usa_medals_by_year.head())
print('---------------')
# Plot the DataFrame usa_medals_by_year
usa_medals_by_year.plot()
plt.show()

""" results or consol output
<script.py> output:
         City  Edition     Sport Discipline             Athlete  NOC Gender  \
    0  Athens     1896  Aquatics   Swimming       HAJOS, Alfred  HUN    Men
    1  Athens     1896  Aquatics   Swimming    HERSCHMANN, Otto  AUT    Men
    2  Athens     1896  Aquatics   Swimming   DRIVAS, Dimitrios  GRE    Men
    3  Athens     1896  Aquatics   Swimming  MALOKINIS, Ioannis  GRE    Men
    4  Athens     1896  Aquatics   Swimming  CHASAPIS, Spiridon  GRE    Men

                            Event Event_gender   Medal
    0              100m freestyle            M    Gold
    1              100m freestyle            M  Silver
    2  100m freestyle for sailors            M  Bronze
    3  100m freestyle for sailors            M    Gold
    4  100m freestyle for sailors            M  Silver
    ---------------
          City  Edition      Sport Discipline         Athlete  NOC Gender  \
    11  Athens     1896  Athletics  Athletics   LANE, Francis  USA    Men
    13  Athens     1896  Athletics  Athletics   BURKE, Thomas  USA    Men
    15  Athens     1896  Athletics  Athletics  CURTIS, Thomas  USA    Men
    19  Athens     1896  Athletics  Athletics   BLAKE, Arthur  USA    Men
    21  Athens     1896  Athletics  Athletics   BURKE, Thomas  USA    Men

               Event Event_gender   Medal
    11          100m            M  Bronze
    13          100m            M    Gold
    15  110m hurdles            M    Gold
    19         1500m            M  Silver
    21          400m            M    Gold
    ---------------
    Edition  Medal
    1896     Bronze     2
             Gold      11
             Silver     7
    1900     Bronze    14
             Gold      27
    Name: Athlete, dtype: int64
    ---------------
    Medal    Bronze  Gold  Silver
    Edition
    1896          2    11       7
    1900         14    27      14
    1904        111   146     137
    1908         15    34      14
    1912         31    45      25
    ---------------
"""





"""
Visualizing USA Medal Counts by Edition: Area Plot
100xp

As in the previous exercise, your job in this exercise is to visualize the medal counts by 'Edition' for the USA. This time, you will use an area plot to see the breakdown better. The usa DataFrame has been created and all reshaping from the previous exercise has been done. You need to write the plotting command.
Instructions

    Create an area plot of usa_medals_by_year. This can be done by using .plot.area().

"""
# Create the DataFrame: usa
usa = medals[medals.NOC == 'USA']

# Group usa by 'Edition', 'Medal', and 'Athlete'
usa_medals_by_year = usa.groupby(['Edition', 'Medal'])['Athlete'].count()

# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')

# Create an area plot of usa_medals_by_year
usa_medals_by_year.plot.area()
plt.show()

""" results or consol output

"""




"""
Visualizing USA Medal Counts by Edition: Area Plot with Ordered Medals
100xp

You may have noticed that the medals are ordered according to a lexicographic (dictionary) ordering: Bronze < Gold < Silver. However, you would prefer an ordering consistent with the Olympic rules: Bronze < Silver < Gold.

You can achieve this using Categorical types. In this final exercise, after redefining the 'Medal' column of the DataFrame medals, you will repeat the area plot from the previous exercise to see the new ordering.
Instructions

    Redefine the 'Medal' column of the DataFrame medals as an ordered categorical. To do this, use pd.Categorical() with three keyword arguments:
        values = medals.Medal.
        categories=['Bronze', 'Silver', 'Gold'].
        ordered=True.
        After this, you can verify that the type has changed using medals.info().
    Plot the final DataFrame usa_medals_by_year as an area plot. This has been done for you, so hit 'Submit Answer' to see how the plot has changed!

"""
print(medals.info())
print('-------------------')
print(medals.head())
print('-------------------')
# Redefine 'Medal' as an ordered categorical
medals.Medal = pd.Categorical(values = medals.Medal,categories=['Bronze', 'Silver', 'Gold'],ordered=True)
print(medals.info())
print('-------------------')
print(medals.head())
print('-------------------')
# Create the DataFrame: usa
usa = medals[medals.NOC == 'USA']

# Group usa by 'Edition', 'Medal', and 'Athlete'
usa_medals_by_year = usa.groupby(['Edition', 'Medal'])['Athlete'].count()

# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')

# Create an area plot of usa_medals_by_year
usa_medals_by_year.plot.area()
plt.show()
""" results or consol output
<script.py> output:
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 29216 entries, 0 to 29215
    Data columns (total 10 columns):
    City            29216 non-null object
    Edition         29216 non-null int64
    Sport           29216 non-null object
    Discipline      29216 non-null object
    Athlete         29216 non-null object
    NOC             29216 non-null object
    Gender          29216 non-null object
    Event           29216 non-null object
    Event_gender    29216 non-null object
    Medal           29216 non-null object
    dtypes: int64(1), object(9)
    memory usage: 2.2+ MB
    None
    -------------------
         City  Edition     Sport Discipline             Athlete  NOC Gender  \
    0  Athens     1896  Aquatics   Swimming       HAJOS, Alfred  HUN    Men
    1  Athens     1896  Aquatics   Swimming    HERSCHMANN, Otto  AUT    Men
    2  Athens     1896  Aquatics   Swimming   DRIVAS, Dimitrios  GRE    Men
    3  Athens     1896  Aquatics   Swimming  MALOKINIS, Ioannis  GRE    Men
    4  Athens     1896  Aquatics   Swimming  CHASAPIS, Spiridon  GRE    Men

                            Event Event_gender   Medal
    0              100m freestyle            M    Gold
    1              100m freestyle            M  Silver
    2  100m freestyle for sailors            M  Bronze
    3  100m freestyle for sailors            M    Gold
    4  100m freestyle for sailors            M  Silver
    -------------------
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 29216 entries, 0 to 29215
    Data columns (total 10 columns):
    City            29216 non-null object
    Edition         29216 non-null int64
    Sport           29216 non-null object
    Discipline      29216 non-null object
    Athlete         29216 non-null object
    NOC             29216 non-null object
    Gender          29216 non-null object
    Event           29216 non-null object
    Event_gender    29216 non-null object
    Medal           29216 non-null category
    dtypes: category(1), int64(1), object(8)
    memory usage: 2.0+ MB
    None
    -------------------
         City  Edition     Sport Discipline             Athlete  NOC Gender  \
    0  Athens     1896  Aquatics   Swimming       HAJOS, Alfred  HUN    Men
    1  Athens     1896  Aquatics   Swimming    HERSCHMANN, Otto  AUT    Men
    2  Athens     1896  Aquatics   Swimming   DRIVAS, Dimitrios  GRE    Men
    3  Athens     1896  Aquatics   Swimming  MALOKINIS, Ioannis  GRE    Men
    4  Athens     1896  Aquatics   Swimming  CHASAPIS, Spiridon  GRE    Men

                            Event Event_gender   Medal
    0              100m freestyle            M    Gold
    1              100m freestyle            M  Silver
    2  100m freestyle for sailors            M  Bronze
    3  100m freestyle for sailors            M    Gold
    4  100m freestyle for sailors            M  Silver
    -------------------
"""
