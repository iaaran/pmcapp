import FreeSimpleGUI as sg
from zip_creator import make_archive, extract_archive


window_title = "File Compressor"

# Tab1
label1 = sg.Text("Select files to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key='files')

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key='folder')

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color='green')

# Tab2
tab2_label1 = sg.Text("Select archive file")
tab2_input1 = sg.Input()
tab2_choose_button1 = sg.FileBrowse("Choose", key='t2_file')

tab2_label2 = sg.Text("Select destination folder")
tab2_input2 = sg.Input()
tab2_choose_button2 = sg.FolderBrowse("Choose", key='t2_folder')

tab2_extract_button = sg.Button("Extract")
tab2_output_label = sg.Text(key="t2_output", text_color='green')

tab_layout1 = [[label1, input1, choose_button1],
                    [label2, input2, choose_button2],
                     [compress_button, output_label]]
tab_layout2 = [[tab2_label1, tab2_input1, tab2_choose_button1],
               [tab2_label2, tab2_input2, tab2_choose_button2],
               [tab2_extract_button, tab2_output_label]]
layout = [[sg.TabGroup([[sg.Tab('Archive', tab_layout1), sg.Tab('Extract', tab_layout2)]])]]

window = sg.Window(window_title,layout)

while True:
    event, values = window.Read()
    print(event)
    print(values['files'])
    print(values['folder'])
    match event:
        case "Compress":
            filepath = values['files'].split(";")
            folder = values['folder']
            make_archive(filepath, folder)
            window['output'].update(value="Compression Successful")
        case "Extract":
            archivepath = values['t2_file']
            dest_dir = values['t2_folder']
            extract_archive(archivepath, dest_dir)
            window['t2_output'].update(value="Extraction completed")
        case sg.WIN_CLOSED:
            break

window.close()