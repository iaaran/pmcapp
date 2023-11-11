
todos = []

while True:
    user_action = input("Type add or show, edit, complete or exit :")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter the todo:  ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):  # enumerate function is used to get index value
                row = f"{index + 1}-{item}"   # f string is used for formatted display
                print(row)
        case "edit":
            number = int(input("Number of the todo to edit :"))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Number of the todo to complete:"))
            todos.pop(number - 1)
        case "exit":
            break

print("Bye!")
