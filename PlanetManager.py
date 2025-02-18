import random
from DevFunctions import AlertPrint

Current_Planet: str = ''
Planet_List: dict = {'Base': ['1', {}, 30_000]}

def MakePlanet(Name: str, Size: int, Resources: dict[str: int], Distance: int):
    Planet_List[Name] = [Size, Resources, Distance]

def GoTo(Name: str, Speed: int):
    """
    Update will be made later
    """

    global Current_Planet
    if Name in Planet_List:
        Current_Planet = Name
    else:
        AlertPrint(f'Invalid Planet Name ! "{Name}"', 'error')

def GenerateGalaxy(size: int) -> dict:
    """
    Update here later
    """
    for i in range(size):
        MakePlanet(f'Planet{i}', random.randint(1, 3), {'idk': 2}, random.randint(1, 50_000))