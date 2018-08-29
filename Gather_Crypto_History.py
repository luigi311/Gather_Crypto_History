from coinbase.wallet.client import Client as CoinBase
from six import string_types
import argparse, csv


parser = argparse.ArgumentParser(
    description="Create CSV of all transactions from multiple exchanges")

parser.add_argument("--source", type=str,
                    help="Specify a specific source only")

args = parser.parse_args()


coinbase_api_file = "API_KEYS/Coinbase.key"
delta_struc = ["Date", "Type", "Exchange", "Base amount", "Base currency", "Quote amount", "Quote currency", "Fee",
               "Fee currency", "Costs/Proceeds", "Costs/Proceeds currency", "Sync Holdings", "Sent/Received from","Sent to", "Notes"]

def coinbase_csv(file):
  print("Starting Coinbase")
  with open(file) as f:
    coinbase_api = f.read().splitlines()

  print("Gathering Accounts")
  client = CoinBase(coinbase_api[0], coinbase_api[1])
  accounts = client.get_accounts()
  print("Accounts Gathered")

  for account_id in range(len(accounts["data"])):
    print("Working on %s" % accounts["data"][account_id]["name"])
    with open('coinbase-'+accounts["data"][account_id]["name"]+".csv", 'w', newline='') as csvfile:
      coinbasewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
      coinbasewriter.writerow(delta_struc)

      txs = accounts[account_id].get_transactions()
      for i in range(len(txs["data"])):
        #print(txs["data"][i])
        txs_sent_received_from = txs["data"][i]["details"]["subtitle"]
        txs_sent_to = ""
        txs_fee = ""
        txs_fee_currency = ""
        txs_costs_proceeds = ""
        txs_costs_proceeds_currency = ""
        txs_sync_holdings = 1
        txs_quote_amount = ""
        txs_quote_currency = ""
        txs_notes = ""
        
        txs_date = txs["data"][i]["created_at"].replace("T"," ").replace("Z","")      
        
        txs_type = txs["data"][i]["type"]

        if txs_type == "send":
          txs_type = "DEPOSIT"
          txs_sent_to = accounts["data"][account_id]["name"]

        txs_exchange = "COINBASE"
        txs_base_amount = txs["data"][i]["amount"]["amount"]
        txs_base_currency = txs["data"][i]["amount"]["currency"]
      
        if txs_type == "buy":
          txs_quote_amount = txs["data"][i]["native_amount"]["amount"]
          txs_quote_currency = txs["data"][i]["native_amount"]["currency"]
          txs_sent_to = accounts["data"][account_id]["name"]               

        if "to" in txs["data"][i]:
          txs_type = "WITHDRAW"
          txs_sent_to = txs["data"][i]["to"]["resource"]
          txs_sent_received_from = accounts["data"][account_id]["name"]

        if txs_type == "sell":
          txs_quote_amount = txs["data"][i]["native_amount"]["amount"]
          txs_quote_currency = txs["data"][i]["native_amount"]["currency"]
          txs_sent_to = txs["data"][i]["details"]["payment_method_name"]
          txs_sent_received_from = accounts["data"][account_id]["name"]          
      
        structure = [txs_date, txs_type, txs_exchange, txs_base_amount,
               txs_base_currency, txs_quote_amount, txs_quote_currency,
               txs_fee, txs_fee_currency, txs_costs_proceeds, 
               txs_costs_proceeds_currency, txs_sync_holdings,
               txs_sent_received_from, txs_sent_to, txs_notes]
        
        coinbasewriter.writerow(
          [x.upper() if isinstance(x, string_types) else '' for x in structure]
        )


try:
  coinbase_csv(coinbase_api_file)

except KeyboardInterrupt:
  print('\nExiting')
