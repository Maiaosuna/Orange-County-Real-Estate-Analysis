# What Determines Property Value? A Case Study of Single-Family Homes in Orange County, FL

# Project Overview

This project performs a comprehensive analysis of the single-family residential real estate market in Orange County, FL. The goal is to move beyond visual analysis to statistically identify the key drivers in property values.

The analysis answers the question “Which characteristics of a single family home (size, features, or location) have the most significant impact on its property value?”

The project demonstrates a data analysis workflow including:

* Data cleaning, preparation, and feature engineering in Python  
* Handling data quality issues and outliers by filtering an initial dataset of 156,664 properties down to a clean dataset of record for analysis  
* Exploratory data visualization in Tableau  
* Statistical modeling (linear regression) and hypothesis testing in Python to quantify the impact of various characteristics

The output is a clean dataset, a summary of key statistical findings, and an interactive Tableau dashboard for visual exploration.

# Technologies Used

* Python: Used for data cleaning, preparation, and statistical analysis  
  * Pandas: For data manipulation, merging, and cleaning raw csv files  
  * SciPy and Statsmodels: For preparing linear regression analysis to calculate R-squared and P-values, to provide statistical evidence conclusions.

* Tableau Public: Used for all data visualization (geographic maps, bar charts, scatter plots) to explore trends and present final findings in an interactive dashboard.  
* Excel: Used for initial data validation to determine quality issues

# How to Use This Repository

The primary outputs for this project are the final dataset and the analytical conclusions.

* orange\_county\_market\_data.csv: The final dataset ready for use in any BI tool  
* orange\_county\_market\_dashboard.twbx: The final tableau workbook containing all visualizations and the interactive dashboard  
* Orange\_county\_market\_analysis (readme): A detailed summary of the project methodology, key findings, and final conclusions

# How to Re-generate the Analysis

Steps to re-run the project and generate the final dataset:

1. Setup:  
   1. Python Libraries (pandas, scipy, statsmodels)  
   2. Place raw data files (property\_characteristics.csv, cities\_and\_zipcodes.csv, sales\_dates\_and\_prices.csv) into the same location and/or update file path script  
   3. Update file directory to save the final dataset in the same location  
2. Run the Script

# Summary of Key Findings

The statistical analysis revealed a hierarchy of what drives property value in this market. All of which were found to be statistically significant (P-value \< 0.05).

The statistical analysis revealed what drives property value this market. The primary variables are as follows (descending) with their respective R-squared values:
1. Total Square Footage (strongest): 51.56%  
2. Number of Bathrooms: 45.02%  
3. Location (Zip Code): 30.87%  
4. Number of Bedrooms (Moderate): 20.25%


A multiple regresion analysis was performed to quantify the specific financial impact of the top features:
1. Every additional bathroom adds approx. $34,500 to the final sale price.
2. Every additional square foot adds approx. $124 to the final sale price.


Business Application:
The findings from this analysis provide a framework for real estate investors to make more strategic decisions. This valuation model can be used to:
1. Identify Undervalued Assets
2. Calcualte Renovation ROI
3. Inform Offering Strategy

Conclusion: The analysis concludes that a property’s physical characteristics, specifically its total square footage and number of bathrooms, are the most significant predictors of its final sale price.

Interactive Dashboard: [https://public.tableau.com/MaiaOsuna](https://public.tableau.com/shared/JG9DBC9MW?:display_count=n&:origin=viz_share_link)

