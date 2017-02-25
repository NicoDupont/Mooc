"""
02/2017
Dataquest : Data Analyst Path
Step 2: Intermediate Python And Pandas
SubStep : Data Analysis With Pandas Intermediate : Data Manipulation with pandas
"""


"""
1: Overview
In the previous mission, we learned how to explore a pandas DataFrame.
In this mission, we'll explore how to manipulate a DataFrame and make transformations to it.
We'll continue to work with the same data set from the USDA on nutritional information.
We'll build a basic nutritional index for people who want to eat high-protein, low-fat foods.
The "Lipid_Tot_(g)" column contains each food's total fat content, and the "Protein_(g)" (in grams) contains each food's total protein content (in grams).
Let's use the following formula to score each food in our data set:

Score=2×(Protein_(g))−0.75×(Lipid_Tot_(g))Score=2×(Protein_(g))−0.75×(Lipid_Tot_(g))
While this formula is by no means scientific, it will act as a guide as we explore pandas further.

Here's a preview of the data set:

NDB_No	Shrt_Desc	Water_(g)	Energy_Kcal	Protein_(g)	Lipid_Tot_(g)	Ash_(g)	Carbohydrt_(g)	Fiber_TD_(g)	Sugar_Tot_(g)
1001	BUTTER WITH SALT	15.87	717	0.85	81.11	2.11	0.06	0.0	0.06
1002	BUTTER WHIPPED WITH SALT	15.87	717	0.85	81.11	2.11	0.06	0.0	0.06
1003	BUTTER OIL ANHYDROUS	0.24	876	0.28	99.48	0.00	0.00	0.0	0.0
1004	CHEESE BLUE	42.41	353	21.40	28.74	5.11	2.34	0.0	0.50
1005	CHEESE BRICK	41.11	371	23.24	29.68	3.18	2.79	0.0	0.51


Instructions
To practice what we learned in the previous mission:
Import the pandas library.
Read food_info.csv into a DataFrame object named food_info.
Use the DataFrame.columns attribute, followed by the Index.tolist() method, to return a list containing only the column names.
Assign the resulting list to col_names, and use the print() function to display the value.
Display the first three rows of food_info.
"""
import pandas as pd
food_info = pd.read_csv("food_info.csv")
col_names = food_info.columns.tolist()
print(col_names)
print("---------------")
print(food_info.head(3))
""" Console Output or Results
Output
['NDB_No', 'Shrt_Desc', 'Water_(g)', 'Energ_Kcal', 'Protein_(g)', 'Lipid_Tot_(g)',
'Ash_(g)', 'Carbohydrt_(g)', 'Fiber_TD_(g)', 'Sugar_Tot_(g)', 'Calcium_(mg)', 'Iron_(mg)',
'Magnesium_(mg)', 'Phosphorus_(mg)', 'Potassium_(mg)', 'Sodium_(mg)', 'Zinc_(mg)', 'Copper_(mg)',
'Manganese_(mg)', 'Selenium_(mcg)', 'Vit_C_(mg)', 'Thiamin_(mg)', 'Riboflavin_(mg)', 'Niacin_(mg)',
'Vit_B6_(mg)', 'Vit_B12_(mcg)', 'Vit_A_IU', 'Vit_A_RAE', 'Vit_E_(mg)', 'Vit_D_mcg', 'Vit_D_IU',
'Vit_K_(mcg)', 'FA_Sat_(g)', 'FA_Mono_(g)', 'FA_Poly_(g)', 'Cholestrl_(mg)']
---------------
   NDB_No                 Shrt_Desc  Water_(g)  Energ_Kcal  Protein_(g)  \
0    1001          BUTTER WITH SALT      15.87         717         0.85
1    1002  BUTTER WHIPPED WITH SALT      15.87         717         0.85
2    1003      BUTTER OIL ANHYDROUS       0.24         876         0.28

   Lipid_Tot_(g)  Ash_(g)  Carbohydrt_(g)  Fiber_TD_(g)  Sugar_Tot_(g)  \
0          81.11     2.11            0.06           0.0           0.06
1          81.11     2.11            0.06           0.0           0.06
2          99.48     0.00            0.00           0.0           0.00

        ...        Vit_A_IU  Vit_A_RAE  Vit_E_(mg)  Vit_D_mcg  Vit_D_IU  \
0       ...          2499.0      684.0        2.32        1.5      60.0
1       ...          2499.0      684.0        2.32        1.5      60.0
2       ...          3069.0      840.0        2.80        1.8      73.0

   Vit_K_(mcg)  FA_Sat_(g)  FA_Mono_(g)  FA_Poly_(g)  Cholestrl_(mg)
0          7.0      51.368       21.021        3.043           215.0
1          7.0      50.489       23.426        3.012           219.0
2          8.6      61.924       28.732        3.694           256.0

[3 rows x 36 columns]
"""



"""
2: Transforming A Column
We can use the arithmetic operators to transform a numerical column.
The values in the "Iron_(mg)" column, for example, are currently in milligrams.
We can divide each value by 1000 to convert the values to grams.
The following code will divide each value in the "Iron_(mg)" column by 1000, and return a new Series object with those values:


div_1000 = food_info["Iron_(mg)"] / 1000
pandas allows us to use any of the arithmetic operators to scale the values in a numerical column:


# Adds 100 to each value in the column and returns a Series object.
add_100 = food_info["Iron_(mg)"] + 100
​
# Subtracts 100 from each value in the column and returns a Series object.
sub_100 = food_info["Iron_(mg)"] - 100
​
# Multiplies each value in the column by 2 and returns a Series object.
mult_2 = food_info["Iron_(mg)"]*2
Instructions
Divide the "Sodium_(mg)" column by 1000 to convert the values to grams, and assign the result to sodium_grams.
Multiply the "Sugar_Tot_(g)" column by 1000 to convert to milligrams, and assign the result to sugar_milligrams.
"""
div_1000 = food_info["Iron_(mg)"] / 1000
add_100 = food_info["Iron_(mg)"] + 100
sub_100 = food_info["Iron_(mg)"] - 100
mult_2 = food_info["Iron_(mg)"]*2
sodium_grams = food_info["Sodium_(mg)"] / 1000
sugar_milligrams = food_info["Sugar_Tot_(g)"] * 1000
print(type(sugar_milligrams))
""" Console Output or Results
Output
<class 'pandas.core.series.Series'>
"""




"""
3: Performing Math With Multiple Columns
In addition to transforming columns by numerical values, we can transform columns by other columns.
When we use an arithmetic operator between two columns (Series objects), pandas will perform that computation in a pair-wise fashion, and return a new Series object.
It applies the arithmetic operator to the first value in both columns, the second value in both columns, and so on.

In the following code, we multiply the "Water_(g)" column by the "Energ_Kcal" column, and assign the resulting Series to water_energy:


water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
The following diagram may help you understand pair-wise computation a bit better:

see img1.png

Instructions
Assign the number of grams of protein per gram of water ("Protein_(g)" column divided by "Water_(g)" column) to grams_of_protein_per_gram_of_water.
Assign the total amount of calcium and iron ("Calcium_(mg)" column plus "Iron_(mg)" column) to milligrams_of_calcium_and_iron

"""
water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
print(water_energy[0:5])
print("--------------")
grams_of_protein_per_gram_of_water = food_info["Protein_(g)"] / food_info["Water_(g)"]
milligrams_of_calcium_and_iron = food_info["Calcium_(mg)"] + food_info["Iron_(mg)"]
print(grams_of_protein_per_gram_of_water[0:5])
print("--------------")
print(milligrams_of_calcium_and_iron[0:5])
print("--------------")
""" Console Output or Results
Output
0    11378.79
1    11378.79
2      210.24
3    14970.73
4    15251.81
dtype: float64
--------------
0    0.053560
1    0.053560
2    1.166667
3    0.504598
4    0.565313
dtype: float64
--------------
0     24.02
1     24.16
2      4.00
3    528.31
4    674.43
dtype: float64
--------------
"""




"""
4: Create A Nutritional Index
Now that we've learned how to transform columns with a numerical value and how to combine columns, we can use the following formula to create a nutritional index:

Score=2×(Protein_(g))−0.75×(Lipid_Tot_(g))Score=2×(Protein_(g))−0.75×(Lipid_Tot_(g))
Instructions
Multiply the "Protein_(g)" column by two, and assign the resulting Series to weighted_protein.
Multiply the "Lipid_Tot_(g)" column by -0.75, and assign the resulting Series to weighted_fat.
Add both Series objects together and assign the result to initial_rating.
"""
weighted_protein = 2 * food_info["Protein_(g)"]
weighted_fat = -0.75 * food_info["Lipid_Tot_(g)"]
initial_rating = weighted_protein + weighted_fat
print(initial_rating[0:5])
print("--------------")
""" Console Output or Results
0   -59.1325
1   -59.1325
2   -74.0500
3    21.2450
4    24.2200
dtype: float64
--------------
"""



"""
5: Normalizing Columns In A Data Set
The columns in the data set use different units (kilo-calories, milligrams, etc.).
As a result, the range of values varies greatly between columns. For example, the "Vit_A_IU" column ranges from 0 to 100000, while the "Fiber_TD_(g)" column ranges from 0 to 79.
For certain calculations, columns like "Vit_A_IU" can have a greater effect on the result, due to the scale of the values.

While there are many ways to normalize data, one of the simplest ways is to divide all of the values in a column by that column's maximum value.
This way, all of the columns will range from 0 to 1.
To calculate the maximum value of a column, we use the Series.max() method.
In the following code, we use the Series.max() method to calculate the largest value in the "Energ_Kcal" column, and assign it to max_calories:


# The largest value in the "Energ_Kcal" column.
max_calories = food_info["Energ_Kcal"].max()
We can then use the division operator (/) to divide the values in the "Energ_Kcal" column by the maximum value, max_calories:


# Divide the values in "Energ_Kcal" by the largest value.
normalized_calories = food_info["Energ_Kcal"] / max_calories
Instructions
Normalize the values in the "Protein_(g)" column, and assign the result to normalized_protein.
Normalize the values in the "Lipid_Tot_(g)" column, and assign the result to normalized_fat.
"""
print(food_info["Protein_(g)"][0:5])
print("-------------")

max_protein = food_info["Protein_(g)"].max()
normalized_protein = food_info["Protein_(g)"] / max_protein
print(normalized_protein[0:5])
print("-------------")

print(food_info["Lipid_Tot_(g)"][0:5])
print("-------------")

max_fat = food_info["Lipid_Tot_(g)"].max()
normalized_fat = food_info["Lipid_Tot_(g)"] / max_fat
print(normalized_fat[0:5])
print("-------------")
""" Console Output or Results
Output
0     0.85
1     0.85
2     0.28
3    21.40
4    23.24
Name: Protein_(g), dtype: float64
-------------
0    0.009624
1    0.009624
2    0.003170
3    0.242301
4    0.263134
Name: Protein_(g), dtype: float64
-------------
0    81.11
1    81.11
2    99.48
3    28.74
4    29.68
Name: Lipid_Tot_(g), dtype: float64
-------------
0    0.8111
1    0.8111
2    0.9948
3    0.2874
4    0.2968
Name: Lipid_Tot_(g), dtype: float64
-------------
"""





"""
6: Creating A New Column
So far, we've assigned the Series object that results from a column transform to a variable.
However, we can add it to the DataFrame as a new column instead.

We add bracket notation to specify the name we want for that column, then use the assignment operator (=) to specify the Series object containing the values we want to assign to that column:


iron_grams = food_info["Iron_(mg)"] / 1000
food_info["Iron_(g)"] = iron_grams
The DataFrame food_info now includes the "Iron_(g)" column, which contains the values from iron_grams.

Instructions
Assign the normalized "Protein_(g)" column to a new column named "Normalized_Protein" in food_info.
Assign the normalized "Lipid_Tot_(g)" column to a new column named "Normalized_Fat" in food_info.
"""
food_info["Normalized_Protein"] = normalized_protein
food_info["Normalized_Fat"] = normalized_fat
print(food_info.head(2))
""" Console Output or Results
Output
   NDB_No                 Shrt_Desc  Water_(g)  Energ_Kcal  Protein_(g)  \
0    1001          BUTTER WITH SALT      15.87         717         0.85
1    1002  BUTTER WHIPPED WITH SALT      15.87         717         0.85

   Lipid_Tot_(g)  Ash_(g)  Carbohydrt_(g)  Fiber_TD_(g)  Sugar_Tot_(g)  \
0          81.11     2.11            0.06           0.0           0.06
1          81.11     2.11            0.06           0.0           0.06

        ...        Vit_E_(mg)  Vit_D_mcg  Vit_D_IU  Vit_K_(mcg)  FA_Sat_(g)  \
0       ...              2.32        1.5      60.0          7.0      51.368
1       ...              2.32        1.5      60.0          7.0      50.489

   FA_Mono_(g)  FA_Poly_(g)  Cholestrl_(mg)  Normalized_Protein  \
0       21.021        3.043           215.0            0.009624
1       23.426        3.012           219.0            0.009624

   Normalized_Fat
0          0.8111
1          0.8111

[2 rows x 38 columns]
"""




"""
7: Create A Normalized Nutritional Index
Combining what you've learned so far, you can now create a nutritional index that uses the normalized fat and protein values, instead of the original values.

Here's the formula for reference:

Score=2×(Normalized_Protein)−0.75×(Normalized_Fat)Score=2×(Normalized_Protein)−0.75×(Normalized_Fat)
Instructions
Use the Normalized_Protein and Normalized_Fat columns with the formula above to create the Norm_Nutr_Index column
"""
food_info["Normalized_Protein"] = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
food_info["Normalized_Fat"] = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()
food_info['Norm_Nutr_Index'] = 2 * food_info["Normalized_Protein"] -0.75 * food_info["Normalized_Fat"]
print(food_info.head(2))
""" Console Output or Results
Output
   NDB_No                 Shrt_Desc  Water_(g)  Energ_Kcal  Protein_(g)  \
0    1001          BUTTER WITH SALT      15.87         717         0.85
1    1002  BUTTER WHIPPED WITH SALT      15.87         717         0.85

   Lipid_Tot_(g)  Ash_(g)  Carbohydrt_(g)  Fiber_TD_(g)  Sugar_Tot_(g)  \
0          81.11     2.11            0.06           0.0           0.06
1          81.11     2.11            0.06           0.0           0.06

        ...         Vit_D_mcg  Vit_D_IU  Vit_K_(mcg)  FA_Sat_(g)  FA_Mono_(g)  \
0       ...               1.5      60.0          7.0      51.368       21.021
1       ...               1.5      60.0          7.0      50.489       23.426

   FA_Poly_(g)  Cholestrl_(mg)  Normalized_Protein  Normalized_Fat  \
0        3.043           215.0            0.009624          0.8111
1        3.012           219.0            0.009624          0.8111

   Norm_Nutr_Index
0        -0.589077
1        -0.589077

[2 rows x 39 columns]
"""




"""
8: Sorting A DataFrame By A Column
The DataFrame currently appears in numerical order according to the NDB_No column.
NDB_No is a unique USDA identifier that isn't really useful for our needs.
To explore which foods rank the highest in the Norm_Nutr_Index column, we need to sort the DataFrame by that column.
DataFrame objects have a sort_values() method that we can use to sort the entire DataFrame.

To sort the DataFrame on the Sodium_(mg) column, pass in the column name to the DataFrame.sort_values() method, and assign the resulting DataFrame to a new variable:


food_info.sort_values("Sodium_(mg)")
By default, pandas will sort the data by the column we specify in ascending order and return a new DataFrame, rather than modifying food_info itself.
To customize the method's behavior, use the parameters listed in the documentation:


# Sorts the DataFrame in-place, rather than returning a new DataFrame.
food_info.sort_values("Sodium_(mg)", inplace=True)
​
# Sorts by descending order, rather than ascending.
food_info.sort_values("Sodium_(mg)", inplace=True, ascending=False)
Instructions
Sort the food_info DataFrame in-place on the Norm_Nutr_Index column in descending order.
"""
food_info["Normalized_Protein"] = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
food_info["Normalized_Fat"] = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()
food_info["Norm_Nutr_Index"] = 2*food_info["Normalized_Protein"] + (-0.75*food_info["Normalized_Fat"])
print(food_info.head(2))
print("------------------")
food_info.sort_values("Norm_Nutr_Index",inplace=True,ascending=False)
print(food_info.head(2))
""" Console Output or Results
Output
   NDB_No                 Shrt_Desc  Water_(g)  Energ_Kcal  Protein_(g)  \
0    1001          BUTTER WITH SALT      15.87         717         0.85
1    1002  BUTTER WHIPPED WITH SALT      15.87         717         0.85

   Lipid_Tot_(g)  Ash_(g)  Carbohydrt_(g)  Fiber_TD_(g)  Sugar_Tot_(g)  \
0          81.11     2.11            0.06           0.0           0.06
1          81.11     2.11            0.06           0.0           0.06

        ...         Vit_D_mcg  Vit_D_IU  Vit_K_(mcg)  FA_Sat_(g)  FA_Mono_(g)  \
0       ...               1.5      60.0          7.0      51.368       21.021
1       ...               1.5      60.0          7.0      50.489       23.426

   FA_Poly_(g)  Cholestrl_(mg)  Normalized_Protein  Normalized_Fat  \
0        3.043           215.0            0.009624          0.8111
1        3.012           219.0            0.009624          0.8111

   Norm_Nutr_Index
0        -0.589077
1        -0.589077

[2 rows x 39 columns]
------------------
      NDB_No                                 Shrt_Desc  Water_(g)  Energ_Kcal  \
4991   16423  SOY PROT ISOLATE K TYPE CRUDE PROT BASIS       4.98         321
6155   19177                  GELATINS DRY PDR UNSWTND      13.00         335

      Protein_(g)  Lipid_Tot_(g)  Ash_(g)  Carbohydrt_(g)  Fiber_TD_(g)  \
4991        88.32           0.53     3.58            2.59           2.0
6155        85.60           0.10     1.30            0.00           0.0

      Sugar_Tot_(g)       ...         Vit_D_mcg  Vit_D_IU  Vit_K_(mcg)  \
4991            0.0       ...               0.0       0.0          0.0
6155            0.0       ...               0.0       0.0          0.0

      FA_Sat_(g)  FA_Mono_(g)  FA_Poly_(g)  Cholestrl_(mg)  \
4991       0.066        0.101        0.258             0.0
6155       0.070        0.060        0.010             0.0

      Normalized_Protein  Normalized_Fat  Norm_Nutr_Index
4991            1.000000          0.0053         1.996025
6155            0.969203          0.0010         1.937656

[2 rows x 39 columns]
"""



"""
9: Next Steps
In this mission, we learned how to transform columns, normalize columns, and use the arithmetic operators to create new columns.
In the next mission, we'll dive into how to work with missing values, use pivot tables, and calculate summary statistics.
"""
