from view import *
from database import *

notebook = {}
notebook_last_id = 0


def main(db: dict, last_id: int) -> None:
    while True:
        menu_item = menu()
        match menu_item:
            case 1:
                record_note = input_note()
                db, last_id = create(db, last_id, *record_note)
            case 2:
                print_data(db)
            case 3:
                export_db(db, 'notes.json')
            case 4:
                db, last_id = import_db(db, last_id, 'notes.json')
            case 5:
                found_surname(db, last_id, get_value())
            case 6:
                change_id = get_operation_id()
                change_item = get_change_item()
                change_line(db, change_id, change_item, get_new_value())
            case 7:
                delete_item = get_operation_id()
                delete_line(db, delete_item)
            case 8:
                break


main(notebook, notebook_last_id)
