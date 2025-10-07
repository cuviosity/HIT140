import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import seaborn as sns
import statsmodels.api as sm

# Read dataframe
df = pd.read_csv('/Users/christoffeljansevanvuuren/Home Documents/University/HIT140/Assessment 2/GitHub/HIT140/Assessment 3/dataset2.csv')

# Convert time column to a simpler format for presenting
df['time'] = pd.to_datetime(df['time'], format='%d/%m/%Y %H:%M')
df['month_year'] = df['time'].dt.strftime('%b %Y')  # e.g., Dec 2017


# # Pairplot
# pairplot = sns.pairplot(df, height=2.5)
# pairplot.fig.suptitle('EDA Pairplot for Dataset 2', y=1.15)
# plt.subplots_adjust(top=0.92, bottom=0.15)  # Add space for title and labels
# plt.show()  
# 
# # Scatterplot
# fig, ax = plt.subplots(figsize=(12, 6))
# sns.scatterplot(data=df, x='time', y='bat_landing_number', color='blue', legend=False, ax= ax)
# plt.xlabel('Time')
# plt.ylabel('Bat Landing Number')
# plt.title('Bat Landing Number Over Time')
# plt.xticks(rotation=45) # Make x-axis labels more readable
# plt.tight_layout()
# plt.show()
# 
# # Relational Plots
# sns.relplot(data=df, x='time', y='bat_landing_number', hue='food_availability', col='rat_arrival_number', kind='scatter', col_wrap=3, height=4, aspect=1)
# plt.show()
# 
# # Remove non-numberic columns from dataframe
# numeric_df = df.select_dtypes(include=[np.number])
# 
# # Plot correlation matrix
# corr = numeric_df.corr()
# 
# # Plot heatmap
# ax = sns.heatmap(corr,
#                  vmin=-1, vmax=1, center=0, 
#                  cmap=sns.diverging_palette(20, 220, n=200),
#                  square=False,
#                  annot=True)
# ax.set_xticklabels(
#     ax.get_xticklabels(),
#     rotation=45,
#     horizontalalignment='right'
# )
# plt.title('Dataset 2 Correlation Matrix')
# plt.show()
# 
# Create a collection of boxplots
# ax = sns.boxplot(data=df, orient='h', palette='Set2', whis=1.5)
# plt.title('Boxplots of Numeric Variables in Dataset 2')
# plt.show()
# 
# # Create a specific boxplot for bat landing number
# ax = sns.boxplot(x='bat_landing_number', data=df, palette='Set3', whis=1.5)
# plt.title('Boxplot of Bat Landing Number')
# plt.xlabel('Bat Landing Number')
# plt.show()
# This shows that there are outliers in bat landing number on the upper end. 
# 
# # In line with hypothesis test 1. create two boxplots for bat landing numbers. One with no rats arriving, and one with rats arriving. Both boxplots should be on the same image.
# # First split the dataframe into two dataframes. One for rat arrival number = 0, and one for rat arrival number > 0.   
df_no_rats = df[df['rat_arrival_number'] == 0]
df_with_rats = df[df['rat_arrival_number'] > 0]
# # Create boxplot for bat landing number where one boxplot is for rat arrivals = 0, and one boxplot is for rats arrivals >0.
# sns.boxplot(
#     x=(df['rat_arrival_number'] > 0).map({False: 'No Rats Arriving', True: 'Rats Arriving'}),
#     y=df['bat_landing_number'],
#     palette='Set3',
#     whis=1.5
# )
# plt.xticks([0, 1], ['No Rats Arriving', 'Rats Arriving'])
# plt.title('Boxplot of Bat Landing Number by Rat Arrival Status')
# plt.xlabel('Rat Arrival Status')
# plt.ylabel('Bat Landing Number')
# plt.show()
# 
# The next figures address hypothesis test 2.
df_less_than_median = df_with_rats[df_with_rats['rat_minutes'] <= df_with_rats['rat_minutes'].median()]
df_greater_than_median = df_with_rats[df_with_rats['rat_minutes'] > df_with_rats['rat_minutes'].median()]
# # Create boxplot for bat landing number where one boxplot is for rat minutes less than or equal to the median, 
# # and one boxplot is for rat minutes greater than the median.
# sns.boxplot(
#     x=(df_with_rats['rat_minutes'] > df_with_rats['rat_minutes'].median()).map({False: 'Rat Minutes <= Median', True: 'Rat Minutes > Median'}),
#     y=df_with_rats['bat_landing_number'],
#     palette='Set3',
#     whis=1.5
# )
# plt.xticks([0, 1], ['Rat Minutes <= Median', 'Rat Minutes > Median'])
# plt.title('Boxplot of Bat Landing Number by Rat Minutes (for Observations with Rats Arriving)')
# plt.xlabel('Rat Minutes Category')
# plt.ylabel('Bat Landing Number')
# plt.show()
# 
# # Next create a scatterplot when rat_minutes≠0 for hypothesis test 2.
# sns.scatterplot(data=df_with_rats, x='rat_minutes', y='bat_landing_number', color='blue')
# plt.xlabel('Rat Minutes')
# plt.ylabel('Bat Landing Number')
# plt.title('Scatterplot of Bat Landing Number vs Rat Minutes (for Observations with Rats Arriving)')
# plt.show()
# 
# Create boxplot for bat landing number where one boxplot is for no rats arriving, and one boxplot is for rats arriving.
# plt.figure(figsize=(10, 6))
# sns.boxplot(x='rat_arrival_number', y='bat_landing_number', data=df, palette='Set3', whis=1.5)
# plt.title('Boxplot of Bat Landing Number by Rat Arrival Number')
# plt.xlabel('Rat Arrival Number (0 = No Rats, >0 = Rats Arriving)')
# plt.ylabel('Bat Landing Number')
# plt.show()
# 
# # Now we will create two sets of comparitive boxplots for hypothesis test 3. The first for rat arrival number = 0, and the second for rat arrival 
# # number > 0.
# # First we will split our data into the two seasons.
df_season1 = df[df['month'].isin([0, 1, 2])]
df_season2 = df[df['month'].isin([3, 4, 5, 6])]
# # Now create subset dataframes for rat arrival number = 0.
# df_season1_no_rats = df_season1[df_season1['rat_arrival_number'] == 0]
# df_season2_no_rats = df_season2[df_season2['rat_arrival_number'] == 0]
# 
# # Create season labels
# df_season1_no_rats['season'] = 'Season 1 (Dec, Jan, Feb)'
# df_season2_no_rats['season'] = 'Season 2 (Mar, Apr, May, Jun)'
# 
# # Combine both DataFrames
# df_seasons_no_rats = pd.concat([df_season1_no_rats, df_season2_no_rats])
# 
# # Plot boxplot with season as x-axis
# sns.boxplot(
#     x='season',
#     y='bat_landing_number',
#     data=df_seasons_no_rats,
#     palette='Set3',
#     whis=1.5
# )
# plt.title('Boxplot of Bat Landing Number by Season (When rat arrivals is zero)')
# plt.xlabel('Season')
# plt.ylabel('Bat Landing Number')
# plt.show()
# 
# # Now we will do the same for rat arrival number > 0.
# df_season1_with_rats = df_season1[df_season1['rat_arrival_number'] > 0]
# df_season2_with_rats = df_season2[df['rat_arrival_number'] > 0]
# 
# # Create season labels again
# df_season1_with_rats['season'] = 'Season 1 (Dec, Jan, Feb)'
# df_season2_with_rats['season'] = 'Season 2 (Mar, Apr, May, Jun)'
# 
# # Again combine both DataFrames
# df_seasons_with_rats = pd.concat([df_season1_with_rats, df_season2_with_rats])
# 
# # Finally plot the boxplot with season as x-axis
# sns.boxplot(
#     x='season',
#     y='bat_landing_number',
#     data=df_seasons_with_rats,
#     palette='Set3',
#     whis=1.5
# )
# plt.title('Boxplot of Bat Landing Number by Season (When rat arrivals is greater than zero)')
# plt.xlabel('Season')
# plt.ylabel('Bat Landing Number')
# plt.show()
# 
# Finally we will do the same for test 4. 
df_season1_less_than_median = df_less_than_median[df_less_than_median['month'].isin([0, 1, 2])]
df_season1_greater_than_median = df_greater_than_median[df_greater_than_median['month'].isin([0, 1, 2])]
df_season2_less_than_median = df_less_than_median[df_less_than_median['month'].isin([3, 4, 5, 6])]
df_season2_greater_than_median = df_greater_than_median[df_greater_than_median['month'].isin([3, 4, 5, 6])]
# 
# # Create boxplot for when rat minutes is less than or equal to the median for both seasons.
# sns.boxplot(
#     x='season',
#     y='bat_landing_number',
#     data=pd.concat([
#         df_season1_less_than_median.assign(season='Season 1 (Dec, Jan, Feb)'),
#         df_season2_less_than_median.assign(season='Season 2 (Mar, Apr, May, Jun)')
#     ]),
#     palette='Set3',
#     whis=1.5
# )
# plt.title('Boxplot of Bat Landing Number by Season (When Rat Minutes is less than the Median)')
# plt.xlabel('Season')
# plt.ylabel('Bat Landing Number')
# plt.show() 
# 
## Create boxplot for when rat minutes is greater than the median for both seasons.
#sns.boxplot(
#    x='season',
#    y='bat_landing_number',
#    data=pd.concat([
#        df_season1_greater_than_median.assign(season='Season 1 (Dec, Jan, Feb)'),
#        df_season2_greater_than_median.assign(season='Season 2 (Mar, Apr, May, Jun)')
#    ]),
#    palette='Set3',
#    whis=1.5
#)
#plt.title('Boxplot of Bat Landing Number by Season (When Rat Minutes is greater than the Median)')
#plt.xlabel('Season')
#plt.ylabel('Bat Landing Number')
#plt.show()
#
# # Create a specific boxplot for rat minutes
# ax = sns.boxplot(x='rat_minutes', data=df, palette='Set3', whis=1.5)   
# plt.title('Boxplot of Rat Minutes')
# plt.xlabel('Rat Minutes')
# plt.show()
# # Data is very right skewed, with a lot of outliers on the upper end. May be worth visualising the data another way.
# 
# # Create a specific boxplot for rat arrival number
# ax = sns.boxplot(x='rat_arrival_number', data=df, palette='Set3', whis=1.5)
# plt.title('Boxplot of Rat Arrival Number')
# plt.xlabel('Rat Arrival Number')
# plt.show()
# #Due to the large number of zero values(no rat arriving in observation period), the data is right skewed and does not represent a normal box plot.
# 
# Create a histogram with bat landing number on the y axis and food availability on the x axis
# plt.figure(figsize=(10, 6))
# sns.histplot(data=df, x='food_availability', bins=20, kde=True, color='skyblue', edgecolor='black')
# plt.title('Histogram of Food Availability')
# plt.xlabel('Food Availability') 
# plt.ylabel('Number of Bat Landings', rotation=0, labelpad=40)
# plt.show()