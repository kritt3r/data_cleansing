# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:32:24 2018

@author: prana

GOAL: Create dummy variables quickly
""" 
 
import pandas as pd

def quick_dummy(df,col_list):
#    Replace all Y and N columns with 1 and 0 
    df = df.replace('Y',1)
    df = df.replace('N',0)
    dummy_col = [col_list]
    for col in dummy_col:
        df = pd.concat([df,pd.get_dummies(df[col],prefix=col)],axis =1)
    return df

print('To use: pass dataframe, and a list of columnst to create dummies of')
