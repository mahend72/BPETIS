import json
from taxii2client import Server, Collection

def read_cti_from_file(file_path):
    with open(file_path, 'r') as file:
        cti_content = json.load(file)
    return cti_content

def publish_cti_from_file(taxii_server_url, collection_id, username, password, file_path):
    # Connect to the TAXII server
    server = Server(taxii_server_url, user=username, password=password)

    # Choose the collection to publish to
    collection = server.get_collection(collection_id)

    # Read CTI content from the JSON file
    cti_content = read_cti_from_file(file_path)

    # Publish the CTI content to the collection
    status = collection.add_objects(cti_content)

    print("CTI published successfully. Status:", status)

if __name__ == "__main__":
    # Replace with your TAXII server details
    taxii_server_url = "localhost"

    # Replace with your collection ID
    collection_id = "your_collection_id"

    # Replace with your TAXII server credentials
    username = "guest"
    password = "guest"

    # Specify the path to your JSON file
    file_path = "data.json"

    publish_cti_from_file(taxii_server_url, collection_id, username, password, file_path)