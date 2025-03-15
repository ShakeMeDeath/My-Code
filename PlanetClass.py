from DevFunctions import AlertPrint

class Planet:
    planets_list: dict = {}
    
    def __init__(self, name: str, size: int, materials: dict, distance: int):
        self.name: str = name
        self.size: int = size
        self.materials: dict = materials
        self.distance: int = distance
        self.machines: list = []
        
        __class__.planets_list[self] = name
        
    def delete(self):
        del __class__.planets_list[self]