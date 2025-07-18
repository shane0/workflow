#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyperclip
import click

class ClipboardStack:
    def __init__(self):
        self.stack = []

    def push(self, text):
        """Copies text to the clipboard and adds it to the stack."""
        pyperclip.copy(text)
        self.stack.append(text)
        click.echo(f"Pushed '{text}' to the stack.")

    def pop(self):
        """Removes and returns the last item from the stack, and copies it to the clipboard."""
        if self.stack:
            item = self.stack.pop()
            pyperclip.copy(item)
            click.echo(f"Popped '{item}' from the stack and copied to clipboard.")
            return item
        else:
            click.echo("Stack is empty.")
            return None

    def paste_all(self):
        """Pastes all items from the stack as a single clipboard item."""
        all_items = "\n".join(self.stack)
        pyperclip.copy(all_items)
        click.echo(f"Pasted:\n{pyperclip.paste()}")
        self.stack.clear()  # Clear the stack after pasting

    def iterate_stack(self):
        """Iterates through the stack, copying each item to the clipboard and pausing."""
        for item in self.stack:
            pyperclip.copy(item)
            click.echo(f"Copied '{item}' to clipboard.")
            click.pause()  # Pause for 1 second

# Example usage:
# if __name__ == "__main__":
#     stack = ClipboardStack()
#     stack.push("First item")
#     stack.push("Second item")
#     stack.push("Third item")

#     stack.paste_all()  # Pastes "First item\nSecond item\nThird item" to the clipboard