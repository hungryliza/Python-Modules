from .light_validator import validate_ingredients

def light_spell_allowed_ingredients():
    return ["earth", "air", "fire", "water"]

def light_spell_record(spell_name: str, ingredients: str):
    valid = validate_ingredients(ingredients)
    if "VALID" in valid:
        return f"Spell recorded: {spell_name} ({valid})"
    else:
        return f"Spell rejected: {spell_name} ({valid})"
