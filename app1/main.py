
todos = []

while True:
    user_action = input("Type add or show or exit :")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter the todo:  ")
            todos.append(todo.capitalize())
        case "show":
            for item in todos:
                print(item)
        case "exit":
            break
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")

