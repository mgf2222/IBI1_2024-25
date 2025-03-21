# ========== Pseudocode Structure ==========
'''
1. Initialize dictionary with language popularity data
    - Key: Language name (string)
    - Value: Usage percentage (float)
2. Print formatted dictionary
3. Create bar plot visualization:
    a. Extract keys/values from dictionary
    b. Configure plot dimensions and style
    c. Add percentage labels above bars
    d. Set axis labels and title
    e. Display plot
4. Retrieve and display usage percentage for specified language
'''

# Create language popularity dictionary
language_popularity = {
    "JavaScript": 62.3,
    "HTML": 52.9,
    "Python": 51.0,
    "SQL": 51.0,
    "TypeScript": 38.5
}

# Display dictionary contents
print("Programming Language Popularity Data:")
print(language_popularity)

# Generate bar plot visualization
import matplotlib.pyplot as plt

# Configure plot data
languages = list(language_popularity.keys())
percentages = list(language_popularity.values())

# Initialize plot canvas
plt.figure(figsize=(10, 6))
bars = plt.bar(languages, percentages, color='#4C72B0')

# Add value labels
for index, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., 
             height + 0.5,
             f'{percentages[index]}%',
             ha='center', 
             va='bottom')

# Customize plot appearance
plt.title('Global Programming Language Popularity (2024)', fontsize=14, pad=20)
plt.xlabel('Programming Languages', fontsize=12, labelpad=15)
plt.ylabel('Usage Percentage (%)', fontsize=12, labelpad=15)
plt.ylim(0, 70)
plt.grid(axis='y', alpha=0.3)

# Display visualization
plt.tight_layout()
plt.show()

# Language query implementation
# ====== Configurable Parameter ======
TARGET_LANGUAGE = "Python"
# ====================================

# Retrieve and display usage data
usage = language_popularity.get(TARGET_LANGUAGE, None)
if usage:
    print(f"\nUsage percentage for {TARGET_LANGUAGE}: {usage}%")
else:
    print(f"\nLanguage '{TARGET_LANGUAGE}' not found in dataset")