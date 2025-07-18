#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""database tools"""

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

import pyperclip
# import subprocess
import os
import sys
import inspect
from datetime import datetime
import plugins.api_tools.api_tools as api_tools
import plugins.jargon.jargon as jargon
import plugins.complexity.examples as examples 
import plugins.complexity.cartesian_product as cartesian_product
import plugins.db.sqlite_tool as sqlite_tool
# import glob
# Set up the logger
# from plugins.mods.log_tools import setup_logger
# logger = setup_logger(logging.DEBUG)

# by adding the parent directory to sys.path, python can find and import modules from that directory and its subdirectories.
# this technique allows you to use relative imports (e.g., from ..module import class) to access modules within the project structure.
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


@click.group()
def cli(args=None):
    """\b
    database tools
    """
    return 0


@cli.command()
def edit():
    """edit plugin"""
    click.edit(filename=inspect.getfile(inspect.currentframe()), editor="code")


@cli.command()
def d():
    """demo sqlite tools"""
    db_engine = sqlite_tool.create_local_sqlite_db("demo_db")
    
    # # Example query to create a table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    );
    """
    sqlite_tool.execute_query(db_engine, create_table_query)
    
    # # Example query to insert data
    insert_data_query = """
    INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 25);
    """
    sqlite_tool.execute_query(db_engine, insert_data_query, commit=True)
    
    # # Example query to fetch data
    fetch_data_query = "SELECT * FROM users;"
    result = sqlite_tool.execute_query(db_engine, fetch_data_query)
    for row in result:
        click.echo(row)

@cli.command()
def q():
    """qurey sqlite db"""
    db_engine = sqlite_tool.create_local_sqlite_db("demo_db")
    folder_choice = 'plugins/db/queries/'
    selected_tests = sqlite_tool.list_files_with_extension(f'{folder_choice}','.sql')
    selected_test = sqlite_tool.choose_from_list(selected_tests)
    selected_test_file  = f'{folder_choice}/{selected_test}'
    query = sqlite_tool.read_file_contents(selected_test_file)
    # click.edit(filename=selected_test_file,editor='code')
    result = sqlite_tool.execute_query(db_engine, query)
    # this returns a goofy ResultProxy object
    # for row in result:
    #     click.echo(row)
    # exploring goofy options
    # result_list = list(result)  # Converts the ResultProxy to a list of tuples
    # print(result_list)
    # column_names = [row[1] for row in result]
    # print(column_names)
    # table_name = result[0][0]  # result[0] accesses the first tuple, and [0] accesses the first element of that tuple
    # click.echo(table_name)
    # result = [('users',), ('orders',), ('products',)]

    # # Use the function to prompt the user
    chosen_table = sqlite_tool.choose_table_from_result(result)
    new_query = f"SELECT * FROM {chosen_table};"
    print(f"query that table with: {new_query}")
    chosen_column = sqlite_tool.choose_column_from_table(db_engine, chosen_table)
    # # Print the selected table and column
    print(f"You chose the table: {chosen_table}")
    print(f"You chose the column: {chosen_column}")
    
    # # Now you can reuse the chosen table and column in a query
    query = f"SELECT {chosen_column} FROM {chosen_table};"
    print(f"Running query: {query}")
    result = sqlite_tool.execute_query(db_engine, query)
    
    # # Print the query result
    for row in result:
        print(row)