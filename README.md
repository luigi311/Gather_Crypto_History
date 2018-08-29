# Gather_Crypto_History
Create a CSV file containing all transations made on a given exchange. Transactions are gathered through API keys that are placed in a file matching the exchange name in the API_KEYS folder. Be sure to use read only api keys just in case anything happens to them in order to prevent issues with your accounts.

Currently supported exchanges:
+ Coinbase

Currently supported CSV format:
+ Delta

Setup:
```
pip3 install -r requirements.txt --user
```
Api Keys must be put in the folder API_KEYS/ with a file matching the exchange.key with the ID on one line and the KEY on the next line.
For example (Fake Keys):
```
API_KEYS/Coinbase.key
ASDFjaskld3135aS
UASDfjasli648468a4sdfASDFAYESSEE

```

Run:
```
python3 Gather_Crypto_History.py
```
All the CSVs will be place in a Output Folder with <exchange_name>-<account_name>.csv naming convention.