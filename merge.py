# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 21:25:20 2023

@author: Soumyajit Saha
"""

import pandas as pd

ItalyActiveData = pd.read_csv('Italy_Active_data.csv')
ItalyConfirmedData = pd.read_csv('Italy_Confirmed_data.csv')
ItalyDeathData = pd.read_csv('Italy_Death_data.csv')
ItalyHospitalizedData = pd.read_csv('Italy_Hospitalized_data.csv')
ItalyVaccineData = pd.read_csv('Italy_vaccine_data.csv')
ItalyVaccineData = ItalyVaccineData.fillna(0)
AirQuality = pd.read_csv('air_quality.csv')
AirQuality['Date'] = pd.to_datetime(dict(year=AirQuality.year, month=AirQuality.month, day=AirQuality.day), format='%Y-%m-%d')
AirQuality['Date'] = AirQuality['Date'].dt.strftime('%Y-%m-%d')
AirQuality = AirQuality.drop(['day', 'month', 'year'], axis = 1)

mergedData = ItalyActiveData.rename({'Cases': 'Active_cases', 'Cases_New': 'Active_cases_new'}, axis = 1)
mergedData['Confirmed_cases'] = ItalyConfirmedData['Cases']
mergedData['Confirmed_cases_new'] = ItalyConfirmedData['Cases_New']
mergedData['Death_cases'] = ItalyDeathData['Cases']
mergedData['Death_cases_new'] = ItalyDeathData['Cases_New']
mergedData['Hospitalized_cases'] = ItalyHospitalizedData['Cases']
mergedData['Hospitalized_cases_new'] = ItalyHospitalizedData['Cases_New']

mergedData = pd.merge(mergedData, ItalyVaccineData, on = 'Date', how = 'left')
mergedData = pd.merge(mergedData, AirQuality, on = 'Date', how = 'left')

mergedData = mergedData.fillna(0)

mergedData = mergedData.drop(['Type'], axis = 1)

mergedData.to_csv('Merged_Data.csv')


