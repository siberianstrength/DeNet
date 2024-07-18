from web3 import Web3
from data import *

def get_balance(address: str) -> int:
    contract = web3.eth.contract(address=Web3.to_checksum_address(address), abi=erc20_abi)
    checksum_address = Web3.to_checksum_address(address) #иначе не принимает :(
    balance = contract.functions.balanceOf(checksum_address).call()
    decimals = contract.functions.decimals().call()
    readable_balance = balance / (10 ** decimals)
    print(f"Balance of address {checksum_address} is {readable_balance} tokens")
    return readable_balance

# test:
# get_balance('0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0')