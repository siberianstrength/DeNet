from web3 import Web3
from data import *
import requests

# не работает
# Sorry, it looks like you are trying to access an API Pro endpoint.
# Contact us to upgrade to API Pro.
# для использования API необходима про-подписка, а без API
# я не смог придумать решение
def get_top_token_holders(token_address):
    api_key = 'H51CMYVRU72IF1QY8KNW5TF6EXUJMYHR9P'
    url = f'https://api.etherscan.io/api?module=token&action=tokenholderlist&contractaddress={token_address}&apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 200: 
        data = response.json()
        if data['status'] == '1':
            holders = data['result']
    ...
    return data

# test:
# token_address = '0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0' #tether usd
# a = get_top_token_holders(token_address)