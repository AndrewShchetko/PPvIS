from __future__ import annotations
from typing import Any
from random import randint as rand
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'


class Interface:
    pass


class Weather:
    __weather_list: tuple = ('rainy', 'sunny', 'drought')
    __actual_weather: str

    def set_sunny_weather(self) -> None:
        self.__actual_weather = self.__weather_list[1]

    def set_rainy_weather(self) -> None:
        self.__actual_weather = self.__weather_list[0]

    def set_drought_weather(self) -> None:
        self.__actual_weather = self.__weather_list[2]

    def get_weather_status(self) -> str:
        return self.__actual_weather

    def set_weather_status(self) -> None:
        status: int = rand(0, 101)
        if 0 <= status <= 50:
            self.set_sunny_weather()
        elif 51 <= status <= 85:
            self.set_rainy_weather()
        else:
            self.set_drought_weather()

    def __init__(self):
        self.set_weather_status()


class Garden:
    __plant_list: list = []
    __fertilizers: int
    __weather: str

    def __init__(self, fertilizers: int, weather: str = 'sunny') -> None:
        self.__fertilizers = fertilizers
        self.__weather = weather  # Возможно поменять инициализацию класса Weather и прописать зависимости от погоды

    def show_plants(self) -> None:
        for plant in self.__plant_list:
            print(f'plant: {plant.__plant_type}:'
                  f'growing state: {plant.__growing_state};'
                  f'water: {plant.__water_scale};'
                  f'fertilizers: {plant.__fertilizer_scale};'
                  f'pests&diseases: {plant.__diseases_and_pests}')

    def include_plant_in_list(self, plant: Plant) -> None:
        self.__plant_list.append(plant)
        print(f'{plant} is included in your garden!')

    def get_plant_list(self) -> list:
        return self.__plant_list

    def change_weather(self, weather: Weather) -> None:
        weather.set_weather_status()
        self.__weather = weather.get_weather_status()

    def delete_plant_from_garden(self, plant: Plant) -> None:
        for i in range(len(self.__plant_list)):
            if self.__plant_list[i].get_plant_id() == plant.get_plant_id():
                self.__plant_list.pop(i)
                del plant
                break

    @staticmethod
    def pour_on(plant: Any) -> None:
        plant.__water_scale = 5


class NumberException(Exception):
    def __str__(self):
        return 'You can not take this number of fetuses. Try to get less!'
        

class Storage:
    __fertilizers: int
    __fetuses_dict: dict[str, int] = {
        'tomatoes': 0,
        'cucumbers': 0,
        'apples': 0,
        'pumpkins': 0
    }
    
    def use_fertilizers(self) -> None:
        self.__fertilizers -= 1

    def get_fetuses(self, pl_type: str, fetuses: int) -> None:
        if pl_type == 'tomatoes':
            self.__fetuses_dict['tomatoes'] += fetuses
        elif pl_type == 'cucumbers':
            self.__fetuses_dict['cucumbers'] += fetuses
        elif pl_type == 'apple tree':
            self.__fetuses_dict['apples'] += fetuses
        elif pl_type == 'pumpkin':
            self.__fetuses_dict['pumpkins'] += fetuses

    def give_fetuses(self, fetuses: int, fetus_name: str) -> int:
        lambda_dict: dict = {
            'tomatoes': lambda obj: self.__fetuses_dict['tomatoes'] - fetuses,
            'cucumbers': lambda obj: self.__fetuses_dict['cucumbers'] - fetuses,
            'apples': lambda obj: self.__fetuses_dict['apples'] - fetuses,
            'pumpkins': lambda obj: self.__fetuses_dict['pumpkins'] - fetuses
        }
        try:
            if lambda_dict[fetus_name] < 0:
                raise NumberException
        except NumberException as exception:
            print(exception)
        else:
            self.__fetuses_dict[fetus_name] -= fetuses
            return fetuses

    def pick_up(self, plant: Plant) -> None:
        fertilizers: int = plant.get_fertilizers() - 1
        plant.set_fertilizers(fertilizers)
        plant.__growing_states_counter = 0
        plant.update_growing_state()
        diseases_and_pests: dict = plant.get_pests_and_diseases()
        if diseases_and_pests['pests']:
            print(f'Your {plant.get_plant_type()} was attacked by pests,'
                  f' so you pick up only {plant.get_fetuses() * 0.5} {plant.get_plant_type()}!')
            self.get_fetuses(plant.get_plant_type(), plant.get_fetuses() * 0.5)
        elif diseases_and_pests['diseases']:
            print(f'Your {plant.get_plant_type()} is ill,'
                  f' so you pick up only {plant.get_fetuses() * 0.75} {plant.get_plant_type()}!')
            self.get_fetuses(plant.get_plant_type(), plant.get_fetuses() * 0.75)
        elif diseases_and_pests['diseases'] and diseases_and_pests['pests']:
            print(f'Your {plant.get_plant_type()} was attacked by pests&diseases,'
                  f' so you pick up only {plant.get_fetuses() * 0.25} {plant.get_plant_type()}!')
            self.get_fetuses(plant.get_plant_type(), plant.get_fetuses() * 0.25)
        else:
            print(f'You pick up {plant.get_fetuses()} {plant.get_plant_type()}!')
            self.get_fetuses(plant.get_plant_type(), plant.get_fetuses())


def use_fertilizers(storage: Storage, plant: Plant) -> None:
    storage.use_fertilizers()
    plant.set_pest_status(False)
    plant.set_disease_status(False)
    plant.__fertilizer_scale = 5
    plant.update_growing_state()


def set_pest_location(location: Plant) -> None:
    location.set_pest_status(True)


def set_disease_location(location: Plant) -> None:
    location.set_disease_status(True)


class PlantConstants:
    __growing_states: tuple = ('flower', 'fetal formation', 'fetus (grown)')
    __growing_states_counter: int = 0
    __steps_counter: int = 0
    __diseases_and_pests: dict = {'pests': False, 'disease': False}


class Plant(PlantConstants):
    __plant_id: str
    __growing_state: str
    __growing_time: int
    __plant_type: str
    __number_of_fetuses: int
    __water_scale: int = 10
    __fertilizer_scale: int = 5

    def __set_plant_id(self) -> None:
        generated_id: str = ''
        for i in range(8):
            generated_id += alphabet[rand(0, 62)]
        self.__plant_id = generated_id

    def get_plant_id(self) -> str:
        return self.__plant_id

    def get_plant_type(self) -> str:
        return self.__plant_type

    def get_fertilizers(self) -> int:
        return self.__fertilizer_scale

    def set_fertilizers(self, fertilizers: int) -> None:
        self.__fertilizer_scale = fertilizers

    def get_pests_and_diseases(self) -> dict:
        return self.__diseases_and_pests

    def get_fetuses(self) -> int:
        return self.__number_of_fetuses

    def __init__(self, plant_type: str, growing_time: int, number_of_fetuses: int) -> None:
        self.__set_plant_id()
        self.__growing_states_counter = 0
        self.__plant_type = plant_type
        self.__growing_time = growing_time
        self.__number_of_fetuses = number_of_fetuses

    def update_growing_state(self) -> None:
        self.__growing_state = self.__growing_states[self.__growing_states_counter]

    def set_pest_status(self, status: bool) -> None:
        self.__diseases_and_pests['pests'] = status

    def set_disease_status(self, status: bool) -> None:
        self.__diseases_and_pests['disease'] = status

    def grow(self, weather: str) -> None:
        self.__steps_counter += 1
        if weather == 'drought':
            self.__water_scale -= 2
        else:
            self.__water_scale -= 1
        if self.__steps_counter == self.__growing_time:
            self.__growing_states_counter += 1
            self.update_growing_state()
            if self.__growing_state == 'fetus (grown)':
                print(f'Your {self.__plant_type} are grown! You can pick them up!')

    def check_plant_health(self, garden: Garden) -> None:
        if self.__fertilizer_scale == 0 or self.__water_scale == 0:
            print(f'Your {self.__plant_type} is dead!')
            garden.delete_plant_from_garden(self)


class TomatoBush(Plant):
    def __init__(self) -> None:
        super().__init__('tomatoes', 3, 4)
        self.__growing_state = self.__growing_states[0]


class CucumberBush(Plant):
    def __init__(self) -> None:
        super().__init__('cucumbers', 4, 8)
        self.__growing_state = self.__growing_states[0]


class AppleTree(Plant):
    def __init__(self) -> None:
        super().__init__('apple tree', 6, 20)
        self.__growing_state = self.__growing_states[0]


class Pumpkin(Plant):
    def __init__(self) -> None:
        super().__init__('pumpkin', 2, 4)
        self.__growing_state = self.__growing_states[0]


def save_progress(
        garden: Garden,
        storage: Storage,
        plants: list
) -> None:
    with open('Saves.txt', 'w') as file:
        pass


def load_progress():
    pass

