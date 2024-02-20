from datetime import datetime


def create(db: dict,
           id_db: int,
           date_now: str,
           title: str,
           note: str) -> tuple:
    db[id_db] = {'id': id_db, 'date': date_now, 'title': title, 'note': note}
    id_db += 1
    return db, id_db


def print_data(db: dict) -> None:
    print('{:<3} {:<20} {:<20} {:<15}'.format('ID', 'Date', 'Title', 'Note'))

    for id_db in sorted_value(db):
        print(
            f'{id_db:<3} {db[id_db]["date"]:<20} {db[id_db]["title"]:<20} {db[id_db]["note"]:<15}')
    print()


def export_db(db: dict,
              filepath: str,
              delimiter: str = ';') -> None:
    with open(filepath, 'w', encoding='UTF-8') as file:
        for id_db, data in db.items():
            file.write(
                f"{data['id']}{delimiter}{data['date']}{delimiter}{data['title']}{delimiter}{data['note']}\n")


def add_db(db: dict,
           filepath: str,
           delimiter: str = ';') -> None:
    with open(filepath, 'a', encoding='UTF-8') as file:
        for id_db, data in db.items():
            file.write(
                f"{data['id']}{delimiter}{data['date']}{delimiter}{data['title']}{delimiter}{data['note']}\n")


def import_db(db: dict,
              id_db: int,
              filepath: str,
              delimiter: str = ';') -> tuple:
    with open(filepath, 'r', encoding='UTF-8') as file:
        for line in file:
            data = line.strip().split(delimiter)
            db[id_db] = {'id': id_db, 'date': data[1], 'title': data[2], 'note': data[3]}
            id_db += 1
    return db, id_db


def found_surname(db: dict,
                  id_db: int,
                  search_item: str) -> int:
    search_item = search_item.lower()
    for id_db in db:
        if search_item in db[id_db]['id'].lower() \
                or search_item in db[id_db]['date'].lower() \
                or search_item in db[id_db]['title'].lower() \
                or search_item in db[id_db]['note'].lower():
            print(f'{db[id_db]}')
    print()


def delete_line(db: dict,
                id_db: int) -> dict:
    return db.pop(id_db)


def change_line(db: dict,
                id_db: int,
                item: int,
                get_item: str) -> dict:
    item = selection_values(item)
    db[id_db][item] = get_item
    db[id_db]['date'] = str(datetime.now()).split('.')[0]
    return db


def selection_values(item: int) -> str:
    if item == 1:
        item = 'title'
    elif item == 2:
        item = 'note'
    else:
        print('Not found')
    return item


def sorted_value(db: dict) -> dict:
    res = dict(sorted(db.items(), key=lambda x: x[1].get('date')))
    return res


