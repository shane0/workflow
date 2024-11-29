#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""favorites"""

from cli import (
    BUJO_FOLDER,
    ISODATE,
    ISOFILE,
    # MONTH,
    # WEEK,
    MONTHFILE,
    DAYFILE,
    WEEKFILE,
    YEAR,
)
import click

# import subprocess
import os
import sys
import inspect
# from plugins.mods.csv_tools import CSVDatabase
from plugins.mods.csv_tools import CSVFile 

from pathlib import Path
CURRENT_DIR = Path.cwd()
FILE_PATH = CURRENT_DIR / "plugins" / "mods" / "favorites.csv"  



# import glob
# import datetime

# using inspect to import globals from parent dir module
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


@click.group()
def cli(args=None):
    """\b
    favorites 
    """
    return 0


@cli.command()
def edit():
    """edit plugin"""
    click.edit(filename=inspect.getfile(inspect.currentframe()), editor="code")

@cli.command()
def p():
    """plans"""
    plans = """
for whatever organizing favorites or test case 
try a csv crud click command set
crud csv files list files pick one show headers pick a line pick a header
create
add 
update
delete
"""
    click.echo(plans)

@cli.command()
def hlv():
    """select header line value"""
    csv_file = CSVFile(FILE_PATH)
    value = csv_file.select_header_and_line()
    click.echo(value)

@cli.command()
def hl():
    """fixme select header and line"""
    csv_file = CSVFile(FILE_PATH)
    csv_file.select_header_and_line()

@cli.command()
def hs():
    """select headers"""
    csv_file = CSVFile(FILE_PATH)
    csv_file.select_header()

@cli.command()
def h():
    """show headers"""
    csv_file = CSVFile(FILE_PATH)
    headers = csv_file.list_headers()
    click.echo(headers)

# headers = csv_file.list_headers()
# print(headers)

# new_line = ['new_value1', 'new_value2', ...]
# csv_file.add_line(new_line)

# csv_file.delete_line(2)  # Deletes the third line
# new_line = ['updated_value1', 'updated_value2', ...]
# csv_file.update_line(1, new_line)  # Updates the second line

@cli.command()
def l():
    """show line"""
    csv_file = CSVFile(FILE_PATH)
    line = csv_file.get_line(0) 
    click.echo(line)

# line = csv_file.get_line(0)  # Gets the first line

@cli.command()
def fs():
    """filter shane"""
    csv_file = CSVFile(FILE_PATH)
    value = csv_file.filter_by_header(0, 'two')  # Gets the value of 'header_name' from the third line
    click.echo(value)
    # fixme
    # click.launch(value)
    click.launch("https://shanenull.com")

# value = csv_file.filter_by_header(2, 'header_name')  # Gets the value of 'header_name' from the third line
# csv_file.save_to_file()

@cli.command()
def f():
    """show favorites"""
    if not os.path.exists(FILE_PATH):
       raise FileNotFoundError(f"File not found: {FILE_PATH}")
    else:
       click.echo(FILE_PATH)
    # fav_db = CSVFile(FILE_PATH)
    # click.echo(fav_db)
    # db = CSVDatabase(FILE_PATH)
    # favorites_data = db.read_data()
    # click.echo(favorites_data)

# # Example Usage
# if __name__ == "__main__":
#     file_path = "my_data.csv"  # Adjust the file path as needed

#     # Create a CSVDatabase instance
#     db = CSVDatabase(file_path)

#     # Read all data
#     all_data = db.read_data()
#     print("All data:", all_data)

#     # Create a new record
#     new_record = ["Alice", "25", "New York"]
#     db.create_record(new_record)
#     print("Data after creating a new record:", db.read_data())

#     # Update an existing record (e.g., index 1)
#     updated_record = ["Bob", "30", "Los Angeles"]
#     db.update_record(1, updated_record)
#     print("Data after updating a record:", db.read_data())

#     # Delete a record (e.g., index 2)
#     db.delete_record(2)
#     print("Data after deleting a record:", db.read_data())

# @cli.command()
# def s():
#     """pick a shell script"""
#     test = find_tools.select_script("utils")
#     test = test.replace("\\", "/")
#     # cmd = f"/usr/bin/bash /{test}"
#     cmd = f"bash {test}"
#     click.echo(cmd)
#     pyperclip.copy(cmd)
#     os.system(cmd)
#     click.edit(filename=test, editor="code")