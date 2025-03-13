# README: Traffic Accidents Data Analysis with Inferences

## Project Overview
This project analyzes a dataset containing traffic accident records from 2017. The analysis focuses on cleaning the data, performing statistical analysis, visualizing key patterns, and deriving meaningful insights. The goal is to understand accident trends, peak hours, and relationships between different factors that contribute to accidents.

## Dataset Information
- **File Name:** `accidents_2017.csv`
- **Key Variables:**
  - `Weekday`, `Month`, `Part of the day`, `District Name`, `Neighborhood Name`
  - `Hour`, `Victims`, `Mild injuries`, `Serious injuries`, `Vehicles involved`
- **Objective:** Identify patterns in accident occurrences, examine severity levels, and explore correlations between accident-related variables.

## Steps in the Analysis

### 1. Data Cleaning
- Replaced 'Unknown' values with `NaN` for better handling.
- Standardized categorical values (trimmed spaces, capitalized words for consistency).
- Converted `Month` names into numerical format for time-series analysis.
- Treated outliers in `Victims`, `Mild injuries`, `Serious injuries`, and `Vehicles involved` using the IQR method.

### 2. Univariate Analysis
- **Histograms:** Showed the distribution of accident-related numerical variables.
- **Box Plots:** Helped detect outliers and understand central tendencies.

### 3. Bivariate Analysis
- **Scatter Plots:** Examined relationships between `Hour` and `Victims`, `Mild injuries`, and `Serious injuries` to identify peak accident times.

### 4. Multivariate Analysis
- **Correlation Heatmap:** Provided insights into relationships between accident severity and other variables.

### 5. Saving Cleaned Data
- The cleaned dataset is saved as `cleaned_accidents_data.csv` for further research or predictive modeling.

## Output Files
- `histograms_accidents.png`: Distribution of numerical accident-related variables.
- `boxplots_accidents.png`: Outlier detection and central tendency visualization.
- `scatter_plots_accidents.png`: Accident trends over time and severity analysis.
- `heatmap_accidents.png`: Correlation analysis.
- `cleaned_accidents_data.csv`: Final cleaned dataset.

## Inferences from the Analysis

### 1. Accident Frequency and Timing
- **Histogram Analysis:**
  - The distribution of `Victims` and `Injuries` is right-skewed, indicating that most accidents have a low number of victims, but a few severe cases exist.
  - `Vehicles Involved` shows a similar pattern, with most accidents involving only a few vehicles.
- **Scatter Plot Analysis:**
  - Peak accident hours occur during rush hours (morning and evening), indicating high traffic density as a major contributing factor.
  - Late-night accidents, though fewer in number, tend to result in more severe injuries.

### 2. Severity of Accidents
- **Box Plot Analysis:**
  - Outliers suggest that while most accidents have mild consequences, some incidents involve significantly higher casualties and injuries.
  - `Serious injuries` have a wider spread, indicating that although rare, severe accidents have a high impact.

### 3. Correlations and Relationships
- **Heatmap Analysis:**
  - A strong correlation exists between `Victims` and `Vehicles Involved`, suggesting that multi-vehicle accidents tend to have more casualties.
  - `Mild Injuries` and `Serious Injuries` show a positive correlation, meaning that more accidents with minor injuries also tend to have some serious injuries.
  - The correlation between `Hour` and `Serious Injuries` is weaker, indicating that while accidents are time-dependent, their severity might be influenced by other factors such as road conditions or driver behavior.

### 4. Potential Areas for Policy and Safety Improvements
- **Time-Based Interventions:**
  - Since most accidents occur during rush hours, implementing stricter traffic regulations, better traffic management, and speed control measures during these periods could help reduce incidents.
  - Late-night severe accidents indicate the need for enhanced lighting, better surveillance, and stricter enforcement of driving laws.
- **District-Specific Policies:**
  - Further geographic analysis could help pinpoint high-risk areas where accidents are more frequent, leading to localized safety measures.
- **Public Awareness Programs:**
  - Campaigns focused on safe driving during high-risk periods could reduce accident severity and frequency.

## Conclusion
This analysis provides key insights into traffic accident trends, helping to understand accident causes and their severity. The findings can assist in policymaking, traffic control measures, and safety initiatives. Further research using machine learning models can enhance predictive capabilities to proactively prevent accidents.





