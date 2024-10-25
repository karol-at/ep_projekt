from ReqParams import *
from DataClasses import *
from Plot import *
import requests as req

connection = buildconnectionstring(
    address = reqParams['address'],
    collection = reqParams['collection']['indicator'],
    lang = 'pl',
    element = reqParams['element']['Inflation'],
    time = '2022'
)

res = req.get(connection).json()

data = [DataPoint(i) for i in res]

for i in data:
    i.calculateDate()
    i.normalizeValue()

fig = createplot(data)

fig.savefig('plot.png')