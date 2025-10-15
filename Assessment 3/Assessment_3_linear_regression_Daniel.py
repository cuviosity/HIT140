import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Load dataset1
df = pd.read_csv('Assessment 3/dataset1.csv')

# Filter rows where bat_landing_to_food is present
df = df[df['bat_landing_to_food'].notnull()]

# Define X and y
X = df[['season']]  # 0 = winter, 1 = spring
y = df['bat_landing_to_food']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Print model coefficients
print("Intercept (b₀):", model.intercept_)
print("Coefficient (b₁):", model.coef_[0])

# Evaluation
mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
rmse = math.sqrt(mse)
nrmse = rmse / (y_test.max() - y_test.min())

print("\nModel Performance:")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("NRMSE:", nrmse)

# Baseline: Predict mean of y_train
y_base = [y_train.mean()] * len(y_test)
mae_base = metrics.mean_absolute_error(y_test, y_base)
mse_base = metrics.mean_squared_error(y_test, y_base)
rmse_base = math.sqrt(mse_base)
nrmse_base = rmse_base / (y_test.max() - y_test.min())

print("\nBaseline Performance:")
print("MAE (baseline):", mae_base)
print("MSE (baseline):", mse_base)
print("RMSE (baseline):", rmse_base)
print("NRMSE (baseline):", nrmse_base)

# --------- Visualisation ---------
sns.set_theme()

plt.figure(figsize=(8, 5))
sns.stripplot(x=X_test['season'], y=y_test, jitter=True, alpha=0.6, label='Actual')
sns.stripplot(x=X_test['season'], y=y_pred, jitter=True, color='red', alpha=0.6, label='Predicted')
plt.xlabel("Season (0 = Winter, 1 = Spring)")
plt.ylabel("Bat Landing to Food Time (seconds)")
plt.title("Simple Linear Regression: Season vs Bat Landing Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show() 