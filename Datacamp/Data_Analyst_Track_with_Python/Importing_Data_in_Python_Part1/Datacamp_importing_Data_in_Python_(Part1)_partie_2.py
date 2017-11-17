# Datacamp - Importing Data in Python (Part 1)
# partie 2 : Importing data from other file types
# Python 3.X


"""  question réponse numéro : 2
Not so flat any more
50xp

In Chapter 1, you learnt how to use the IPython magic command ! ls to explore your current working directory. You can also do this natively in Python using the library os, which consists of miscellaneous operating system interfaces.

The first line of the following code imports the library os, the second line stores the name of the current directory in a string called wd and the third outputs the contents of the directory in a list to the shell.

import os
wd = os.getcwd()
os.listdir(wd)

Run this code in the IPython shell and answer the following questions. Ignore the files that begin with a period ..

Check out the contents of your current directory and answer the following questions: (1) which file is in your directory and NOT an example of a flat file; (2) why is it not a flat file?
Possible Answers

    database.db is not a flat file because relational databases contain structured relationships and flat files do not.
    1
    battledeath.xlsx is not a flat because it is a spreadsheet consisting of many sheets, not a single table.
    2
    titanic.txt is not a flat file because it is a .txt, not a .csv.

"""
import os
wd = os.getcwd()
os.listdir(wd)
""" sortie Ipython
In [1]: import os
... wd = os.getcwd()
... os.listdir(wd)
Out[1]: ['titanic.txt', 'battledeath.xlsx']
"""






"""
Loading a pickled file
100xp

There are a number of datatypes that cannot be saved easily to flat files, such as lists and dictionaries. If you want your files to be human readable, you may want to save them as text files in a clever manner (JSONs, which you will see in a later chapter, are appropriate for Python dictionaries).

If, however, you merely want to be able to import them into Python, you can serialize them. All this means is converting the object into a sequence of bytes, or bytestream.

In this exercise, you'll import the pickle package, open a previously pickled data structure from a file and load it.
Instructions

    Import the pickle package.
    Complete the second argument of open() so that it is read only for a binary file. This argument will be a string of two letters, one signifying 'read only', the other 'binary'.
    Pass the correct argument to pickle.load(): it should use the variable that is bound to open.
    Print the data d.
    Print the datatype of d; take your mind back to your previous use of the function type().

"""
# Import pickle package
import pickle

# Open pickle file and load data: d
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

# Print d
print(d)

# Print datatype of d
print(type(d))
""" sortie Ipython
<script.py> output:
    {'Mar': '84.4', 'Aug': '85', 'Airline': '8', 'June': '69.4'}
    <class 'dict'>
"""







"""
Listing sheets of Excel spreadsheets
100xp

Whether you like it or not, any working data scientist will need to deal with Excel spreadsheets at some point in time. You won't always want to do so in Excel, however!

Here you'll learn how to use pandas to import Excel spreadsheets and how to list the names of the sheets in any loaded .xlsx file.

Recall from the video that, given an Excel file imported into a variable spreadsheet, you can retrieve a list of the sheet names using the command spreadsheet.sheet_names.

Specifically, you'll be loading and checking out the spreadsheet 'battledeath.xlsx', modified from the Peace Research Institute Oslo's (PRIO) dataset. This data contains age-adjusted mortality rates due to war in various countries over several years.
Instructions

    Assign the filename to the variable file.
    Pass the correct argument to pd.ExcelFile() to load the file using pandas.
    Print the sheetnames of the Excel spreadsheet by passing the necessary argument to the print() function.

"""
# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)
""" sortie Ipython

<script.py> output:
    ['2002', '2004']
"""






"""
Importing sheets of Excel spreadsheets
100xp

In the previous exercises, you saw that the Excel files contain two sheets, '2002' and '2004'. The next step is to import these.

In this exercise, you'll learn how to import any given sheet of your loaded .xslx file as a DataFrame. You'll be able to do so by specifying the sheet's name or its index.

The spreadsheet 'battledeath.xlsx' is already loaded as xl.
Instructions

    Load the sheet '2004' into the DataFrame df1 using its name as a string.
    Print the head of df1 to the shell.
    Load the sheet 2002 into the DataFrame df2 using its index.
    Print the head of df2 to the shell.

"""
# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xl.parse(0)

# Print the head of the DataFrame df2
print(df2.head())
""" sortie Ipython
<script.py> output:
      War(country)      2004
    0  Afghanistan  9.451028
    1      Albania  0.130354
    2      Algeria  3.407277
    3      Andorra  0.000000
    4       Angola  2.597931
      War, age-adjusted mortality due to       2002
    0                        Afghanistan  36.083990
    1                            Albania   0.128908
    2                            Algeria  18.314120
    3                            Andorra   0.000000
    4                             Angola  18.964560

"""






"""
Customizing your spreadsheet import
100xp

Here you'll parse your spreadsheets and use additional arguments to skip rows, rename columns and select only particular columns.

The spreadsheet 'battledeath.xlsx' is already loaded as xl.

As before, you'll use the method parse(). This time, however, you'll add the additional arguments skiprows, names and parse_cols. These skip rows, name the columns and designate which columns to parse, respectively. All these arguments can be assigned to lists containing the specific row numbers, strings and column numbers, respectively.
Instructions

    Parse the first sheet by index. In doing so, skip the first row of data, then name the columns 'Country' and 'AAM due to War (2002)' by using the argument names. The arguments passed to skiprows and names will all need to be of type list.
    Parse the second sheet by index. In doing so, parse only the first column with the parse_cols parameter, skip the first row and rename the column 'Country'. The argument passed to parse_cols will need to be of type list.

"""
# Parse the first sheet and rename the columns: df1
df1 = xl.parse(0, skiprows=1, names=['Country','AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xl.parse(1, parse_cols=0, skiprows=1, names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())
""" sortie Ipython
In [1]: df1 = xl.parse(0, skiprows=1, names=['Country','AAM due to War (2002)'])

In [2]: print(df1.head())
               Country  AAM due to War (2002)
0              Albania               0.128908
1              Algeria              18.314120
2              Andorra               0.000000
3               Angola              18.964560
4  Antigua and Barbuda               0.000000

In [3]: df2 = xl.parse(1, parse_cols=0, skiprows=1, names=['Country'])

In [4]: print(df2.head())
               Country
0              Albania
1              Algeria
2              Andorra
3               Angola
4  Antigua and Barbuda

<script.py> output:
                   Country  AAM due to War (2002)
    0              Albania               0.128908
    1              Algeria              18.314120
    2              Andorra               0.000000
    3               Angola              18.964560
    4  Antigua and Barbuda               0.000000
                   Country
    0              Albania
    1              Algeria
    2              Andorra
    3               Angola
    4  Antigua and Barbuda

"""





""" question réponse : 4
How to import SAS7BDAT  importer des tables SAS
50xp

How do you correctly import the function SAS7BDAT() from the package sas7bdat?
Possible Answers

    import SAS7BDAT from sas7bdat
    1
    from SAS7BDAT import sas7bdat
    2
    import sas7bdat from SAS7BDAT
    3
    from sas7bdat import SAS7BDAT
    4
"""







"""
Importing SAS files
100xp

In this exercise, you'll figure out how to import a SAS file as a DataFrame using SAS7BDAT and pandas. The file 'sales.sas7bdat' is already in your working directory and both pandas and pyplot have already been imported as follows:

import pandas as pd
import matplotlib.pyplot as plt

The data are adapted from the website of the undergraduate text book Principles of Economics by Hill, Griffiths and Lim.
Instructions

    Import the module SAS7BDAT from the library sas7bdat.
    In the context of the file 'sales.sas7bdat', load its contents to a DataFrame df_sas, using the method to_data_frame() on the object file.
    Print the head of the DataFrame df_sas.
    Execute your entire script to produce a histogram plot!

"""
# Import sas7bdat package
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()
""" sortie Ipython
<script.py> output:
         YEAR     P           S
    0  1950.0  12.9  181.899994
    1  1951.0  11.9  245.000000
    2  1952.0  10.7  250.199997
    3  1953.0  11.3  265.899994
    4  1954.0  11.2  248.500000
"""






""" question : réponse numéro => 3
Using read_stata to import Stata files
50xp

The pandas package has been imported in the environment as pd and the file disarea.dta is in your directory. The data consist of disease extent for several diseases in various countries (more information can be found here).

What is the correct way of using the read_stata() function to import disarea.dta into an object, df?
Possible Answers

    df = 'disarea.dta'
    1
    df = read_stata.pd('disarea.dta')
    2
    df = pd.read_stata('disarea.dta')
    3
    df = pd.read_stata(disarea.dta)
    4
"""






"""
Importing Stata files
100xp

Herein, you'll gain expertise in importing Stata files as DataFrames using the pd.read_stata() function from pandas. The file 'disarea.dta' is already in your working directory. The data consist of disease extent for several diseases in various countries (more information can be found here).
Instructions

    Use pd.read_stata() to load the file 'disarea.dta' into the DataFrame df.
    Print the head of the DataFrame df.
    Visualize your results by plotting a histogram of the column disa10. We’ve already provided this code for you, so just run it!

"""
# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of coutries')
plt.show()
""" sortie Ipython
<script.py> output:
      wbcode               country  disa1  disa2  disa3  disa4  disa5  disa6  \
    0    AFG           Afghanistan   0.00   0.00   0.76   0.73    0.0   0.00   
    1    AGO                Angola   0.32   0.02   0.56   0.00    0.0   0.00   
    2    ALB               Albania   0.00   0.00   0.02   0.00    0.0   0.00   
    3    ARE  United Arab Emirates   0.00   0.00   0.00   0.00    0.0   0.00   
    4    ARG             Argentina   0.00   0.24   0.24   0.00    0.0   0.23   
    
       disa7  disa8   ...    disa16  disa17  disa18  disa19  disa20  disa21  \
    0   0.00    0.0   ...       0.0     0.0     0.0    0.00    0.00     0.0   
    1   0.56    0.0   ...       0.0     0.4     0.0    0.61    0.00     0.0   
    2   0.00    0.0   ...       0.0     0.0     0.0    0.00    0.00     0.0   
    3   0.00    0.0   ...       0.0     0.0     0.0    0.00    0.00     0.0   
    4   0.00    0.0   ...       0.0     0.0     0.0    0.00    0.05     0.0   
    
       disa22  disa23  disa24  disa25  
    0    0.00    0.02    0.00    0.00  
    1    0.99    0.98    0.61    0.00  
    2    0.00    0.00    0.00    0.16  
    3    0.00    0.00    0.00    0.00  
    4    0.00    0.01    0.00    0.11  
    
    [5 rows x 27 columns]

"""






""" question réponse : 2
Using File to import HDF5 files
50xp

The h5py package has been imported in the environment and the file LIGO_data.hdf5 is loaded in the object h5py_file.

What is the correct way of using the h5py function, File() to import the file in h5py_file into an object, h5py_data for reading only?
Possible Answers

    h5py_data = File(h5py_file, 'r')
    1
    h5py_data = h5py.File(h5py_file, 'r')
    2
    h5py_data = h5py.File(h5py_file, read)
    3
    h5py_data = h5py.File(h5py_file, 'read')
    4
"""

""" sortie Ipython

"""






"""
Using h5py to import HDF5 files
100xp

The file 'LIGO_data.hdf5' is already in your working directory. In this exercise, you'll import it using the h5py library. You'll also print out its datatype to confirm you have imported it correctly. You'll then study the structure of the file in order to see precisely what HDF groups it contains.

You can find the LIGO data plus loads of documentation and tutorials here and here is a great tutorial on Signal Processing with the data.
Instructions

    Import the package h5py.
    Assign the name of the file to the variable file.
    Load the file as read only into the variable data.
    Print the datatype of data.
    Print the names of the groups in the HDF5 file 'LIGO_data.hdf5'.

"""
# Import packages
import numpy as np
import h5py

# Assign filename: file
file = 'LIGO_data.hdf5'

# Load file: data
data = h5py.File(file,'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)
""" sortie Ipython
script.py> output:
    <class 'h5py._hl.files.File'>
    meta
    quality
    strain
"""




"""
Extracting data from your HDF5 file
100xp

In this exercise, you'll extract some of the LIGO experiment's actual data from the HDF5 file and you'll visualize it.

To do so, you'll need to first explore the HDF5 group 'strain'.
Instructions

    Assign the HDF5 group data['strain'] to group.
    In the for loop, print out the keys of the HDF5 group in group.
    Assign to the variable strain the values of the time series data data['strain']['Strain'] using the attribute .value.
    Set num_samples equal to 10000, the number of time points we wish to sample.
    Execute the rest of the code to produce a plot of the time series data in LIGO_data.hdf5.

"""
# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()
""" sortie Ipython
In [1]: # Get the HDF5 group: group
... group = data['strain']
... 
... # Check out keys of group
... for key in group.keys():
...     print(key)
Strain

In [2]: strain = data['strain']['Strain'].value

<script.py> output:
    Strain

"""




"""
Loading .mat files
100xp

In this exercise, you'll figure out how to load a MATLAB file using scipy.io.loadmat() and you'll discover what type of Python datatype it yields.

The file 'albeck_gene_expression.mat' is in your working directory. This file contains gene expression data from the Albeck Lab at UC Davis. You can find the data and some great documentation here.
Instructions

    Import the package scipy.io.
    Load the file 'albeck_gene_expression.mat' into the variable mat; do so using the function scipy.io.loadmat().
    Use the function type() to print the datatype of mat to the IPython shell.

"""
# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))
""" sortie Ipython
<script.py> output:
    <class 'dict'>

"""





"""
The structure of .mat in Python
100xp

Here you'll discover what is in the MATLAB dictionary that you loaded in the previous exercise.

The file 'albeck_gene_expression.mat' is already loaded into the variable mat. The following libraries have already been imported as follows:

import scipy.io
import matplotlib.pyplot as plt
import numpy as np

Once again, this file contains gene expression data from the Albeck Lab at UCDavis. You can find the data and some great documentation here.
Instructions

    Use the method .keys() on the dictionary mat to print the keys. Most of these keys (in fact the ones that do NOT begin and end with '__') are variables from the corresponding MATLAB environment.
    Print the type of the value corresponding to the key 'CYratioCyt' in mat. Recall that mat['CYratioCyt'] accesses the value.
    Print the shape of the value corresponding to the key 'CYratioCyt' using the numpy function shape().
    Execute the entire script to see some oscillatory gene expression data!

"""
# Print the keys of the MATLAB dictionary
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))


# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()

""" sortie Ipython
In [1]: for key in mat.keys:
...     print(key)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    for key in mat.keys:
TypeError: 'builtin_function_or_method' object is not iterable


In [2]: for key in mat.keys():
...     print(key)
cfpCyt
__globals__
yfpNuc
rfpNuc
cfpNuc
rfpCyt
yfpCyt
__version__
CYratioCyt
__header__

In [3]: print(type(mat['CYratioCyt']))
<class 'numpy.ndarray'>

In [4]: print(mat['CYratioCyt'].shape)
(200, 137)

<script.py> output:
    cfpCyt
    __globals__
    yfpNuc
    rfpNuc
    cfpNuc
    rfpCyt
    yfpCyt
    __version__
    CYratioCyt
    __header__
    <class 'numpy.ndarray'>
    (200, 137)

<script.py> output:
    cfpCyt
    __globals__
    yfpNuc
    rfpNuc
    cfpNuc
    rfpCyt
    yfpCyt
    __version__
    CYratioCyt
    __header__
    <class 'numpy.ndarray'>
    (200, 137)

In [5]: print(mat.keys())
dict_keys(['cfpCyt', '__globals__', 'yfpNuc', 'rfpNuc', 'cfpNuc', 'rfpCyt', 'yfpCyt', '__version__', 'CYratioCyt', '__header__'])

<script.py> output:
    dict_keys(['cfpCyt', '__globals__', 'yfpNuc', 'rfpNuc', 'cfpNuc', 'rfpCyt', 'yfpCyt', '__version__', 'CYratioCyt', '__header__'])
    <class 'numpy.ndarray'>
    (200, 137)

In [6]: print(np.shape(mat['CYratioCyt']))
(200, 137)

<script.py> output:
    dict_keys(['cfpCyt', '__globals__', 'yfpNuc', 'rfpNuc', 'cfpNuc', 'rfpCyt', 'yfpCyt', '__version__', 'CYratioCyt', '__header__'])
    <class 'numpy.ndarray'>
    (200, 137)
"""





