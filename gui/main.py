import functions
import FreeSimpleGUI as sg

from ToDo_App.gui.functions import write_todos

label = sg.Text(
    "To Do Task" )
input_box = sg.InputText(tooltip="Enter To DO item",key="todo")
add_button = sg.Button("Add")
window = sg.Window("My To Do App",
                   layout=[[label],[input_box,add_button]],
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
        case sg.WIN_CLOSED:
            break

window.close()
