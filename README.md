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

Run:
```
python3 Gather_Crypto_History.py
```