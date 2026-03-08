import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("Online Retail.csv", encoding="ISO-8859-1")

print("\nFirst 5 Rows:")
print(df.head())

# -----------------------------
# Data Cleaning
# -----------------------------

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Remove rows with missing CustomerID
df = df.dropna(subset=["CustomerID"])

# Create Sales column
df["Sales"] = df["Quantity"] * df["UnitPrice"]

# -----------------------------
# Create Monthly Sales
# -----------------------------

df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

# Convert period to timestamp
monthly_sales.index = monthly_sales.index.to_timestamp()

print("\nMonthly Sales:")
print(monthly_sales.head())

# -----------------------------
# Plot Sales Trend
# -----------------------------

plt.figure(figsize=(10,5))
plt.plot(monthly_sales, label="Monthly Sales")

plt.title("Retail Sales Trend Over Time")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()

plt.show()

# -----------------------------
# Moving Average (Trend)
# -----------------------------

rolling_mean = monthly_sales.rolling(window=3).mean()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales, label="Original Sales")
plt.plot(rolling_mean, label="3-Month Moving Average", color="red")

plt.title("Sales Trend with Moving Average")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()

plt.show()

# -----------------------------
# Seasonality Plot
# -----------------------------

df["Month_Name"] = df["InvoiceDate"].dt.month_name()

seasonality = df.groupby("Month_Name")["Sales"].sum()

plt.figure(figsize=(10,5))
seasonality.plot(kind="bar")

plt.title("Seasonal Sales Pattern")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.show()

# -----------------------------
# Simple Forecast (Bonus)
# -----------------------------

forecast = monthly_sales.rolling(window=6).mean()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales, label="Actual Sales")
plt.plot(forecast, label="Forecast (Rolling Mean)", linestyle="dashed")

plt.title("Simple Sales Forecast")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()

plt.show()

print("\nTask 7 Completed Successfully")