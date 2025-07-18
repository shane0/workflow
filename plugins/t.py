#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""timers """

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
import plugins.timer.timer as timer 
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
    timer tools
    """
    return 0


@cli.command()
def edit():
    """edit plugin"""
    click.edit(filename=inspect.getfile(inspect.currentframe()), editor="code")


@cli.command()
def t():
    """timer demo"""
     # UsesSeattle's timezone ('America/Los_Angeles')
    timer1 = timer.Timer("demo timer") 
    click.echo(timer1.start())
    click.echo('press a key to stop timer')
    click.pause()
    click.echo(timer1.stop())
    click.echo(timer1.elapsed())

@cli.command()
def x():
    """update pydocs"""
    file = 'plugins/timer/timer.py'
    tool = 'timer'
    # puts it here not in the folder
    cmd = f'python -m pydoc -w {file}'
    # cmd = f'python -m pydoc -w {file} > plugins/{tool}/{tool}.html'
    os.system(cmd)