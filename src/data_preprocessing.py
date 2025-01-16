# This File will be filled after the initial data preprocessing is done in the jupyter notebook.
import pandas as pd
import numpy as np

def clean_data(dataset: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans a pandas DataFrame by:
    - Dropping rows with any missing values.
    - Dropping duplicate rows, keeping the last occurrence.
    
    Args:
        dataset (pd.DataFrame): The input dataset to clean.
        
    Returns:
        pd.DataFrame: The cleaned dataset.
    """

    # drop null values
    cleaned_dataset = dataset.dropna(axis=0, how='any')

    # drop duplicates in the dataset
    cleaned_dataset = cleaned_dataset.drop_duplicates(keep='last')

    return cleaned_dataset