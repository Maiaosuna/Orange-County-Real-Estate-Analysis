# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from pandas import read_csv
import numpy as np
import os
# start by importing the data files:
    # Directly after importing each file I'll be cleaning, formatting, and converting data types
    # for seamless merging between dataframes
    
prop_char = pd.read_csv("c:/code_and_data/code_and_data/data/python and r data/property_characteristics.csv")
# make sure 'propertyusecode' is a string, not an integer
prop_char['propertyusecode'] = prop_char['propertyusecode'].astype(str)
# format 'datebuilt' to appear as Year, month, day
prop_char['datebuilt'] = pd.to_datetime(prop_char['datebuilt'], format='%Y%m%d', errors='coerce')

locations = pd.read_csv("c:/code_and_data/code_and_data/data/python and r data/cities_and_zipcodes.csv")


sales = pd.read_csv("c:/code_and_data/code_and_data/data/python and r data/sales_dates_and_prices.csv")
# format 'saledate' to appear as Year, month, day
sales['saledate'] = pd.to_datetime(sales['saledate'], format='%Y%m%d', errors='coerce')

# Here i'm merging the dataframes
# I'm starting with the sales data since the sales transactions are the main focus of this analysis
    # sales, locations, and prop_char all have 'pid' (property ID) specific to each property
# merge sales and locations on 'pid'
merged_df = pd.merge(sales, locations, on='pid', how='left')
# merge merge_df with the prop_char data on 'pid'
merged_df = pd.merge(merged_df, prop_char,on='pid', how='left')


# Metric Calculations and table organization:
    # I want to calculate the age of the property at the time of sale
    # this will give more insight than just the build date
merged_df['property_age_at_sale'] = (merged_df['saledate'].dt.year - merged_df['datebuilt'].dt.year).fillna(0).astype(int)
    # some of property ages are negative so I'll replace them with 0
merged_df['property_age_at_sale'] = merged_df['property_age_at_sale'].clip(lower=0)
    # I want to know the price per square foot, which is a common/important real estate metric
merged_df['price_per_sqft'] = (merged_df['saleprice'] / merged_df['totalareasqft'].replace(0, np.nan))

    # Here I'm ordering the columns for easier readability 
    # I want to group related information together so the table makes more sense
columns = [
    'pid',
    'saledate',
    'saleprice',
    'situscity',
    'situszip',
    'propertyusecode',
    'totalareasqft', 
    'totalcamaareasqft',
    'totalbedroom', 
    'totalbath',
    'datebuilt', 
    'property_age_at_sale', 
    'price_per_sqft'
    ]

# convert 'saleprice' and 'totalareasqft' into numeric values
merged_df['saleprice'] = pd.to_numeric(merged_df['saleprice'], errors='coerce')
merged_df['totalareasqft'] = pd.to_numeric(merged_df['totalareasqft'], errors='coerce')

# Filtering out properties with unrealistic square footage (over 15,000)
# and property values (over 2M)
max_sqft = 15000
max_price = 2000000

# 'mod' - modified columns
mod = (merged_df['saleprice'] > 0) & \
      (merged_df['saleprice'] <= max_price) & \
      (merged_df['totalareasqft'] > 0) & \
      (merged_df['totalareasqft'] <= max_sqft)
# .loc to apply modification to final_df and specified columns
final_df = merged_df.loc[mod, columns].copy()


# I want to determine how totalareasqft, number of bathrooms, and number of bedrooms
# predict a property's value
import scipy
from scipy import stats

variables = ['totalareasqft', 'totalbedroom', 'totalbath']

for variable in variables:
    regression_df = final_df[['saleprice', variable]].dropna()
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(
        regression_df[variable],
        regression_df['saleprice']
        )
    # calculate R-squared to determine how much of the varianace in property value 
    # is explained by the independent variables
    r_squared = r_value**2
    
    # (" \n") for exta space between each result
    print("  \n")
    print(f"Analysis for: {variable}")
    print("--" * 30)
    

    # print R-Squared as percentage with 2 decimal places
    print(f"R-Squared: {r_squared:.4f} ({r_squared:.2%})")
    # print P-value in scientific notation
    print(f"P-Value: {p_value: .4e}")
    if p_value < 0.05:
        print("Statistically significant.")
    else: 
        print("NOT statistically significant.")



import statsmodels.formula.api as smf

# I want to determine how much of the variance in sale price is explained by location (zip code)
final_df['situszip'] = final_df['situszip'].astype('category')
model = smf.ols(formula = 'saleprice ~ C(situszip)', data = final_df)
results = model.fit()

adj_r_squared = results.rsquared_adj
f_stat = results.f_pvalue
print("  \n")
print(f"Analysis for: 'situszip' (Location)")
print("--" * 30)
print(f"Adjusted R-Squared: {adj_r_squared:.4f} ({adj_r_squared: .2%})")
print(f"P-value (F-Statistic): {f_stat:.4f}")
if f_stat < 0.05:
    print("Statistically significant")
else:
    print("NOT statistically significant")


# download final_df table to import into tableau
output_location =("c:/code_and_data/code_and_data/data/python and r data")
file_name = 'orange_county_market_data.csv'
file_path = os.path.join(output_location, file_name)

final_df.to_csv(file_path, index=False)
