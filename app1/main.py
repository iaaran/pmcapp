def get_todos(filepath="todos.txt"):
    """ Read the text file and return
       the list of to-do items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def set_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


text = """
   To Do List
   ==========
A simple command based ToDo app developed using Python.

Instructions to use app
1. To add item to list then type
'add <enter to do item here>'
2. To show the list of to do items
then type 'Show'
3. To edit any existing item
'edit <enter item number>'
4. To remove item from the list
'done <enter item number>'
5. Type 'exit' to close the app

"""
print(text)

while True:
    # Get user input and strip space char from it
    user_action = input("Type add, show, edit, done or exit :")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')
        print(todos)

        set_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):  # enumerate function is used to get index value
            item = item.strip('\n')   # to remove the new line character
            row = f"{index + 1}-{item}"   # f string is used for formatted display
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            if 0 < number < len(todos):
                new_todo = input("Enter new todo: ") + "\n"
                todos[number] = new_todo
            else:
                print("The Todo number is not in the list")

            set_todos(todos)

        except ValueError:
            print("Your command in invalid")
            continue

    elif user_action.startswith("done"):
        try:
            number = int(user_action[5:])
            index = number - 1

            todos = get_todos()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            set_todos(todos)

            print(f"Todo '{todo_to_remove}' was done")
        except IndexError:
            print("The Todo number is not in the list")
            continue
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is invalid")

print("Bye!")
