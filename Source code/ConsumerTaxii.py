from taxii2client import Server, Collection

def consume_cti(taxii_server_url, collection_id, username, password):
    # Connect to the TAXII server
    server = Server(taxii_server_url, user=username, password=password)

    # Choose the collection to consume from
    collection = server.get_collection(collection_id)

    # Retrieve STIX objects from the collection
    stix_bundle = collection.get_objects()

    # Print the STIX objects
    print("STIX Objects:")
    for stix_object in stix_bundle['objects']:
        print(json.dumps(stix_object, indent=2))
        print("\n" + "=" * 50 + "\n")  # Separator between objects

if __name__ == "__main__":
    # Replace with your TAXII server details
    taxii_server_url = "localhost"

    # Replace with your collection ID
    collection_id = "your_collection_id"

    # Replace with your TAXII server credentials
    username = "guest"
    password = "guest"

    consume_cti(taxii_server_url, collection_id, username, password)