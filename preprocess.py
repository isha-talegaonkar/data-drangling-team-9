# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:30:50 2023

@author: Soumyajit Saha
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

covidData = pd.read_csv('COVID-19.csv')


covidData = covidData.drop(['Age', 'Sex', 'Source'], axis = 1)

activeData = covidData[covidData['Type'] == 'Active']
confirmedData = covidData[covidData['Type'] == 'Confirmed']
deathData = covidData[covidData['Type'] == 'Deaths']
hospitalizedData = covidData[covidData['Type'] == 'Hospitalized']

vaccineData = covidData = pd.read_csv('Vaccine.csv')





ItalyActiveData = activeData[activeData['ID'] == 'IT'].fillna(method = 'ffill').drop_duplicates(subset='Date', keep="first")
ItalyActiveData['Date'] = pd.to_datetime(ItalyActiveData['Date'], format='%Y-%m-%d')
# ItalyActiveData = ItalyActiveData[ItalyActiveData['Cases_New'] >= 0]
# ItalyActiveData[ItalyActiveData['Cases_New'] < 0] = 0

ItalyConfirmedData = confirmedData[confirmedData['ID'] == 'IT'].fillna(method = 'ffill').drop_duplicates(subset='Date', keep="first")
ItalyConfirmedData['Date'] = pd.to_datetime(ItalyConfirmedData['Date'], format='%Y-%m-%d')
# ItalyConfirmedData = ItalyConfirmedData[ItalyConfirmedData['Cases_New'] >= 0]
# ItalyConfirmedData[ItalyConfirmedData['Cases_New'] < 0] = 0

ItalyDeathData = deathData[deathData['ID'] == 'IT'].fillna(method = 'ffill').drop_duplicates(subset='Date', keep="first")
ItalyDeathData['Date'] = pd.to_datetime(ItalyDeathData['Date'], format='%Y-%m-%d')
# ItalyDeathData = ItalyDeathData[ItalyDeathData['Cases_New'] >= 0]
# ItalyDeathData[ItalyDeathData['Cases_New'] < 0] = 0

ItalyHospitalizedData = hospitalizedData[hospitalizedData['ID'] == 'IT'].fillna(method = 'ffill').drop_duplicates(subset='Date', keep="first")
ItalyHospitalizedData['Date'] = pd.to_datetime(ItalyHospitalizedData['Date'], format='%Y-%m-%d')
# ItalyHospitalizedData = ItalyHospitalizedData[ItalyHospitalizedData['Cases_New'] >= 0]
# ItalyHospitalizedData[ItalyHospitalizedData['Cases_New'] < 0] = 0

ItalyVaccineData = vaccineData[vaccineData['ID'] == 'IT'].fillna(method = 'ffill').drop_duplicates(subset='Date', keep="first")
ItalyVaccineData['Date'] = pd.to_datetime(ItalyVaccineData['Date'], format='%Y-%m-%d')

plt.figure(figsize=(20, 10))
plt.plot(ItalyActiveData['Date'], ItalyActiveData['Cases'], label='Active Data')
plt.plot(ItalyConfirmedData['Date'], ItalyConfirmedData['Cases'], label='Confiremd Data')
plt.plot(ItalyDeathData['Date'], ItalyDeathData['Cases'], label='Death Data')
plt.plot(ItalyHospitalizedData['Date'], ItalyHospitalizedData['Cases'], label='Hospitalized Data')
# plt.plot(ItalyVaccineData['Date'], ItalyVaccineData['DoseValue'], label='Vaccine Data')

plt.title('CASES TRENDS IN ITALY')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=100))
plt.gcf().autofmt_xdate()
plt.legend()
plt.show()

plt.figure(figsize=(20, 10))
plt.plot(ItalyActiveData['Date'], ItalyActiveData['Cases_New'], label='Active Data')
plt.plot(ItalyConfirmedData['Date'], ItalyConfirmedData['Cases_New'], label='Confiremd Data')
plt.plot(ItalyDeathData['Date'], ItalyDeathData['Cases_New'], label='Death Data')
plt.plot(ItalyHospitalizedData['Date'], ItalyHospitalizedData['Cases_New'], label='Hospitalized Data')
# plt.plot(ItalyVaccineData['Date'], ItalyVaccineData['DoseValue'], label='Vaccine Data')

plt.title('NEW CASES TRENDS IN ITALY')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=100))
plt.gcf().autofmt_xdate()
plt.legend()
plt.show()

plt.figure(figsize=(20, 10))
# plt.plot(ItalyActiveData['Date'], ItalyActiveData['Cases'], label='Active Data')
# plt.plot(ItalyConfirmedData['Date'], ItalyConfirmedData['Cases'], label='Confiremd Data')
# plt.plot(ItalyDeathData['Date'], ItalyDeathData['Cases'], label='Death Data')
# plt.plot(ItalyHospitalizedData['Date'], ItalyHospitalizedData['Cases'], label='Hospitalized Data')
plt.plot(ItalyVaccineData['Date'], ItalyVaccineData['DoseValue'], label='Vaccine Data')

plt.title('VACCINE TRENDS IN ITALY')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=100))
plt.gcf().autofmt_xdate()
plt.legend()
plt.show()

ItalyActiveData.to_csv('Italy_Active_data.csv')
ItalyConfirmedData.to_csv('Italy_Confirmed_data.csv')
ItalyDeathData.to_csv('Italy_Death_data.csv')
ItalyHospitalizedData.to_csv('Italy_Hospitalized_data.csv')
ItalyVaccineData.to_csv('Italy_vaccine_data.csv')