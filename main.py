from ReqParams import *
from DataClasses import *
from Plot import *
import requests as req

year = input('Please enter requested year (from 2010 to 2023):')

try:
    connection = buildconnectionstring(
        address = reqParams['address'],
        collection = reqParams['collection']['indicator'],
        lang = 'pl',
        element = reqParams['element']['Inflation'],
        time = year
    )
except ValueError as e:
    print(e)
    exit()

res = req.get(connection).json()

data = [DataPoint(i) for i in res]

for i in data:
    i.calculateDate()
    i.normalizeValue()

fig = createplot(data, year)

fig.savefig('plot.png')