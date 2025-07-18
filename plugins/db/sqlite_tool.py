#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pick a sql server and run a query against it"""
import os
from sqlalchemy import create_engine, text

# db_name = "test_database.db"
# if os.path.exists(db_name):
#     os.remove(db_name)

def create_local_sqlite_db(db_name):
    """
    Creates a local SQLite database file.
    
    Parameters:
        db_name (str): Name of the SQLite database file to create.
    
    Returns:
        engine: SQLAlchemy engine connected to the SQLite database.
    """
    if not db_name.endswith('.sqlite'):
        db_name += '.sqlite'
    engine = create_engine(f'sqlite:///{db_name}')
    print(f"SQLite database '{db_name}' created successfully.")
    return engine

def execute_query(engine, query, commit=False):
    """
    Executes a SQL query on the specified SQLite database.
    
    Parameters:
        engine: SQLAlchemy engine connected to the SQLite database.
        query (str): SQL query to execute.
        commit (bool): Whether to commit the transaction (for INSERT/UPDATE/DELETE).
    
    Returns:
        result: The result of the query execution (if applicable).
    """
    with engine.connect() as connection:
        result = connection.execute(text(query))
        if commit:
            connection.commit()  # Commit the transaction for data-modifying queries
            print("Transaction committed.")
        return result




def list_folders(folder_name):
  """
  Lists all folders within a given folder.

  Args:
    folder_name: The path to the folder.

  Returns:
    A list of folder names within the specified folder, or an empty list if the folder does not exist or contains no subfolders.
    Returns None if input is invalid.
  """
  if not isinstance(folder_name, str) or not folder_name:
    return None

  if not os.path.isdir(folder_name):
    return []

  folders = []
  for item in os.listdir(folder_name):
    item_path = os.path.join(folder_name, item)
    if os.path.isdir(item_path):
      folders.append(item)
  return folders


# Sample test cases
def test_list_folders():
  # Test case 1: Valid folder
  test_folder = "test_folder"
  os.makedirs(test_folder, exist_ok=True)  # Create the test folder if it doesn't exist
  os.makedirs(os.path.join(test_folder, "subfolder1"), exist_ok=True)
  os.makedirs(os.path.join(test_folder, "subfolder2"), exist_ok=True)

  folders = list_folders(test_folder)
  assert folders == ["subfolder1", "subfolder2"], f"Expected ['subfolder1', 'subfolder2'], but got {folders}"

  #clean up test folder
  # !rm -rf test_folder

  # Test case 2: Non-existent folder
  folders = list_folders("non_existent_folder")
  assert folders == [], f"Expected [], but got {folders}"

  # Test case 3: Empty folder
  os.makedirs("empty_folder", exist_ok=True)
  folders = list_folders("empty_folder")
  assert folders == [], f"Expected [], but got {folders}"
  # !rm -rf empty_folder

  # Test case 4: Invalid input
  result = list_folders(123)
  assert result is None, f"Expected None, but got {result}"

  result = list_folders("")
  assert result is None, f"Expected None, but got {result}"

# test_list_folders()
# print("All test cases passed!")



def list_folders(folder_name):
  """
  Lists all folders within a given folder.

  Args:
    folder_name: The path to the folder.

  Returns:
    A list of folder names within the specified folder, or an empty list if the folder does not exist or contains no subfolders.
    Returns None if input is invalid.
  """
  if not isinstance(folder_name, str) or not folder_name:
    return None

  if not os.path.isdir(folder_name):
    return []

  folders = []
  for item in os.listdir(folder_name):
    item_path = os.path.join(folder_name, item)
    if os.path.isdir(item_path):
      folders.append(item)
  return folders

"""
function that
has a parameter for folder name
has a parameter for file extension
returns lists with the files in the folder that match the extension
add a sample test


"""

# prompt: function that
# has a parameter for folder name
# has a parameter for file extension
# returns lists with the files in the folder that match the extension
# add a sample tes

import os

def list_files_with_extension(folder_name, file_extension):
    """
    Lists files with a specific extension within a given folder.

    Args:
        folder_name: The path to the folder.
        file_extension: The file extension to search for (e.g., ".txt", ".pdf").

    Returns:
        A list of file names with the specified extension within the folder,
        or an empty list if the folder does not exist, contains no files with the extension,
        or if the inputs are invalid.
        Returns None if input folder_name is invalid.
    """
    if not isinstance(folder_name, str) or not folder_name:
        return None

    if not isinstance(file_extension, str) or not file_extension:
        return []

    if not os.path.isdir(folder_name):
        return []

    files = []
    for item in os.listdir(folder_name):
        if item.endswith(file_extension):
            files.append(item)
    return files

# Sample Test Cases
def test_list_files_with_extension():
    # Test case 1: Valid folder and extension
    test_folder = "test_folder"
    os.makedirs(test_folder, exist_ok=True)
    with open(os.path.join(test_folder, "file1.txt"), "w") as f:
        f.write("test")
    with open(os.path.join(test_folder, "file2.txt"), "w") as f:
        f.write("test")
    with open(os.path.join(test_folder, "file3.pdf"), "w") as f:
        f.write("test")

    files = list_files_with_extension(test_folder, ".txt")
    assert files == ["file1.txt", "file2.txt"], f"Expected ['file1.txt', 'file2.txt'], but got {files}"

    #clean up test folder
    # !rm -rf test_folder

    # Test case 2: Invalid folder
    files = list_files_with_extension("non_existent_folder", ".txt")
    assert files == [], f"Expected [], but got {files}"

    # Test case 3: Empty folder
    os.makedirs("empty_folder", exist_ok=True)
    files = list_files_with_extension("empty_folder", ".txt")
    assert files == [], f"Expected [], but got {files}"
    # !rm -rf empty_folder

    # Test case 4: Invalid input
    result = list_files_with_extension(123, ".txt")
    assert result is None, f"Expected None, but got {result}"

    result = list_files_with_extension("", ".txt")
    assert result is None, f"Expected None, but got {result}"

    result = list_files_with_extension("valid_folder", 123)
    assert result == [], f"Expected [], but got {result}"

# test_list_files_with_extension()
# print("All test cases passed!")

"""
function that
has a parameter for a list
prompts the user to choose one by number
returns the list item selected
add a sample test
"""

# prompt: function that
# has a parameter for a list
# prompts the user to choose one by number
# returns the list item selected
# add a sample test

import os

def choose_from_list(items):
  """
  Prompts the user to choose an item from a list by number.

  Args:
    items: A list of items.

  Returns:
    The selected item from the list, or None if the input is invalid or the choice is out of range.
  """
  if not isinstance(items, list) or not items:
    return None

  for i, item in enumerate(items):
    print(f"{i + 1}. {item}")

  while True:
    try:
      choice = int(input("Enter your choice: "))
      if 1 <= choice <= len(items):
        return items[choice - 1]
      else:
        print("Invalid choice. Please enter a number within the valid range.")
    except ValueError:
      print("Invalid input. Please enter a number.")


# Sample Test
def test_choose_from_list():
    # Test case 1: Valid list
    items = ["apple", "banana", "cherry"]
    selected_item = choose_from_list(items)
    assert selected_item in items, f"Selected item '{selected_item}' not found in the list."

    #Test case 2: Empty List
    selected_item = choose_from_list([])
    assert selected_item is None

    # Test case 3: Invalid input
    selected_item = choose_from_list(123)
    assert selected_item is None

# test_choose_from_list()
# print("All test cases passed!")

# prompt: function that
# has a parameter for a bash command
# runs the bash command
# add a sample test

import subprocess

def run_bash_command(command):
  """Runs a bash command and returns the output."""
  try:
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr:
      print(f"Error executing command: {stderr.decode()}")
      return None
    return stdout.decode()
  except FileNotFoundError:
    print(f"Error: Command not found.")
    return None
  except Exception as e:
      print(f"An unexpected error occurred: {e}")
      return None

def test_run_bash_command():
    # Test case 1: Valid command
    output = run_bash_command("ls -l")
    assert output is not None, "Output should not be None for a valid command."

    # Test case 2: Invalid command
    output = run_bash_command("invalid_command")
    assert output is None, "Output should be None for an invalid command."

# test_run_bash_command()
# print("All test cases passed!")

"""function that
has a parameter for a bash command
runs the bash command
add a sample test

how to return only the value given a list item
"""

# prompt: how to return only the value given a list item

def get_list_item_value(items, index):
    """
    Returns the value of a list item at a given index.

    Args:
        items: The list of items.
        index: The index of the item to retrieve.

    Returns:
        The value of the list item at the specified index, or None if the index is out of range or the input is invalid.
    """
    if not isinstance(items, list):
        return None

    if not isinstance(index, int) or index < 0 or index >= len(items):
        return None

    return items[index]

# Sample Test
def test_get_list_item_value():
    # Test case 1: Valid list and index
    items = ["apple", "banana", "cherry"]
    value = get_list_item_value(items, 1)
    print(value)
    assert value == "banana", f"Expected 'banana', but got {value}"

    # Test case 2: Invalid index
    value = get_list_item_value(items, 5)  # index out of range
    print(value)
    assert value is None, f"Expected None, but got {value}"

    # Test case 3: Invalid input (not a list)
    value = get_list_item_value("not a list", 0)
    print(value)
    assert value is None, f"Expected None, but got {value}"

    # Test case 4: Negative index
    value = get_list_item_value(items, -1)
    print(value)
    assert value is None, f"Expected None, but got {value}"

# test_get_list_item_value()
# print("All test cases passed!")
def choose_table_from_result(result):
    """
    Prompts the user to choose a table from the result.
    
    Parameters:
        result (list): A list of tuples, each containing a table name (e.g., [('users',), ('orders',)]).
    
    Returns:
        str: The selected table name.
    """
    # Extract the table names from the result (first element of each tuple)
    table_names = [row[0] for row in result]
    
    # Display the list of tables
    print("Available tables:")
    for i, table_name in enumerate(table_names, 1):
        print(f"{i}. {table_name}")
    
    # Prompt user to choose a table
    choice = None
    while choice not in range(1, len(table_names) + 1):
        try:
            choice = int(input(f"Choose a table (1-{len(table_names)}): "))
        except ValueError:
            continue  # If the user doesn't input a number, keep prompting.
    
    # Return the chosen table name
    return table_names[choice - 1]

# Example result from `PRAGMA table_info` or `sqlite_master`
# result = [('users',), ('orders',), ('products',)]

# # Use the function to prompt the user
# chosen_table = choose_table_from_result(result)
# print(f"You chose the table: {chosen_table}")


def choose_column_from_table(engine, table_name):
    """
    Prompts the user to choose a column from the selected table.
    
    Parameters:
        engine: SQLAlchemy engine connected to the SQLite database.
        table_name (str): The name of the table to inspect.
    
    Returns:
        str: The selected column name.
    """
    # Get the column information using PRAGMA table_info
    query = f"PRAGMA table_info('{table_name}');"
    result = execute_query(engine, query)
    
    # Extract column names
    column_names = [row[1] for row in result]  # Column names are in the second position of each row
    
    # Display available columns
    print(f"Available columns in '{table_name}':")
    for i, column_name in enumerate(column_names, 1):
        print(f"{i}. {column_name}")
    
    # Prompt user to choose a column
    choice = None
    while choice not in range(1, len(column_names) + 1):
        try:
            choice = int(input(f"Choose a column (1-{len(column_names)}): "))
        except ValueError:
            continue  # If the user doesn't input a number, keep prompting.
    
    # Return the selected column name
    return column_names[choice - 1]

    # db_engine = create_local_sqlite_db("test_database.db")  # Adjust with your actual engine

    # # Get all tables first
    # result = execute_query(db_engine, "SELECT name FROM sqlite_master WHERE type='table';")
    # chosen_table = choose_table_from_result(result)
    
    # # Then, get the columns of the selected table
    # chosen_column = choose_column_from_table(db_engine, chosen_table)
    
    # # Print the selected table and column
    # print(f"You chose the table: {chosen_table}")
    # print(f"You chose the column: {chosen_column}")
    
    # # Now you can reuse the chosen table and column in a query
    # query = f"SELECT {chosen_column} FROM {chosen_table};"
    # print(f"Running query: {query}")
    # result = execute_query(db_engine, query)
    
    # # Print the query result
    # for row in result:
    #     print(row)

def read_file_contents(file_path):
    """
    Reads the contents of a file and returns it.

    Parameters:
        file_path (str): The relative file path of the file to read.

    Returns:
        str: The contents of the file.
    """
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except IOError:
        print(f"Error: An error occurred while reading the file '{file_path}'.")
        return None


if __name__ == "__main__":
    print('call from cli.py')
    # Create SQLite database
    # db_engine = create_local_sqlite_db("test_database")
    
    # # Create a table
    # create_table_query = """
    # CREATE TABLE IF NOT EXISTS users (
    #     id INTEGER PRIMARY KEY,
    #     name TEXT NOT NULL,
    #     age INTEGER
    # );
    # """
    # execute_query(db_engine, create_table_query)
    
    # # Insert data
    # insert_data_query = """
    # INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 25);
    # """
    # execute_query(db_engine, insert_data_query, commit=True)
    
    # # Fetch data
    # fetch_data_query = "SELECT * FROM users;"
    # result = execute_query(db_engine, fetch_data_query)
    # for row in result:
    #     print(row)
