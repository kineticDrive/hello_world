# Hello Universe

A professional, Pythonic "Hello World" application.

## Description

Hello Universe is a simple yet robust Python application demonstrating best practices in project structure, testing, and type hinting. It provides a `Greeter` class to generate greeting messages.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/hello_universe.git
    cd hello_universe
    ```

2.  **Recommended: Automated Setup**
    Run the setup script to create the virtual environment and install dependencies automatically:
    ```bash
    chmod +x setup_env.sh
    ./setup_env.sh
    ```

3.  **Manual Setup** (Alternative):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Usage

### Run as a Script

```bash
python3 src/hello_universe/main.py
# Output: Hello, World!
```

### Run as a Module

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
python3 -m hello_universe.main --name="Galaxy"
# Output: Hello, Galaxy!
```

## Testing

Run the test suite with `pytest`:

```bash
pytest tests/
```
