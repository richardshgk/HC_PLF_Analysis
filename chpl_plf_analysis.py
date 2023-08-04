import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
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
plt.style.use("ggplot")

# plt.bar(year, plf)

# plt.title('Ohio Public Library Funds by Year')
# plt.xlabel('Calendar Year')
# plt.ylabel('PLF Money Awarded in USD')

plt.barh(year, visits)
plt.barh(year, circ, left=visits)
plt.barh(year, computers, left=visits+circ)
plt.barh(year, wifi, left=visits+circ+computers)

plt.legend(['Visits', 'Circulation', 'PC Usage', 'Wifi Usage'])
plt.yticks(ticks=year)


plt.title('CHPL Usage by Year')
plt.ylabel('Calendar Year')
plt.xlabel('Instances of Sevices Used')
# plt.yticks(np.arange(0, 30000000, step=))

plt.show()