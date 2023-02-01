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

from faker import Faker
from varname import nameof
from icecream import ic

# faker object
fake = Faker()

number_of_clients = int(sys.argv[1])

#@snoop
def make_database():
    # client - transaction
    client_name = fake.name()
    id = random.randint(1000, 10000)
    value = random.random()*100
    date = fake.date_between(start_date='-90d', end_date='today') # 3 months ago!
    date_register = fake.date_between(start_date='-3y', end_date='today')

    name_cols = []

    # fake database
    database = {f'id': id, 
                f'client_name': client_name,
                f'date': date,
                f'date_register': date_register,
                f'value': value
                }

    ## transaction
    # data - sell
    #print(f'id ....................: {id}')
    #print(f'client name............: {client_name}')
    #print(f'date...................: {date}')
    #print(f'date register..........: {date_register}')
    #print(f'value..................: {value}')


    return name_cols, database

#@snoop
def generate_fakedata(nrows):    

    irow = 1
    name_cols, database = make_database()
    df = pd.DataFrame(columns=name_cols)

    while(irow <= nrows):
        name_cols, database = make_database()
        df_database = pd.DataFrame([database])
        df = pd.concat([df, df_database], ignore_index=True)
        irow += 1

    return df