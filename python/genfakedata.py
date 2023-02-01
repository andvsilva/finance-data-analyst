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
    
    # generate fake data
    date = fake.date_between(start_date='-90d', end_date='today') # 3 months ago! start_date='-3y', end_date='today'
    cca = random.randint(1000, 10000)
    ccb = random.randint(1000, 10000)
    descricao = fake.name()
    debito = random.randint(1000, 1000000)
    credito = random.randint(1000, 1000000) 
    movimentacao = random.randint(1000, 1000000)
    cc_id = random.randint(100000, 1000000)
    cc_descricao = fake.name()
    grupo = fake.country()
    subgrupo = fake.job()
    detail = fake.name()
    cenario = fake.country()
    grupo_empresarial = fake.currency_name()
    empresa = fake.name()
    
    # fake database
    database = {'date': date,
                'cca': cca,
                'ccb': ccb,
                'descricao': descricao,
                'debito': debito,
                'credito': credito,
                'movimentacao': movimentacao,
                'cc_id': cc_id,
                'cc_descricao': cc_descricao,
                'grupo': grupo,
                'subgrupo': subgrupo,
                'detail': detail,
                'cenario': cenario,
                'grupo_empresarial': grupo_empresarial,
                'empresa': empresa
                }

    return database

#@snoop
def generate_fakedata(nrows):    

    irow = 1
    database = make_database()
    df = pd.DataFrame()

    while(irow <= nrows):
        database = make_database()
        df_database = pd.DataFrame([database])
        df = pd.concat([df, df_database], ignore_index=True)
        irow += 1

    return df