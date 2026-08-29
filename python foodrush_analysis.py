
# ============================================================
# FOODRUSH - CUSTOMER & DELIVERY ANALYTICS
# Data Analyst Portfolio Project
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------

df = pd.read_csv("foodrush_orders.csv")

print("\n" + "=" * 65)
print("             FOODRUSH ANALYTICS")
print("        Customer & Delivery Insights")
print("=" * 65)

print(f"\nDataset Loaded Successfully!")
print(f"Total Records : {len(df):,}")
print(f"Total Columns : {len(df.columns)}")


# ------------------------------------------------------------
# 2. DATA CLEANING
# ------------------------------------------------------------

print("\n" + "-" * 65)
print("DATA CLEANING")
print("-" * 65)

# Convert date
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Remove duplicates
duplicates = df.duplicated().sum()
df.drop_duplicates(inplace=True)

# Missing values
missing_before = df.isnull().sum().sum()

# Fill numerical missing values
df["Rating"] = df["Rating"].fillna(df["Rating"].median())
df["Delivery_Time"] = df["Delivery_Time"].fillna(
    df["Delivery_Time"].median()
)
df["Discount"] = df["Discount"].fillna(
    df["Discount"].median()
)

missing_after = df.isnull().sum().sum()

print(f"Duplicates Removed : {duplicates}")
print(f"Missing Values Before Cleaning : {missing_before}")
print(f"Missing Values After Cleaning  : {missing_after}")


# ------------------------------------------------------------
# 3. CREATE NEW COLUMNS
# ------------------------------------------------------------

df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

df["Net_Value"] = (
    df["Order_Value"]
    - df["Discount"]
    + df["Delivery_Fee"]
)

df["Age_Group"] = pd.cut(
    df["Customer_Age"],
    bins=[17, 25, 35, 45, 60],
    labels=["18-25", "26-35", "36-45", "46-60"]
)


# ------------------------------------------------------------
# 4. KPI CALCULATION
# ------------------------------------------------------------

total_orders = df["Order_ID"].nunique()

total_revenue = df["Order_Value"].sum()

total_customers = df["Customer_ID"].nunique()

average_order_value = df["Order_Value"].mean()

average_rating = df["Rating"].mean()

average_delivery_time = df["Delivery_Time"].mean()

cancelled_orders = (
    df["Order_Status"] == "Cancelled"
).sum()

cancellation_rate = (
    cancelled_orders / len(df)
) * 100


# ------------------------------------------------------------
# 5. EXECUTIVE SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("                  EXECUTIVE SUMMARY")
print("=" * 65)

print(f"\nTotal Orders           : {total_orders:,}")
print(f"Total Revenue         : ₹{total_revenue:,.2f}")
print(f"Total Customers       : {total_customers:,}")
print(f"Average Order Value   : ₹{average_order_value:,.2f}")
print(f"Average Rating        : {average_rating:.2f} ⭐")
print(f"Average Delivery Time : {average_delivery_time:.1f} min")
print(f"Cancellation Rate     : {cancellation_rate:.2f}%")


# ------------------------------------------------------------
# 6. CITY PERFORMANCE
# ------------------------------------------------------------

city_revenue = (
    df.groupby("City")["Order_Value"]
    .sum()
    .sort_values(ascending=False)
)

city_orders = (
    df.groupby("City")["Order_ID"]
    .nunique()
    .sort_values(ascending=False)
)

print("\n" + "-" * 65)
print("TOP CITIES BY REVENUE")
print("-" * 65)

print(city_revenue.head(10))


# ------------------------------------------------------------
# 7. CATEGORY PERFORMANCE
# ------------------------------------------------------------

category_revenue = (
    df.groupby("Category")["Order_Value"]
    .sum()
    .sort_values(ascending=False)
)

category_orders = (
    df.groupby("Category")["Order_ID"]
    .count()
    .sort_values(ascending=False)
)

print("\n" + "-" * 65)
print("FOOD CATEGORY PERFORMANCE")
print("-" * 65)

print(category_revenue)


# ------------------------------------------------------------
# 8. TOP RESTAURANTS
# ------------------------------------------------------------

top_restaurants = (
    df.groupby("Restaurant")["Order_Value"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n" + "-" * 65)
print("TOP 10 RESTAURANTS")
print("-" * 65)

print(top_restaurants)


# ------------------------------------------------------------
# 9. MONTHLY REVENUE
# ------------------------------------------------------------

monthly_revenue = (
    df.groupby("Month")["Order_Value"]
    .sum()
)

print("\n" + "-" * 65)
print("MONTHLY REVENUE")
print("-" * 65)

print(monthly_revenue)


# ------------------------------------------------------------
# 10. PAYMENT ANALYSIS
# ------------------------------------------------------------

payment_analysis = (
    df.groupby("Payment_Mode")
    .agg(
        Orders=("Order_ID", "count"),
        Revenue=("Order_Value", "sum")
    )
    .sort_values("Revenue", ascending=False)
)

print("\n" + "-" * 65)
print("PAYMENT METHOD ANALYSIS")
print("-" * 65)

print(payment_analysis)


# ------------------------------------------------------------
# 11. AGE GROUP ANALYSIS
# ------------------------------------------------------------

age_analysis = (
    df.groupby("Age_Group", observed=True)
    .agg(
        Customers=("Customer_ID", "nunique"),
        Orders=("Order_ID", "count"),
        Revenue=("Order_Value", "sum")
    )
)

print("\n" + "-" * 65)
print("CUSTOMER AGE GROUP ANALYSIS")
print("-" * 65)

print(age_analysis)


# ------------------------------------------------------------
# 12. DELIVERY PERFORMANCE
# ------------------------------------------------------------

delivery_status = (
    df.groupby("Order_Status")
    .size()
    .sort_values(ascending=False)
)

print("\n" + "-" * 65)
print("ORDER STATUS")
print("-" * 65)

print(delivery_status)


# ============================================================
#                       VISUALIZATION
# ============================================================

sns.set_theme(
    style="whitegrid",
    font_scale=1.0
)


# ------------------------------------------------------------
# CHART 1 - MONTHLY REVENUE
# ------------------------------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    marker="o",
    linewidth=2
)

plt.title(
    "FoodRush Monthly Revenue Trend",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Month")
plt.ylabel("Revenue (₹)")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# CHART 2 - CITY REVENUE
# ------------------------------------------------------------

plt.figure(figsize=(11, 6))

city_revenue.head(10).sort_values().plot(
    kind="barh"
)

plt.title(
    "Top Cities by Revenue",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Revenue (₹)")
plt.ylabel("City")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# CHART 3 - CATEGORY PERFORMANCE
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

category_revenue.sort_values().plot(
    kind="barh"
)

plt.title(
    "Revenue by Food Category",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Revenue (₹)")
plt.ylabel("Category")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# CHART 4 - TOP RESTAURANTS
# ------------------------------------------------------------

plt.figure(figsize=(11, 6))

top_restaurants.sort_values().plot(
    kind="barh"
)

plt.title(
    "Top 10 Restaurants by Revenue",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Revenue (₹)")
plt.ylabel("Restaurant")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# CHART 5 - PAYMENT METHODS
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

payment_analysis["Revenue"].plot(
    kind="bar"
)

plt.title(
    "Revenue by Payment Method",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Payment Method")
plt.ylabel("Revenue (₹)")

plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# CHART 6 - CUSTOMER AGE GROUP
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

age_analysis["Revenue"].plot(
    kind="bar"
)

plt.title(
    "Revenue by Customer Age Group",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Age Group")
plt.ylabel("Revenue (₹)")

plt.xticks(rotation=0)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# CHART 7 - DELIVERY TIME vs RATING
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Delivery_Time",
    y="Rating",
    alpha=0.5
)

plt.title(
    "Delivery Time vs Customer Rating",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Delivery Time (Minutes)")
plt.ylabel("Customer Rating")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# CHART 8 - ORDER STATUS
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

df["Order_Status"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title(
    "Order Status Distribution",
    fontsize=16,
    fontweight="bold"
)

plt.ylabel("")

plt.tight_layout()
plt.show()


# ============================================================
# BUSINESS INSIGHTS
# ============================================================

best_city = city_revenue.idxmax()
best_category = category_revenue.idxmax()
best_restaurant = top_restaurants.idxmax()
best_payment = payment_analysis["Revenue"].idxmax()
best_age_group = age_analysis["Revenue"].idxmax()

print("\n" + "=" * 65)
print("                 BUSINESS INSIGHTS")
print("=" * 65)

print(f"""
1. 🏙️ Best performing city:
   {best_city}

2. 🍔 Highest revenue category:
   {best_category}

3. 🏆 Top restaurant:
   {best_restaurant}

4. 💳 Most valuable payment method:
   {best_payment}

5. 👥 Highest revenue age group:
   {best_age_group}

6. ⭐ Average customer rating:
   {average_rating:.2f}

7. 🚚 Average delivery time:
   {average_delivery_time:.1f} minutes

8. ❌ Cancellation rate:
   {cancellation_rate:.2f}%
""")

print("=" * 65)
print("           FOODRUSH ANALYSIS COMPLETED ✅")
print("=" * 65)

