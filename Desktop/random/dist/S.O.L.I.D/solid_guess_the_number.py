import random
import PySimpleGUI as sg

class Game:
    def __init__(self):
        self.secret_number = self.generate_secret_number()
        self.attempts = 0

    @staticmethod
    def generate_secret_number():
        return random.randint(1, 100)

    def check_guess(self, user_guess):
        if user_guess < self.secret_number:
            return "Загадане число більше."
        elif user_guess > self.secret_number:
            return "Загадане число менше."
        else:
            return f"Вітаємо! Ви вгадали число {self.secret_number} за {self.attempts} спроб."

def main():
    sg.theme("LightGreen")

    game = Game()

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
            game.attempts += 1

            window["output"].update(game.check_guess(user_guess))
        except ValueError:
            window["output"].update("Будь ласка, введіть ціле число.")

    window.close()

if __name__ == "__main__":
    main()
