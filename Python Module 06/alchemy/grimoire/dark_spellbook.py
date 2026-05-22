from .dark_validator import validate_ingredients

def dark_spell_allowed_ingredients():
    return ["bats", "frogs", "arsenic", "eyeball"]

def dark_spell_record(spell_name: str, ingredients: str):
    valid = validate_ingredients(ingredients)
    if "VALID" in valid:
        return f"Spell recorded: {spell_name} ({valid})"
    else:
        return f"Spell rejected: {spell_name} ({valid})"
