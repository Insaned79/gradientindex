import pandas as pd 
import numpy as np


def get_all_symbols(token):
    url='https://financialmodellingprep.com/api/v3/stock/list?apikey='+token
    DATA = pd.read_json(url)
    return list(DATA['symbol'])

