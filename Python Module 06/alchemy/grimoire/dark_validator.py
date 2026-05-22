from .dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str):
    allowed = dark_spell_allowed_ingredients()
    for ingredient in allowed:
        if ingredient in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
