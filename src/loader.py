from pathlib import Path

import pandas as pd

def load_dataset(path:str):
    """
    Load a CSV dataset.

    parameters are:
    path : str
        The path to the CSV file.   

    Returns
    -------
    pandas.DataFrame
        Loaded dataframe.

    Raises(exceptions):
    FileNotFoundError
        If the file does not exist at the specified path.

    ValueError 
        If the file is not a CSV file.
    """
    file=Path(path)

    if not file.exists():
        raise FileNotFoundError(f"{path} does not exist.")

    if file.suffix.lower() != ".csv":
        raise ValueError("Only CSV files are currently supported.")
    try:
        df= pd.read_csv(file)
    except Exception as error:
        raise Exception(f"Could not load the dataset: {error}")

    return df