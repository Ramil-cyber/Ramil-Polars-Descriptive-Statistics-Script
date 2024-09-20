# Descriptive Statistics Script with Pandas

This project contains a Python script that uses Polars to compute descriptive statistics for a dataset and generate data visualizations. The script reads data from a CSV or Excel file and provides key summary statistics such as the mean, median, and standard deviation.

## Features

- Reads a dataset from a CSV or Excel file.
- Generates summary statistics:
  - Mean
  - Median
  - Standard Deviation
- Produces at least one data visualization (e.g., histogram, boxplot, etc.).
- Continuous Integration/Continuous Deployment (CI/CD) pipeline integrated with a build status badge.

## Visualizations

- **Histogram**:  
  ![Histogram](https://github.com/nogibjj/Ramil-Polars-Descriptive-Statistics-Script/blob/7e4e45c57d52528c90a6feeb3770f8985f6bb73c/image/histogram.png)
  
- **Line Graph**:  
  ![Line Graph](https://github.com/nogibjj/Ramil-Polars-Descriptive-Statistics-Script/blob/7e4e45c57d52528c90a6feeb3770f8985f6bb73c/image/linegraph.png)




## Summary Statistics Report

You can view the detailed summary statistics report generated in PDF format here:
- [Summary Statistics Report (PDF)](https://github.com/nogibjj/Polars-Descriptive-Statistics-Script/blob/7e4e45c57d52528c90a6feeb3770f8985f6bb73c/Summary-Statistics.pdf)


## Requirements

- Python 3.x
- Polars
- Matplotlib or Seaborn (for visualization)
- pytest (for testing)
- pylint for linting

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/nogibjj/Ramil-Polars-Descriptive-Statistics-Script.git
    cd Ramil-Polars-Descriptive-Statistics-Script
    ```

2. **Install required dependencies**:
    You can install all required packages by running:
    ```bash
    make setup
    ```

3. **Run the script**:
    To run the descriptive statistics script, use the following command:
    ```bash
    python main.py
    ```

## Usage

- Place your dataset in the project directory.
- Modify the script (`main.py`) to specify the path to your CSV or Excel file.
  
The script will automatically compute and display the descriptive statistics, and generate the data visualization.

## Running Tests

The project includes tests to ensure the correctness of the script. To run the tests, use:

```bash
make test
```

## Linting
To ensure code quality, Pylint is used. You can check for linting issues by running:

```bash
make lint
```
