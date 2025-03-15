from DevFunctions import AlertPrint
from PlanetClass import Planet

class Machine:

    def __init__(self, machine_type: str, planet_location: object, max_lvl: int):
        self.machine_type: str = machine_type
        self.level: list = [0, max_lvl]
        self.planet_location: object = planet_location

        planet_location.machines.append(self)
        

    def MachineUpgrade(self):
        if self.level[0] < self.level[1]:
            self.level[0] += 1
        
        else:
            AlertPrint("Max level already reached !", "error")