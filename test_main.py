from main import read_csv, get_descriptive_stats, get_histogram, get_line_graph
import polars as po


file_path = "Health_Sleep_Statistics.csv"


def test_read_csv():
    df = read_csv(file_path)
    assert isinstance(df, po.dataframe.frame.DataFrame)
    assert df.shape[0] > 0
    assert df.shape[1] > 0


def test_get_descriptive_stats():
    df = read_csv(file_path)
    stats = get_descriptive_stats(df)

    assert isinstance(stats, po.dataframe.frame.DataFrame)
    stat_rows = ["mean", "std", "min", "max"]
    assert all(stat in stats.to_series() for stat in stat_rows)


def test_get_histogram():
    df = read_csv(file_path)
    result = get_histogram(df, "Age")
    assert result is True  # check if the function executes successfully


def test_get_line_graph():
    df = read_csv(file_path)
    result = get_line_graph(dataframe=df, x_col="Daily Steps", y_col="Calories Burned")
    assert result is True  # check if the function executes successfully


def test_main():
    df = read_csv(file_path)

    assert isinstance(df, po.dataframe.frame.DataFrame)
    assert df.shape[0] == 100
    assert df.shape[0] != 0

    # Check if all required columns are present
    expected_columns = [
        "User ID",
        "Age",
        "Gender",
        "Sleep Quality",
        "Bedtime",
        "Wake-up Time",
        "Daily Steps",
        "Calories Burned",
        "Physical Activity Level",
        "Dietary Habits",
        "Sleep Disorders",
        "Medication Usage",
    ]
    assert all(column in df.columns for column in expected_columns)
    # Check if 'Age' is within a realistic range
    assert df["Age"].is_between(0, 120).all()
    # Check if 'Sleep Quality' is between 1 and 10
    assert df["Sleep Quality"].is_between(1, 10).all()
    # Check for missing values in required columns
    required_columns = ["User ID", "Age", "Gender", "Sleep Quality"]
    assert (
        df.select([po.col(col).is_not_null().all() for col in required_columns])
        .to_series()
        .all()
    )
