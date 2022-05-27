from weather import Weather
from plant import Plant


class Garden:
    __plant_list: list
    __weather: str

    def __init__(self, weather: str = 'sunny', plant_list: list = []) -> None:
        self.__weather = weather
        self.__plant_list = plant_list

    def show_plants(self) -> None:
        for plant in self.__plant_list:
            print(f'{plant.get_plant_type()}: '
                  f'growing state: {plant.get_growing_state()}; '
                  f'water: {plant.get_water_scale()}/10; '
                  f'fertilizers: {plant.get_fertilizers()}/5; '
                  f'pests&diseases: {plant.get_pests_and_diseases()}\n')

    def include_plant_in_list(self, plant: Plant) -> None:
        self.__plant_list.append(plant)
        print(f'{plant.get_plant_type()} is included in your garden!')

    def get_plant_list(self) -> list:
        return self.__plant_list

    def change_weather(self, weather: Weather) -> None:
        weather.set_weather_status()
        self.__weather = weather.get_weather_status()

    def check_plant_health(self, plant: Plant) -> None:
        if plant.get_fertilizers() == 0 or plant.get_water_scale() == 0:
            print(f'Your {plant.get_plant_type()} is dead!')
            self.delete_plant_from_garden(plant)

    def delete_plant_from_garden(self, plant: Plant) -> None:
        for i in range(len(self.__plant_list)):
            if self.__plant_list[i].get_plant_id() == plant.get_plant_id():
                self.__plant_list.pop(i)
                del plant
                break

    def clear_garden(self):
        self.__plant_list = []

    def pour_on(self) -> None:
        pos: int = int(input('What plant do you want to pour on(input position in list)?')) - 1
        for i in range(len(self.__plant_list)):
            if i == pos:
                plant = self.__plant_list[i]
                plant.pour_on()
                break

    def grow_plants(self, weather: str) -> None:
        for plant in self.__plant_list:
            plant.grow(weather)
            self.check_plant_health(plant)
