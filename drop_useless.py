# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:23:00 2018

@author: prana

GOAL: Drop all columns that are minimal added value
        drops columns with only a single unique value or
        with more than half null values
"""

import pandas as pd

def drop_useless(df):
    col = list()
    print('Dropped Variables')
    for x in df.columns:
        if len(df[x].unique()) == 1 or df[x].isnull().sum() > len(df[x])/2:
            print(str(x))
            col.append(x)
    return col

print('To use: df.drop(col)')