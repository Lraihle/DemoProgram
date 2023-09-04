import PySimpleGUI as sg


def main():
    version = get_version()
    layout = [[sg.Text("I am the IV software, version: " + version )], [sg.Button("RUN")], [sg.Button("EXIT")]]

    window = sg.Window("Demo", layout, margins = (150, 150))

    check_update = True
    while True:

        event, values = window.read()

        if event == "RUN":
            sg.popup("Results are good")

        if event == "EXIT" or event == sg.WIN_CLOSED:
            break

    window.close()


def get_version():
    with open("version.txt", "r") as f:
        for line in f:
            version = line[1:]
    return(version)

main()