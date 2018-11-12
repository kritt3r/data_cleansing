# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:50:39 2018

@author: prana

GOAL: Read and compile txt files into dataframe

Source: Martjin Pieters
"""

import os 
import time
import glob
import shutil

def file2df(folder,outfilename, ext):
    ndir = os.getcwd()
    os.chdir(folder)
    filext = '*.%s' % ext
    
    with open(outfilename, 'wb') as outfile:
        for filename in glob.glob(filext):
            if filename == outfilename:
                continue
            with open(filename,'rb') as readfile:
                shutil.copyfileobj(readfile, outfile)
    os.chdir(ndir)