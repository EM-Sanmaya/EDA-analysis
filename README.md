# README: Traffic Accidents Data Analysis

## Project Overview
This project focuses on analyzing a dataset containing traffic accident records from 2017. The primary objectives of the analysis are to clean and preprocess the data, perform statistical analysis, and visualize key trends. This analysis helps in identifying accident patterns, peak hours, and relationships between different variables, which can be useful for traffic management and accident prevention strategies.

## Dataset Information
- **File Name:** `accidents_2017.csv`
- **Key Columns:** 
  - `Weekday`, `Month`, `Part of the day`, `District Name`, `Neighborhood Name`
  - `Hour`, `Victims`, `Mild injuries`, `Serious injuries`, `Vehicles involved`
- **Data Sources:**
  - The dataset is assumed to be sourced from traffic department records, government reports, or open-source accident databases.
- **Objective:** Identify patterns in accident occurrences, understand relationships between different variables, and derive insights that can help reduce accidents.

## Steps in the Analysis

### 1. Data Cleaning
- **Handling Missing Values:** 
  - Replaced 'Unknown' values with `NaN` to ensure proper data handling during analysis.
- **Standardizing Categorical Data:**
  - Trimmed extra spaces and capitalized the first letter in categorical columns (`Weekday`, `Month`, `Part of the day`, `District Name`, and `Neighborhood Name`) for consistency.
- **Converting Month Names to Numerical Format:**
  - Converted month names into numerical values (January = 1, February = 2, etc.) to facilitate time-series analysis.
- **Outlier Treatment using IQR Method:**
  - Used the interquartile range (IQR) method to detect and remove extreme values in numerical columns such as `Victims`, `Mild injuries`, `Serious injuries`, and `Vehicles involved`.
  - Ensured that only reasonable data points were retained for accurate statistical modeling.

### 2. Univariate Analysis
- **Histograms:**
  - Plotted the distribution of `Victims`, `Mild injuries`, `Serious injuries`, and `Vehicles involved` using histograms.
  - Helped visualize the frequency, spread, and skewness of accident-related statistics.
- **Box Plots:**
  - Created box plots for numerical variables to detect outliers and understand the central tendency.
  - Showed whether data distributions were symmetric or had extreme values.

### 3. Bivariate Analysis
- **Scatter Plots:**
  - Explored relationships between `Hour` and other numerical variables:
    - `Hour` vs `Victims`: Identified accident frequency trends during the day.
    - `Hour` vs `Mild injuries`: Analyzed at what times minor injuries were most frequent.
    - `Hour` vs `Serious injuries`: Investigated whether severe accidents occurred more at specific times.
  - Helped identify peak accident hours and trends over different time slots.

### 4. Multivariate Analysis
- **Correlation Matrix & Heatmap:**
  - Computed correlation coefficients between `Victims`, `Mild injuries`, `Serious injuries`, and `Vehicles involved`.
  - Used a heatmap to visualize the relationships between these variables:
    - Strong correlations indicate dependencies, e.g., higher victims count correlating with more vehicles involved.
    - Weak correlations suggest independent occurrences of certain accidents.

### 5. Saving Cleaned Data
- The cleaned dataset was saved as `cleaned_accidents_data.csv` for further statistical modeling or predictive analysis.
- This file can be used for machine learning models, policy evaluation, or urban planning studies.

## Output Files
- `histograms_accidents.png`: Histogram plots showing the distribution of numerical variables.
- `boxplots_accidents.png`: Box plots highlighting outliers and central tendencies.
- `scatter_plots_accidents.png`: Scatter plots showing relationships between accident time and severity.
- `heatmap_accidents.png`: Correlation heatmap displaying variable dependencies.
- `cleaned_accidents_data.csv`: The final cleaned dataset ready for further analysis.

## Insights & Findings
- **Time-Based Analysis:**
  - Certain hours of the day (morning and evening rush hours) showed a higher number of accidents.
  - Midnight and early morning accidents were more likely to result in serious injuries.
- **Severity of Accidents:**
  - Accidents involving more vehicles were correlated with a higher number of victims.
  - Mild injuries were more common than serious injuries, but some patterns indicated severe accidents in specific time windows.
- **Geographical Impact:**
  - Further analysis can explore whether specific districts or neighborhoods have higher accident rates.
  - Policy measures like better lighting, stricter traffic laws, or improved road conditions could be targeted at high-risk areas.

## Conclusion
This project provides an in-depth exploration of traffic accident data, highlighting key insights using statistical and visual analysis. The findings can assist in policymaking, traffic control measures, and future accident prevention strategies. Further exploration using machine learning techniques can enhance predictive capabilities to proactively reduce accident occurrences.

