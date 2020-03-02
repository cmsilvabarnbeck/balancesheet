import json

import requests

import urllib

import pandas as pd

import pprint

from IPython.core.display import HTML

 

ticker = input("Enter Stock Ticker:")

type(ticker)

 

url = urllib.request.urlopen('https://financialmodelingprep.com/api/financials/balance-sheet-statement/'+ticker)

data = url.read().decode('utf-8')

dex = int(len(ticker)) + 15

 

new_data = data[dex:-6]

 

 

new_data = json.loads(new_data)

 

dataframe = pd.DataFrame.from_dict(new_data)

 

display(HTML(dataframe.to_html()))
