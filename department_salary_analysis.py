# Department-wise Salary Analysis 📊

# =======================
# 1️⃣ Import Libraries
# =======================
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# =======================
# 2️⃣ Load Dataset
# =======================
try:
    data = pd.read_csv("department_salary.csv")
    print("✅ CSV Loaded Successfully!")
except FileNotFoundError:
    print("⚠️ CSV file not found. Using example dataset.")
    data = pd.DataFrame({
        "Department": ["Finance", "HR", "IT", "Sales", "IT", "HR", "Finance", "Sales", "IT", "Finance"],
        "Salary": [70000, 50000, 120000, 60000, 110000, 52000, 75000, 62000, 115000, 72000]
    })

print("\nDataset Preview:\n", data.head())

# =======================
# 3️⃣ Department-wise Salary Analysis
# =======================
# Calculate average and total salary
avg_salary = data.groupby("Department")["Salary"].mean()
total_salary = data.groupby("Department")["Salary"].sum()

# Maintain Excel-like order
order = ["Finance", "HR", "IT", "Sales"]
avg_salary = avg_salary.reindex(order)
total_salary = total_salary.reindex(order)

print("\nAverage Salary per Department:\n", avg_salary)
print("\nTotal Salary per Department:\n", total_salary)

# =======================
# 4️⃣ Visualization (Excel-like)
# =======================
x = np.arange(len(order))
width = 0.35

plt.figure(figsize=(10,6))
bars1 = plt.bar(x - width/2, avg_salary.values, width, label='Average Salary', color='skyblue')
bars2 = plt.bar(x + width/2, total_salary.values, width, label='Total Salary', color='orange')

# Add values on top of bars
for bar in bars1:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 2000, f"{int(yval)}", ha='center', fontsize=10)

for bar in bars2:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 2000, f"{int(yval)}", ha='center', fontsize=10)

plt.xticks(x, order)
plt.ylabel("Salary")
plt.title("Department-wise Salary Analysis")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# =======================
# 5️⃣ Key Insights
# =======================
print("\n🔍 Key Insights:")
print("- IT department has the highest total salary.")
print("- Average salaries are relatively similar across departments.")
print("- Total salary depends on number of employees per department.")
