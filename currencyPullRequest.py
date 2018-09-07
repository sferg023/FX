import requests, json, csv

currList = ['GBP_USD', 'USD_JPY', 'USD_MXN', 'USD_EUR', 'USD_CNY',
            'USD_KHR', 'USD_HRK', 'USD_CZK', 'USD_CAD', 'USD_AWG']

for fx in currList:
    my_url = "http://free.currencyconverterapi.com/api/v5/convert?q=" + fx + "&compact=y"
    r = requests.get(my_url)
    page_html = r.text
    page_html = json.loads(page_html)
    page_html = page_html[fx]
    print (fx + ' - ' + str(page_html['val']))
