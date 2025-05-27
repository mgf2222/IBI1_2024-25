# Import libraries
import os
import pandas as pd
import matplotlib.pyplot as plt

# Load data
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Filter and analyze UK/France data
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs","Year"]]
uk_mean = uk["DALYs"].mean()
france = dalys_data.loc[dalys_data["Entity"] == "France", ["DALYs","Year"]]
france_mean = france["DALYs"].mean()

print(f"UK Average DALYs: {uk_mean:.2f}")
print(f"France Average DALYs: {france_mean:.2f}")

# Plot UK trends
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

# Compare China and UK
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