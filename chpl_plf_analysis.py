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

chpl_totals = chpl.sum(axis=1)

# Set overall seaborn and pyplot visuals
sns.set()
plt.style.use("ggplot")

# Create subplots and set figure size
fig, (ax1, ax2) = plt.subplots(2,1)
fig.set_figheight(8.5)
fig.set_figwidth(9)

# Create first horizontal bar chart showing Public Library Fund awarded to Hamilton County
hor1 = ax1.barh(year, plf)

# Tick formatting
ax1.ticklabel_format(style='plain')
ax1.tick_params(axis='both', labelsize=10)
ax1.tick_params(axis='x', labelrotation=45)
ax1.set_yticks(ticks=year)

ax1.set_title('Ohio Public Library Funds by Year', fontweight='bold')
ax1.set_xlabel('Calendar Year', fontweight='bold', labelpad=5)
ax1.set_ylabel('PLF Money Awarded in USD', fontweight='bold', labelpad=10)
ax1.bar_label(hor1, labels=plf, label_type='center', color ='white', fmt='%.2f')

# Create second horizontal bar chart comparing the use of services at CHPL
ax2.barh(year, visits)
hor2=ax2.barh(year, circ, left=visits)
ax2.barh(year, computers, left=visits+circ)
ax2.barh(year, wifi, left=visits+circ+computers)

# # Legend and tick formatting 
ax2.legend(['Visits', 'Circulation', 'PC Usage', 'Wifi Usage'], title='Usage Type', fontsize=10, bbox_to_anchor=(1.0, 1.0), loc='upper left')
ax2.ticklabel_format(style='plain')
ax2.tick_params(axis='both', labelsize=10)
ax2.tick_params(axis='x', labelrotation=45)
ax2.set_yticks(ticks=year)

ax2.set_title('Cincinnati and Hamilton County Public Library Usage by Year', fontweight='bold')
ax2.set_ylabel('Calendar Year', fontweight='bold', labelpad=10)
ax2.set_xlabel('Instances of Sevices Used', fontweight='bold', labelpad=10)
ax2.bar_label(hor2, labels=chpl_totals, label_type='center', color ='white')

plt.tight_layout(h_pad=2.0)

plt.show()