import pandas as pd
from io import StringIO


def dataset_shape(df:pd.DataFrame) -> tuple[int, int]:
    """
    number of rows and columns
    """
    return df.shape

def get_columns(df:pd.DataFrame)-> pd.Index:
    """
    Get the column names of the dataset.
    """
    return df.columns
def numeric_columns(df:pd.DataFrame) -> pd.Index:
    """
    Get the numeric columns of the dataset.
    """
    return df.select_dtypes(include='number').columns
def categorical_columns(df:pd.DataFrame) -> pd.Index:
    """
    Get the categorical columns of the dataset.
    """
    return df.select_dtypes(include='object').columns
def datetime_columns(df:pd.DataFrame) ->pd.Index:
    """
    Get the datetime columns of the dataset.
    """
    return df.select_dtypes(include='datetime').columns
def boolean_columns(df:pd.DataFrame) -> pd.Index:
    """
    Get the boolean columns of the dataset.
    """
    return df.select_dtypes(include='bool').columns
def constant_columns(df:pd.DataFrame) -> pd.Index:
    """
    Get the constant columns of the dataset.
    """
    return df.columns[df.nunique() <= 1]
def empty_columns(df:pd.DataFrame) -> pd.Index:
    """
    Get the empty columns of the dataset.
    """
    return df.columns[df.isnull().all()]
def low_cardinality_columns(df:pd.DataFrame, threshold: int = 10) ->pd.Index:
    """
    Get the low cardinality columns of the dataset.
    """
    return df.columns[df.nunique() <= threshold]
def high_cardinality_columns(df:pd.DataFrame, threshold: int = 10) -> pd.Index:
    """
    Get the high cardinality columns of the dataset.
    """
    return df.columns[df.nunique() > threshold]
def get_data_types(df:pd.DataFrame) -> pd.Series:
    """
    Get the data types of the columns in the dataset.
    """
    return df.dtypes.astype(str)

def get_info(df:pd.DataFrame)-> str:
    """
    Get information about the dataset:
    Shows
        number of rows
        number of columns
        column names
        data types
        missing values
        memory usage
    """
    buffer=StringIO()
    df.info(buf=buffer)
    return buffer.getvalue()

def missing_values(df:pd.DataFrame) -> pd.Series:
    """
    Get the number of missing values in each column of the dataset.
    """
    return df.isnull().sum()

def columns_with_missing_values(df:pd.DataFrame) -> pd.Index:
    """
    Get the columns with missing values in the dataset.
    """
    return df.columns[df.isnull().any()]

def missing_percentage(df:pd.DataFrame) -> pd.Series:
    """
    Get the percentage of missing values in each column of the dataset.
    """
    return (df.isnull().sum()/len(df)*100).round(2)

def duplicate_values(df:pd.DataFrame) -> int:
    """
    Get the number of duplicate rows in the dataset.
    """
    return df.duplicated().sum()
def duplicate_rows(df:pd.DataFrame) -> pd.DataFrame:
    """
    Get the duplicate rows in the dataset.
    every row that belongs to a duplicate group will be marked as True
    """
    return df[df.duplicated(keep=False)]
def unique_values(df: pd.DataFrame) -> pd.Series:
    """
    Get the number of unique values in each column of the dataset.
    """
    return df.nunique()
def unique_percentage(df: pd.DataFrame) -> pd.Series:
    """
    Get the percentage of unique values in each column of the dataset.
    """
    return (df.nunique()/len(df)*100).round(2)
def dataset_statistics(df:pd.DataFrame)-> pd.DataFrame:
    """
    get summary statistics of the whole dataset, it shows:
        count
        mean
        std
        min
        25%
        50%
        75%
        max
    """
    return df.describe(include="all")
def mean(df:pd.DataFrame) -> pd.Series:
    """
    Get the mean of each column in the dataset.
    """
    return df.mean(numeric_only=True)
def median(df:pd.DataFrame) -> pd.Series:
    """
    Get the median of each column in the dataset.
    """
    return df.median(numeric_only=True)
def mode(df:pd.DataFrame) ->pd.DataFrame:
    """
    Get the mode of each column in the Dataset.
    """
    return df.mode(numeric_only=True)
def variance(df:pd.DataFrame) -> pd.Series:
    """
    Get the variance of each column in the dataset.
    """
    return df.var(numeric_only=True)
def standard_deviation(df:pd.DataFrame) -> pd.Series:
    """
    Get the standard deviation of each column in the dataset.
    """
    return df.std(numeric_only=True)
def quantiles(df: pd.DataFrame, q: float | list[float]=0.5 ) -> pd.Series | pd.DataFrame:
    """
    Get the quantiles of each column in the dataset.
    """
    return df.quantile(q=q, numeric_only=True)
def skewness(df:pd.DataFrame) -> pd.Series:
    """
    Get the skewness of each column in the dataset.
    """
    return df.skew(numeric_only=True)
def kurtosis(df:pd.DataFrame) -> pd.Series:
    """
    Get the kurtosis of each column in the dataset.
    """
    return df.kurt(numeric_only=True)
def memory_usage(df:pd.DataFrame) -> pd.Series:
    """
    Get the memory usage of each column.
    """
    return df.memory_usage(deep=True)

def correlation_matrix(df:pd.DataFrame) -> pd.DataFrame:
    """
    Get the correlation matrix of the dataset.
    """
    return df.corr(numeric_only=True)
def correlation_with(df:pd.DataFrame, column: str) -> pd.Series:
    """
    Get the correlation of each column with a specific column in the dataset.
    """
    return df.corr(numeric_only=True)[column]

def dataset_size(df:pd.DataFrame) -> int:
    """
    Total number of values
    """
    return df.size
def generate_report(df: pd.DataFrame) -> dict:
    """
    Run the core checks and return them as a single dictionary.
    This is the main entry point main.py should call for a quick
    first look at any dataset.
    """
    return {
        "shape": dataset_shape(df),
        "columns": list(get_columns(df)),
        "dtypes": get_data_types(df).to_dict(),
        "missing_values": missing_values(df).to_dict(),
        "missing_percentage": missing_percentage(df).to_dict(),
        "duplicate_rows": duplicate_values(df),
        "constant_columns": list(constant_columns(df)),
        "high_cardinality_columns": list(high_cardinality_columns(df)),
        "statistics": dataset_statistics(df).to_dict(),
    }