from datetime import datetime


_id = 100


def menu() -> int:
    while True:
        print('Выберите действие:\n'
              '1 - Создать заметку\n'
              '2 - Вывести имеющиеся заметки в консоль\n'
              '3 - Записать данные в файл\n'
              '4 - Загрузить данные из файла\n'
              '5 - Найти заметку\n'
              '6 - Изменить заметку\n'
              '7 - Удалить заметку\n'
              '8 - Выход\n')
        user_input = int(input('Введите цифру действия => '))
        print()
        return user_input


def input_note() -> tuple:
    date_now = str(datetime.now()).split('.')[0]
    print('Дата записи: ' + date_now)
    title = input('Введите заголовок: ')
    note = input('Введите текст заметки: ')
    return date_now, title, note,


def get_value():
    value = input('Введите искомое значение: ')
    print()
    return value


def get_operation_id() -> int:
    delete_item = int(input('Введите id (номер) заметки с которой будут проводится операции: '))
    print()
    return delete_item


def get_new_value() -> str:
    new_value = input('Введите новые данные: ')
    return new_value


def get_change_item() -> int:
    list_values()
    change_item = int(input('Введите номер параметра, которое будем менять => '))
    print()
    return change_item


def list_values() -> None:
    print('\nПараметры для изменения:\n'
          '1 - Заголовок\n'
          '2 - Тело заметки\n')


