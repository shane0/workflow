#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""api tools"""

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
    api tools
    """
    return 0


@cli.command()
def edit():
    """edit plugin"""
    click.edit(filename=inspect.getfile(inspect.currentframe()), editor="code")


@cli.command()
def d():
    """get the julian day from an api"""
    url = "https://cors-shane0.vercel.app/api/day"
    response = api_tools.get_api_data(url)
    parsed_response = api_tools.extract_number_from_json_or_dict(response)
    days_left = 365 - parsed_response 
    percent = (parsed_response / 365) * 100
    click.echo(f' this year is {percent}% over \n the day number is {parsed_response} \n there are {days_left} days left in the year')


@cli.command()
def f():
    """html front end displaying data from api requests with templating"""
    url = "https://cors-shane0.vercel.app/api/day"
    response = api_tools.get_api_data(url)
    parsed_response = api_tools.extract_number_from_json_or_dict(response)
    days_left = 365 - parsed_response 
    percent = (parsed_response / 365) * 100
    front_url = f'http://localhost:5001/two/the day number {parsed_response}/the year is {percent}% over'
    click.launch(front_url)
    cmd = 'python plugins/flask_tools/flask_tools.py'
    os.system(cmd)


@cli.command()
def c():
    """complexity calculate cartesian product"""
    environment = examples.environments
    variation = examples.variations
    mutations = examples.mutations
    lists = [environment,variation,mutations]
    combinations = cartesian_product.cartesian_product(lists)
    click.echo('combinations')
    click.echo(combinations)
    counts = cartesian_product.cartesian_product_count(lists)
    click.echo('count')
    click.echo(counts)

@cli.command()
def x():
    """update pydocs"""
    file = 'plugins/api_tools/api_tools.py'
    tool = 'api_tools'
    # puts it here not in the folder
    cmd = f'python -m pydoc -w {file}'
    # cmd = f'python -m pydoc -w {file} > plugins/{tool}/{tool}.html'
    os.system(cmd)

@cli.command()
def xx():
    """update pydocs cartesian"""
    file = 'plugins/complexity/cartesian_product.py'
    tool = 'cartesian_product'
    # puts it here not in the folder
    cmd = f'python -m pydoc -w {file}'
    # cmd = f'python -m pydoc -w {file} > plugins/complexity/{tool}.html'
    os.system(cmd)


@cli.command()
def doc():
    """api documentation"""
    url = 'https://docs.gitlab.com/ee/development/documentation/restful_api_styleguide.html'
    click.launch(url)

# select an api cucumber test
# expand my apis endpoints
# generate documentation for apis endpoints
# launch a local fast api server 