# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 12:55:31 2023

@author: Soumyajit Saha
"""

import pandas as pd

def aggregate(month, year):
    
    month_df = pd.DataFrame(columns = ['SLP', 'PS', 'H', 'T', 'U', 'V', 'QV', 'O3', 'month', 'day', 'year'])
    
    if month == 'January':
        mon = 1
        days = 31
    elif month == 'February':
        mon = 2
        days = 29
    elif month == 'March':
        mon = 3
        days = 31
    elif month == 'April':
        mon = 4
        days = 30
    elif month == 'May':
        mon = 5
        days = 31
    elif month == 'June':
        mon = 6
        days = 30
    elif month == 'July':
        mon = 7
        days = 31
    elif month == 'August':
        mon = 8
        days = 31
    elif month == 'September':
        mon = 9
        days = 30
    elif month == 'October':
        mon = 10
        days = 31
    elif month == 'November':
        mon = 11
        days = 30
    elif month == 'December':
        mon = 12
        days = 31
    
    # days = 1
    for day in range(1, days + 1):
        df = pd.read_csv('2020' + "{:02d}".format(mon) + "{:02d}".format(day) + '_final.csv')
        df = df.fillna(0)
        df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S')
        df['month'] = pd.DatetimeIndex(df['time']).month
        df['day'] = pd.DatetimeIndex(df['time']).day
        df['year'] = pd.DatetimeIndex(df['time']).year
        df = df.drop(columns = ['time', 'lon', 'lat', 'lev'])
        df = df.groupby(['day']).mean()
        # print(df)
        month_df = month_df.append({'SLP': df['SLP'].iloc[0], 'PS': df['PS'].iloc[0], 'H': df['H'].iloc[0], 'T': df['T'].iloc[0], 'U': df['U'].iloc[0], 'V': df['V'].iloc[0], 'QV': df['QV'].iloc[0], 'O3': df['O3'].iloc[0], 'month': mon, 'day': day, 'year': year}, ignore_index = True)
        print('days done: ' + str(day))
        
    month_df.to_csv(month + '.csv', index = False)

    

if __name__ == '__main__':
    aggregate('April', 2020)