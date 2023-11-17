
while True:
    # Get user input and strip space char from it
    user_action = input("Type add or show, edit, complete or exit :")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter the todo:  ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = [item.strip('\n) for item in todos] # This is list comprehension

            for index, item in enumerate(todos):  # enumerate function is used to get index value
                item = item.strip('\n')   # to remove the new line character
                row = f"{index + 1}-{item}"   # f string is used for formatted display
                print(row)
        case "edit":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            number = int(input("Number of the todo to edit :"))
            number = number - 1
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "complete":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            number = int(input("Number of the todo to complete:"))
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            print(f"Todo '{todo_to_remove}' was completed")

        case "exit":
            break

print("Bye!")
