from web3 import Web3
from data import *

def get_additional_info(address):
    contract = web3.eth.contract(address=Web3.to_checksum_address(address), abi=erc20_abi)
    symbol = contract.functions.symbol().call()
    name = contract.functions.name().call()
    amount = contract.functions.totalSupply().call()
    print(f'Symbol {symbol} belongs to token {name}, with total quantity of {amount}')
    return {'symbol': symbol,
            'name': name,
            'amount': amount}

data = get_additional_info('0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0')