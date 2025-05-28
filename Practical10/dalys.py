# Import libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
# Set working directory
os.chdir('Practical10')
#If the file cannot be read correctly, use the absolute path below
#os.chdir(r"D:\IBI\IBImidterm\IBI1_2024-25\Practical10")

# Load data
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print(dalys_data.iloc[0:10, 2]) #showing the third column (the year) for the first 10 rows(inclusive)
# DALYs data recorded in Afghanistan in the 10th year(1999) is 82624.94

# used a Boolean to show DALYs for all countries in 1990
data1990 = dalys_data[dalys_data["Year"] == 1990]
print(data1990.head())

# Filter and analyze UK/France data
# comput the mean DALYs in the UK and France
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs","Year"]]
uk_mean = uk["DALYs"].mean()
france = dalys_data.loc[dalys_data["Entity"] == "France", ["DALYs","Year"]]
france_mean = france["DALYs"].mean()
#  UK's DALYs are higher than French
print(f"UK Average DALYs: {uk_mean:.2f}")
print(f"France Average DALYs: {france_mean:.2f}")

# Plot UK DALYS trends over time
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.title("UK DALYs Trend Over Time")
plt.xticks(uk.Year, rotation=45)
plt.tight_layout()
plt.show()

plt.plot(uk.Year, uk.DALYs, 'r--', label='UK DALYs')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# The code answer another question
# Compare China and UK DALYS from 1990 to 2019
china = dalys_data.loc[dalys_data["Entity"] == "China", ["DALYs", "Year"]]
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs", "Year"]]

plt.figure(figsize=(10, 6))
plt.plot(china.Year, china.DALYs, 'r-', label='China')
plt.plot(uk.Year, uk.DALYs, 'b--', label='UK')
plt.title("DALYs Trend Comparison: China vs UK")
plt.xticks(uk.Year, rotation=45)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()