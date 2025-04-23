import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("D:/IBI/IBImidterm/IBI1_2024-25/Practical10") 
print(os.getcwd())
print(os.listdir())
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
"""print(dalys_data.head(6))
dalys_data.info()
print(dalys_data.describe())

print(dalys_data.iloc[0:10,2])
print(dalys_data.loc[2:4,"Year"])
my_columns = [True, True, False, True] 
print(dalys_data.iloc[0:3,my_columns])

a_1990 = dalys_data["Year"] == 1990
dalys_1990 = dalys_data.loc[a_1990, "DALYs"]
print(dalys_1990)"""
# 筛选英国数据（Entity为"United Kingdom"）
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs","Year"]]
uk_mean = uk["DALYs"].mean()

# 筛选法国数据（Entity为"France"）
france = dalys_data.loc[dalys_data["Entity"] == "France", ["DALYs","Year"]]
france_mean = france["DALYs"].mean()

print(f"英国平均DALYs: {uk_mean:.2f}")
print(f"法国平均DALYs: {france_mean:.2f}")

plt.plot(uk.Year, uk.DALYs, 'b+')  # 'b+'表示蓝色+号标记
plt.title("英国DALYs随时间变化趋势")
plt.xlabel("年份")
plt.ylabel("DALYs")
plt.show()
plt.plot(uk.Year, uk.DALYs, 'r--', label='英国DALYs')  # 红色虚线
plt.legend()
plt.show()

# 筛选中国和英国数据
china = dalys_data.loc[dalys_data["Entity"] == "China", ["DALYs", "Year"]]
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs", "Year"]]


