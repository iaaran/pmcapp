import PySimpleGUI as sg
from converter14 import convert

feet_label = sg.Text("Enter Feet")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter Inches")
inches_input = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(" ", key="output")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [convert_button, output_label]])

while True:
    event, values = window.read()
    feet = float(values['feet'])
    inches = float(values['inches'])

    result = convert(feet, inches)
    window['output'].update(value=f"{result} m", text_color="white")