reqParams = {
    'address' : 'https://api-sdp.stat.gov.pl/api/1.0.0/',
    'collection' : {
        'indicatorList' : 'indicators/indicator-indicator',
        'indicator' : 'indicators/indicator-data-indicator'
    },
    'element' : {
        'GDP' : '216',
        'Inflation' : '639'
    }
}

def buildconnectionstring(address, collection, lang, element = '', time = '') -> str:
    if time not in [str(i) for i in range(2010, 2023)]:
        raise ValueError('Invalid time value')
    return f'{address}{collection}?id-wskaznik={element}&id-rok={time}&lang={lang}'