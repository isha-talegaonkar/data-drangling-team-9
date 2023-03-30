import requests
import xarray as xr
import pandas as pd


file = open("subset_M2I6NPANA_5.12.4_20230323_230605_.txt", "r")
lines = file.readlines()

for url in lines:
    r = requests.get(url, allow_redirects=True)
    name = url.split('/')[-1].strip('\n') 
    with open('data/'+name, 'wb') as f:
        f.write(r.content)
    ds = xr.open_dataset('data/'+name, engine='netcdf4')
    print(ds)
    csv_name = name.split('.nc4')[0]+'.csv'        
    ds.to_dataframe().to_csv('data/'+csv_name)



# import netCDF4
# import csv
# import urllib.request

# with open('subset_M2I6NPANA_5.12.4_20230323_230605_.txt') as f:
#     urls = f.read().splitlines()

# for url in urls:
#     filename = url.split('/')[-1]
#     urllib.request.urlretrieve(url, filename)

#     with netCDF4.Dataset(filename) as data:
#         with open(f"{filename}.csv", "w", newline='') as csv_file:
#             writer = csv.writer(csv_file)

#             writer.writerow(data.variables.keys())

#             for i in range(len(data.variables['time'])):
#                 row = [data.variables[var][i] for var in data.variables.keys()]
#                 writer.writerow(row)

#     print(f"{filename} converted to CSV")
