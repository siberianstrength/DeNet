from web3 import Web3
node_url = 'https://polygon-mainnet.core.chainstack.com/a5bc8bd3048659fcdc92be395d1951d5'
web3 = Web3(Web3.HTTPProvider(node_url))
erc20_abi = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [{"name": "", "type": "uint256"}],
        "name": "tokenHolders",
        "outputs": [{"name": "", "type": "address"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
    "constant": True,
    "inputs": [],
    "name": "symbol",
    "outputs": [{"name": "", "type": "string"}],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
},
{
    "constant": True,
    "inputs": [],
    "name": "name",
    "outputs": [{"name": "", "type": "string"}],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
}
]