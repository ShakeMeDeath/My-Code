from PlanetManager import *
from MaterialList import MakePlanetMaterials
from UI_elements import *

while True:
    call_MainMenu()
    user_input = input(" >> ")
    if user_input not in ['1', '2', '3']:
        AlertPrint(f'the input should be 1, 2 or 3 not {user_input} !', 'info')
    else:
        break

print(Planet_List)