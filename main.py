from PlanetClass import Planet
from MachineClass import Machine

planet1 = Planet("tatouine", 3, {"titanium": 2, "ruby": 1}, 13_000)

machine_drill = Machine("drill", planet1, 3)

print(planet1.machines[0].machine_type)
print(f'Where: {machine_drill.planet_location.name} level: {machine_drill.level[0]}/{machine_drill.level[1]}')