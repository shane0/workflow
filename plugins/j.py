#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""words and jargon"""

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
import plugins.jargon.jargon as jargon
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
    words and jargon
    """
    return 0


@cli.command()
def edit():
    """edit plugin"""
    click.edit(filename=inspect.getfile(inspect.currentframe()), editor="code")


@cli.command()
def d():
    """lookup a defintion"""
    word = click.prompt(text="type a word")
    # curl = f"curl https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    # os.system(curl)
    response = jargon.get_word_definition(word)
    pretty = jargon.pretty_print_definitions(response)
    click.echo(pretty)

@cli.command()
def d():
    """lookup a defintion"""