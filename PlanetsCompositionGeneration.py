import random
from DevFunctions import AlertPrint

possible_materials = {
    "basalt": 1,
    "iron": 1,
    "coal": 1,
    "copper": 2,
    "aluminium": 2,
    "diamond": 2,
    "platinum": 3,
    "gold": 3,
    "titanium": 3,
    "tungsten": 4,
    "uranium": 4,
    "ruby": 4
}


common_materials = [
    "basalt",
    "iron",  
    "coal" 
]

uncommon_materials = [
    "copper",        
    "aluminium",     
    "diamond"        
]

rare_materials = [
    "platinum",      
    "gold",          
    "titanium"        
]

very_rare_materials = [
    "tungsten",       
    "uranium",      
    "ruby"      
]


def GenMaterialComp(material: str) -> dict:
    if possible_materials[material] not in [1, 2, 3, 4]:
        AlertPrint(f'Rarity not between the set range (1 - 4) ! "{possible_materials[material]}"',"error")

    elif material in possible_materials:
        if possible_materials[material] == 1:
            ouput_rarity = random.randint(0, 5)

        elif possible_materials[material] == 2:
            ouput_rarity = random.randint(6, 9)

        elif possible_materials[material] == 3:
            ouput_rarity = random.randint(10, 12)

        elif possible_materials[material] == 4:
            ouput_rarity = 13

        return {material: ouput_rarity}
    else:
        AlertPrint(f'Not an existing/declared material type ! {material}', "error")

def GenPlanetComp() -> dict:
    output_material_gen: dict = {}
    for item in possible_materials:
        material_chance: int = random.randint(0, 13)

        output_material_gen[item] = mat
        


print(GenMaterialComp("titanium"))
print(GenMaterialComp("ruby"))

print({**GenMaterialComp("titanium"), **GenMaterialComp("ruby")})