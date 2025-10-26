import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Retail_sales.csv", encoding='latin1')


print("Dataset Loaded Successfully!")
print(df.shape)
print(df.info())

#Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create new columns
df['Month'] = df['Order Date'].dt.month_name()
df['Year'] = df['Order Date'].dt.year

#  Exploratory Analysis


# Total Sales and Profit
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print(f"\n Total Sales: {total_sales:,.2f}")
print(f" Total Profit: {total_profit:,.2f}")

# Sales by Category
plt.figure(figsize=(8,5))
sns.barplot(x='Category', y='Sales', data=df, estimator='sum', palette='Blues')
plt.title("Total Sales by Category")
plt.show()

# Sales by Region
plt.figure(figsize=(8,5))
sns.barplot(x='Region', y='Sales', data=df, estimator='sum', palette='Greens')
plt.title("Sales by Region")
plt.show()

# Monthly Sales Trend
monthly_sales = df.groupby('Month')['Sales'].sum().sort_values()
plt.figure(figsize=(10,6))
monthly_sales.plot(kind='bar', color='coral')
plt.title("Monthly Sales Trend")
plt.ylabel("Total Sales")
plt.show()

#  Export Cleaned Data

df.to_excel("Cleaned_Retail_Sales.xlsx", index=False)
print("\n Cleaned dataset exported successfully to Excel!")
