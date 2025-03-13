import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==============================
# STEP 1: LOAD & CLEAN THE DATA
# ==============================

# Load Accidents Dataset
file_path = "accidents_2017.csv"  # Update with correct path if needed
df = pd.read_csv(file_path)
print("Missing values before handling:")
print(df.isnull().sum())
print(df.dtypes)
# Number of unique values
print(df.nunique())

# Descriptive statistics for numerical features
print(df.describe())

# Replace 'Unknown' values with NaN for better handling
df.replace("Unknown", np.nan, inplace=True)

# Standardize categorical values
df['Weekday'] = df['Weekday'].str.strip().str.title()
df['Month'] = df['Month'].str.strip().str.title()
df['Part of the day'] = df['Part of the day'].str.strip().str.title()
df['District Name'] = df['District Name'].str.strip().str.title()
df['Neighborhood Name'] = df['Neighborhood Name'].str.strip().str.title()

# Convert 'Month' to numerical representation for better analysis
month_order = {month: index for index, month in enumerate([
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], 1)}
df['Month'] = df['Month'].map(month_order)

# Treat outliers in 'Victims' and injury-related columns using IQR method
num_cols = ['Mild injuries', 'Serious injuries', 'Victims', 'Vehicles involved']
for col in num_cols:
    Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound, upper_bound = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

# ==============================
# STEP 2: UNIVARIATE ANALYSIS
# ==============================

# Histograms
fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for i, col in enumerate(num_cols):
    axes[i].hist(df[col], bins=20, color='skyblue', edgecolor='black')
    axes[i].set_title(f"Distribution of {col}")
plt.tight_layout()
plt.savefig("histograms_accidents.png")
plt.show()

# Box Plots
fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for i, col in enumerate(num_cols):
    axes[i].boxplot(df[col].dropna(), patch_artist=True, boxprops=dict(facecolor="lightblue"))
    axes[i].set_title(f"Box Plot of {col}")
plt.tight_layout()
plt.savefig("boxplots_accidents.png")
plt.show()

# ==============================
# STEP 3: BIVARIATE ANALYSIS
# ==============================

# Scatter Plots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].scatter(df['Hour'], df['Victims'], color='blue', alpha=0.5)
axes[1].scatter(df['Hour'], df['Mild injuries'], color='red', alpha=0.5)
axes[2].scatter(df['Hour'], df['Serious injuries'], color='green', alpha=0.5)
axes[0].set_title("Hour vs Victims")
axes[1].set_title("Hour vs Mild Injuries")
axes[2].set_title("Hour vs Serious Injuries")
plt.tight_layout()
plt.savefig("scatter_plots_accidents.png")
plt.show()

# ==============================
# STEP 4: MULTIVARIATE ANALYSIS
# ==============================

# Correlation Matrix Heatmap
correlation_matrix = df[num_cols].corr()
fig, ax = plt.subplots(figsize=(6, 5))
cax = ax.matshow(correlation_matrix, cmap="coolwarm")

# Add correlation values inside heatmap
for (i, j), val in np.ndenumerate(correlation_matrix):
    ax.text(j, i, f"{val:.2f}", ha='center', va='center', color='white')

plt.xticks(range(len(num_cols)), num_cols, rotation=45)
plt.yticks(range(len(num_cols)), num_cols)
plt.colorbar(cax)
plt.title("Correlation Heatmap")
plt.savefig("heatmap_accidents.png")
plt.show()

# ==============================
# STEP 5: SAVE CLEANED DATA
# ==============================

df.to_csv("cleaned_accidents_data.csv", index=False)
print("Cleaned dataset saved as 'cleaned_accidents_data.csv'")

print("Analysis completed successfully!")
