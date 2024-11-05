#!/usr/bin/env python3

import csv
from pathlib import Path
import os

def read_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read header line
        data = [row for row in reader]  # Read the rest of the data
    return data, headers

class CSVFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data, self.headers = read_csv(file_path)

    def select_header(self):
        # Display headers with indices for selection
        for i, header in enumerate(self.headers, 1):
            print(f"{i}. {header}")
        
        choice = int(input("Select a header by number: ")) - 1  # Adjust for 0-based index
        if choice < 0 or choice >= len(self.headers):
            raise ValueError("Invalid header selection")

    def select_value(self):
        # Select header first
        header_choice, selected_header = self.select_header()
        print(f"Selected Header: {selected_header}")

        # Display rows with only the selected header column value
        for i, line in enumerate(self.data, 1):
            print(f"{i}. {line[header_choice]}")  # Display only the selected column value for each row

    # def select_header(self):
    #     for i, header in enumerate(self.headers, 1):
    #         print(f"{i}. {header}")

    #     choice = int(input("Select a header by number: "))
    #     return self.headers[choice - 1]

    # def select_value(self):
    #     # Display headers for selection
    #     for i, header in enumerate(self.headers, 1):
    #         print(f"{i}. {header}")

    #     header_choice = int(input("Select a header by number: ")) - 1  # Adjust for 0-based indexing
    #     selected_header = self.headers[header_choice]

    #     # Display lines for selection
    #     for i, line in enumerate(self.data, 1):
    #         print(f"{i}. {line}")

    #     line_choice = int(input("Select a line by number: ")) - 1  # Adjust for 0-based indexing
    #     selected_line = self.data[line_choice]

    #     # Return only the selected value
    #     return selected_line[header_choice]

    # def select_value_poop(self):
    #     for i, header in enumerate(self.headers, 1):
    #         print(f"{i}. {header}")

    #     header_choice = int(input("Select a header by number: ")) - 1  # Adjust for 0-based indexing
    #     selected_header = self.headers[header_choice]

    #     for i, line in enumerate(self.data, 1):
    #         print(f"{i}. {line}")

    #     line_choice = int(input("Select a line by number: ")) - 1  # Adjust for 0-based indexing
    #     selected_line = self.data[line_choice]

    #     return selected_line[header_choice]

    def select_header_and_line(self):
        for i, header in enumerate(self.headers, 1):
            print(f"{i}. {header}")

        header_choice = int(input("Select a header by number: "))
        selected_header = self.headers[header_choice - 1]

        for i, line in enumerate(self.data, 1):
            print(f"{i}. {line}")

        line_choice = int(input("Select a line by number: "))
        selected_line = self.data[line_choice - 1]

        return selected_header, selected_line

    def list_headers(self):
        return self.headers

    def add_line(self, line):
        self.data.append(line)

    def delete_line(self, index):
        del self.data[index]

    def update_line(self, index, new_line):
        self.data[index] = new_line

    def get_line(self, index):
        return self.data[index]

    def filter_by_header(self, index, header):
        return self.data[index][self.headers.index(header)]

    def save_to_file(self):
        write_csv(self.file_path, self.data, self.headers)

# # Example usage:
# file_path = Path.cwd() / "plugins" / "mods" / "favorites.csv"
# try:
#     csv_file = CSVFile(file_path)

#     # ... use the CSVFile object's methods
#     print(csv_file.list_headers())
#     # ... add, delete, update, or filter lines as needed
#     csv_file.save_to_file()

# except FileNotFoundError as e:
#     print(f"Error: {e}")

# class CSVDatabase:
#     def __init__(self, filename):
#         self.filename = filename

#     def read_data(self):
#         with open(self.filename, 'r') as file:
#             reader = csv.reader(file)
#             data = list(reader)
#         return data

#     def write_data(self, data):
#         with open(self.filename, 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerows(data)

#     def create_record(self, record):
#         data = self.read_data()
#         data.append(record)
#         self.write_data(data)

#     def update_record(self, index, new_record):
#         data = self.read_data()
#         data[index] = new_record
#         self.write_data(data)

#     def delete_record(self, index):
#         data = self.read_data()
#         del data[index]
#         self.write_data(data)

# # Example Usage
# # if __name__ == "__main__":
# #     file_path = "my_data.csv"  # Adjust the file path as needed

# #     # Create a CSVDatabase instance
# #     db = CSVDatabase(file_path)

# #     # Read all data
# #     all_data = db.read_data()
# #     print("All data:", all_data)

# #     # Create a new record
# #     new_record = ["Alice", "25", "New York"]
# #     db.create_record(new_record)
# #     print("Data after creating a new record:", db.read_data())

# #     # Update an existing record (e.g., index 1)
# #     updated_record = ["Bob", "30", "Los Angeles"]
# #     db.update_record(1, updated_record)
# #     print("Data after updating a record:", db.read_data())

# #     # Delete a record (e.g., index 2)
# #     db.delete_record(2)
# #     print("Data after deleting a record:", db.read_data())

# def read_csv(file_path):
#     with open(file_path, newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         headers = next(reader)
#         data = [row for row in reader]
#     return data, headers

# def read_csv(file_path):
#     if not os.path.exists(file_path):
#         raise FileNotFoundError(f"File not found: {file_path}")

#     with file_path.open('r') as f:
#         reader = csv.reader(f)
#         headers = next(reader)
#         data = []
#         for row in reader:
#             data.append(row)
#         return data, headers

# def write_csv(file_path, data, headers):
#     with file_path.open('w', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(headers)
#         writer.writerows(data)
