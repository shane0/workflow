import sys
import click
import datetime
import os
import importlib.util
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Add the project root to sys.path (so it can find the src module)
PLUGINS_DIR = os.path.join(os.path.dirname(__file__), "plugins")
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
MONTHFILE = BUJO_FOLDER + "/" +  MONTH + ".md"
YEAR = datetime.date.today().strftime("%Y")


# class PluginCLI(click.MultiCommand):
class PluginCLI(click.Group):
    def list_commands(self, ctx):
        """Dynamically get the list of commands."""
        rv = []
        for filename in os.listdir(PLUGINS_DIR):
            if filename.endswith(".py") and not filename.startswith("__init__"):
                rv.append(filename[:-3])  # Remove '.py' extension
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        """Dynamically get the command from a plugin."""
        ns = {}
        fn = os.path.join(PLUGINS_DIR, name + ".py")
        with open(fn) as f:
            code = compile(f.read(), fn, "exec")
            eval(code, ns, ns)  # Run the plugin code in its own namespace
        return ns.get("cli")  # Return the cli function from the plugin


@click.command(cls=PluginCLI)
def cli():
    """Shane Null Workflows"""
    pass


if __name__ == "__main__":
    cli()

