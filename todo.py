#!/usr/bin/env python3
"""quick-todo-cli – a tiny in‑memory TODO manager.

Commands:
  add <task>   Add a new task.
  list        List current tasks.
  done <id>   Complete and remove a task.
  clear       Remove all tasks.
"""
import sys

class TodoApp:
    def __init__(self):
        self.tasks = []

    def add(self, *args):
        if not args:
            print('Error: No task description provided.')
            return
        task = ' '.join(args)
        self.tasks.append(task)
        print(f'Added task #{len(self.tasks)}: {task}')

    def list(self, *_):
        if not self.tasks:
            print('No tasks.')
            return
        for idx, task in enumerate(self.tasks, 1):
            print(f'{idx}. {task}')

    def done(self, *args):
        if not args:
            print('Error: No task ID provided.')
            return
        try:
            idx = int(args[0]) - 1
            if idx < 0 or idx >= len(self.tasks):
                raise IndexError
        except (ValueError, IndexError):
            print('Error: Invalid task ID.')
            return
        completed = self.tasks.pop(idx)
        print(f'Completed and removed task: {completed}')

    def clear(self, *_):
        self.tasks.clear()
        print('All tasks cleared.')

def main():
    if len(sys.argv) < 2:
        print('Usage: todo.py <command> [args]')
        return
    cmd, *args = sys.argv[1:]
    app = TodoApp()
    # Simple REPL‑style loop: keep state across commands in one run
    while True:
        if cmd == 'add':
            app.add(*args)
        elif cmd == 'list':
            app.list()
        elif cmd == 'done':
            app.done(*args)
        elif cmd == 'clear':
            app.clear()
        else:
            print(f'Unknown command: {cmd}')
        # Prompt for next command without restarting the script
        try:
            line = input('todo> ').strip()
        except EOFError:
            break
        if not line:
            continue
        parts = line.split()
        cmd, args = parts[0], parts[1:]

if __name__ == '__main__':
    main()
