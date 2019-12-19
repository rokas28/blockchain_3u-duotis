from bitcoin.rpc import RawProxy

proxy = RawProxy()

tx_id = '0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2'

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
    print(transaction_fee)
except KeyError:
    print(KeyError)
