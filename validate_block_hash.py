from bitcoin.rpc import RawProxy
import hashlib
import binascii

proxy = RawProxy()


def little_endian(hexstring):
    arr = bytearray.fromhex(hexstring)
    arr.reverse()
    str = ''.join(format(x, '02x') for x in arr)
    return str

#block id for test
blockhash = '00000000000000000011a8d31534a4f3dc24591a65e9cf658a05a347eb96f4bb'
header = proxy.getblockheader(blockhash)

header_hex = (little_endian(header['versionHex'])
              + little_endian(header['previousblockhash'])
              + little_endian(header['merkleroot'])
              + little_endian(format(int(header['time']), 'x'))
              + little_endian(header['bits'])
              + little_endian(format(int(header['nonce']), 'x')))

header_bin = binascii.unhexlify(header_hex)
correct_hash = little_endian(hashlib.sha256(hashlib.sha256(header_bin).digest()).hexdigest())

if header['hash'] == correct_hash:
    print("The hashes match!")
else:
    print('Something is wrong, the hashes do not match!')
