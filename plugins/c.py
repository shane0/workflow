#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""cucumber"""

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
import plugins.cucumber.cucumber_tools as cucumber_tools

# import glob
# import datetime

# using inspect to import globals from parent dir module
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


@click.group()
def cli(args=None):
    """\b
    cucumber
    """
    return 0


@cli.command()
def edit():
    """edit plugin"""
    click.edit(filename=inspect.getfile(inspect.currentframe()), editor="code")

@cli.command()
def t():
    """run all tests with behave """
    cmd = "behave"
    os.system(cmd)

@cli.command()
def h():
    """show behave help"""
    cmd = "behave -h"
    os.system(cmd)

@cli.command()
def p():
    """pick one test """
    folder_choice = 'features/' 
    selected_tests = cucumber_tools.list_files_with_extension(f'{folder_choice}','.feature')
    selected_test = cucumber_tools.choose_from_list(selected_tests)
    test_command = f'behave {folder_choice}/{selected_test}'
    click.echo(f'{test_command}')
    os.system(test_command)
    selected_test_file  = f'{folder_choice}/{selected_test}'
    click.edit(filename=selected_test_file,editor='code')


@cli.command()
def m():
    """pick a manual test """
    click.echo('pick a test suite')
    selected_suite = cucumber_tools.list_folders('features')
    folder_choice = cucumber_tools.choose_from_list(selected_suite)
    click.echo(f' pick a test in {folder_choice}')
    selected_tests = cucumber_tools.list_files_with_extension(f'features/{folder_choice}','.feature')
    selected_test = cucumber_tools.choose_from_list(selected_tests)
    test_command = f'behave features/{folder_choice}/{selected_test}'
    click.echo(f'{test_command}')
    os.system(test_command)
    selected_test_file  = f'features/{folder_choice}/{selected_test}'
    click.edit(filename=selected_test_file,editor='code')



@cli.command()
def d():
    """demo: with selenium"""
    folder_choice = 'utils/'
    selected_tests = cucumber_tools.list_files_with_extension(f'{folder_choice}','.py')
    selected_test = cucumber_tools.choose_from_list(selected_tests)
    test_command = f'python {folder_choice}{selected_test}'
    click.echo(f'{test_command}')
    os.system(test_command)
