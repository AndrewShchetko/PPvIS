from interface import save_progress, load_progress, Garden, Storage
from storage import use_fertilizers
from plant import Plant, PestsAndDiseases, TomatoBush, CucumberBush, AppleTree, Pumpkin
from weather import Weather


weather = Weather()
pests_and_diseases = PestsAndDiseases()
while True:
    command: str = input('commands: \nnew garden;'
                         '\nload;\nsave;'
                         '\nstep;\npour;\nfertilize;\nplant;\npick up;\nshow plants.\ncommand: ')

    if command == 'new garden':
        garden = Garden()
        storage = Storage(fertilizers=10)

    elif command == 'load':
        fields: list = load_progress()

        gard: dict = fields[0]['garden']
        garden: Garden = Garden(weather=gard['_Garden__weather'])

        st: dict = fields[1]['storage']
        storage: Storage = Storage(fertilizers=st['_Storage__fertilizers'],
                                   fetuses_dict=st['_Storage__fetuses_dict'])

        for i in range(2, len(fields)):
            pl_dict: dict = fields[i]['plant']
            if pl_dict['type'] == 'tomato':
                plant = TomatoBush(pl_dict)
                garden.include_plant_in_list(plant)
            if pl_dict['type'] == 'cucumber':
                plant = CucumberBush(pl_dict)
                garden.include_plant_in_list(plant)
            if pl_dict['type'] == 'apple tree':
                plant = AppleTree(pl_dict)
                garden.include_plant_in_list(plant)
            if pl_dict['type'] == 'pumpkin':
                plant = Pumpkin(pl_dict)
                garden.include_plant_in_list(plant)

    elif command == 'save':
        save_progress(garden=garden, storage=storage)
        break

    elif command == 'step':
        garden.grow_plants(weather.get_weather_status())
        garden.change_weather(weather)
        garden.show_plants()

    elif command == 'pour':
        garden.pour_on()

    elif command == 'fertilize':
        pos = int(input('What plant do you want to fertilize(input position in list)?')) - 1
        for i in range(len(garden.get_plant_list())):
            if i == pos:
                use_fertilizers(storage, garden.get_plant_list()[i])

    elif command == 'plant':
        pl_type: str = input('What plant do you want to plant: tomato, cucumber, apple tree, pumpkin?')
        if pl_type == 'tomato':
            plant = TomatoBush()
            garden.include_plant_in_list(plant)
        elif pl_type == 'cucumber':
            plant = CucumberBush()
            garden.include_plant_in_list(plant)
        elif pl_type == 'apple tree':
            plant = AppleTree()
            garden.include_plant_in_list(plant)
        elif pl_type == 'pumpkin':
            plant = Pumpkin()
            garden.include_plant_in_list(plant)

    elif command == 'pick up':
        pos = int(input('What plant do you want to pick up fetuses from(input position in list)?')) - 1
        for i in range(len(garden.get_plant_list())):
            if i == pos:
                storage.pick_up(garden.get_plant_list()[i], pests_and_diseases)

    elif command == 'show plants':
        garden.show_plants()

    print(f'weather: {weather.get_weather_status()}')
