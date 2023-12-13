#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""commitizen"""

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

# import glob
# import datetime

# using inspect to import globals from parent dir module
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


@click.group()
def cli(args=None):
    """\b
    commitizen handles version and changelog
    """
    return 0


@cli.command()
def edit():
    """edit plugin"""
    click.edit(filename=inspect.getfile(inspect.currentframe()), editor="code")


@cli.command()
def h():
    """help"""
    cmd = "cz -h"
    os.system(cmd)


@cli.command()
def b():
    """bump up version"""
    cmd = "cz bump"
    os.system(cmd)

@cli.command()
def i():
    """commit examples"""
    cmd = "cz info"
    os.system(cmd)


@cli.command()
def c():
    """generate changelog"""
    cmd = ["cz changelog", "cat CHANGELOG.md"]
    for c in cmd:
        os.system(c)


@cli.command()
def v():
    """version"""
    cmd = [
        "echo citizen is at version",
        "cz version ",
        "echo this app is at version",
        "cz version -p",
    ]
    for c in cmd:
        os.system(c)
