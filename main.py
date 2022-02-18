from __future__ import annotations
import time
from abc import ABC, abstractmethod


class Garden:
    __plants_list: list
    __fertilizers: int

    def __init__(self, fertilizers: int = 10) -> None:
        self.__gardeners_list = []
        self.__fertilizers = fertilizers


class Weather:
    __weather_list: tuple = ('rainy', 'sunny', 'drought')
    __actual_weather: str

    def set_sunny_weather(self) -> None:
        self.__actual_weather = self.__weather_list[1]

    def set_rainy_weather(self) -> None:
        self.__actual_weather = self.__weather_list[0]

    def set_drought_weather(self) -> None:
        self.__actual_weather = self.__weather_list[2]


class Plant(ABC):
    __growing_states: tuple = ('flower', 'fetal formation', 'fetus (grown)')
    __growing_states_counter: int
    # __growing_time: int
    __growing_state: str

    def __init__(self):
        self.__growing_states_counter = 0
        self.update_growing_state()

    # @abstractmethod
    # def get_growing_time(self, growing_time: int) -> int:
    #     pass

    def update_growing_state(self):
        self.__growing_state = self.__growing_states[self.__growing_states_counter]


class TomatoBush(Plant):
    __number_of_tomatoes: int

    def __init__(self, number_of_tomatoes: int = 6) -> None:
        super().__init__()
        self.__number_of_tomatoes = number_of_tomatoes
        self.__growing_state = self.__growing_states[0]

    def grow(self) -> None:
        start: float = time.time()
        end: float = time.time()
        while start - end != 30:
            pass
        self.__growing_states_counter += 1
        self.__growing_state = self.__growing_states[self.__growing_states_counter]
        if self.__growing_state == 'fetus (grown)':
            print('Your tomatoes are grown!')

    def pick_up(self) -> None:
        self.__growing_states_counter = 0
        self.__growing_state = self.__growing_states[self.__growing_states_counter]
        print('You pick up 6 tomatoes!')
        # storage.tomatoes += 6

    # def set_growing_time(self, growing_time: int) -> None:
    #     self.__growing_time = growing_time
