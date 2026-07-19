import sys

from loader import load_dataset
from analysis import generate_report
from visualization import DatasetVisualizer

def print_report(report: dict) -> None:
    print("\n ---< DATASET REPORT >---")
    print(f"Shape: {report['shape']}")
    print(f"Columns: {report['columns']}")
    print(f"Duplicate rows: {report['duplicate_rows']}")

    print("\n Missing values percentage %: ")
    for col, perc in report['missing_percentage'].items():
        if pct >0:
            print(f" {col}: {pct}%")
    if report['constant_columns']:
        print(f"\n Constant columns: {report['constant_columns']}")
    if report['high_cardinality_columns']:
        print(f"high cardinality columns: {report['high_cardinality_columns']}")

def save_plots(viz: DatasetVizualizer, numeric_columns: list[str], output_dir: Path) -> None:
    output_dir.mkdir(exist_ok=True)
    """
    for now this is a minimal version of save_plots function , the full function
    with the loops will be expanded after version 3 of the project is done

    """
    if numeric_columns:
        first_col=numeric_columns[0]
        fig=viz.histogram(first_column)
        fig.savefig(output_dir/f"histogram_{first_col}.png")
    if len(numeric_columns) >= 2:
        fig = viz.correlation_heatmap()
        fig.savefig(output_dir/"correlation_heatmap.png")

    print(f"\n Plots are saved to {output_dir}/")



def main():
    if len(sys.argv) !=2 :
        print("Usage: python main.py <path_to_csv>")
        sys.exit(1)

    path=sys.argv[1]

    df=load_dataset(path)

    report=generate_report(df)
    print_report(report)

    viz=DatasetVisualization(df)
    numeric_columns=df.select_dtypes(include="number").columns.tolist()
    save_plots(viz, numeric_cols, output_dir=Path("outputs"))


if __name__== "__main__":
    main()
