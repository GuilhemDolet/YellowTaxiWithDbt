import os
import requests

months_to_collect_2024 = ["2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06", "2024-07", "2024-08", "2024-09", "2024-10", "2024-11", "2024-12"]
months_to_collect_2025 = ["2025-01", "2025-02", "2025-03", "2025-04", "2025-05", "2025-06", "2025-07", "2025-08"]

for month in months_to_collect_2024:

    url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{month}.parquet"

    dest_folder = "data/parquet_RAW/2024"
    os.makedirs(dest_folder, exist_ok=True)

    filename = f"{month}.parquet"
    dest_path = os.path.join(dest_folder, filename)

    print(f"Téléchargement en cours : {url}")

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(dest_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Fichier téléchargé : {dest_path}")