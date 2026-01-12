import pytest
import os
import pandas as pd
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
project_path = "data"
data_path = os.path.join(project_path,  "census.csv")
print(data_path)
data = pd.read_csv(data_path)

#@pytest.fixture(scope="session")


def test_file_is_imported():
    """
    applying test to verify data is successfully imported
    """

    df = pd.read_csv(data_path)

    assert not df.empty, f"File loaded correctly"


# TODO: implement the second test. Change the function name and input as needed
def test_file_has_enough_records():
    """
    applying test to verify there are sufficient records to conduct analysis, let's say more than 1000 records
    """
    df = pd.read_csv(data_path)
    rc = df.shape[0]

    assert rc > 1000, f"Number of rows: {data.shape[0]}"


# TODO: implement the third test. Change the function name and input as needed
def test_column_names():
    """
    Test if all the expected columns as there
    """
    expected_columns = [
        "age",
        "workclass",
        "fnlgt",
        "education",
        "education-num",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "capital-gain",
        "capital-loss",
        "hours-per-week",
        "native-country",
        "salary"
    ]
    df = pd.read_csv(data_path)
    these_columns = df.columns.values

    # This also enforces the same order
    assert list(expected_columns) == list(these_columns), f"Expected columns as expected: {expected_columns}"

