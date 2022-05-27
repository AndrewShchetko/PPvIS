from garden import Garden
from storage import Storage
import json


def save_progress(
        garden: Garden,
        storage: Storage
) -> None:
    lst: list = []
    plants: list = garden.get_plant_list()
    garden.clear_garden()
    with open('Saves.json', 'w') as database:
        gard: dict = {'garden': garden.__dict__}
        lst.append(gard)
        storage: dict = {'storage': storage.__dict__}
        lst.append(storage)
        pl_counter: int = 1
        for plant in plants:
            pl_dict: dict = {f'plant': plant.convert_in_dict()}
            lst.append(pl_dict)
            pl_counter += 1
        fields: str = json.dumps(lst, indent=2, separators=(', ', ': '))
        database.write(fields)
        print('Your progress is saved!')


def load_progress():
    try:
        with open('Saves.json', 'r') as database:
            fields_json: str = database.read()
        fields: dict = json.loads(fields_json)
        print('Your progress is loaded!')
        return fields
    except FileNotFoundError:
        print('File not found')
        pass
