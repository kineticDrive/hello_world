"""
Unit tests for the Hello Universe application.
"""

from hello_universe.main import Greeter, main


def test_default_greeting():
    """Test the default greeting message."""
    greeter = Greeter()
    assert greeter.greet() == "Hello, World!"


def test_custom_greeting():
    """Test greeting with a custom name."""
    greeter = Greeter("Universe")
    assert greeter.greet() == "Hello, Universe!"


def test_main_execution(capsys):
    """Test the main function output."""
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"


def test_main_custom_execution(capsys):
    """Test the main function with a custom name."""
    main("Python")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Python!"
