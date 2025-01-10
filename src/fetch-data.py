import os
from kaggle.api.kaggle_api_extended import KaggleApi
from global_logger import logger

def download_kaggle_dataset(dataset_name=None, download_path="data/raw"):
    """
    downlaod kaggle dataset function downloads the datasets into the specified download
    path with considering the root path is the root of the project.
    
    """

    if not dataset_name: 
        logger.warning("No dataset_name specified.")
        return
    
    try:
        api = KaggleApi()
        api.authenticate()
    except Exception as error:
        logger.error(f"Kaggle API failder: {error}")

    # create the directory for download path if it does not exist yet
    os.makedirs(download_path, exist_ok=True)

    logger.info(f"Downloading dataset '{dataset_name}'...")

    try:
        api.dataset_download_files(dataset_name, download_path, unzip=True)
        logger.info(f"dataset '{dataset_name}'downloaded to {download_path}")
    
    except Exception as error:
        logger.error(f"Donwload faild: {error}")

# Example usage
if __name__ == "__main__":
    dataset = "camnugent/california-housing-prices"  # Replace with your desired dataset
    download_kaggle_dataset(dataset)