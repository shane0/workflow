#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import csv
from pathlib import Path

# DEBUG: 
# INFO: 
# WARNING:
# ERROR: 
# CRITICAL: 


class CSVLogger:
    def __init__(self, filename, columns):
        """
        Initialize the CSVLogger.

        :param filename: Name of the CSV file to be created/updated.
        :param columns: List of column names for the CSV file.
        """
        self.filename = Path(filename)
        self.columns = columns

        # Initialize the CSV file
        self._initialize_csv()

    def _initialize_csv(self):
        """
        Initializes the CSV file by creating it with the specified columns if it doesn't already exist.
        """
        if not self.filename.exists():
            try:
                with open(
                    self.filename, mode="w", newline="", encoding="utf-8"
                ) as file:
                    writer = csv.DictWriter(file, fieldnames=self.columns)
                    writer.writeheader()
                # print(f"CSV file '{self.filename}' created with columns: {self.columns}")
            except Exception as e:
                # print(f"Failed to create CSV file '{self.filename}': {e}")
                raise

    def log_row(self, data):
        """
        Log a row of data into the CSV file.

        :param data: A dictionary where keys match the column names.
        """
        if not set(data.keys()).issubset(self.columns):
            # print("Error: Data keys do not match CSV columns.")
            raise ValueError("Data keys do not match CSV columns.")

        try:
            with open(self.filename, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=self.columns)
                writer.writerow(data)
            # print(f"Row added to '{self.filename}': {data}")
        except Exception as e:
            # print(f"Failed to write row to CSV file '{self.filename}': {e}")
            raise

    # filename = "results/example_log.csv"
    # columns = ["Timestamp", "Event", "Details"]

    # # Initialize the CSV logger
    # csv_logger = CSVLogger(filename, columns)

    # # Log some data
    # csv_logger.log_row({"Timestamp": "2024-12-05 12:34:56", "Event": "Login", "Details": "User logged in successfully"})
    # csv_logger.log_row({"Timestamp": "2024-12-05 12:35:56", "Event": "Logout", "Details": "User logged out"})


def timestamp_to_hhmm(timestamp):
    """Converts a Unix timestamp to HH:MM format.

    Args:
      timestamp: The Unix timestamp in seconds.

    Returns:
      The time in HH:MM format as a string.
    """

    dt_object = datetime.datetime.fromtimestamp(timestamp)
    return dt_object.strftime("%H:%M")


# Example usage:
# timestamp = 1696372800  # A Unix timestamp
# hhmm_time = timestamp_to_hhmm(timestamp)
# print(hhmm_time)  # Output: 12:00



def get_current_timestamp():
    """Gets the current Unix timestamp."""
    now = datetime.datetime.now()
    return int(now.timestamp())


# timestamp = get_current_timestamp()

def count_failures(filename):
    """
    Counts the number of rows in a CSV file where the 'result' column has the value 'FAIL'.

    :param filename: str, path to the CSV file
    :return: int, count of rows where 'result' is 'FAIL'
    """
    fail_count = 0

    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["result"] == "FAIL":
                    fail_count += 1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except KeyError:
        print("Error: The 'result' column is missing in the CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return fail_count


# Example usage:
# filename = 'your_file.csv'
# print(f"Number of failures: {count_failures(filename)}")

# Usage example
if __name__ == "__main__":
    # Define the filename and columns
    print("this is a plugin for ../cli.py")