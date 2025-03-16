import random
from DevFunctions import AlertPrint

possible_materials = {
    "basalt": 1,
    "iron": 1,
    "coal": 1,
    "copper": 2,
    "aluminium": 2,
    "diamond": 2,
    "platinum": 2,
    "gold": 2,
    "titanium": 3,
    "tungsten": 3,
    "uranium": 3,
    "ruby": 3
}

common_materials: list = [x for x in list(possible_materials.keys()) if possible_materials[x] == 1]
uncommon_materials: list = [x for x in list(possible_materials.keys()) if possible_materials[x] == 2]
rare_materials: list = [x for x in list(possible_materials.keys()) if possible_materials[x] == 3]


def CreateMaterialComp(size: int) -> dict:
    output_material_type: str = ''
    output_material_quantity: list = [0, 0]

    material_rarity: int = random.randint(1, 100)
    if size == 1:
        if material_rarity >= 1 and material_rarity <= 80:
            output_material_type = common_materials[random.randint(0, len(common_materials)-1)]

        elif material_rarity >= 81 and material_rarity <= 98:
            output_material_type = uncommon_materials[random.randint(0, len(uncommon_materials)-1)]

        elif material_rarity >= 99 and material_rarity <= 100:
            output_material_type = rare_materials[random.randint(0, len(rare_materials)-1)]

    elif size == 2:
        if material_rarity >= 1 and material_rarity <= 70:
            output_material_type = common_materials[random.randint(0, len(common_materials)-1)]

        elif material_rarity >= 71 and material_rarity <= 94:
            output_material_type = uncommon_materials[random.randint(0, len(uncommon_materials)-1)]

        elif material_rarity >= 95 and material_rarity <= 100:
            output_material_type = rare_materials[random.randint(0, len(rare_materials)-1)]

    elif size == 3:
        if material_rarity >= 1 and material_rarity <= 66:
            output_material_type = common_materials[random.randint(0, len(common_materials)-1)]

        elif material_rarity >= 67 and material_rarity <= 91:
            output_material_type = uncommon_materials[random.randint(0, len(uncommon_materials)-1)]

        elif material_rarity >= 92 and material_rarity <= 100:
            output_material_type = rare_materials[random.randint(0, len(rare_materials)-1)]

    if size == 1:
        output_material_quantity[0] = random.randint(1, 5)
        output_material_quantity[1] = output_material_quantity[0]

    elif size == 2:
        output_material_quantity[0] = random.randint(5, 10)
        output_material_quantity[1] = output_material_quantity[0]

    elif size == 3:
        output_material_quantity[0] = random.randint(10, 15)
        output_material_quantity[1] = output_material_quantity[0]

    return {output_material_type: output_material_quantity}

def CreatePlanetComp(size: int) -> dict:
    output_planet_comp: dict = {}

    if size == 1:
        for i in  range(2):
            add_material = CreateMaterialComp(size)
            while list(add_material.keys())[0] in list(output_planet_comp.keys()):
                add_material = CreateMaterialComp(size)

            output_planet_comp = {**output_planet_comp, **add_material}

    elif size == 2:
        for i in  range(4):
            add_material = CreateMaterialComp(size)
            while list(add_material.keys())[0] in list(output_planet_comp.keys()):
                add_material = CreateMaterialComp(size)
                
            output_planet_comp = {**output_planet_comp, **add_material}

    elif size == 3:
        for i in  range(6):
            add_material = CreateMaterialComp(size)
            while list(add_material.keys())[0] in list(output_planet_comp.keys()):
                add_material = CreateMaterialComp(size)
                
            output_planet_comp = {**output_planet_comp, **add_material}
    return output_planet_comp