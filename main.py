from Caesar import Caesar
from Vernam import Vernam


def main():
    print("""Что вы хотите сделать:
1. Зашифровать сообщение по Цезарю.
2. Зашифровать сообщение по Вернаму с ключом.
3. Зашифровать сообщение по Вернаму со случайным ключом.
4. Дешифровать сообщение по Цезарю.
5. Дешифровать сообщение по Вернаму.
6. Взломать зашифрованное сообщение по Цезарю.
7. Выйти.""")
    while True:
        act = input("Введите номер действия: ")
        if act == '7':
            break
        elif act == '1':
            message = input("Введите ваше сообщение: ")
            language = input("Введите язык сообщения (eng - e/рус - р): ")
            try:
                step = int(input("Введите шаг (целое число): "))
                print("Результат:", Caesar(message).encrypt(step, language), '\n')
            except ValueError:
                print("Ошибка! Шаг может быть только целым числом; доступные языки: русский (р), english (e).")
        elif act in '25':
            message = input("Введите ваше сообщение: ")
            key = input("Введите ваш ключ: ")
            print("Результат:", Vernam(message).crypt(key), '\n')
        elif act == '3':
            message = input("Введите ваше сообщение: ")
            message, key = Vernam(message).rand_encrypt()
            print("Результат:", "Сообщение:", message, "Ключ:", key, '\n')
        elif act == '4':
            message = input("Введите ваше сообщение: ")
            language = input("Введите язык сообщения (eng - e/рус - р): ")
            step = int(input("Введите шаг (целое число): "))
            print("Результат:", Caesar(message).decrypt(step, language), '\n')
        elif act == '6':
            message = input("Введите ваше сообщение: ")
            language = input("Введите язык сообщения (eng - e/рус - р): ")
            print("Результат:")
            Caesar(message).hack(language)
        else:
            print("Неизвестное действие.")


if __name__ == '__main__':
    main()
