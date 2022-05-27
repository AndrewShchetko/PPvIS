from random import randint as rand


class Weather:
    __weather_list: tuple = ('rainy', 'sunny', 'drought')
    __actual_weather: str

    def __init__(self, status: str = 'sunny'):
        self.__actual_weather = status

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
