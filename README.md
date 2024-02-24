# Implementation :
**Copy and run this from the same dir as the doginals .js**

# Auto_inscriber_v1.py : 💯 

Big Chiefs Version of Auto inscriber (auto_inscriber_v1.py) I tweaked a hair with
 MAX_RETRIES = 6
BASE_RETRY_DELAY_SECONDS = 300

this was added for when mempool was congested it would occasionaly get stuck in powershell and I kept getting transactions that I had to abandon which waisted Doge, this gives a 300 second break to allow utxo's and pending balance to return, so you can start the broadcast of next transaction successfully. this is the version i actively run now .....cooks for me

# Auto_inscriber_OG2.py : 👍🏻 
Auto Minter Version Changed 60 Second Sleep to 300 seconds Because of mempool congestion.....change parameters to your needs. 60 seconds Cooks FAST.....When mempools not busy


# Auto_inscriber_OG2.py : 🔢 

An untested work in Progress Auto inscriber Version of Big Chiefs OG script free to play with i would also like to still add @BookOnDoge  's   utxo tracker script idea as well Auto inscriber Version im working on for auto mempool tracking, auto fee set in .env file based on mempool congestion, max retry limit with breaktime parameters as well. This modification adds a functionality to adjust fees in the .env file based on mempool congestion, and adds a wallet sync command after adjusting fees and waits for 60 seconds before proceeding with the next commands. Make sure to place it in the appropriate location within your script.


@Books part of script i want to add to  Version OG 2 : 🔢 

UTXO Tracker to V3 auto inscriber at the very top of script:

import requests
import time

# Function to check for UTXOs at a specified Dogecoin address using the BlockCypher API
def check_utxos(address):
    url = f"https://api.blockcypher.com/v1/doge/main/addrs/{address}?unspentOnly=true"
    response = requests.get(url)
    data = response.json()
    return len(data.get("txrefs", [])) > 0

# Function to wait for UTXO completion before proceeding
def wait_for_utxo_completion(wallet_address):
    while not check_utxos(wallet_address):
        print("Waiting for UTXOs to complete...")
        time.sleep(60)  # Check every minute




