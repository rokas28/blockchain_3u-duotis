from bitcoin.rpc import RawProxy

proxy = RawProxy()

tx_id = input("Enter transaction id: ")
#Viena vertingiausių transakcijų Bitcoin tinkle
#tx_id = '4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d'
#0.06534852 BTC
#tx_id = '0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2'
#0.00050000 BTC

try:
    raw_tx = proxy.getrawtransaction(tx_id)
    decoded_tx = proxy.decoderawtransaction(raw_tx)
    vin = decoded_tx['vin']
    vout = decoded_tx['vout']

    vin_sum = 0
    for tx_in in vin:
        vin_tx = proxy.getrawtransaction(tx_in['txid'])
        decoded_tx_in = proxy.decoderawtransaction(vin_tx)
        vin_sum += decoded_tx_in['vout'][tx_in['vout']]['value']

    vout_sum = 0
    for tx_out in vout:
        vout_sum += tx_out['value']

    transaction_fee = vin_sum - vout_sum

    print("Transaction's id: " + tx_id)
    print("Transaction's fee: " + str(transaction_fee) + " BTC")
except KeyError:
    print(KeyError)
