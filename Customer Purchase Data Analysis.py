import pandas as pd
import matplotlib.pyplot as plt

#  Dataset Load

data = pd.read_csv("customers.csv")

print("✅ Dataset Loaded Successfully!\n")
print(data.head())   # पहले 5 rows दिखाओ

#  कुल Sales Calculation

data["TotalAmount"] = data["Price"] * data["Quantity"]

#  Product-wise Sales
product_sales = data.groupby("Product")["TotalAmount"].sum()
print("\n💰 Product-wise Sales:\n", product_sales)

#  Gender-wise Spending

gender_sales = data.groupby("Gender")["TotalAmount"].sum()
print("\n👩‍🦰👨 Gender-wise Sales:\n", gender_sales)


#  Daily Sales Trend

daily_sales = data.groupby("PurchaseDate")["TotalAmount"].sum()
print("\n📅 Daily Sales Trend:\n", daily_sales)

#  Average Age of Customers per Product

avg_age = data.groupby("Product")["Age"].mean()
print("\n📊 Average Age of Customers per Product:\n", avg_age)


#  Visualization

plt.figure(figsize=(14, 8))

# Bar Chart - Product Sales
plt.subplot(2,2,1)
product_sales.plot(kind="bar", color="skyblue")
plt.title("💰 Product-wise Sales")
plt.ylabel("Sales Amount")

# Pie Chart - Gender-wise Sales
plt.subplot(2,2,2)
gender_sales.plot(kind="pie", autopct="%1.1f%%", colors=["lightcoral","lightgreen"])
plt.title("👩‍🦰👨 Gender-wise Sales")
plt.ylabel("")

# Line Chart - Daily Sales Trend
plt.subplot(2,2,3)
daily_sales.plot(kind="line", marker="o", color="orange")
plt.title("📅 Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales Amount")

# Bar Chart - Avg Age per Product
plt.subplot(2,2,4)
avg_age.plot(kind="bar", color="violet")
plt.title("📊 Avg Age of Customers per Product")
plt.ylabel("Average Age")

plt.tight_layout()
plt.show()


