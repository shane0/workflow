Here's how you can add logging to your `bujo.py` module to use the same log file and log the arguments passed to its commands:

**1. Import necessary libraries:**

```python
import logging
import click
```

**2. Access the logger from `cli.py`:**

There are two main approaches to access the logger from `cli.py` within `bujo.py`:

**A. Passing the logger as an argument:**

- In `cli.py`, before loading the `bujo` command, create a logger instance:

```python
# In cli.py (before loading bujo command)
logger = logging.getLogger(__name__)
```

- Pass the logger instance to `bujo.cli` as an argument:

```python
# In cli.py (get_command function)
bujo_command = ns.get("cli")
if bujo_command:
    bujo_command.cli(logger=logger)  # Pass the logger
```

- In `bujo.py`, accept the logger as an argument in your `cli` function:

```python
# In bujo.py
@click.group()
def cli(args=None, logger=None):
    """
    bullet journaling & todocli
    """
    if logger:
        # Use the passed logger
        logging.getLogger(__name__).addHandler(logger.handlers[0])  # Add handler
    return 0
```

**B. Using a global logger:**

- Define a global logger instance in a separate module (e.g., `logging_utils.py`):

```python
# In logging_utils.py
import logging

logger = logging.getLogger(__name__)
```

- Import the `logger` from `logging_utils.py` in both `cli.py` and `bujo.py`:

```python
# In cli.py and bujo.py
from logging_utils import logger
```

**3. Log arguments in subcommands:**

- Decorate your subcommands within `bujo.cli` with a custom decorator that logs arguments.

Here's an example decorator:

```python
def log_arguments(func):
    """Decorator to log arguments to the provided logger."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Command '{func.__name__}' executed in 'bujo' with arguments: {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper
```

- Decorate your subcommands in `bujo.py`:

```python
@click.command()
@log_arguments  # Apply the decorator
def add_task(task_text):
    # ... your implementation for adding task ...

@click.command()
@log_arguments  # Apply the decorator
def list_tasks():
    # ... your implementation for listing tasks ...
```

**4. Remember to configure logging in `cli.py`**:

Ensure you have the logging configuration in your `cli.py`:

```python
# In cli.py
# ... existing logging configuration code ...
```

**Choosing the Approach:**

- Passing the logger explicitly (approach A) might be preferred if you want more control over individual command logging.
- Using a global logger (approach B) can be simpler if all commands within the plugin share the same logging needs.

By implementing these steps and choosing the appropriate method, you should be able to log command arguments in your `bujo.py` module using the same log file from `cli.py`.