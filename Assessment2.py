import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import math
import statsmodels.stats.weightstats as stm
import pandas as pd

df_dataset1 = pd.read_csv('dataset1.csv')
df_dataset2 = pd.read_csv('dataset2.csv')

# Do bats perceive rats not just as competitors for food but also as potential predators?

df_dataset1_risk = df_dataset1['risk']
df_dataset1_reward = df_dataset1['reward']

x_bar_risk = np.mean(df_dataset1_risk)
x_bar_reward = np.mean(df_dataset1_reward)

print(f"Mean risk: {x_bar_risk}, Mean reward: {x_bar_reward}")

# First count the number of occurrences of each habit
habit_types = df_dataset1['habit'].value_counts()
print("Habit types are:\n", habit_types)

# Does the bats behavior change over time with the experiment?
# If bats perceive rats as predators. Their behavior may change over time to become more avoidant to rats.
# If bats perceive rats as competitors. Their behavior may change over time to become more aggressive towards rats.
df1_cleaned = df_dataset1.dropna(subset=['habit']).copy()

df_month0 = df1_cleaned[df1_cleaned['month'] == 0]
df_month1 = df1_cleaned[df1_cleaned['month'] == 1]
df_month2 = df1_cleaned[df1_cleaned['month'] == 2]
df_month3 = df1_cleaned[df1_cleaned['month'] == 3]
df_month4 = df1_cleaned[df1_cleaned['month'] == 4]
df_month5 = df1_cleaned[df1_cleaned['month'] == 5]

top_habits = df1_cleaned['habit'].value_counts().nlargest(10).index

# Filter dataset to include only those habits
filtered = df1_cleaned[df1_cleaned['habit'].isin(top_habits)]

# Recompute counts
habit_counts = filtered.groupby(["month", "habit"]).size().reset_index(name="count")
habit_pivot = habit_counts.pivot(index="month", columns="habit", values="count").fillna(0)

# Plot as grouped column (bar) chart
habit_pivot.plot(kind="bar", figsize=(14, 7))

plt.title("Occurrences of Each Habit by Month")
plt.xlabel("Month")
plt.ylabel("Number of Occurrences")
plt.legend(title="Habit", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Next, try to see if there is a relationship with how long the bat takes to approach the food and seconds after rat arrival.
fig, axes = plt.subplots(2, 3, figsize=(15, 8), sharex=True, sharey=True)

for i, month in enumerate(sorted(df_dataset1['month'].unique())):
    ax = axes[i//3, i%3]
    subset = df_dataset1[df_dataset1['month'] == month]
    ax.hist(subset['seconds_after_rat_arrival'], bins=20, color="skyblue", edgecolor="black")
    ax.set_title(f"Month {month}")
    ax.set_xlabel("Seconds After Rat Arrival")
    ax.set_ylabel("Count")

plt.suptitle("Histogram of Seconds After Rat Arrival by Month")
plt.tight_layout()
plt.show()

stats = df_dataset1.groupby("month")["seconds_after_rat_arrival"].agg(["mean", "median", "std", "count"])
print(stats)

# DO the same for the bat landing to food time
fig, axes = plt.subplots(2, 3, figsize=(15, 8), sharex=True, sharey=True)

for i, month in enumerate(sorted(df_dataset1['month'].unique())):
    ax = axes[i//3, i%3]
    subset = df_dataset1[df_dataset1['month'] == month]
    ax.hist(subset['bat_landing_to_food'], bins=20, color="lightgreen", edgecolor="black")
    ax.set_title(f"Month {month}")
    ax.set_xlabel("Bat Landing to Food Time (seconds)")
    ax.set_ylabel("Count")

plt.suptitle("Histogram of Bat Landing to Food Time by Month")
plt.tight_layout()
plt.show()

stats = df_dataset1.groupby("month")["bat_landing_to_food"].agg(["mean", "median", "std", "count"])
print(stats)

# Due to month 4 having a much larger sample size than other months it is necessary to do the 
# other months individually due to scaling difficulties for showing all months on the same plot.

month_to_plot = 3  # Change this to plot different months  

# Filter dataset for that month
subset = df_dataset1[df_dataset1['month'] == month_to_plot]

# Plot histogram
plt.figure(figsize=(8, 5))
plt.hist(subset['bat_landing_to_food'], bins=20, color="skyblue", edgecolor="black")
plt.title(f"Histogram of Bat Landing to Food Time (Month {month_to_plot})")
plt.xlabel("Bat Landing to Food Time (seconds)")
plt.ylabel("Count")
plt.show()

# If the bat sees the rat as a competitor to food it might try to fight the rat for it or get it as fast as possible. Therefore, leading to a shorter bat landing to food time.
# If the bat sees the rat as a preditor it might try to avoid the rat and see if it goes away before approaching the food. Therefore, leading to longer bat landing to food time.

# Next I will look at the hours after sunset variable and loot at the measure of central tendency and spread.
stats = df_dataset1["bat_landing_to_food"].agg(["mean", "median", "std", "count"])
print(stats)

