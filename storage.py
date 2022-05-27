from plant import Plant
from plant import PestsAndDiseases


class NumberException(Exception):
    def __str__(self):
        return 'You can not take this number of fetuses. Try to get less!'


class Storage:
    __fertilizers: int
    __fetuses_dict: dict

    def __init__(self,
                 fertilizers: int,
                 fetuses_dict: dict = {'tomatoes': 0, 'cucumbers': 0, 'apples': 0, 'pumpkins': 0}
                 ):
        self.__fertilizers = fertilizers
        self.__fetuses_dict = fetuses_dict

    def use_fertilizers(self) -> None:
        self.__fertilizers -= 1

    def get_fetuses(self, pl_type: str, fetuses: float) -> None:
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

    def pick_up(self, plant: Plant, damage: PestsAndDiseases) -> None:
        fertilizers: int = plant.get_fertilizers() - 1
        plant.set_fertilizers(fertilizers)
        plant.__growing_states_counter = 0
        plant.update_growing_state()
        diseases_and_pests: dict = plant.get_pests_and_diseases()
        if diseases_and_pests['pests']:
            print(f'Your {plant.get_plant_type()} was attacked by pests,'
                  f' so you pick up only {plant.get_fetuses() * 0.5} {plant.get_plant_type()}!')
            self.get_fetuses(plant.get_plant_type(), plant.get_fetuses() * damage.get_pest_damage())
        elif diseases_and_pests['diseases']:
            print(f'Your {plant.get_plant_type()} is ill,'
                  f' so you pick up only {plant.get_fetuses() * 0.75} {plant.get_plant_type()}!')
            self.get_fetuses(plant.get_plant_type(), plant.get_fetuses() * damage.get_disease_damage())
        elif diseases_and_pests['diseases'] and diseases_and_pests['pests']:
            print(f'Your {plant.get_plant_type()} was attacked by pests&diseases,'
                  f' so you pick up only {plant.get_fetuses() * 0.25} {plant.get_plant_type()}!')
            self.get_fetuses(plant.get_plant_type(), plant.get_fetuses() * damage.get_both_damage())
        else:
            print(f'You pick up {plant.get_fetuses()} {plant.get_plant_type()}!')
            self.get_fetuses(plant.get_plant_type(), plant.get_fetuses())
        plant.reset_states()


def use_fertilizers(storage: Storage, plant: Plant) -> None:
    storage.use_fertilizers()
    plant.set_pest_status(False)
    plant.set_disease_status(False)
    plant.fertilize()
    plant.update_growing_state()
