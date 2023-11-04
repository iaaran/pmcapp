user_prompt = "Enter a todo:"
<<<<<<< HEAD

todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo.capitalize())
    print(todo.upper())
    print(todo.lower())
    print(todos)

# print("type of todo", type(todo))
# print("type of prompt", type(user_prompt))
# print("type of todos", type(todos))
=======
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3]
print(todos)
print("type of todo1", type(todo1))
print("type of prompt", type(user_prompt))
print("type of todos", type(todos))
>>>>>>> 6aa442f703a7423afa85cc53646ec1c2fc7a8c01
