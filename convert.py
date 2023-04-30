# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 11:14:58 2023

@author: Soumyajit Saha
"""
# fpath = 'OMI-Aura_L2-OMAERUV_2023m0131t0453-o98646_v883-2023m0131t075154.he5'
fpath = 'MLS-Aura_L2GP-O3_v05-01-NRT-17-c01_2023d033t2055.he5'
    
# import pandas as pd
# import sys

# # if len(sys.argv)>2:
# #     key = sys.argv[2]
# #     df = pd.read_hdf(fpath, key=key)
# # else:
# # df = pd.read_hdf(fpath)

# # df.to_csv(sys.stdout, index=False)


# # import numpy as np
# # pd.Series(np.zeros((3,5),dtype=np.float32).to_hdf(fpath,'test'))

import h5py
import numpy as np

# arr = np.random.randn(1000)


# # file = h5py.File(fpath,'r')

# # with h5py.File(fpath, 'w') as f:
# #     dset = f.create_dataset("default", data=arr)

# f = h5py.File(fpath, 'r')
# data = f['HDFEOS', 'HDFEOS INFORMATION'][()]
# f.close()
# print(data[10])

# h5f= h5py.File(fpath,'r')
# for a in h5f.keys() :
#     outf = open('./save_'+a+'.txt','w')
#     np.savetxt(outf, file[a][:], '%g', ',')
#     outf.close




dataset = h5py.File(fpath, 'r')

# grid = dataset['default']

# import h5py
# import pandas as pd 

# paths = []
# with h5py.File(fpath,'r') as hf:
#     hf.visit(paths.append)
# dt = pd.HDFStore(fpath).get(paths[1])
# dt.to_csv('test.csv')

