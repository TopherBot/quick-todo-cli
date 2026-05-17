# quick-todo-cli

A tiny command‑line utility written in Python that lets you manage a temporary TODO list.

## Features
- `add <task>`  Add a new task.
- `list`     List all pending tasks.
- `done <id>`  Mark a task as completed and remove it.
- `clear`    Remove all tasks.

## Usage
```bash
# Run the script (requires Python 3.7+)
python todo.py add "Write project proposal"
python todo.py list
python todo.py done 1
python todo.py clear
```

All data lives only in memory; once the program exits the list is cleared.

## Installation
No installation needed—just copy `todo.py` and run it with Python.

## License
MIT (see LICENSE file if you add one).