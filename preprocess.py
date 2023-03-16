# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:30:50 2023

@author: Soumyajit Saha
"""

import pandas as pd

covidData = pd.read_csv('COVID-19.csv', index_col=0)


covidData = covidData.drop(['Age', 'Sex', 'Source'], axis = 1)

activeData = covidData[covidData['Type'] == 'Active']
confirmedData = covidData[covidData['Type'] == 'Confirmed']
deathData = covidData[covidData['Type'] == 'Deaths']
hospitalizedData = covidData[covidData['Type'] == 'Hospitalized']

vaccineData = covidData = pd.read_csv('Vaccine.csv', index_col=0)
