import xarray as xr
import pathlib
import pickle
import pandas as pd
import glob
import io
from geopy.geocoders import Nominatim
import os
import numpy as np

geolocator = Nominatim(user_agent="getData")

print("hi")

def convert_to_csv(filename):
    DS = xr.open_dataset(filename, engine='netcdf4')
    name = filename.split(".")[-2]
    DS.to_dataframe().to_csv(name+".csv")
    print("CSV created")
    return name

def create_chunks(filename):
    in_path = filename+".csv" 
    out_path = "pickle/" 
    chunk_size = 400000 
    reader = pd.read_csv(in_path,chunksize=chunk_size, 
                        low_memory=False)    
    print("Converting the CSV to chunks")
    for i, chunk in enumerate(reader):
        out_file = out_path + "/data_{}.pkl".format(i+1)
        with open(out_file, "wb") as f:
            pickle.dump(chunk,f,pickle.HIGHEST_PROTOCOL)

def is_in_italy(lat, lon):
    italy_lat_range = (35.5, 47.1)
    italy_lon_range = (6.6, 18.5)
    in_lat_range = np.logical_and(lat >= italy_lat_range[0], lat <= italy_lat_range[1])
    in_lon_range = np.logical_and(lon >= italy_lon_range[0], lon <= italy_lon_range[1])
    return np.logical_and(in_lat_range, in_lon_range)
    
def filter_country(filename):
    pickle_path = "pickle/" 
    data_p_files=[]
    for name in glob.glob(pickle_path + "/data_*.pkl"):
       data_p_files.append(name)

    df = pd.DataFrame([])
    for i in range(len(data_p_files)):
        print("Reading file: ", data_p_files[i])
        df = pd.read_pickle(data_p_files[i])
        mask = is_in_italy(df['lat'], df['lon'])
        df = df[mask]
        
        if not os.path.isfile(filename):
           df.to_csv(filename, header='column_names', index=False)
        else: 
           df.to_csv(filename, mode='a', header=False, index=False)  

if __name__ == '__main__':
    csv_name = convert_to_csv('MERRA2_400.inst6_3d_ana_Np.20200101.nc4')
    create_chunks(csv_name)
    filter_country(csv_name+"_final.csv")
    
