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


# Pairplot
sns.pairplot(df)
plt.suptitle('Time to Approach Food vs Seconds After Rat Arrival by Month', y=1.02)
plt.tight_layout()
plt.show()  

# Scatterplot
fig, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(data=df, x='time', y='bat_landing_number', color='blue', legend=False, ax= ax)
plt.xlabel('Time')
plt.ylabel('Bat Landing Number')
plt.title('Bat Landing Number Over Time')
plt.xticks(rotation=45) # Make x-axis labels more readable
plt.tight_layout()
plt.show()

# Relational Plots
sns.relplot(data=df, x='time', y='bat_landing_number', hue='food_availability', col='rat_arrival_number', kind='scatter', col_wrap=3, height=4, aspect=1)
plt.show()

# Remove non-numberic columns from dataframe
numeric_df = df.select_dtypes(include=[np.number])

# Plot correlation matrix
corr = numeric_df.corr()

# Plot heatmap
ax = sns.heatmap(corr,
                 vmin=-1, vmax=1, center=0, 
                 cmap=sns.diverging_palette(20, 220, n=200),
                 square=False,
                 annot=True)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
)
plt.title('Dataset 2 Correlation Matrix')
plt.show()