import pandas as pd


def drop_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows that contain nothing but missing values
    (completely empty).
    """
    return df.dropna(axis=0, how="all").copy()


def drop_empty_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Same as drop_empty_rows but for columns.
    """
    return df.dropna(axis=1, how="all").copy()


def drop_duplicate_rows(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates().copy()


def drop_constant_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df.loc[:, df.nunique(dropna=False) > 1].copy()


def drop_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Drop a specific column and raise a KeyError if it does not exist.
    """
    if column not in df.columns:
        raise KeyError(f"Column '{column}' does not exist.")

    return df.drop(columns=column).copy()


def drop_row(df: pd.DataFrame, row) -> pd.DataFrame:
    """
    Drop a specific row and raise a KeyError if it does not exist.
    """
    if row not in df.index:
        raise KeyError(f"Row '{row}' does not exist.")

    return df.drop(index=row).copy()


def drop_rows_with_missing(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna(axis=0, how="any").copy()


def clean_strings(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans all strings:
    - removes leading and trailing spaces
    - replaces multiple spaces with only one
    - converts text to lowercase

    Non-string columns remain untouched.
    """

    cleaned_df = df.copy()

    string_columns = cleaned_df.select_dtypes(include=["object", "string"]).columns

    for column in string_columns:
        cleaned_df[column] = (
            cleaned_df[column]
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
            .str.lower()
        )

    return cleaned_df


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    The pipeline performs:
    1. Remove completely empty rows.
    2. Remove completely empty columns.
    3. Remove duplicate rows.
    4. Remove constant columns.
    5. Clean string values.
    """

    cleaned_df = df.copy()

    cleaned_df = drop_empty_rows(cleaned_df)
    cleaned_df = drop_empty_columns(cleaned_df)
    cleaned_df = drop_duplicate_rows(cleaned_df)
    cleaned_df = drop_constant_columns(cleaned_df)
    cleaned_df = clean_strings(cleaned_df)

    return cleaned_df