# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:38:03 2018

@author: prana

GOAL: Find columns with most variance, supposedly most added value to models

"""

#   unique id must be some unique id for each instance, can be index
def find_unique(df,col):
    x = df.groupby(col)['unique id'].nunique()
    print(x)
    print()
    return len(x)

print('To use: df is the data, col is column to be analyzed)

def check_unique(df,size):
    for col in df.columns:
        if df[col].nunique() > size:
            pass
        else:
            find_unique(df,col)
            
print('To use: df is the data, size is number of unique values that is considered useful)