import matplotlib.pyplot as plt
import pandas as pd

class DatasetVisualizer:
    """
    Generates plots for a pandas DataFrame
    it holds the dataframe along with shared plot settings (figure size)
    so they don't get repeated on every function call.
    Use set_data() to swap in a new dataframe without losing the settings.
    """
    def __init__(self, df: pd.DataFrame, figsize: tuple[int, int]=(8,5)):
        self.df = df
        self.figsize=figsize
    def set_data(self, df:pd.DataFrame)-> None:
        """swap the dataframe this visualizer works on"""
        self.df = df
    def check_column(self, column:str) -> None:
        """check if the column exists in the dataframe"""
        if column not in self.df.columns:
            raise ValueError(f"Column {column} not found in the dataset.")
    
    def histogram(self, column:str , bins:int=30) -> plt.Figure:
        self.check_column(column)
        fig, ax=plt.subplots(figsize=self.figsize)
        ax.hist(self.df[column].dropna(), bins=bins, color='steelblue', edgecolor='black')
        ax.set_title(f"Histogram/Distribution of {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Frequency")
        return fig
    def boxplot(self, column:str) -> plt.Figure:
        self.check_column(column)
        fig, ax=plt,subplots(figsize=self.figsize)
        ax.boxplot(self.df[column].dropna(), vert=True)
        ax.set_title(f"Boxplot of {column}")
        ax.set_ylabel(column)
        return fig
    def scatter(self, x: str, y:str) -> plt.Figure:
        self.check_column(x)
        self.check_column(y)
        fig, ax=plt.subplots(figsize=self.figsize)
        data=self.df[[x,y]].dropna()
        ax.scatter(data[x], data[y],alpha=0.6, color="darkorange", edgecolor="black")
        ax.set_title(f"Scatter Plot of {y} vs {x}")
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        return fig
    def pie_chart(self, column:str, top_n: int=6) -> plt.Figure:
        self.check_column(column)
        counts=self.df[column].value_counts().head(top_n)
        fig, ax=plt.subplots(figsize=self.figsize)
        ax.pie(counts.values, labels=counts.index, autopct='%1.1f%%', colors=plt.cm.tab20.colors)
        ax_set_title(f"Distribution of {column} (top{top_n})")
        return fig
    
    def correlation_heatmap(self) -> plt.Figure:
        corr=self.df.corr(numeric_only=True)
        fig, ax=plt.subplots(figsize=self.figsize)
        im=ax.imshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
        ax.set_xticks(range(len(corr.columns)))
        ax.set_xticklabels(corr.columns, rotation=45, ha='right')
        ax.set_yticks(range(len(corr.index)))
        ax.set_yticklabels(corr.index)
        fig.colorbar(im, ax=ax)
        ax.set_title("Correlation Heatmap")
        fig.tight_layout()
        return fig
    def distribution_plot(self, column:str) -> plt.Figure:
        self.check_column(column)
        fig, ax=plt.subplots(figsize=self.figsize)
        self.df[column].dropna().plot(kind='density', ax=ax, color='purple')
        ax.set_title(f"Density plot of {column}")
        ax.set_xlabel(column)
        return fig
