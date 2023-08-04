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

# Set overall seaborn and pyplot visuals
sns.set()
plt.style.use("ggplot")

# plt.bar(year, plf)

# plt.title('Ohio Public Library Funds by Year')
# plt.xlabel('Calendar Year')
# plt.ylabel('PLF Money Awarded in USD')

# Create horizontal bar chart comparing the use of services at CHPL
plt.barh(year, visits)
plt.barh(year, circ, left=visits)
plt.barh(year, computers, left=visits+circ)
plt.barh(year, wifi, left=visits+circ+computers)

# Legend and tick formatting 
plt.legend(['Visits', 'Circulation', 'PC Usage', 'Wifi Usage'], title='Usage Type', fontsize=10, bbox_to_anchor=(1.0, 1.0), loc='upper left')
plt.ticklabel_format(style='plain')
plt.yticks(ticks=year, fontsize=10)
plt.xticks(rotation=45, fontsize=10)

plt.title('Cincinnati and Hamilton County Public Library Usage by Year', fontweight='bold')
plt.ylabel('Calendar Year', fontweight='bold', labelpad=10)
plt.xlabel('Instances of Sevices Used', fontweight='bold', labelpad=10)

plt.tight_layout()

plt.show()