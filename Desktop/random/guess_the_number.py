import random

# Функція для гри "Вгадай число"
def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("Спробуйте вгадати число від 1 до 100: "))
            attempts += 1

            if user_guess < secret_number:
                print("Загадане число більше.")
            elif user_guess > secret_number:
                print("Загадане число менше.")
            else:
                print(f"Вітаємо! Ви вгадали число {secret_number} за {attempts} спроб.")
                break

        except ValueError:
            print("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    guess_the_number()
