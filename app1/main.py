
while True:
    # Get user input and strip space char from it
    user_action = input("Type add, show, edit, done or exit :")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')
        print(todos)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):  # enumerate function is used to get index value
            item = item.strip('\n')   # to remove the new line character
            row = f"{index + 1}-{item}"   # f string is used for formatted display
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            if 0 < number < len(todos):
                new_todo = input("Enter new todo: ") + "\n"
                todos[number] = new_todo
            else:
                print("The Todo number is not in the list")

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command in invalid")
            continue

    elif user_action.startswith("done"):
        try:
            number = int(user_action[5:])
            index = number - 1
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

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
