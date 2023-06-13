import os
import requests
import pandas as pd
from datetime import datetime

ses = requests.Session()
ses.headers.update({
    'accept': 'application/json',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
})

def parse_json(data):
    temp =  {
    "Pair": data['_id'].get('pair', None),
    "Token": data['_id'].get('token', None),
    "Price": data.get('price', None),
    "Price 24h": data.get('price24h', None),
    "Volume 24h": data.get('volume24h', None),
    "Swaps 24h": data.get('swaps24h', None),
    "Created At": data['pair'].get('creationTime', None),
    "Liquidity": data['pair']['metrics'].get('liquidity', None),
    "Name": data['pair'].get('name', None),
    "Symbol": data['pair'].get('symbol', None),
    "Market_cap": data['token']['metrics'].get('fdv', None),
    "Website": data['token']['links'].get('website', None),
    "Discord": data['token']['links'].get('discord', None),
    "Linkedin": data['token']['links'].get('linkedin', None),
    "Telegram": data['token']['links'].get('telegram', None),
    "Email": data['token']['info'].get('email', None),
    # "date" : data['token']['audit']['date'],
    # "Lock Transaction" : data['token']['audit']['lockTransactions'],
    }
    print("["+str(datetime.now().strftime("%H:%M:%S.%f"))+f"::{page}]",temp['Token'])
    return temp


def get_data(page):
    params = {
        'limit': '200',
        'interval': '24h',
        'page': f'{page}',
        'maxFdv': '2000000',
    }
    response = ses.get('https://www.dextools.io/shared/analytics/pairs', params=params)
    if response.status_code == 400:return False
    data = response.json()['data']
    for i in data:
        pair = i['pair']
        if 'locks' in pair:
        
            if len(pair['locks']):
                
                main_data.append(parse_json(i))
    return True
if __name__ == "__main__":
    main_data = []
    page = 1
    try:
        while get_data(page):
            page+=1
            pd.DataFrame(main_data).to_csv('Data.csv',index=False,mode='a',header=not os.path.exists('Data.csv'))
            main_data = []
    except Exception as e:
        print(f"Script Stoped due to {e}")
        pass

    
