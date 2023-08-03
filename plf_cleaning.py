import pandas as pd

"""
This file shows how the "plf-annuals.csv" was generated from the annual Ohio Public Library Fund data, located in the "PLF 2012-22" subfolder.
Each of the excel files is read in, the data for Hamilton County is located and saved to a variable. At the end of the file the variables are concatinated into one Series. They are then merdge with a Sereis of years for labeling, and the final database is exported as a csv to the assets folder, "plf_annuals.csv".
This file does not need to be run in order to the analysis file, "chpl_plf_analysis.py". 
"""

# Read first Excel file in as a dataframe, naming the variable accouring to the report year
twelve = pd.read_excel(r'assets/PLF 2012-22/LG10CY12.xls')

"""
These reports were formatted for printing and have multiple pairs of County : Amount in each row. So before we can save the dollar amount to a variable we must find and confrim Hamilton County's location in the dataset.
"""

# Find column and row names; confrim location of data
# print(twelve.head)
# print(twelve.columns)
# print(twelve.index)
# print(twelve.iloc[10]['Unnamed: 3'])
# print(twelve.iloc[10]['Unnamed: 4'])

# Limit data to only Hamilton County and save back to the variable 
twelve = twelve[['Unnamed: 4']]
twelve = twelve.iloc[10]
# print(twelve)

"""
We will now repeat these same steps for the rest of the reports, years 2013-22. 
"""

# ------ 2013

thirteen = pd.read_excel(r'assets/PLF 2012-22/LG10CY13.xls')

# print(thirteen.head)
# print(thirteen.columns)
# print(thirteen.index)
# print(thirteen.iloc[40]['Unnamed: 0'])
# print(thirteen.iloc[40]['Unnamed: 1'])

thirteen = thirteen[['Unnamed: 1']]
thirteen = thirteen.iloc[40]
# print(thirteen)

# ------- 2014

fourteen = pd.read_excel(r'assets/PLF 2012-22/LG10CY14.xls')

# print(fourteen.head)
# print(fourteen.iloc[40]['Unnamed: 0'])
# print(fourteen.iloc[40]['Unnamed: 1'])

fourteen = fourteen[['Unnamed: 1']]
fourteen = fourteen.iloc[40]
# print(fourteen)

# ------- 2015

fifteen = pd.read_excel(r'assets/PLF 2012-22/LG10CY15.xls')

# print(fifteen.head)
# print(fifteen.iloc[40]['Unnamed: 0'])
# print(fifteen.iloc[40]['Unnamed: 1'])

fifteen = fifteen[['Unnamed: 1']]
fifteen = fifteen.iloc[40]
# print(fifteen)

# ------- 2016

sixteen = pd.read_excel(r'assets/PLF 2012-22/LG10CY16.xls')

# print(sixteen.head)
# print(sixteen.iloc[40]['Unnamed: 0'])
# print(sixteen.iloc[40]['Unnamed: 1'])

sixteen = sixteen[['Unnamed: 1']]
sixteen = sixteen.iloc[40]
# print(sixteen)

# ------- 2017

seventeen = pd.read_excel(r'assets/PLF 2012-22/LG10CY17.xls')

# print(seventeen.head)
# print(seventeen.iloc[40]['Unnamed: 0'])
# print(seventeen.iloc[40]['Unnamed: 1'])

seventeen = seventeen[['Unnamed: 1']]
seventeen = seventeen.iloc[40]
# print(seventeen)

# ------- 2018

eighteen = pd.read_excel(r'assets/PLF 2012-22/LG10CY18.xls')

# print(eighteen.head)
# print(eighteen.iloc[40]['Unnamed: 0'])
# print(eighteen.iloc[40]['Unnamed: 1'])

eighteen = eighteen[['Unnamed: 1']]
eighteen = eighteen.iloc[40]
# print(eighteen)

# ------- 2019

nineteen = pd.read_excel(r'assets/PLF 2012-22/LG10CY19.xls')

# print(nineteen.head)
# print(nineteen.iloc[40]['Unnamed: 0'])
# print(nineteen.iloc[40]['Unnamed: 1'])

nineteen = nineteen[['Unnamed: 1']]
nineteen = nineteen.iloc[40]
# print(nineteen)

# ------- 2020

twenty = pd.read_excel(r'assets/PLF 2012-22/LG10CY20.xls')

# print(twenty.head)
# print(twenty.iloc[40]['Unnamed: 0'])
# print(twenty.iloc[40]['Unnamed: 1'])

twenty = twenty[['Unnamed: 1']]
twenty = twenty.iloc[40]
# print(twenty)

# ------- 2021

one = pd.read_excel(r'assets/PLF 2012-22/LG10CY21.xls')

# print(one.head)
# print(one.iloc[40]['Unnamed: 0'])
# print(one.iloc[40]['Unnamed: 1'])

one = one[['Unnamed: 1']]
one = one.iloc[40]
# print(one)

# ------- 2022

two = pd.read_excel(r'assets/PLF 2012-22/LG10CY22.xls')

# print(two.head)
# print(two.iloc[39]['Unnamed: 0'])
# print(two.iloc[39]['Unnamed: 1'])

two = two[['Unnamed: 1']]
two = two.iloc[39]
# print(two)

# ------- 

# Create one dataframe for all years, add lables for readability 
plf = pd.concat([twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, one, two], ignore_index=True)
plf = plf.to_frame()
plf = plf.set_axis(['Amount'], axis=1)
years = pd.Series(['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
years = years.to_frame()
years = years.set_axis(['Years'], axis=1)

plf_annuals = pd.concat([years, plf], axis=1)
# print(plf_annuals)

# Save as new file in assets folder
plf_annuals.to_csv(r'assets/plf_annuals.csv', index = False)