#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""click management"""

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
    click management
    """
    return 0


@cli.command()
def edit():
    """edit plugin"""
    click.edit(filename=inspect.getfile(inspect.currentframe()), editor="code")


# todo
# manage my projects 
# pick one & deploy click updates to it