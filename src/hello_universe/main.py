"""
Main module for the Hello Universe application.
"""

from typing import Optional
import sys

def check_venv():
    """Check if running in a virtual environment."""
    if sys.prefix == sys.base_prefix:
        print("Error: This application must be run within a virtual environment.")
        print("Please run 'source setup_env.sh' to set up the environment.")
        sys.exit(1)

check_venv()


class Greeter:
    """Class to handle greeting functionality."""

    def __init__(self, name: str = "World"):
        """
        Initialize the Greeter.

        Args:
            name (str): The name to greet. Defaults to "World".
        """
        self.name = name

    def greet(self) -> str:
        """
        Generates a greeting message.

        Returns:
            str: The greeting message.
        """
        return f"Hello, {self.name}!"

    def __repr__(self) -> str:
        """
        Return string representation of the Greeter.
        """
        return f"Greeter(name='{self.name}')"


def main(name: Optional[str] = None) -> None:
    """
    Main function to execute the greeting.

    Args:
        name (Optional[str]): Name to greet. If None, uses default.
    """
    greeter = Greeter(name if name else "World")
    print(greeter.greet())


if __name__ == "__main__":
    main()
