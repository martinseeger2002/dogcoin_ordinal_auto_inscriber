import json
import os
import re
import subprocess
import time

def load_json_file(file_path):
    """
    Loads a JSON file from the given file path.

    :param file_path: Path to the JSON file.
    :return: Dictionary loaded from the JSON file.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def load_airdrop_list(json_data):
    """
    Parses the provided JSON data to create a mapping from file numbers to Dogecoin addresses.

    :param json_data: Dictionary loaded from the JSON-formatted airdrop list.
    :return: Dictionary mapping file numbers to Dogecoin addresses.
    """
    air_drop_list = json_data['airDropList']
    address_map = {}
    for item in air_drop_list:
        note_range = item.get('note', '')
        match = re.match(r'NR(\d+)-(\d+)', note_range)
        if match:
            start_range = int(match.group(1))
            end_range = int(match.group(2))
            for i in range(start_range, end_range + 1):
                address_map[i] = item['dogecoin_address']
    return address_map

def run_node_commands(start, end, directory, file_prefix, file_extension, address_map, air_drop_list):
    """
    Processes each file in the specified range for minting. Executes node commands for minting and handles the output.

    :param start: Starting file number in the range.
    :param end: Ending file number in the range.
    :param directory: Directory where the files are located.
    :param file_prefix: Prefix of the file names.
    :param file_extension: Extension of the files.
    :param address_map: Dictionary mapping file numbers to Dogecoin addresses.
    :param air_drop_list: List of airdrop details loaded from JSON.
    """
    for i in range(start, end + 1):
        doge_address = address_map.get(i)
        if not doge_address:
            print(f"No address mapped for file number {i}")
            continue

        file_number = str(i).zfill(5)
        image_path = os.path.join(directory, f"{file_prefix}{file_number}.{file_extension}")

        if not os.path.isfile(image_path):
            print(f"File not found: {image_path}")
            continue

        base_file_name = os.path.basename(image_path).split('.')[0][:-5]
        mint_command = f"node . mint {doge_address} {image_path}"

        # Check if file exists
        if not os.path.isfile(image_path):
            print(f"File not found: {image_path}")
            continue

        # Extract base file name without serial number
        base_file_name = os.path.basename(image_path).split('.')[0][:-5]

        # Construct and run the first command
        mint_command = f"node . mint {doge_address} {image_path}"
        result_mint = subprocess.run(mint_command, shell=True, capture_output=True, text=True)
        print("Output from mint command:")
        print(result_mint.stdout)

        # Check if there is an error in the first command
        if result_mint.stderr:
            print("Error in mint command:")
            print(result_mint.stderr)

        # Check for success message in the first command's output
        txid_search = re.search("inscription txid: (\w+)", result_mint.stdout)
        if txid_search:
            txid = txid_search.group(1)
            print("Successful mint, updating JSON file, continuing in 100 seconds....")
            air_drop_details = next((item for item in air_drop_list if item['dogecoin_address'] == doge_address), None)
            update_json_file(base_file_name, image_path, txid, air_drop_details)
            time.sleep(100)
            continue

        # Check for specific error message in the first command's output
        if "'64: too-long-mempool-chain'" in result_mint.stdout:
            print("Detected specific error message, proceeding to wallet sync...")

            # Loop for the second command
            while True:
                wallet_sync_command = "node . wallet sync"
                result_sync = subprocess.run(wallet_sync_command, shell=True, capture_output=True, text=True)
                print("Output from wallet sync command:")
                print(result_sync.stdout)

                if result_sync.stderr:
                    print("Error in wallet sync command:")
                    print(result_sync.stderr)

                # Check for success message
                if "inscription txid" in result_sync.stdout:
                    print("Successful inscription, extracting txid and updating JSON file.")
                    txid = re.search("inscription txid: (\w+)", result_sync.stdout).group(1)
                    air_drop_details = next((item for item in air_drop_list if item['dogecoin_address'] == doge_address), None)
                    update_json_file(base_file_name, image_path, txid, air_drop_details)
                    break

                # Check for the specific error and retry
                elif "'64: too-long-mempool-chain'" in result_sync.stdout:
                    print("Detected specific error message, retrying in 100 seconds...")
                    time.sleep(100)
                else:
                    print("Unknown response, stopping the retry loop.")
                    break



def update_json_file(base_file_name, image_path, txid, air_drop_details):
    """
    Updates a JSON file with the minting transaction ID and the corresponding details from the airdrop list.

    :param base_file_name: Base file name used in the JSON file name.
    :param image_path: Path of the image file.
    :param txid: Transaction ID from the minting process.
    :param air_drop_details: Details from the airdrop list related to the minted item.
    """
    json_file_name = f"{base_file_name}.json"
    data = {}
    
    if os.path.isfile(json_file_name):
        with open(json_file_name, 'r') as file:
            data = json.load(file)

    key = os.path.basename(image_path)

    data[key] = {
        "txid": txid,
        "details": air_drop_details
    }

    with open(json_file_name, 'w') as file:
        json.dump(data, file, indent=4)


# Load the airDropList.json file
json_file_path = os.path.join(os.getcwd(), 'airDropList.json')
json_data = load_json_file(json_file_path)

# Load the address map from JSON data
address_map = load_airdrop_list(json_data)

# Specify your directory, prefix, extension, and file range
directory = 'C:\\doginals-main\\RiceCerts\\serializers'
file_prefix = 'smallCert_c'
file_extension = 'png'
start = 327
end = 337

# Run the node commands function with the loaded data
run_node_commands(start, end, directory, file_prefix, file_extension, address_map, json_data["airDropList"])
