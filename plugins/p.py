#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""clipboard stack"""

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
import plugins.clipstack.clipstack as clipstack
import plugins.complexity.examples as examples

# import glob
# import datetime

# using inspect to import globals from parent dir module
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


@click.group()
def cli(args=None):
    """\b
    clipboard stack
    """
    return 0


@cli.command()
def edit():
    """edit plugin"""
    click.edit(filename=inspect.getfile(inspect.currentframe()), editor="code")


@cli.command()
def d():
    """demo of stacking things into the clipboard"""
    stack = clipstack.ClipboardStack()
    for e in examples.meditations:
        click.echo(f"pushing {e} to stack")
        append = click.prompt(text=f"do you have a note for {e}", default=" is ok")
        stack.push(f"{e} notes are {append}")
    click.echo(f"your clipboard contains this stack: ")
    stack.paste_all()
