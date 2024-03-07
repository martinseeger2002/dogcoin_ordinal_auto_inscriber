# Implementation :
**Copy and run this from the same dir as the doginals .js**

# Auto_inscriber_OG.py : 💯 

Big Chiefs Version of Auto inscriber (auto_inscriber_OG.py) 


# Auto_inscriber_OG2.py : 👍🏻 
Auto Minter Version Changed 60 Second Sleep to 300 seconds Because of mempool congestion.....change parameters to your needs. 60 seconds Cooks FAST.....When mempools not busy


# Auto_inscriber_v3.py : 🔢 

An untested work in Progress Auto inscriber Version of Big Chiefs OG script free to play with i would also like to still add @BookOnDoge's  utxo tracker script idea as well Auto inscriber Version im working on for auto mempool tracking, auto fee set in .env file based on mempool congestion, max retry limit with breaktime parameters as well. This modification adds a functionality to adjust fees in the .env file based on mempool congestion, and adds a wallet sync command after adjusting fees and waits for 60 seconds before proceeding with the next commands. Make sure to place it in the appropriate location within your script.

# Auto_inscriber_v4.py 👍🏻

This version (v4) of the Python script enhances the inscription automation process for a collection of digital images using Node.js commands. Specifically, it addresses and resolves errors related to 25KB file-sized inscriptions. The script interacts with a blockchain-based system, performing minting and wallet synchronization for each image within a specified range.


# Auto Inscriber Airdrop v1 👍🏻

This Python script automates the process of inscribing and airdroppng images. It extracts Dogecoin addresses from a specified JSON file, mints inscriptions from specified filepath, airdrops the minted inscription, and updates a JSON file with transaction details. The script handles specific error messages and ensures successful inscription.

# Itimized-00001-99999 File Name Conversion Script

This Python script is designed to rename all files in a specified folder with a sequential numbering pattern. It's useful for organizing and numbering files in a consistent manner.

## Usage

1. **Clone the Repository:**

    git clone https://github.com/GreatApe42069/Itimized-00001-99999-File-Name-convert.git
    
2. **Navigate to the Script Directory:**

    `cd Itimized-00001-99999-File-Name-convert`

3. **Adjust Parameters:**

    Open the `Itimized-00001-99999_File_name_convert.py` script and provide the correct path to the folder containing the files.

4. **Run the Script:**

    Execute the script using the following command:

    python "Itimized-00001-99999_File_name_convert.py"

5. **Parameters:**

    - `folder_path` (str): Provide the path to the folder containing files that need renaming.

6. **Notes:**

    - The script uses a sequential numbering pattern from (00001 to 99999) for renaming.
    - Files will be renamed in the order they are listed in the folder.
    - The script renames all types of files in the specified folder.

7. **Example:**

    python "Itimized-00001-99999_File_name_convert.py"

    This will rename all files in the specified folder with a sequential numbering pattern (00001 - 99999)

*Feel free to customize the script parameters and usage instructions to suit your specific needs.*


### Wish List to add:

@Books part of script i want to add to  Version OG 2 : 🔢 

UTXO Tracker to V3 auto inscriber at the very top of script:

import requests
import time

#### Function to check for UTXOs at a specified Dogecoin address using the BlockCypher API
def check_utxos(address):
    url = f"https://api.blockcypher.com/v1/doge/main/addrs/{address}?unspentOnly=true"
    response = requests.get(url)
    data = response.json()
    return len(data.get("txrefs", [])) > 0

#### Function to wait for UTXO completion before proceeding
def wait_for_utxo_completion(wallet_address):
    while not check_utxos(wallet_address):
        print("Waiting for UTXOs to complete...")
        time.sleep(60)  # Check every minute

## Security Note:
There are always Potential security considerations, qand risk especially when deploying online, I strrongly encourage users to follow best practices.

# Contributing
If you'd like to contribute or donate to our projects, please donate in Dogecoin. For contributors its as easy as opening issues, and creating pull requests

***If You would like to support with Donations, Send all Dogecoin tothe following Contributors:***

**"handle": "Big Chief"
"at": "@MartinSeeger2"
"dogecoin_address": "DCHxodkzaKCLjmnG4LP8uH6NKynmntmCNz"**


**"handle": "Great Ape"
"at": "@Greatape42069E"
"dogecoin_address": "DBpLvNcR1Zj8B6dKJp4n3XEAT4FmRxbnJb"**


**"handle": "BillyBitcoins"
"at": "@BillyBitcoins"
"dogecoin_address": "DQAWs4LQKY3zVmorsLHDUCV7LE5ox6rho6"**


# License
This project is licensed under the MIT License.
