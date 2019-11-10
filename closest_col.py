# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 15:27:17 2018

@author: prana

GOAL: Find how many unique values between two columns are similar
helps in matching columns from seperate dataframes that should be same
"""

import pandas as pd

def unique_diff(df1,df2, col1, col2):
    df1_col = df1.ix[:col1]
    df2_col = df2.ix[:col2]
    count_1 = len(df1.col.unique())
    count_2 = len(df2.col.unique())
    count_both = len(pd.concat([df1_col,df2_col]).unique())
    count_total = count1 + count2
    diff = count_total - count_both
    diff_perc = round(diff/count_total * 100,2)
    sent = ('%s unique overlap values, %s%% of total' % (diff, diff_perc))
    print(sent)
    return sent, diff, diff_perc
    
def closest_col(df1,df2):
    val= pd.DataFrame(columns = ['closest','%','val'])
    
    for col1 in df1.columns:
        diffmax = -1
        closest _col = ''
        for col2 in df.columns:
            sent, diff, diff_perc = unique_diff(df1,df2,col1,col2)
            
            if diff_perc > diff_max:
                diff_max = diff_perc
                diff_max_val = diff
                
                closest_col = col2
        print('Closest column to %s is %s with %s%% match' % (col1,closest_col, diff_max))
        
        val.loc[col1] = [closest_col,diff_max,diff_max_val]
    return val