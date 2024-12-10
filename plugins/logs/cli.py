#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""shane null command line workflows"""
import click
import os
import logging
import inspect
import sys
import shutil
import datetime

plugin_folder = os.path.join(os.path.dirname(__file__), "plugins")
homedir = os.path.expanduser("~")
TODAY = datetime.date.today().strftime("%Y-%m-%d")
ISODATE = datetime.date.today().strftime("%Y-%m-%d")
ISOFILE = ISODATE + ".md"
BUJO_FOLDER = os.path.join(os.path.dirname(__file__), "docs/bujo")
MONTH = datetime.date.today().strftime("%m_%B")
WEEK = datetime.date.today().strftime("%U")
DAYFILE = BUJO_FOLDER + "/" + TODAY + ".md"
WEEKFILE = BUJO_FOLDER + "/" + WEEK + ".md"
MONTHFILE = BUJO_FOLDER + "/" + MONTH + ".md"
YEAR = datetime.date.today().strftime("%Y")

# Define the log file path in the plugins/ directory
log_directory = "plugins/logs"
os.makedirs(log_directory, exist_ok=True)  # Create the 'logs' directory if it doesn't exist
log_file = os.path.join(log_directory, "cli_commands.log")

# Set up the logger to log to a file
logging.basicConfig(
    level=logging.INFO,  # Adjust level as needed (DEBUG, INFO, WARNING, etc.)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Customize log format
    handlers=[
        logging.FileHandler(log_file, mode='a'),  # Append to log file instead of overwriting
        logging.StreamHandler()  # Also print logs to the console
    ]
)
logger = logging.getLogger(__name__)


class PluginCLI(click.MultiCommand):
    def list_commands(self, ctx):
        """Dynamically get the list of commands."""
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith(".py") and not filename.startswith("__init__"):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        """Dynamically get the command."""
        logger.info(f"Loading command: {name}")  # Log the command being loaded
        ns = {}
        fn = os.path.join(plugin_folder, name + ".py")
        try:
            with open(fn) as f:
                code = compile(f.read(), fn, "exec")
                eval(code, ns, ns)
            logger.info(f"Executing command: {name}")  # Log the command being executed
        except Exception as e:
            logger.error(f"Error loading command {name}: {e}")
        return ns.get("cli")



@click.command(cls=PluginCLI)
def cli():
    """Shane Null Terminal Workflows"""
    pass

if __name__ == "__main__":
    logger.info("Starting the CLI application...")  # Log when the application starts
    cli()