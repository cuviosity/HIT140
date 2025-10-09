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

df_with_rats = df[df['rat_arrival_number'] > 0] # <- Use this for regression model. Regression model between bat_landing_number and rat_arrival_number. Investigation A.

# ------- or you can do a regression between bat_landing_number and rat_minutes -----------
# Note that rat_arrival_number > 0 implies that rat_minutes > 0


