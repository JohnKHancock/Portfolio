# =============================================================================
# Utilities for Capstone Project - August 2018
# Udacity Machine Learning Nanodegree 2018
# jkhancock@gmail.com
# =============================================================================

# Import the libraries needed
import os
import numpy as np
import pandas as pd
import pprint as pp
import collections
from matplotlib import pyplot as plt
import seaborn as sns
from glob import glob




# =============================================================================
# Because duplicate feature names appear in the dataset,
# This function prepends a prefix to the appropriate feature
# =============================================================================

def prepend_col_names(df, prefix):
    for i in df.columns.values:
        if i in ["Team", "W", "L"]:
            next
        else:
            df.rename(columns={i : prefix + i}, inplace=True)
            
            
# =============================================================================
# This function reads in the the csv, prepends a prefix, combines the fielding, hitting, pitching by year csv files into
# one per year, and finally, it writes out to a csv.
# 
# =============================================================================
def mergeCSVs(directory, csv_name, output):
    os.chdir(directory)
    
    pitch_df= pd.DataFrame()
    offense_df= pd.DataFrame()
    fielding_df= pd.DataFrame()
    compiled_df = pd.DataFrame()
    
    files = glob("*.csv")
    for f in files:
        if "Pitching" in f:
            pitch_df = pd.read_csv(f)
            prepend_col_names(pitch_df, "PITCH_")
        elif "Hitting" in f:
            offense_df = pd.read_csv(f)
            prepend_col_names(offense_df, "OFF_")
        elif "Fielding" in f:
            fielding_df = pd.read_csv(f)
            prepend_col_names(fielding_df , "FIELD_")
        compiled_df = pd.concat([pitch_df, offense_df,fielding_df ], axis=1)
    os.chdir(output)
    compiled_df.to_csv(csv_name)  
    return  compiled_df       


# =============================================================================
# This function removes duplicate column names
# =============================================================================
def removeDuplicateFeatures(df, features_list):
    for col in df.columns.values:
        if ".1" in col:
            del df[str(col)]
            features_list.append(col)    

# =============================================================================
# This function cleans up the data by removing the percent symbol
# =============================================================================
def remove_percentages(percent):
    if isinstance(percent, str):
        percentlist = percent.split(' ')
        if '%' in percentlist:
              return (float(percentlist[0])/100)
        elif '%' in percent:
              return float(percent.strip('%'))/100
        else:
              return float(percent)
    else:
        return percent            

# =============================================================================
# This function detects outliers in a dataset if a feature exceeds the 
# interquartile range. Turkey's method.
# =============================================================================

def detect_outliers(features):

    cnt = collections.Counter()
    
    for feature in features.keys():
        
       # Calculate Q1 (25th percentile of the data) for the given feature
        Q1 = np.percentile(features[feature], 25)
        
        # Calculate Q3 (75th percentile of the data) for the given feature
        Q3 = np.percentile(features[feature], 75)
        
        # Use the interquartile range to calculate an outlier step (1.5 times the interquartile range)
        step = (Q3-Q1)*1.5
        
        # Display the outliers
        print("Data points considered outliers for the feature '{}':".format(feature))
        display(features[~((features[feature] >= Q1 - step) & (features[feature] <= Q3 + step))])
        for i in features[~((features[feature] >= Q1 - step) & (features[feature] <= Q3 + step))].index.values.astype(int):
            cnt[i] += 1
        
    # Select the indices for data points you wish to remove
    return cnt

        