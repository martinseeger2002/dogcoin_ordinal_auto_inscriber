import json

# Load the original JSON data from 'OW.json'
with open('OW.json', 'r') as file:
    original_data = json.load(file)

# Transform the data
transformed_data = {"body": []}
for item in original_data:
    new_item = {
        "inscriptionId": item["id"],
        "name": item["meta"]["name"],
        "imageURI": "https://media.ordinalswallet.com/c32ff552851a130d4100aeec5950725884bd8f3efa18d25b56a5e0a589c28847.jpeg",
        "collectionSymbol": "nerd_stones"
    }
    transformed_data["body"].append(new_item)

# Save the transformed data to a new JSON file
with open('DL.json', 'w') as file:
    json.dump(transformed_data, file, indent=4)

print("The JSON data has been transformed and saved to 'DL.json'.")
