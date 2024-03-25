# Четверте завдання

# Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.



# Вимоги до завдання:

# Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error.
# Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
# Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler і це винятки: KeyError, ValueError, IndexError.
# Коли відбувається виняток декоратор повинен повертати відповідну відповідь користувачеві. Виконання програми при цьому не припиняється.


# Рекомендації для виконання:

# В якості прикладу додамо декоратор input_error для обробки помилки ValueError

#         def input_error(func):
#             def inner(*args, **kwargs):
#                 try:
#                     return func(*args, **kwargs)
#                 except ValueError:
#                     return "Give me name and phone please."

#             return inner



# Та обгорнемо декоратором функцію add_contact нашого бота, щоб ми почали обробляти помилку ValueError.

#         @input_error
#         def add_contact(args, contacts):
#             name, phone = args
#             contacts[name] = phone
#             return "Contact added."



# Вам треба додати обробники до інших команд (функцій), та додати в декоратор обробку обробку винятків інших типів з відповідними повідомленнями.


# Критерії оцінювання:

#     Наявність декоратора input_error, який обробляє помилки введення користувача для всіх команд.
#     Обробка помилок типу KeyError, ValueError, IndexError у функціях за допомогою декоратора input_error.
#     Кожна функція для обробки команд має власний декоратор input_error, який обробляє відповідні помилки і повертає відповідні повідомлення про помилку.
#     Коректна реакція бота на різні команди та обробка помилок введення без завершення програми.


# Приклад використання:

# При запуску скрипту діалог з ботом повинен бути схожим на цей.

#     Enter a command: add
#     Enter the argument for the command
#     Enter a command: add Bob
#     Enter the argument for the command
#     Enter a command: add Jime 0501234356
#     Contact added.
#     Enter a command: phone
#     Enter the argument for the command
#     Enter a command: all
#     Jime: 0501234356 
#     Enter a command:





# Четвертий крок - Декоратор для обробки помилок вводу
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError:
            return "Enter the argument for the command"
        except IndexError:
            return "Error: Missing arguments."
    return wrapper



# Другий крок - Парсер команди. Частина, яка відповідає за розбір введених користувачем рядків, виділення з рядка ключових слів та модифікаторів команд.
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


# Третій крок - Функції обробники команд - набір функцій, які ще називають handler, вони відповідають за безпосереднє виконання команд.
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name, = args
    return contacts[name]


def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts available.")



# Перший крок - Цикл запит-відповідь. Ця частина застосунку відповідає за отримання від користувача даних та повернення користувачеві відповіді від функції - handler-а.
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))
        
        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))
        
        elif command == "all":
            show_all(contacts)

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
