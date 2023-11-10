import random
import PySimpleGUI as sg

# Генерація випадкового числа
secret_number = random.randint(1, 100)
attempts = 0

# Визначення кольорової палітри
sg.theme("LightGreen")

layout = [
    [sg.Text("Спробуйте вгадати число від 1 до 100:")],
    [sg.InputText(key="user_input")],
    [sg.Button("Вгадати")],
    [sg.Text("", size=(30, 1), key="output")],
]

window = sg.Window("Гра 'Вгадай число'", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    try:
        user_guess = int(values["user_input"])
        attempts += 1

        if user_guess < secret_number:
            window["output"].update("Загадане число більше.")
        elif user_guess > secret_number:
            window["output"].update("Загадане число менше.")
        else:
            window["output"].update(f"Вітаємо! Ви вгадали число {secret_number} за {attempts} спроб.")
            break
    except ValueError:
        window["output"].update("Будь ласка, введіть ціле число.")

window.close()
