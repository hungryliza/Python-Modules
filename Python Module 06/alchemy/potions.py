import elements
from .elements import create_earth, create_air

def healing_potion():
    return f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"

def strength_potion():
    return f"Strength potion brewed with '{elements.create_fire()}' and '{elements.create_water()}'"
