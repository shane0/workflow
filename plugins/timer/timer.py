#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import pytz
import time

def get_current_timestamp():
    """Gets the current Unix timestamp."""
    now = datetime.datetime.now()
    return int(now.timestamp())


class Timer:
    def __init__(self, name: str, timezone: str = "America/Los_Angeles"):
        """
        Initialize a NamedTimer instance.

        Args:
            name (str): The name of the timer.
            timezone (str): The timezone to use (e.g., 'America/Los_Angeles'). Default is Seattle's time.
        """
        self.name = name
        self.start_time = None
        self.end_time = None
        self.elapsed_time = timedelta(0)

        # Use the specified timezone (defaults to 'America/Los_Angeles' for Seattle)
        self.timezone = pytz.timezone(timezone)

    def _format_time(self, time: datetime):
        """Helper method to format time as 'YYYY-MM-DD HH:MM' in the local timezone."""
        local_time = time.astimezone(self.timezone)
        return local_time.strftime("%Y-%m-%d %H:%M")

    def start(self):
        """Start the timer."""
        self.start_time = datetime.now(self.timezone)  # Now in the local timezone (Seattle)
        self.end_time = None
        self.elapsed_time = timedelta(0)
        return f"Timer '{self.name}' started at {self._format_time(self.start_time)}"

    def stop(self):
        """Stop the timer and calculate the elapsed time."""
        if not self.start_time:
            raise ValueError(f"Timer '{self.name}' has not been started.")
        self.end_time = datetime.now(self.timezone)  # Now in the local timezone (Seattle)
        self.elapsed_time = self.end_time - self.start_time
        return f"Timer '{self.name}' stopped at {self._format_time(self.end_time)}"

    def elapsed(self):
        """Get the elapsed time in a readable format."""
        if not self.start_time:
            raise ValueError(f"Timer '{self.name}' has not been started.")
        if self.end_time:
            elapsed = self.elapsed_time
        else:
            elapsed = datetime.now(self.timezone) - self.start_time

        # Format elapsed time as HH:MM:SS
        total_seconds = int(elapsed.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"Elapsed time for '{self.name}': {hours}h {minutes}m {seconds}s"

# Example Usage
# if __name__ == "__main__":
#     timer1 = NamedTimer("Timer1")  # Use Seattle's timezone ('America/Los_Angeles')
#     print(timer1.start())

#     # Simulate a delay
#     time.sleep(2)

#     print(timer1.stop())
#     print(timer1.elapsed())
