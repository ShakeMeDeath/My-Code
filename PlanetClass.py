from DevFunctions import AlertPrint
from PlanetsCompositionGeneration import CreatePlanetComp

class Planet:
    planets_list: dict = {}
    
    def __init__(self, name: str, size: int, distance: int):
        self.name: str = name
        self.size: int = size
        self.materials: dict = CreatePlanetComp(size)
        self.distance: int = distance
        self.machines: list = []
        
        __class__.planets_list[self] = name
        
    def delete(self):
        del __class__.planets_list[self]
        del self

    def DisplayMachines(self, screen_size: int) -> None:
        between_char = "|"

        print(f'{between_char}', flush=True, end="")
        for i, machine in enumerate(self.machines):
            print(f'---', flush=True, end="")
            print(f'{between_char}', flush=True, end="")
        print("")

        print(f'{between_char}', flush=True, end="")
        for i, machine in enumerate(self.machines):
            print(f' {i+1} ', flush=True, end="")
            print(f'{between_char}', flush=True, end="")
        print("")
        
        print(f'{between_char}', flush=True, end="")
        for i, machine in enumerate(self.machines):
            print(f'{machine.machine_type[0:3].capitalize()}', flush=True, end="")
            print(f'{between_char}', flush=True, end="")

        print("")

        print(f'{between_char}', flush=True, end="")
        for i, machine in enumerate(self.machines):
            print(f'---', flush=True, end="")
            print(f'{between_char}', flush=True, end="")
        print("")

