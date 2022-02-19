from __future__ import annotations
from typing import Union
import time
from abc import ABC


class Garden:
    __plants_list: list
    __fertilizers: int

    def __init__(self, fertilizers: int = 10) -> None:
        self.__fertilizers = fertilizers

    def use_fertilizers(self, plant: Union[TomatoBush, CucumberBush]) -> None:
        plant.set_pest_status(False)
        plant.update_growing_state()
        self.__fertilizers -= 1


class Pest:
    __pest_location: Union[TomatoBush, CucumberBush]

    def set_pest_location(self, location: Union[TomatoBush, CucumberBush]) -> None:
        self.__pest_location = location
        location.set_pest_status(True)


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


class Plant(ABC):
    __growing_states: tuple = ('flower', 'fetal formation', 'fetus (grown)')
    __growing_states_counter: int
    __growing_time: int
    __growing_state: str
    __is_pest: bool
    __plant_type: str
    __number_of_fetuses: int
    __water_scale: int = 10
    __fertilizer_scale: int = 5

    def __init__(self, plant_type: str, growing_time: int, number_of_fetuses: int) -> None:
        self.__growing_states_counter = 0
        self.__plant_type = plant_type
        self.__growing_time = growing_time
        self.__number_of_fetuses = number_of_fetuses
        self.__is_pest = False

    def update_growing_state(self) -> None:
        self.__growing_state = self.__growing_states[self.__growing_states_counter]

    def set_pest_status(self, status: bool) -> None:
        self.__is_pest = status

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
        if self.__is_pest == True:
            print(f'Your {self.__plant_type} was attacked by pests,'
                  f' so you pick up only {self.__number_of_fetuses / 2} {self.__plant_type}!')
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

    # def grow(self) -> None:
    #     start: float = time.time()
    #     while True:
    #         end: float = time.time()
    #         while start - end != self.__growing_time:
    #             pass
    #         self.__growing_states_counter += 1
    #         self.update_growing_state()
    #         if self.__growing_state == 'fetus (grown)':
    #             print(f'Your {self.__plant_type} are grown!')
    #             break
    #         else:
    #             self.grow()

    # def pick_up(self) -> None:
    #     self.__growing_states_counter = 0
    #     self.update_growing_state()
    #     if self.__is_pest == True:
    #         print(f'Your {self.__plant_type} was attacked by pests,'
    #               f' so you pick up only {self.__number_of_fetuses / 2} {self.__plant_type}!')
    #     else:
    #         print(f'You pick up {self.__number_of_fetuses} {self.__plant_type}!')
        # storage.tomatoes += 6

    # def set_growing_time(self, growing_time: int) -> None:
    #     self.__growing_time = growing_time
