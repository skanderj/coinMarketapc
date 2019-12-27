#coinMarketapp

import json
import requests
from datetime import datetime

 
 
globalURL = 'https:/api.coinmarquetcap.com/v2/global/'

def coinMarket(currency)
    currencis = "YEN"
    globalURL = 'https:/api.coinmarquetcap.com/v2/global/{}'.format(currency)
    request = requests.get(globalURL)
    results = requesT.json()

    #change to readible form
    result_dumps = json.dumps(results, sort_keys= True, indent= 10)
    #assigned fetched data to variable 
    active_currencies = results['data']['active_cryptocurencies']
    active_markets = results['data']['active_markets']
    bitcoin_percentage = results['data']['bicoin_pecentage']
    laste_updated = results['data']['laste_updated']
    global_cap = results['data'][currency]['global_cap']
    global_volume = results['data'][curency]['global_volume']

    #add coma to the integer value
    active_currencies_string = {:,}.format(active_currencies)
    active_markets_string = {:,}.format(active_markets)
    bitcoin_percentage_string = {:,}.format(bitcoin_percentage)
    global_cap = {:,}.format(global_cap_string)
    global_volume ={:,}.format(global_volum_string)
    last_Updated_strigformat = datetime.fromtimestamp(last_updated).strtime('%B %d, %y at %I:%M%p


    print()

    print("there are curently " + active_currencies_string + "active cryptocurrencies" +
           + "the global cap result " + global_cap_string + "and the 24h global volume is " + global_volume_string
          active_markets_string +"active markets ." + "the bitoin percentage of the global is " + bitcoin_pecentage_string +
          "%"+ "this information was updated on " + last_updated_stringformat ".")


if __name__="__main_" :
    coinMarket(currency)
