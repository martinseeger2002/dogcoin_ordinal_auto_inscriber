# Implementation :
**Copy and run this from the same dir as the doginals .js**

# Auto_inscriber_OG.py : 💯 

Big Chiefs Version of Auto inscriber (auto_inscriber_OG.py) 


# Auto_inscriber_OG2.py : 👍🏻 
Auto Minter Version Changed 60 Second Sleep to 300 seconds Because of mempool congestion.....change parameters to your needs. 60 seconds Cooks FAST.....When mempools not busy


# Auto_inscriber_v3.py : 🔢 

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


# Itimized-00001-99999 File Name Conversion Script

This Python script is designed to rename all files in a specified folder with a sequential numbering pattern. It's useful for organizing and numbering files in a consistent manner.

## Usage

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/GreatApe42069/Itimized-00001-99999-File-Name-convert.git
    ```

2. **Navigate to the Script Directory:**

    ```bash
    `cd Itimized-00001-99999-File-Name-convert`
    ```

3. **Adjust Parameters:**

    Open the `Itimized-00001-99999_File_name_convert.py` script and provide the correct path to the folder containing the files.

4. **Run the Script:**

    Execute the script using the following command:

    ```bash
    python "Itimized-00001-99999_File_name_convert.py"
    ```

5. **Parameters:**

    - `folder_path` (str): Provide the path to the folder containing files that need renaming.

6. **Notes:**

    - The script uses a sequential numbering pattern from (00001 to 99999) for renaming.
    - Files will be renamed in the order they are listed in the folder.
    - The script renames all types of files in the specified folder.

7. **Example:**

    ```bash
    python "Itimized-00001-99999_File_name_convert.py"
    ```

    This will rename all files in the specified folder with a sequential numbering pattern (00001 - 99999)

Feel free to customize the script parameters and usage instructions to suit your specific needs.


