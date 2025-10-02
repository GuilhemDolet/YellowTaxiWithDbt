from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os   
load_dotenv()

connection_string = os.getenv("CONNEXION_STRING_STORAGE_ACCOUNT") # compte de stockage
container_name = "yellow-taxi"
local_folder = "./data/parquet_RAW/2024"
print(connection_string)

# blob_name = os.path.basename(local_file_path)  # le fichier gardera son nom dans le blob

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Vérifie si le conteneur existe 
try:
    container_client = blob_service_client.get_container_client(container_name)
    container_client.get_container_properties()
    print(f"Conteneur '{container_name}' trouvé.")
except Exception:
    print(f"Conteneur '{container_name}' introuvable, création...")
    blob_service_client.create_container(container_name)

for filename in os.listdir(local_folder):
    if filename.endswith(".parquet"):
        local_file_path = os.path.join(local_folder, filename)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=filename)

        try:
            blob_client.get_blob_properties()
            print(f"Fichier '{filename}' existe déjà dans '{container_name}', passage au suivant.")
            continue  # passe au fichier suivant
        except Exception:
            # Le blob n'existe pas, on peut uploader
            with open(local_file_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=False, max_concurrency=4)
            print(f"Fichier '{filename}' uploadé dans '{container_name}/{filename}'.")