"""Utility functions."""

__author__ = "730409403"

from csv import DictReader
DATA_DIRECTORY = "../../data"
DATA_FILE_PATH = f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv"


def read_csv_rows(path_CSV: str) -> list[dict[str, str]]:
    """Reading CSV files."""
    result: list[dict[str, str]] = []
    file_handle = open(path_CSV, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """List the values in named column of data."""
    column_values: list[str] = []
    for row in table:
        item: str = row[column_name]
        column_values.append(item)
    return column_values


def columnar(list_table_rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table list of rows, to a dictionary of columns."""
    column_oriented_table: dict[str, list[str]] = {}
    first_row: dict[str, str] = list_table_rows[0]
    for column in first_row:
        column_oriented_table[column] = column_values(list_table_rows, column)
    return column_oriented_table


def head(column_table: dict[str, list[str]], number_rows: int) -> dict[str, list[str]]:
    """Produce a table with a specific number of rows of data per column."""
    returned_dict: dict[str, list[str]] = {}
    columns = column_table.keys()
    for column in columns:
        list_for_N_values = []
        values = column_table[column]
        if number_rows >= len(values):
            return column_table
        i: int = 0
        while i < number_rows:
            list_for_N_values.append(values[i])
            i += 1
        returned_dict[column] = list_for_N_values
    return returned_dict


def select(column_oriented_table: dict[str, list[str]], names_of_columns: list[str]) -> dict[str, list[str]]:
    """Making a column-based table with specific sets of columns."""
    specific_column_table: dict[str, list[str]] = {}
    columns_in_table = list(column_oriented_table.keys())
    for column in names_of_columns:
        for original_column in columns_in_table:
            if column == original_column:
                specific_column_table[column] = column_oriented_table[column]
    return specific_column_table


def concat(column_based_table_1: dict[str, list[str]], column_based_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Create a new table of two column based tables combined."""
    combined_data_table: dict[str, list[str]] = {}
    for column in column_based_table_1:
        combined_data_table[column] = column_based_table_1[column]
    keys_list = list(combined_data_table.keys())
    for column in column_based_table_2:
        if column in keys_list:
            column_data = combined_data_table[column]
            column_data_2 = column_based_table_2[column]
            # append to list
            for item in column_data_2:
                column_data.append(item)
            combined_data_table[column] = column_data
        else:
            combined_data_table[column] = column_based_table_2[column]
    return combined_data_table


def count(freq_list: list[str]) -> dict[str, int]:
    """Counting frequencies of item in list given."""
    returned_dict: dict[str, int] = {}
    for item in freq_list:
        if item in returned_dict.keys():
            # increase the value associated with that key 
            returned_dict[item] += 1
        else:
            # assign that key the value of 1
            returned_dict[item] = 1
    return returned_dict