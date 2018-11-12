# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:47:28 2018

@author: prana
 
GOAL: Return previous weekday
"""

import datetime as dt

def prev_weekday(date):
    date  -= dt.timedelta(day = 1)
    while date.weekday() > 4:
        date -= dt.timedelta(days = 1)
    return date

print('To use: pass date as current day to return previous weekday)