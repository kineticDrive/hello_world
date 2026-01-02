# Professional Hello World

A classic Hello World program re-imagined as a production-ready Python project. Features strict type hinting, 100% test coverage, virtual environment enforcement, and industrial-grade linting.

## What is this?

This is the classic "Hello World" program, but built with the rigorous standards of a large-scale enterprise application. It demonstrates how to establish a robust foundation for any Python project, no matter how simple the logic.

## Key Additions & Features

*   **🛡️ Virtual Environment Enforcement**: The application self-checks at runtime to ensure it's running in an isolated environment, preventing dependency conflicts. Includes an automated `setup_env.sh` script.
*   **🏗️ Production-Grade Structure**: Organized using the `src/` layout pattern with a proper `pyproject.toml` configuration, separating source code from tests.
*   **🧪 Comprehensive Testing**: Includes a full `pytest` suite covering default behaviors and edge cases.
*   **✨ Strict Code Quality**: Maintains a perfect **10.00/10 Pylint score** and is auto-formatted with **Black**.
*   **📝 Type Safety**: Fully annotated with Python type hints for static analysis reliability.
*   **📦 Object-Oriented Design**: Logic is encapsulated in a dedicated `Greeter` class rather than a loose script.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/kineticDrive/hello_world.git
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
