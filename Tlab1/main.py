def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    pass


def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    pass


def median(data: list) -> float:
    """
    """
    pass


def range(data: list) -> float:
    """
    """
    pass


def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    data = []

    # open file using file I/O and read it into the `data` list
    ...

    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    cleaned_list, removed_values = ...

    # calculate the average, median, and range of this file using the functions you've wrote
    ...

    # print out your data quality measure to the console
    ...

    # print out your descriptive statistics to the console
    ...


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
