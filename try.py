# Set the URL string to point to a specific data URL. Some generic examples are:
#   https://servername/data/path/file
#   https://servername/opendap/path/file[.format[?subset]]
#   https://servername/daac-bin/OTF/HTTP_services.cgi?KEYWORD=value[&KEYWORD=value]
# URL = 'https://goldsmr5.gesdisc.eosdis.nasa.gov/data/MERRA2/M2I3NVCHM.5.12.4/2020/01/MERRA2_400.inst3_3d_chm_Nv.20200101.nc4'
   
# # Set the FILENAME string to the data file name, the LABEL keyword value, or any customized name. 
# FILENAME = 'data.csv'

# import requests
# result = requests.get(URL)
# try:
#     result.raise_for_status()
#     f = open(FILENAME,'wb')
#     f.write(result.content)
#     f.close()
#     print('contents of URL written to '+FILENAME)
# except:
#     print('requests.get() returned an error code '+str(result.status_code))

#
import xarray as xr
import pathlib


DS = xr.open_dataset('data/MERRA2_400.inst6_3d_ana_Np.20200101.nc4', engine='netcdf4')
DS.to_dataframe().to_csv("file_6_hourly.csv")