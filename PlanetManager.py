from DevFunctions import AlertPrint

Current_Planet: str = ''
Planet_List: dict = {'Base': "hem"}

def MakePlanet(Name: str,Size: int, Resources: dict, Distance: int):
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
    for i in range(size):
        MakePlanet()

MakePlanet('Planet1344', 2, {'hem': 1, "titanium": 2}, 34)
print(Planet_List)
GoTo('Planet1344', 3)