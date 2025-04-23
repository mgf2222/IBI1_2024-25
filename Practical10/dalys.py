# Import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set working directory
os.chdir("D:/IBI/IBImidterm/IBI1_2024-25/Practical10")
print("Current Directory:", os.getcwd())
print("Directory Contents:", os.listdir())

# Load dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

"""
print(dalys_data.head(6))
print(dalys_data.info())
print(dalys_data.describe())

# Demonstrate iloc and loc usage
print(dalys_data.iloc[0:10,2])  # Year column for first 10 rows
print(dalys_data.loc[2:4,"Year"])  # Year values for rows 2-4
my_columns = [True, True, False, True] 
print(dalys_data.iloc[0:3,my_columns])  # Boolean column selection

# Filter 1990 data
a_1990 = dalys_data["Year"] == 1990
dalys_1990 = dalys_data.loc[a_1990, "DALYs"]
print(dalys_1990)
"""

# --- PSEUDOCODE ---
# 1. IMPORT required libraries
# 2. SET working directory
# 3. LOAD CSV data into DataFrame
# 4. FILTER UK and France data using loc
# 5. CALCULATE mean DALYs for both countries
# 6. PLOT time series data with different styles
# 7. COMPARE China and UK trends
# ------------------

# Filter UK data (Entity = "United Kingdom")
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs","Year"]]
uk_mean = uk["DALYs"].mean()

# Filter France data (Entity = "France")
france = dalys_data.loc[dalys_data["Entity"] == "France", ["DALYs","Year"]]
france_mean = france["DALYs"].mean()

print(f"UK Average DALYs: {uk_mean:.2f}")
print(f"France Average DALYs: {france_mean:.2f}")

# Plot UK data with blue plus markers
plt.plot(uk.Year, uk.DALYs, 'b+')  # 'b+' = blue plus markers
plt.title("UK DALYs Trend Over Time")
plt.xlabel("Year")
plt.ylabel("DALYs per 100,000")
plt.xticks(rotation=45)  # Rotate x-axis labels[14,16](@ref)
plt.tight_layout()  # Adjust layout[18,19](@ref)
plt.show()

# Plot with red dashed line
plt.plot(uk.Year, uk.DALYs, 'r--', label='UK DALYs')  # 'r--' = red dashed line
plt.legend()
plt.title("UK DALYs Trend Comparison")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.grid(True, alpha=0.3)  # Add semi-transparent grid[11](@ref)
plt.show()

# Filter data for China and UK comparison
china = dalys_data.loc[dalys_data["Entity"] == "China", ["DALYs", "Year"]]
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs", "Year"]]

