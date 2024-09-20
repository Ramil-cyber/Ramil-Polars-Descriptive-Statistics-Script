import polars as pd
import matplotlib.pyplot as plt


def read_csv(file_name):
    """P
    Read file name and return pandas dataframe

    file_name
    """

    dataframe = pd.read_csv(file_name)

    return dataframe


def get_descriptive_stats(dataframe):
    """
    Return descriptive statistics from dataframe
    """

    return dataframe.describe()


def get_histogram(dataframe, col):
    """
    Return histogram from given column based on given dataframe
    """
    plt.hist(dataframe[col], bins=5, edgecolor="black")
    plt.title(f"Histogram of {col}")
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    plt.show()
    return True


def get_line_graph(dataframe, x_col, y_col):
    """
    Return line graph from given x and y columns based on given dataframe.
    """
    plt.close()
    x = dataframe[x_col].to_list()
    y = dataframe[y_col].to_list()

    plt.plot(x, y, marker="o")
    plt.title(f"Line Graph: {x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)

    plt.show()
    return True
