import pandas as pd

def _normalize_columns(columns: str | list[str]) -> list[str]:
    """
    Normalize the columns parameter to a list of strings.
    """
    if isinstance(columns, str):
        return [columns]
    return columns

def _validate_columns(df: pd.DataFrame, columns: list[str]) ->None:
    """
    Validate that the specified columns do exist in the dataframe.
    """
    missing=[col for col in columns if col not in df.columns]
    if missing:
        raise KeyError(f"Columns {missing} do not exist in the dataframe.")

def _validate_no_missing(df: pd.DataFrame, columns: list[str]) -> None:
    """
    Validate that the specified columns do not contain any missing values.
    """
    for col in columns:
        if df[col].isnull().any():
            raise ValueError(f"Column '{col}' contains missing values. Please handle them before encoding.")

def one_hot_encode(df: pd.DataFrame, columns:list[str] | str , drop_first: bool=True) -> pd.DataFrame:
    """
    One-Hot Encode the specified categorical columns.
    """
    columns = _normalize_columns(columns)
    _validate_columns(df, columns)
   
    return pd.get_dummies(df.copy(), columns=columns, drop_first=drop_first, dtype=int)

def label_encode(df:pd.DataFrame, columns: list[str] | str) -> pd.DataFrame:
    """
    Label Encode the specified categorical columns
    """
    columns = _normalize_columns(columns)
    _validate_columns(df, columns)

    encoded_df=df.copy()
    for col in columns:
        unique_values = encoded_df[col].dropna().unique()
        mapping = { 
            value: index
            for index, value in enumerate(unique_values)
        }
        encoded_df[col] = encoded_df[col].map(mapping)

    return encoded_df

def ordinal_encode(df: pd.DataFrame, column : str, order: list[str]) -> pd.DataFrame:
    """
    Ordinal Encode a categorical column using the provided order list
    """
    _validate_columns(df, [column])

    encoded_df= df.copy()
    dataset_categories = set(encoded_df[column].dropna().unique())
    provided_categories = set(order)

    missing_categories= dataset_categories - provided_categories

    if missing_categories:
        raise ValueError(f"Missing categories in '{column}': {missing_categories}")
    mapping = {
        category : rank
        for rank , category in enumerate(order)
    }
    encoded_df[column] = encoded_df[column].map(mapping)

    return encoded_df

def frequency_encode(df: pd.DataFrame, columns:list[str] | str) -> pd.DataFrame:
    """
    Replace each category by its frequency
    """
    columns = _normalize_columns(columns)
    _validate_columns(df , columns)

    encoded_df = df.copy() 
    for col in columns:
        frequency = encoded_df[col].value_counts(normalize= True)
        encoded_df[col]= encoded_df[col].map(frequency)
    return encoded_df

def binary_encode(df : pd.DataFrame, columns:list[str] | str ) -> pd.DataFrame:
    """
    Label encode, then represent the integer as a binary digit columns.
    Compromise between the one-hot (many columns) and label encoding (false order)
    """
    columns= _normalize_columns(columns)
    _validate_columns(df, columns)
    _validate_no_missing(df, columns)

    encoded_df= label_encode(df, columns)

    for col in columns:
        integer_codes = encoded_df[col]
        max_code = integer_codes.max()
        n_bits = max(max_code.bit_length() , 1)

        for bit in range(n_bits):
            encoded_df[f"{col}_bin_{bit}"]= (integer_codes.astype(int) >> bit) & 1

    return encoded_df.drop(columns=columns)