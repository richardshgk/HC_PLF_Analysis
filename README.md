# An Analysis of Ohio Public Library Funds Awarded to the Cincinnati and Hamilton County Public Library

The Cincinnati and Hamilton County Public Library (CHPL) is fairly unique among Ohio libraries in that it gets a majority of it's yearly budget from the state of Ohio, via the Public Library Fund. This year is a budget year and, as an employee of CHPL, I was listening to the general hubbub aroudn the budget I became interested in whether there was a connection in the data. For example, if we see a major increase in circulation, does that translate into a larger budget the next year?

## Analysis
After seeing the graphs, the majority of the comparisons were not surpising to me. The years before March 2020 and the disruptions caused by Covid show a general increase in library usage. When one service dips another picks up, but overall there is growth and we see the same with the PLF budget. 

However the number overall uses drops significantly during Covid and, more surpising to me, they do not appear to have recovered in the last two years. While 2020 saw many library locations were closed or offering limited hours and services, CHPL has been back to "full service" for almost two years now. 

One statistic I would like to delve into deeper is the PC usage since Covid. The usage of computers in the library is by the number of logins and not by the number of minutes the machines are in use. Until recently 

#### About the data: 
There are several little idiosyncrasies in the CHPL reports that come from real world data. But I think it is important to clarify what library "use" is in this data. "Visits" are counted every time someone walks through the doors, use of the drive thrus are not included. "Circulation" includes any time physical itmes are checked out or renewed. As noted above, "PC Useage" only counts the number of times computers are logged into not the overall time spent on them. "Wifi Useage" is similarly the number of times devices connect to the wifi, not the time spent on it. 

All statistics for the Cincinnati and Hamilton County Public Library were generated internally by the library and then released to the public as part of the annual reports issued to the Board of Trustees. The file "chpl_annual_2012-22_totals.xlsx" was created in excel using data found in the CHPL annual board reports. The most recent annual board reports can be found [here](https://chpl.org/about/annual-report/). The original files, all pdfs, are included in the assets subfolder labled "CHPL Annual Report 2012-22". 

All statistics for the Ohio Public Library Fund come from the Ohio Department of Taxation and can be found [here](https://tax.ohio.gov/researcher/tax-analysis/tax-data-series/local.government.funds).

#### Requirements:
Please use the included "requirements.txt" file for the required packages. 

I reccommend creating a virtual environment inside of the project folder using the following code in the command line:


-------------------------------------------------------------------------------------------------------------------------

## Code Kentucky
This project was done for a final grade for Code Kentucky. 

- Data was read in from multiple xslx files and a csv file. 
- Data was cleaned, selected, and combined into new dataframes and exported as a csv file using pandas. 
- General pandas calculations were used to learn more about the data and do calculations over the dataframe for plotting. 
- Two horizontal bar plots, one stacked and one not, were created using seaborn and the pyplot feature in matplotlib.
- Instructions for creating a virtual environment and installing the requirements file are included above.
- Please see the Analysis section above for my interpretation of the data. 