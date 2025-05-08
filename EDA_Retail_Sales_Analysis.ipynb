# Exploratory Data Analysis on Retail Sales Data - OIBSIP Data Analytics Task

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("Retail_Sales.csv")

# Display first 5 rows
print("Dataset Preview:\n", data.head())

# Check for missing values
print("\nMissing Values:\n", data.isnull().sum())

# Drop duplicate rows (if any)
data.drop_duplicates(inplace=True)

# Descriptive Statistics
print("\nDescriptive Statistics:\n", data.describe())

# Data Types and Info
print("\nData Types and Info:\n")
print(data.info())

# Convert 'Date' column to datetime format (if applicable)
if 'Date' in data.columns:
    data['Date'] = pd.to_datetime(data['Date'])

# Time Series Analysis: Sales Trends Over Time
if 'Date' in data.columns and 'Sales' in data.columns:
    sales_data = data.groupby('Date')['Sales'].sum()
    plt.figure(figsize=(12, 6))
    sales_data.plot(title="Sales Trends Over Time", color="blue")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

# Top 10 Products by Sales
if 'Product' in data.columns and 'Sales' in data.columns:
    top_products = data.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
    plt.title("Top 10 Products by Sales")
    plt.xlabel("Total Sales")
    plt.ylabel("Product")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

# Heatmap of Sales Across Different Categories (Optional)
if 'Category' in data.columns and 'Sales' in data.columns:
    category_sales = data.groupby('Category')['Sales'].sum().reset_index()
    category_sales = category_sales.pivot("Category", "Sales")
    plt.figure(figsize=(10, 6))
    sns.heatmap(category_sales, annot=True, cmap="YlGnBu")
    plt.title("Sales Heatmap by Category")
    plt.tight_layout()
    plt.show()
