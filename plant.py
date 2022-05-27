from random import randint as rand
from typing import Optional
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'


class PestsAndDiseases:
    __pest_damage: float = 0.5
    __disease_damage: float = 0.25
    __both_damage: float = 0.75

    def get_pest_damage(self):
        return self.__pest_damage

    def get_disease_damage(self):
        return self.__disease_damage

    def get_both_damage(self):
        return self.__both_damage


class PlantConstants:
    growing_states: tuple = ('flower', 'fetal formation', 'fetus (grown)')


class Plant(PlantConstants):
    __growing_states_counter: int
    __steps_counter: int
    __diseases_and_pests: dict
    __plant_id: str
    __growing_state: str
    __growing_time: int
    __plant_type: str
    __number_of_fetuses: int
    __water_scale: int
    __fertilizer_scale: int

    def __init__(self,
                 plant_type: str,
                 growing_time: int,
                 number_of_fetuses: int,
                 growing_states_counter: int,
                 steps_counter: int,
                 diseases_and_pests: Optional[dict],
                 plant_id: str,
                 growing_state: str,
                 water: int,
                 fertilizer: int) -> None:
        self.__plant_type = plant_type
        self.__growing_states_counter = growing_states_counter
        self.__steps_counter = steps_counter
        if diseases_and_pests is None:
            self.__diseases_and_pests = {'pests': False, 'diseases': False}
        else:
            self.__diseases_and_pests = diseases_and_pests
        self.__plant_id = plant_id
        if plant_id == '':
            self.__set_plant_id()
        self.__growing_state = growing_state
        self.__growing_time = growing_time
        self.__number_of_fetuses = number_of_fetuses
        self.__water_scale = water
        self.__fertilizer_scale = fertilizer

    def __set_plant_id(self):
        for i in range(8):
            self.__plant_id += alphabet[rand(0, 61)]

    def get_plant_type(self) -> str:
        return self.__plant_type

    def get_plant_id(self) -> str:
        return self.__plant_id

    def get_fertilizers(self) -> int:
        return self.__fertilizer_scale

    def set_fertilizers(self, fertilizers: int) -> None:
        self.__fertilizer_scale = fertilizers

    def get_water_scale(self) -> int:
        return self.__water_scale

    def get_growing_state(self) -> str:
        return self.__growing_state

    def get_pests_and_diseases(self) -> dict:
        return self.__diseases_and_pests

    def get_fetuses(self) -> int:
        return self.__number_of_fetuses

    def reset_states(self) -> None:
        self.__growing_states_counter = 0
        self.__growing_state = 'flower'
        self.__steps_counter = 0

    def pour_on(self) -> None:
        self.__water_scale = 10

    def fertilize(self) -> None:
        self.__fertilizer_scale = 5

    def update_growing_state(self) -> None:
        self.__growing_state = PlantConstants.growing_states[self.__growing_states_counter]

    def set_pest_status(self, status: bool) -> None:
        self.__diseases_and_pests['pests'] = status

    def set_disease_status(self, status: bool) -> None:
        self.__diseases_and_pests['disease'] = status

    def grow(self, weather: str) -> None:
        self.__steps_counter += 1

        status: int = rand(0, 101)
        if status >= 95:
            self.set_pest_status(True)
        elif 90 <= status < 95:
            self.set_disease_status(True)

        if weather == 'drought':
            self.__water_scale -= 2
        elif weather == 'rain':
            self.__water_scale += 2
        elif weather == 'sunny':
            self.__water_scale -= 1

        if self.__steps_counter == self.__growing_time:
            self.__growing_states_counter += 1
            self.update_growing_state()
            self.__steps_counter = 0
            if self.__growing_state == 'fetus (grown)':
                print(f'Your {self.__plant_type} are grown! You can pick them up!')

    def convert_in_dict(self) -> dict:
        pl_dict: dict = {
            'type': self.__plant_type,
            'growing_time': self.__growing_time,
            'number_of_fetuses': self.__number_of_fetuses,
            'growing_states_counter': self.__growing_states_counter,
            'steps_counter': self.__steps_counter,
            'diseases_and_pests': self.__diseases_and_pests,
            'plant_id': self.__plant_id,
            'growing_state': self.__growing_state,
            'water': self.__water_scale,
            'fertilizers': self.__fertilizer_scale
        }
        return pl_dict


class TomatoBush(Plant):
    __plant_type: str = 'tomato'
    __growing_time: int = 3
    __number_of_fetuses: int = 4

    def __init__(self, const_dict: Optional[dict] = None):
        if const_dict is not None:
            super().__init__(
                const_dict['type'],
                const_dict['growing_time'],
                const_dict['number_of_fetuses'],
                const_dict['growing_states_counter'],
                const_dict['steps_counter'],
                const_dict['diseases_and_pests'],
                const_dict['plant_id'],
                const_dict['growing_state'],
                const_dict['water'],
                const_dict['fertilizers']
            )
        else:
            super().__init__(self.__plant_type,
                             self.__growing_time,
                             self.__number_of_fetuses,
                             0, 0, None, '', 'flower', 10, 5)


class CucumberBush(Plant):
    __plant_type: str = 'cucumber'
    __growing_time: int = 4
    __number_of_fetuses: int = 8

    def __init__(self, const_dict: Optional[dict] = None):
        if const_dict is not None:
            super().__init__(
                const_dict['type'],
                const_dict['growing_time'],
                const_dict['number_of_fetuses'],
                const_dict['growing_states_counter'],
                const_dict['steps_counter'],
                const_dict['diseases_and_pests'],
                const_dict['plant_id'],
                const_dict['growing_state'],
                const_dict['water'],
                const_dict['fertilizers']
            )
        else:
            super().__init__(self.__plant_type,
                             self.__growing_time,
                             self.__number_of_fetuses,
                             0, 0, None, '', 'flower', 10, 5)


class AppleTree(Plant):
    __plant_type: str = 'apple tree'
    __growing_time: int = 5
    __number_of_fetuses: int = 20

    def __init__(self, const_dict: Optional[dict] = None):
        if const_dict is not None:
            super().__init__(
                const_dict['type'],
                const_dict['growing_time'],
                const_dict['number_of_fetuses'],
                const_dict['growing_states_counter'],
                const_dict['steps_counter'],
                const_dict['diseases_and_pests'],
                const_dict['plant_id'],
                const_dict['growing_state'],
                const_dict['water'],
                const_dict['fertilizers']
            )
        else:
            super().__init__(self.__plant_type,
                             self.__growing_time,
                             self.__number_of_fetuses,
                             0, 0, None, '', 'flower', 10, 5)


class Pumpkin(Plant):
    __plant_type: str = 'pumpkin'
    __growing_time: int = 2
    __number_of_fetuses: int = 4

    def __init__(self, const_dict: Optional[dict] = None):
        if const_dict is not None:
            super().__init__(
                const_dict['type'],
                const_dict['growing_time'],
                const_dict['number_of_fetuses'],
                const_dict['growing_states_counter'],
                const_dict['steps_counter'],
                const_dict['diseases_and_pests'],
                const_dict['plant_id'],
                const_dict['growing_state'],
                const_dict['water'],
                const_dict['fertilizers']
            )
        else:
            super().__init__(self.__plant_type,
                             self.__growing_time,
                             self.__number_of_fetuses,
                             0, 0, None, '', 'flower', 10, 5)
