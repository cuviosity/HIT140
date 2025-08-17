import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import math
import statsmodels.stats.weightstats as stm

df_dataset1 = pd.read_csv('dataset1.csv')
df_dataset2 = pd.read_csv('dataset2.csv')

# Do bats perceive rats not just as competitors for food but also as potential predators?

df_dataset1_risk = df_dataset1['risk']
df_dataset1_reward = df_dataset1['reward']

x_bar_risk = np.mean(df_dataset1_risk)
x_bar_reward = np.mean(df_dataset1_reward)

