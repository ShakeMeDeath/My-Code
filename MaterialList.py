import random
from DevFunctions import AlertPrint

Very_Rare_Materials: list = [
    'Gold',
    'Saphire',
    'Uranium'
]

Rare_Materials: list = [
    'Titanium',
    'Platinum',
    'Diamond'
]

Uncommon_Materials: list = [
    'Copper',
    'Iron',
    'Aluminum'
]

Common_Materials: list = [
    'Nickel',
    'Rock'
]

def MakePlanetMaterials(Richness: int, size: int) -> dict:
    ouput_dict: dict = {}
    if size < 1 or size > 3:
        AlertPrint(f'Size must be between 1 and 3 ! but got {size}', 'error')
    else:
        ouput_dict['size'] = size
        
    for i in range(Richness):
        rand_num: int = random.randint(1, 100)
        if rand_num > 0 and rand_num <= 50:
            ouput_dict[random.choice(Common_Materials)] = random.randint(1, 4)
            
        elif rand_num > 50 and rand_num <= 75:
            ouput_dict[random.choice(Uncommon_Materials)] = random.randint(1, 4)

        elif rand_num > 75 and rand_num <= 90:
            ouput_dict[random.choice(Rare_Materials)] = random.randint(1, 4)

        elif rand_num > 90 and rand_num <= 100:
            ouput_dict[random.choice(Very_Rare_Materials)] = random.randint(1, 4)

    return ouput_dict

print(MakePlanetMaterials(3, random.randint(1, 3)))