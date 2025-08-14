#!/usr/bin/env python3
import click


@click.command()
@click.argument("filepath")
def review(filepath):
    """Analyze a code file using Claude"""
    with open(filepath) as f:
        code = f.read()

    # Call to MCP server would go here
    print(f"Reviewing {filepath}...")
    print("Result: This needs error handling (Security: 4/10)")


if __name__ == "__main__":
    review()