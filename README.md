# Blockchain 3užduotis „Bitcoin Core“ programinės sąsajos naudojimas

Užduoties reikalavimus galite pamatyti [čia](https://github.com/blockchain-group/Blockchain-technologijos/blob/master/pratybos/3uzduotis-Bitcoin-Core-API.md).


## [V1.0](https://github.com/rokas28/blockchain_3u-duotis/releases/tag/v1.0)
### Pridėta:
- `calculate_fee.py`
- `validate_block_hash.py`
- `.gitignore` 
- `README.md` 

Panaudojant `python-bitcoinlib` biblioteką, Python aplinkoje realizuokitos dvi programos:
- `calculate_fee.py` apskaičiuoja transakcijos mokestį pagal pateiktą transakcijos id.
- `validate_block_hash.py`  iš bloko header'yje esančių `versionHex`, `previousblockhash`, `merkleroot`, `time`, `bits`, `nonce` patikrina ar bloko hash'as yra teisingas, pagal pateiktą bloko id.
