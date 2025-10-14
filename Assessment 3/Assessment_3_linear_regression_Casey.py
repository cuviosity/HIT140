import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import statsmodels.stats.proportion as stm
import scipy.stats as st

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Load the dataset into python
df = pd.read_csv('/Users/christoffeljansevanvuuren/Home Documents/University/HIT140/Assessment 2/GitHub/HIT140/Assessment 3/dataset2.csv')

df_with_rats = df[df['rat_arrival_number'] > 0] # <- Use this for regression model. Regression model between bat_landing_number and rat_arrival_number. Investigation A.

# ------- or you can do a regression between bat_landing_number and rat_minutes -----------
# Note that rat_arrival_number > 0 implies that rat_minutes > 0

#define x and y axis 

x = df_with_rats[["rat_arrival_number"]]  
y = df_with_rats["bat_landing_number"] 

#train testing split 

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.4,random_state=0) 
model = LinearRegression() 
model.fit(x_train,y_train) 

print("Intercept (b_0): ", model.intercept_) 
print("Coefficient of X (b_1): ", model.coef_) 

# y = 29.92 + -1.01*x 

y_pred = model.predict(x_test) 
df_pred = pd.DataFrame({"Actual": y_test, "Predicted": y_pred}) 

#print(df_pred) 
#MAE 

mae = metrics.mean_absolute_error(y_test, y_pred) 

#MSE 

mse = metrics.mean_squared_error(y_test, y_pred) 

#RMSE 

rmse = math.sqrt(mse)  

#normalised RMSE 

y_max = y_test.max() 
y_min = y_test.min() 
nrmse = rmse / (y_max - y_min) 

#print("MAE: ", mae) 

#print("MSE: ", mse) 

#print("RMSE: ", rmse) 

#print("NRMSE: ", nrmse) 

#GET BASELINE 

y_base = np.mean(y_train) 
y_pred_base = [y_base] * len(y_test)  

#MAE 

mae = metrics.mean_absolute_error(y_test, y_pred_base) 

#MSE 

mse = metrics.mean_squared_error(y_test, y_pred_base) 

#RMSE 

rmse = math.sqrt(mse)  

#normalised RMSE 

y_max = y_test.max() 
y_min = y_test.min() 
nrmse = rmse / (y_max - y_min) 

#print("MAE (baseline): ", mae) 

#print("MSE (baseline): ", mse) 

#print("RMSE (baseline): ", rmse) 

#print("NRMSE (baseline): ", nrmse) 

#------------------------------------------------- 

#Visualisation Investigation A 

#------------------------------------------------- 

sns.set_theme() 

#scatterplot blaj

sns.scatterplot(data=df_with_rats, x=x_test, y=y_test) 
plt.xlabel('Rat Arrival Number') 
plt.ylabel('Bat Landing Number') 
plt.plot(x_test, y_pred, color='red', linewidth=2, label='Predicted') 
plt.show() 

#----------------------------------------------- 

#Visualisation Investigatiom B 

#----------------------------------------------- 

#df_with_rats['month'] =pd.to_datetime(df_with_rats['month']) 

#sns.set_theme() 

#scatterplot 

#sns.scatterplot(data=df_with_rats, x=x_test, y=y_test) 

#plt.xlabel('Rat Arrival Number') 

#plt.ylabel('Bat Landing Number') 

#plt.plot(x_test, y_pred, color='red', linewidth=2, label='Predicted') 

#plt.show() 
