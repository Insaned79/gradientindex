import pandas as pd 
import numpy as np
import requests
import re 

# Видмо это функция получения всех доступных инструментов на financialmodellingprep.com/
def get_all_symbols(token):
    url='https://financialmodellingprep.com/api/v3/stock/list?apikey='+token
    DATA = pd.read_json(url)
    return list(DATA['symbol'])

# Функция получения cookie и токена для yahoo finance
def cookie_crumb():
# search with regular expressions
# "CrumbStore":\{"crumb":"(?<crumb>[^"]+)"\}
    url = 'https://uk.finance.yahoo.com/quote/AAPL/history' # url for a ticker symbol, with a download link
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})  # download page

    txt = r.text # extract html

    cookie = r.cookies['B'] # the cooke we're looking for is named 'B'
    #print('Cookie: ', cookie)

    # Now we need to extract the token from html. 
    # the string we need looks like this: "CrumbStore":{"crumb":"lQHxbbYOBCq"}
    # regular expressions will do the trick!

    pattern = re.compile('.*"CrumbStore":\{"crumb":"(?P<crumb>[^"]+)"\}')

    for line in txt.splitlines():
        m = pattern.match(line)
        if m is not None:
            crumb = m.groupdict()['crumb']
        
        
    #print('Crumb=',crumb)
    return cookie,crumb