import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import statsmodels.stats.proportion as stm
import scipy.stats as st

# Load the dataset into python
df = pd.read_csv('/Users/christoffeljansevanvuuren/Home Documents/University/HIT140/Assessment 2/GitHub/HIT140/Assessment 3/dataset2.csv')

# For hypothesis test 1. we need to determine whether there is an increased level of bat avoidance as the number of rats increases. 
# To carry out this test we will compare when there are no rats present on the platform to when rats are present on the platform.
# First we will need to seperate the data into two groups. One dataframe for when there are no rats present (rat arrival number = 0) 
# and one for when there are rats present (rat arrival number > 0).

df_no_rats = df[df['rat_arrival_number'] == 0]
df_with_rats = df[df['rat_arrival_number'] > 0]

# Next we will calculate the mean number of bat landings for both dataframes.
mean_no_rats = df_no_rats['bat_landing_number'].mean()
mean_with_rats = df_with_rats['bat_landing_number'].mean()

print(f'Mean number of bat landings with no rats: {mean_no_rats}')
print(f'Mean number of bat landings with rats: {mean_with_rats}')

# # Now we will perform a two-sample t-test to determine if the difference in means is statistically significant given the size of the data sample.
# t_stats, p_value, dfree = sm.stats.ttest_ind(df_no_rats['bat_landing_number'], df_with_rats['bat_landing_number'])
# alpha = 0.05
# print(f'T-stat: {t_stats}, P-val: {p_value}')
# if p_value < alpha:
#     print('Reject the null hypothesis: There is a significant difference in bat landings when rats are present.')
# else:
#     print('Fail to reject the null hypothesis: There is no significant difference in bat landings with and without rats present.')
# 
# # Now run the test with an alpha of 0.01
# alpha = 0.01
# if p_value < alpha:
#     print('Reject the null hypothesis at alpha 0.01: There is a significant difference in bat landings when rats are present.')
# else:
#     print('Fail to reject the null hypothesis at alpha 0.01: There is no significant difference in bat landings with and without rats present.')

# Next we will conduct a hypothesis test to determine if there is a decrease in bat landings as the number of rat minutes increases.
# If the bats perceive the rats as predators, we would expect to see a decrease in bat landings as the number of rat minutes increases.
# If the bats perceive the rats as competitors, we would expect to see an increase in bat landings as the number of rat minutes increases.
# We already know from the previous test that there is a difference in bat landings when rat_minutes =0 compared to when rat_minutes > 0.
# Therefore we will only be testing the data where rat_minutes > 0. 
# The first test we will do will split the data into two groups. One group where rat_minutes is less than or equal to the median rat_minutes, 
# and one group where rat_minutes is greater than the median rat_minutes.
# We will then perform a two-sample t-test to determine if there is a significant difference in bat landings between the two groups.
# print("Median rat minutes:", df_with_rats['rat_minutes'].median())
df_less_than_median = df_with_rats[df_with_rats['rat_minutes'] <= df_with_rats['rat_minutes'].median()]
df_greater_than_median = df_with_rats[df_with_rats['rat_minutes'] > df_with_rats['rat_minutes'].median()]
# 
# t_stats, p_value, dfree = sm.stats.ttest_ind(df_less_than_median['bat_landing_number'], df_greater_than_median['bat_landing_number'])
# alpha = 0.05
# print(f'T-stat: {t_stats}, P-val: {p_value}')
# if p_value < alpha:
#     print('Reject the null hypothesis: There is a significant difference in bat landings between low and high rat minutes.')
# else:
#     print('Fail to reject the null hypothesis: There is no significant difference in bat landings between low and high rat minutes.')
# 
# # We will use a correlation test to determine if there is a significant correlation between the number of rat minutes and the number of bat landings.
# correlation, p_value = st.pearsonr(df_with_rats['rat_minutes'], df_with_rats['bat_landing_number'])
# alpha = 0.05
# print(f'Correlation: {correlation}, P-val: {p_value}')
# if p_value < alpha:
#     print('Reject the null hypothesis: There is a significant correlation between rat minutes and bat landings.')
# else:
#     print('Fail to reject the null hypothesis: There is no significant correlation between rat minutes and bat landings.')  
# 
# # Now we will run hypothesis test 3. Null hypothesis – as the seasons change bat arrivals decrease at the same rate when 
# # rat arrival numbers increase. Tested to a 95% confidence level. 
# # First we will split the dataframe into two new dataframes. One for summer months (December, January, February) and one for non-summer months (March, April, May, June, July, August, September, October, November).
df_season1 = df[df['month'].isin([0, 1, 2])]
df_season2 = df[df['month'].isin([3, 4, 5, 6])]
# 
# # Now we will test to see if there is a significant difference in bat landings between the two seasons when rat arrival number = 0.
# df_season1_no_rats = df_season1[df_season1['rat_arrival_number'] == 0]
# df_season2_no_rats = df_season2[df_season2['rat_arrival_number'] == 0]
# t_stats, p_value, dfree = sm.stats.ttest_ind(df_season1_no_rats['bat_landing_number'], df_season2_no_rats['bat_landing_number'])
# alpha = 0.05
# print(f'T-stat (no rats): {t_stats}, P-val: {p_value}')
# if p_value < alpha:
#     print('Reject the null hypothesis: There is a significant difference in bat landings between seasons when no rats are present.')
# else:
#     print('Fail to reject the null hypothesis: There is no significant difference in bat landings between seasons when no rats are present.')
# 
# # Now we will test to see if there is a significant difference in bat landings between the two seasons when rat arrival number > 0.
# df_season1_with_rats = df_season1[df_season1['rat_arrival_number'] > 0]
# df_season2_with_rats = df_season2[df_season2['rat_arrival_number'] > 0]
# t_stats, p_value, dfree = sm.stats.ttest_ind(df_season1_with_rats['bat_landing_number'], df_season2_with_rats['bat_landing_number'])
# alpha = 0.05
# print(f'T-stat (with rats): {t_stats}, P-val: {p_value}')
# if p_value < alpha:
#     print('Reject the null hypothesis: There is a significant difference in bat landings between seasons when rats are present.')
# else:
#     print('Fail to reject the null hypothesis: There is no significant difference in bat landings between seasons when rats are present.')  
# 
# Finally we will run hypothesis test 4. Null hypothesis – There will be no significant change in the rate that bat landing numbers decrease 
# as rat minutes increase between the seasons. This will be tested to a 95% confidence level. Here we will use the previous dataframes seperated 
# based on the median rat minutes and then divide each of those further into two datasets based on their seasons.
df_season1_less_than_median = df_less_than_median[df_less_than_median['month'].isin([0, 1, 2])]
df_season1_greater_than_median = df_greater_than_median[df_greater_than_median['month'].isin([0, 1, 2])]
df_season2_less_than_median = df_less_than_median[df_less_than_median['month'].isin([3, 4, 5, 6])]
df_season2_greater_than_median = df_greater_than_median[df_greater_than_median['month'].isin([3, 4, 5, 6])]
# Now we will perform t-tests to determine if there is a significant difference in bat landings between seasons for low rate minutes.
t_stats, p_value, dfree = sm.stats.ttest_ind(df_season1_less_than_median['bat_landing_number'], df_season2_less_than_median['bat_landing_number'])
alpha = 0.05
print(f'T-stat (low rat minutes): {t_stats}, P-val: {p_value}')
if p_value < alpha:
    print('Reject the null hypothesis: There is a significant difference in bat landings between seasons for low rat minutes.')
else:
    print('Fail to reject the null hypothesis: There is no significant difference in bat landings between seasons for low rat minutes.')

# Now we will perform t-tests to determine if there is a significant difference in bat landings between seasons for high rate minutes.
t_stats, p_value, dfree = sm.stats.ttest_ind(df_season1_greater_than_median['bat_landing_number'], df_season2_greater_than_median['bat_landing_number'])
alpha = 0.05
print(f'T-stat (high rat minutes): {t_stats}, P-val: {p_value}')
if p_value < alpha:
    print('Reject the null hypothesis: There is a significant difference in bat landings between seasons for high rat minutes.')
else:
    print('Fail to reject the null hypothesis: There is no significant difference in bat landings between seasons for high rat minutes.')