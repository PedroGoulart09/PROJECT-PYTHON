from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """

    new_data = []
    with open(path) as file:
        all_data = csv.DictReader(file)
        for data in all_data:
            new_data.append(data)
    return new_data
