# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 08:50:44 2019

@author: singhp5

PURPOSE: Additional Data Analysis Tool
"""

import pandas as pd
import datetime as dt


def read_clipboard():
    df = pd.read_clipboard()
    df.columns = [x.lower() for x in df.columns]
    print(df.iloc[0])
    return(df)
   
   
def read_excel(filename):
    df = pd.read_excel(filename)
    df.columns = [x.lower() for x in df.columns]
    print(df.iloc[0])
    return(df)
   
def read_csv(filename):
    df = pd.read_csv(filename)
    df.columns = [x.lower() for x in df.columns]
    print(df.iloc[0])
    return(df)
 

def prev_weekday(date):
    date = pd.to_datetime(date)
    date  -= dt.timedelta(days = 1)
    while date.weekday() > 4:
        date -= dt.timedelta(days = 1)
    return date

def print_col(df):
    print('\n'.join(df.columns))