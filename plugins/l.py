#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""loggers"""

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
import time
from datetime import datetime
import plugins.logger.logger as logger
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
    logging tools
    """
    return 0


@cli.command()
def edit():
    """edit plugin"""
    click.edit(filename=inspect.getfile(inspect.currentframe()), editor="code")


@cli.command()
def l():
    """logger demo"""
    filename = "plugins/logger/logger.csv"
    columns = ["Timestamp", "Event", "Details"]
    timestamp = logger.timestamp_to_hhmm(logger.get_current_timestamp())
    logtimer = timer.Timer("log timer") 
    csv_logger = logger.CSVLogger(filename, columns)
    starttime = logtimer.start()
    csv_logger.log_row({"Timestamp": timestamp, "Event": "timer started ","Details": starttime})
    events = [
        "app initialized",
        "reloading canibulators",
        "shutting down canibulators",
    ]
    details = ["successfully", "the motor is running", "the motor is shut down"]

    for event, detail in zip(events, details):
        click.echo(f"logging {timestamp} {event} {detail}")
        csv_logger.log_row({"Timestamp": timestamp, "Event": event, "Details": detail})

    time.sleep(2)
    csv_logger.log_row({"Timestamp": timestamp, "Event": "idle for two seconds","Details": "2 second pause"})
    stoptime = logtimer.stop()
    csv_logger.log_row({"Timestamp": timestamp, "Event": "timer stopped","Details": stoptime})

    elapsed = logtimer.elapsed()

    csv_logger.log_row({"Timestamp": timestamp, "Event": "timer elapsed time ","Details": elapsed})
    click.edit(filename=filename, editor="code")

# todo
# pick a log file open it
# pick a regex pattern
# pick a log file grep it for regex pattern save to result file
# pick a logfile pick a regex type something to replace the match with 
# add a log level log messages at every level
# parse a log out into files for every log level
# run a cucumber test against a log