# Data Mining Dataset Explorer "DataLab-AI"

A Python tool that automates the first stage of any data science workflow:
understanding a dataset before doing anything else with it.

Give it a CSV file. It reports shape, column types, missing values,
duplicates, and summary statistics, and generates plots — automatically.

## Why this project exists

Before training any machine learning model, you need to understand your
data: how big it is, what's missing, what's constant or useless, how
features relate to each other. This project automates that first step,
the way a data scientist would do it manually before modeling.

## Features (current)

- **Loading**: CSV loading with validation (file exists, correct format).
- **Analysis**: shape, column types, missing values, duplicates, summary
  statistics, correlation, and more — bundled into a single report via
  `generate_report()`.
- **Visualization**: histograms, boxplots, scatter plots, correlation
  heatmaps, pie charts, and density plots, via the `DatasetVisualizer`
  class.

## Installation

```bash
git clone <your-repo-url>
cd DataLab-AI
pip install -r requirements.txt
```

## Usage

```bash
python src/main.py data/your_file.csv
```

This prints a summary report to the terminal and saves plots to `outputs/`.

## Project structure