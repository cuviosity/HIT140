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
habit_types = df_dataset1['habit'].value_co_unts()
print("Habit types are:\n", habit_types)

# Does the bats behavior change over time with the experiment?
# If bats perceive rats as predators. Their behavior may change over time to become more avoidant to rats.
# If bats perceive rats as competitors. Their behavior may change over time to become more aggressive towards rats.

df_month0 = df_dataset1[df_dataset1['month'] == 0]
df_month1 = df_dataset1[df_dataset1['month'] == 1]
df_month2 = df_dataset1[df_dataset1['month'] == 2]
df_month3 = df_dataset1[df_dataset1['month'] == 3]
df_month4 = df_dataset1[df_dataset1['month'] == 4]
df_month5 = df_dataset1[df_dataset1['month'] == 5]


# Next, try to see if there is a relationship with how long the bat takes to approach the food and seconds after rat arrival.
# If the bat sees the rat as a competitor to food it might try to fight the rat for it or get it as fast as possible. Therefore, leading to a shorter bat landing to food time.
# If the bat sees the rat as a preditor it might try to avoid the rat and see if it goes away before approaching the food. Therefore, leading to longer bat landing to food time.