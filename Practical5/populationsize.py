# Pseudocode 

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


# Define population data for UK constituent countries
# UK constituent countries population (in millions)
uk_countries = [57.11, 3.13, 1.91, 5.45]  # Population data for England, Wales, Northern Ireland, and Scotland
uk_nations = ["England", "Wales", "Northern Ireland", "Scotland"]  # Names of the UK constituent countries

# Define population data for Zhejiang-neighboring provinces in China
# Zhejiang-neighboring Chinese provinces population (in millions)
zhejiang_neighbours = [65.77, 41.88, 45.28, 61.27, 85.15]  # Population data for Zhejiang, Fujian, Jiangxi, Anhui, and Jiangsu
china_provinces = ["Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"]  # Names of the provinces


# Sort UK population data in descending order
uk_sorted = sorted(uk_countries, reverse=True)  # Sort the list from largest to smallest
print("Sorted UK countries population (in millions):")  # Print the sorted list
print(uk_sorted)

# Sort Chinese provinces population data in descending order
china_sorted = sorted(zhejiang_neighbours, reverse=True)  # Sort the list from largest to smallest
print("\nSorted Zhejiang-neighboring provinces population (in millions):")  # Print the sorted list
print(china_sorted)


# Import the pyplot module from matplotlib to create visualizations
import matplotlib.pyplot as plt

# Configure the visual style of the plots
plt.style.use('seaborn-v0_8-muted')  # Use a specific style for better aesthetics
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))  # Create a figure with two subplots side by side

# Create a pie chart for UK population distribution
ax1.pie(
    uk_countries,  # Population data
    labels=uk_nations,  # Labels for each slice
    autopct='%1.1f%%',  # Display percentage on each slice
    startangle=90,  # Start angle for the first slice
    shadow=True,  # Add shadow for depth
    colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Custom colors for each slice
)
ax1.set_title('UK Countries Population Distribution', fontsize=14)  # Set title for the chart

# Create a pie chart for Chinese provinces population distribution
ax2.pie(
    zhejiang_neighbours,  # Population data
    labels=china_provinces,  # Labels for each slice
    autopct='%1.1f%%',  # Display percentage on each slice
    startangle=90,  # Start angle for the first slice
    shadow=True,  # Add shadow for depth
    colors=['#ff6666', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']  # Custom colors for each slice
)
ax2.set_title('Zhejiang-neighboring Provinces Population Distribution', fontsize=14)  # Set title for the chart

# Adjust layout and display the plots
plt.tight_layout()  # Ensure all elements fit well within the figure
plt.show()  # Display the charts