from DevFunctions import Alert_Print

Current_Planet: str = ''
Planet_List: dict = {'Base': "hem"}

def MakePlanet(Name: str,Size: int, Resources: dict, Distance: int):
    Planet_List[Name] = [Size, Resources, Distance]

def GoTo(Name: str, Speed: int):
    try:
        Current_Planet[Planet_List[Name]] = 
    except KeyError:
        Alert_Print('Invalid Planet Name !', 'error')   

MakePlanet('Planet1344', 2, {'hem': 1, "titanium": 2}, 34)
print(Planet_List)
GoTo('Planet1344', 3)
print(Current_Planet)