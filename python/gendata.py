import random
import pandas as pd
import snoop
import feather
import time
import gc
import sys
import feather
import os
import toolkit as tool
import genfakedata as fd

from faker import Faker
from varname import nameof
from icecream import ic

number_of_clients = int(sys.argv[1])

os.system('date')

# Get start time 
start_time = time.time()

# time - multithreading
start = time.perf_counter()

print("----------------------------- DATABASE ----------------------------") 
df = fd.generate_fakedata(nrows=number_of_clients)
# display the database
print(df)
print("-------------------------------------------------------------------") 

#print("saving the file format feather...")
# this is important to do before save in feather format.
df = df.reset_index(drop=True) 
#df.to_feather('dataset/fakeDatabase.ftr')
df.to_csv('../dataset/banking.csv')
tool.release_memory(df)

# time of execution in minutes
time_exec_min = round( (time.time() - start_time)/60, 4)

print(f'time of execution: {time_exec_min} minutes')
os.system('date')
print(f"All Done. :)")