# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 15:51:20 2018

@author: prana

GOAL: Returns columns with excessively 1 unique value

"""

df missing_val(df):
    
    part = .5
    for col in df.columns:
        top_count = df[col].value_counts().max()
        total = len(df)
        per = top_count / total
        top_value = df[col].value_counts().idxmax()
        
        if perc > part:
            print('%s top value is %s of %s which is %s%%' % (col,top_value,top_count,perc))