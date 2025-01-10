import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_kaggle_dataset(dataset_name=None, download_path="data/raw"):
    """
    downlaod kaggle dataset function downloads the datasets into the specified download
    path with considering the root path is the root of the project.
    
    """

    if not dataset_name: # TODO: add proper logging or print for warning  
        return
    
    api = KaggleApi()
    api.authenticate()

    # create the directory for download path if it does not exist yet
    os.makedirs(download_path, exist_ok=True)

    print(f"Downloading dataset '{dataset_name}'...")
    api.dataset_download_files(dataset_name, download_path, unzip=True)
    print(f"dataset '{dataset_name}'downloaded to {download_path}")

# Example usage
if __name__ == "__main__":
    dataset = "camnugent/california-housing-prices"  # Replace with your desired dataset
    download_kaggle_dataset(dataset)