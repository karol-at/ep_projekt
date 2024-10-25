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
    return f'{address}{collection}?id-wskaznik={element}&id-rok={time}&lang={lang}'