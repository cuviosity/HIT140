import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Read dataframe
df = pd.read_csv('/Users/christoffeljansevanvuuren/Home Documents/University/HIT140/Assessment 2/GitHub/HIT140/Assessment 3/dataset2.csv')


# Pairplot
sns.pairplot(df)
#    month_data = df[df['month'] == month]
#    ax.scatter(month_data['seconds_after_rat_arrival'], month_data['time_to_approach_food'])
#    ax.set_title(f'Month {month}')
#    ax.set_xlabel('Seconds After Rat Arrival')
#    ax.set_ylabel('Time to Approach Food')
plt.suptitle('Time to Approach Food vs Seconds After Rat Arrival by Month', y=1.02)
plt.tight_layout()
plt.show()  

# Scatterplot
sns.scatterplot(data=df, x='time', y='bat_landing_number', hue='time', palette='tab10')
plt.xlabel('Time')
# Make x-axis labels more readable
plt.xticks(rotation=45)

plt.ylabel('Bat Landing Number')
plt.title('Bat Landing Number Over Time')
plt.tight_layout()
plt.show()

# Relational Plots
sns.relplot(data=df, x='time', y='bat_landing_number', hue='food_availability', col='time', kind='scatter', col_wrap=3, height=4, aspect=1)
plt.show()