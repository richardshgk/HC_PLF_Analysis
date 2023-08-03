import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read in data files
chpl = pd.read_excel(r'assets/chpl_annual_2012-22_totals.xlsx')
plf_annuals = pd.read_csv(r'assets/plf_annuals.csv')

# Assign variables for values
circ = chpl["Circ YTD"]
visits = chpl["Visits YTD"]
computers = chpl["PC Usage YTD"]
wifi = chpl["WiFi Usage YTD"]
plf = plf_annuals["Amount"]
year = plf_annuals["Year"]

# Seaborn visuals
sns.set()

plt.plot(year, plf)
plt.plot(year, visits)

plt.xlabel('Calendar Year')
plt.ylabel('Amount in USD')

plt.show()