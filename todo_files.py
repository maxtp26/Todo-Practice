import json
class TodoList:
    def __init__(self, todo_list=None):
        if todo_list is None:
            self.todo_list = []
        else:
            self.todo_list = todo_list
    def add(self, task, marked_done=False):
        self.todo_list.append({"task": task, "done": marked_done})
    def remove(self, index):
        self.todo_list.pop(index)
    def mark_done(self, index):
        self.todo_list[index]["done"] = True
    def mark_undone(self, index):
        self.todo_list[index]["done"] = False
    def list_all(self):
        for index, item in enumerate(self.todo_list):
            if item["done"]:
                print(f"{index + 1}: [X] {item['task']}")
            else:
                print(f"{index + 1}: [_] {item['task']}")
    def load(self, filename):
        try:
            with open(filename, "r") as file:
                self.todo_list = json.load(file)
        except FileNotFoundError:
            self.todo_list = [
                {"task": "Learn Python", "done": False},
                {"task": "Build project", "done": False}
            ]
    def save(self, filename):
        with open(filename, "w") as file:
            json.dump(self.todo_list, file)
    def __len__(self):
        return len(self.todo_list)

def get_todo_index(todos, index_str):
    try:
        index = int(index_str) - 1
        if 0 <= index < len(todos):
            return index
        else:
            return None
    except ValueError:
        return None
def usage_error(command):
    print(f"Usage: {command} [number]")

def main():
    todos = TodoList()
    todos.load("todos.json")
    while True:
        modified = False
        command = input("Command?: ").split(" ", 1)
        command_input = command[0].lower()
        if len(command) > 1:
            command_argument = command[-1]
        else:
            command_argument = None
        if command_input == "add":
            todos.add(command_argument)
            print("Added item!")
            modified = True
        elif command_input == "done" or command_input == "check":
            index = get_todo_index(todos, command_argument)
            if index is not None:
                todos.mark_done(index)
                print("Marked as done!")
                modified = True
            else:
                usage_error("done")
        elif command_input == "uncheck" or command_input == "undo":
            index = get_todo_index(todos, command_argument)
            if index is not None:
                todos.mark_undone(index)
                print("Unmarked as done!")
                modified = True
            else:
                usage_error("undo")
        elif command_input == "remove":
            index = get_todo_index(todos, command_argument)
            if index is not None:
                todos.remove(index)
                print("Removed todo!")
            else:
                usage_error("remove")
        elif command_input == "list":
            todos.list_all()
        elif command_input == "quit":
            break
        else:
            print("Invalid input!")
        if modified:
            todos.save("todos.json")
main()