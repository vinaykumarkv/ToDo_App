import functions
import FreeSimpleGUI as sg

from ToDo_App.gui.functions import write_todos, get_todos

label = sg.Text(
    "To Do Task" )
input_box = sg.InputText(tooltip="Enter To DO item",key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=get_todos(),key="todos",
                      enable_events=True, size=(45,10))
edit_button = sg.Button("Edit")
mark_button = sg.Button("Complete")

layout = [[label],
          [input_box, add_button],
          [list_box, edit_button],
          [mark_button]]

window = sg.Window("My To Do App",
                       layout=layout,
                       font=("Helvetica", 12))
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"]
            todos.append(new_todo+"\n")
            write_todos(todos)
            window["todos"].Update(values=todos)
        case "Edit":
            todos = functions.get_todos()
            todo_edit = values["todos"][0]
            edit_todo = f"{values["todo"]}\n"
            todos[todos.index(todo_edit)]=edit_todo
            write_todos(todos)
            window["todos"].Update(values=todos)
        case "todos":
            window["todo"].update(value=values['todos'][0])
        case "Complete":
            todos = functions.get_todos()
            todo_complete = values["todos"][0]
            todos.remove(todo_complete)
            write_todos(todos)
            window["todos"].Update(values=todos)
        case sg.WIN_CLOSED:
            break

window.close()
