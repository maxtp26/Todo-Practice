import json
def load_todos(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [
                {"task": "Learn Python", "done": False},
                {"task": "Build project", "done": False}
            ]
def save_todos(todos, filename):
    with open(filename, "w") as file:
        json.dump(todos, file)
def get_todo_index(todos, index_str):
    try:
        index = int(index_str) - 1
        if 0 <= index < len(todos):
            return index
        else:
            return None
    except ValueError:
        return None
def invalid_todo():
    print("Invalid todo number!")
def usage_error(command):
    print(f"Usage: {command} [number]")
def add_todos(todos, task):
    todos.append({"task": task, "done": False})
def list_todos(todos):
    for index, item in enumerate(todos):
        if item["done"]:
            print(f"{index + 1}: [X] {item['task']}")
        else:
            print(f"{index + 1}: [_] {item['task']}")
def mark_done(todos, index_str):
    index = get_todo_index(todos, index_str)
    if index is not None:
        todos[index]["done"] = True
        return True  # success
    return False  # failed
def mark_undone(todos, index_str):
    index = get_todo_index(todos, index_str)
    if index is not None:
        todos[index]["done"] = False
        return True  # success
    return False  # failed
def remove_todo(todos, index_str):
    index = get_todo_index(todos, index_str)
    if index is not None:
        todos.pop(index)
        return True  # success
    return False  # failed
def main():
    todos = load_todos("todos.json")
    while True:
        modified = False
        command = input("Command?: ").split(" ", 1)
        command_input = command[0].lower()
        if len(command) > 1:
            command_argument = command[-1]
        else:
            command_argument = None
        if command_input == "add":
            add_todos(todos, command_argument)
            print("Added item!")
            modified = True
        elif command_input == "done" or command_input == "check":
            if command_argument is None:
                usage_error("done")
            elif mark_done(todos, command_argument):
                print("Marked as done!")
                modified = True
            else:
                invalid_todo()
        elif command_input == "uncheck" or command_input == "undo":
            if command_argument is None:
                usage_error("undo")
            elif mark_undone(todos, command_argument):
                print("Unmarked as done!")
                modified = True
            else:
                invalid_todo()
        elif command_input == "remove":
            if command_argument is None:
                usage_error("remove")
            elif remove_todo(todos, command_argument):
                print("Removed todo!")
                modified = True
            else:
                invalid_todo()
        elif command_input == "list":
            list_todos(todos)
        elif command_input == "quit":
            break
        else:
            print("Invalid input!")
        if modified:
            save_todos(todos, "todos.json")
main()