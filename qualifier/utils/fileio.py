# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from os import read


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(csvpath, data, header=None):
    """Saves the qualifying loans to a CSV file from CSV path provided.

    Args:
        csvpath(Path): CSV file path.
        data(list of lists): A list of data for the CSV file.
        header(list): Header for the CSV.

    """
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        if header:
            csvwriter.writerow(header)
        csvwriter.writerow(data)