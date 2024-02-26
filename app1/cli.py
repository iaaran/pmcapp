# from functions import get_todos, set_todos

import functions    # local module
import time         # standard python module

now = time.strftime("%d %b %Y %H:%M:%S")
print("It is", now)
while True:
    # Get user input and strip space char from it
    user_action = input("Type add, show, edit, done or exit :")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo + '\n')

        functions.set_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):  # enumerate function is used to get index value
            item = item.strip('\n')   # to remove the new line character
            row = f"{index + 1}-{item}"   # f string is used for formatted display
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            if 0 <= number < len(todos):
                new_todo = input("Enter new todo: ") + "\n"
                todos[number] = new_todo
            else:
                print("The Todo number is not in the list")

            functions.set_todos(todos)

        except ValueError:
            print("Your command in invalid")
            continue

    elif user_action.startswith("done"):
        try:
            number = int(user_action[5:])
            index = number - 1

            todos = functions.get_todos()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.set_todos(todos)

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
