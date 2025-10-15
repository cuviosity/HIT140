import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import seaborn as sns
import statsmodels.api as sm

# Examine dataframe
df = pd.read_csv('Assessment 3/dataset1.csv')

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())
print(df['season'].unique())
print(df['month'].unique())
print(df['risk'].unique())
print(df['reward'].unique())
print("Dataset Shape:", df.shape)
print(df.dtypes)
print(df.head())
print(df.describe())
print(df.isnull().sum())


# Convert time column 
if 'time' in df.columns:
    df['time'] = pd.to_datetime(df['time'], format='%d/%m/%Y %H:%M')
    df['month_year'] = df['time'].dt.strftime('%b %Y')

# Pairplot - Overview of relationships between variables
pairplot = sns.pairplot(df, height=2.5)
pairplot.fig.suptitle('EDA Pairplot for Dataset 1', y=1.02)
plt.tight_layout()
plt.show()

# Remove non-numeric columns for correlation matrix
numeric_df = df.select_dtypes(include=[np.number])

# Plot correlation matrix
corr = numeric_df.corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
ax = sns.heatmap(corr,
                 vmin=-1, vmax=1, center=0, 
                 cmap=sns.diverging_palette(20, 220, n=200),
                 square=True,
                 annot=True,
                 fmt='.2f')
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
)
plt.title('Dataset 1 Correlation Matrix')
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
ax = sns.boxplot(data=numeric_df, orient='h', palette='Set2', whis=1.5)
plt.title('Boxplots of Numeric Variables in Dataset 1')
plt.tight_layout()
plt.show()


for col in numeric_df.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=col, bins=20, kde=True, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# Time series plot if time column exists
if 'time' in df.columns:
    # Replace 'target_variable' with your actual target column name
    target_col = numeric_df.columns[0]  # Modify this
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.scatterplot(data=df, x='time', y=target_col, color='blue', legend=False, ax=ax)
    plt.xlabel('Time')
    plt.ylabel(target_col)
    plt.title(f'{target_col} Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

print("\nExploratory Data Analysis Complete!")
