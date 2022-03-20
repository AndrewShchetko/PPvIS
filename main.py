from __future__ import annotations
from typing import Union, Any
import time
from random import randint as rand


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
    __fertilizers: int
    __weather: Weather

    def __init__(self, fertilizers: int = 10) -> None:
        self.__fertilizers = fertilizers
        self.__weather = Weather()

    def use_fertilizers(self, plant: Union[TomatoBush, CucumberBush, AppleTree]) -> None:
        plant.set_pest_status(False)
        plant.set_disease_status(False)
        plant.__fertilizer_scale = 5
        plant.update_growing_state()
        self.__fertilizers -= 1

    @staticmethod
    def pour_on(plant: Any) -> None:
        plant.__water_scale = 10


class PestsAndDiseases:
    @staticmethod
    def set_pest_location(location: Union[TomatoBush, CucumberBush, AppleTree]) -> None:
        location.set_pest_status(True)

    @staticmethod
    def set_disease_location(location: Union[TomatoBush, CucumberBush, AppleTree]) -> None:
        location.set_disease_status(True)


class PlantConstants:
    __growing_states: tuple = ('flower', 'fetal formation', 'fetus (grown)')
    __growing_states_counter: int
    __diseases_and_pests: dict = {'pests': False, 'disease': False}


class Plant(PlantConstants):
    __growing_time: int
    __growing_state: str
    __plant_type: str
    __number_of_fetuses: int
    __water_scale: int = 10
    __fertilizer_scale: int = 5

    def __init__(self, plant_type: str, growing_time: int, number_of_fetuses: int) -> None:
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

    def grow(self) -> None:
        self.__water_scale -= 1
        start: float = time.time()
        while True:
            end: float = time.time()
            while start - end != self.__growing_time:
                pass
            self.__growing_states_counter += 1
            self.update_growing_state()
            if self.__growing_state == 'fetus (grown)':
                print(f'Your {self.__plant_type} are grown! You can pick them up!')
                break
            else:
                self.grow()

    def pick_up(self) -> None:
        self.__fertilizer_scale -= 1
        self.__growing_states_counter = 0
        self.update_growing_state()
        if self.__diseases_and_pests['pests']:
            print(f'Your {self.__plant_type} was attacked by pests,'
                  f' so you pick up only {self.__number_of_fetuses * 0.5} {self.__plant_type}!')
        if self.__diseases_and_pests['diseases']:
            print(f'Your {self.__plant_type} is ill,'
                  f' so you pick up only {self.__number_of_fetuses * 0.75} {self.__plant_type}!')
        else:
            print(f'You pick up {self.__number_of_fetuses} {self.__plant_type}!')


class TomatoBush(Plant):
    def __init__(self) -> None:
        super().__init__('tomatoes', 30, 6)
        self.__growing_state = self.__growing_states[0]


class CucumberBush(Plant):
    def __init__(self) -> None:
        super().__init__('cucumbers', 45, 8)
        self.__growing_state = self.__growing_states[0]


class AppleTree(Plant):
    def __init__(self) -> None:
        super().__init__('apple tree', 90, 20)
        self.__growing_state = self.__growing_states[0]


class Pumpkin(Plant):
    def __init__(self) -> None:
        super().__init__('apple tree', 40, 1)
        self.__growing_state = self.__growing_states[0]


def save_progress() -> None:
    with open() as file:
        pass
