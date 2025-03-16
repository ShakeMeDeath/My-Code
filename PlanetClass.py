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

planet1 = Planet("tataouianana lemed", 1, 13_000)
print(planet1.materials)