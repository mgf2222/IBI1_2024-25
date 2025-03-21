# ========== Pseudocode Structure ==========
'''
1. Data Preparation:
    - Initialize two datasets:
        a. UK constituent countries population
        b. Zhejiang-neighboring Chinese provinces population
2. Data Processing:
    - Sort both datasets in descending order
    - Print sorted results
3. Visualization:
    - Create comparative pie charts:
        a. Configure plot dimensions and style
        b. Generate UK population distribution chart
        c. Generate Chinese provinces distribution chart
        d. Add percentage labels and styling
4. Display visualizations
'''

# ========== DATA PREPARATION ==========
# UK constituent countries population (millions)
uk_countries = [57.11, 3.13, 1.91, 5.45]
uk_nations = ["England", "Wales", "Northern Ireland", "Scotland"]

# Zhejiang-neighboring Chinese provinces population (millions)
zhejiang_neighbours = [65.77, 41.88, 45.28, 61.27, 85.15]
china_provinces = ["Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"]

# ========== DATA PROCESSING ==========
# PSEUDOCODE: SORT POPULATION DATA DESCENDING
uk_sorted = sorted(uk_countries, reverse=True)
print("Sorted UK countries population (in millions):")
print(uk_sorted)

# PSEUDOCODE: SORT NEIGHBORING PROVINCES DESCENDING
china_sorted = sorted(zhejiang_neighbours, reverse=True)
print("\nSorted Zhejiang-neighboring provinces population (in millions):")
print(china_sorted)

# ========== VISUALIZATION ==========
import matplotlib.pyplot as plt

# Configure plot aesthetics
plt.style.use('seaborn-v0_8-muted')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

# PSEUDOCODE: GENERATE UK POPULATION PIE CHART
ax1.pie(
    uk_countries,
    labels=uk_nations,
    autopct='%1.1f%%',
    startangle=90,
    shadow=True,
    colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
)
ax1.set_title('UK Countries Population Distribution', fontsize=14)

# PSEUDOCODE: GENERATE CHINESE PROVINCES PIE CHART
ax2.pie(
    zhejiang_neighbours,
    labels=china_provinces,
    autopct='%1.1f%%',
    startangle=90,
    shadow=True,
    colors=['#ff6666', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
)
ax2.set_title('Zhejiang-neighboring Provinces Population Distribution', fontsize=14)

# Finalize and display
plt.tight_layout()
plt.show()