from flask import Flask, request, jsonify
from web3 import Web3
from LevelA import get_balance
from LevelB import get_balance_batch
from LevelF import get_additional_info



node_url = 'https://polygon-mainnet.core.chainstack.com/a5bc8bd3048659fcdc92be395d1951d5'
web3 = Web3(Web3.HTTPProvider(node_url))

app = Flask(__name__)


@app.route('/get_balance', methods=['GET'])
def get_balance_route():
    address = request.args.get('address')
    if not address:
        return jsonify({"error": "Address parameter is required"}), 400
    
    try:
        balance = get_balance(address)
        return jsonify({"address": address, "balance": balance})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/get_balance_batch', methods=['POST'])
def get_balance_batch_route():
    data = request.get_json()
    print(data)
    if not data or 'addresses' not in data:
        return jsonify({"error": "Addresses is empty"}), 400

    addresses = data['addresses']
    try:
        balances = get_balance_batch(addresses)
        return jsonify(balances)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/get_additional_info', methods=['GET'])
def get_additional_info_route():
    address = request.args.get('address')
    if not address:
        return jsonify({"error": "Address parameter is required"}), 400
    
    try:
        data = get_additional_info(address)
        name = data['name']
        symbol = data['symbol']
        amount = data['amount']
        return jsonify({"address": address, 'symbol': symbol,
                'name': name,
                'amount': amount})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)