import functions
import PySimpleGUI as sg
import time


todos = functions.get_todos()

sg.theme("SystemDefault")

clock = sg.Text(time.strftime("%d %b %Y %H:%M:%S"), key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter Todo", key='todo', size=40)
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=todos, key='listTodo',
                      enable_events="True", size=[40, 10])
edit_button = sg.Button("Edit", size=10)
done_button = sg.Button(image_source="image/done.png", mouseover_colors="lightblue2",
                        tooltip="Done the To-Do", size=10, key='Done')
exit_button = sg.Button("Exit", size=10)

row3 = [[sg.Column([[input_box]]), sg.Column([[add_button]])]]

column1 = [[list_box]]
column2 = [[edit_button],[done_button], [exit_button]]
row4 = [[sg.Column(column1),sg.Column(column2)]]

layout = [ [clock], [label], row3, row4]
window = sg.Window("My To-Do App", layout, font=('Helvetica',20))


def update_todos_window(atodos):
    functions.set_todos(atodos)
    window['listTodo'].update(values=atodos)
    window['todo'].update(value='')


while True:
    event, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime("%d %b %Y %H:%M:%S"))
    match event:
        case 'Add':
           if len((values['todo']).strip()) != 0:
                new_todo = values['todo'] + '\n'
                todos.append(new_todo)
                update_todos_window(todos)

        case 'Edit':
            try:
                todo_to_edit = values['listTodo'][0]
                new_todo = values['todo'] + '\n'
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                update_todos_window(todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 16), title="Error Message")

        case 'listTodo':
            window['todo'].update(value=values['listTodo'][0])
        case 'Done':
            try:
                todo_done = values['listTodo'][0]
                todos.remove(todo_done)
                update_todos_window(todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 16), title="Error Message")
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()