# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 15:09:48 2018

@author: prana

GOAL: Quickly slim down dataset
"""

import pandas as pd


def slim(df):
#    Drop columns with only na values
    bcol = df.columns
    df = df.dropna(axis = 1, how = 'all')
#    Drop columns with only 1 value
    df = df.drop(singledrop(df), axis = 1)
    
    df = df.drop_extra(df)
    
#    Order the columns alphabetically for ease of access
    df = df.reindex_axis(sorted(df.columns),axis = 1)
    
    return df

def single_drop(df):
    col = list()
    
    for x in df.columns:
        if len(df[x].unique()) == 1:
            col.append(x)
    return col