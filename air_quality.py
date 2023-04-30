# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 15:39:39 2023

@author: Soumyajit Saha
"""

import pandas as pd

months = ['January', 'February', 'March', 'April', 'May']

df = pd.read_csv(months[0] + '.csv')

for month in months[1:]:
    df = pd.concat([df, pd.read_csv(month + '.csv')], sort = False)
    
df.to_csv('air_quality.csv')