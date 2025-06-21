
# retail_sales_eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
retail_sales_df = pd.read_csv("retail_sales_dataset.csv")
menu_df = pd.read_csv("menu.csv")

# Convert 'Date' to datetime format
retail_sales_df['Date'] = pd.to_datetime(retail_sales_df['Date'])

# Descriptive Statistics
desc_stats = retail_sales_df.describe()

# Add 'Month' column for time series analysis
retail_sales_df['Month'] = retail_sales_df['Date'].dt.to_period('M')

# Monthly Sales Trend
monthly_sales = retail_sales_df.groupby('Month')['Total Amount'].sum()
plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.close()

# Product Category Analysis
category_sales = retail_sales_df.groupby('Product Category')['Total Amount'].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
category_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product Category')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("category_sales.png")
plt.close()

# Age Distribution of Customers
plt.figure(figsize=(8,5))
sns.histplot(retail_sales_df['Age'], bins=10, kde=True, color='coral')
plt.title('Customer Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("age_distribution.png")
plt.close()

# Gender-based Sales
gender_sales = retail_sales_df.groupby('Gender')['Total Amount'].sum()
plt.figure(figsize=(6,5))
gender_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Sales Distribution by Gender')
plt.ylabel('')
plt.tight_layout()
plt.savefig("gender_sales_pie.png")
plt.close()

# Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(retail_sales_df[['Quantity', 'Price per Unit', 'Total Amount', 'Age']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

# Print insights
print("Descriptive Statistics:\n", desc_stats)
print("\nTop Product Categories:\n", category_sales.head())
print("\nSales by Gender:\n", gender_sales)
