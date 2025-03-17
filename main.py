from PlanetClass import Planet
from MachineClass import Machine

planet1 = Planet("tatouine", 3, 13_000)

machine_drill1 = Machine("drill", planet1, 3)
machine_drill2 = Machine("excavator", planet1, 3)
machine_drill2 = Machine("processor", planet1, 3)

print(planet1.machines)
planet1.DisplayMachines(30)