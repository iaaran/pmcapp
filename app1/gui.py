import functions
import PySimpleGUI as sg

todos = functions.get_todos()


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter Todo", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=todos, key='listTodo',
                      enable_events="True", size=[45, 10])
edit_button = sg.Button("Edit")
done_button = sg.Button("Done")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout = [[label],
                             [input_box, add_button],
                             [list_box, edit_button, done_button],
                             [exit_button]],
                   font=('Helvetica',20))


def update_todos_window(atodos):
    functions.set_todos(atodos)
    window['listTodo'].update(values=atodos)
    window['todo'].update(value='')


while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
           #  todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            update_todos_window(todos)

        case 'Edit':
            todo_to_edit = values['listTodo'][0]
            new_todo = values['todo'] + '\n'
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            update_todos_window(todos)

        case 'listTodo':
            window['todo'].update(value=values['listTodo'][0])
        case 'Done':
            todo_done = values['listTodo'][0]
            todos.remove(todo_done)
            update_todos_window(todos)

        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()