from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"

def fireball(target: str, power: int) -> str:
    return f"Fireball damages {target} for {power} HP"

def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} armor"

def condition_test(_, power):
    return power >= 20

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def spelled(target, power):
        spelled1 = spell1(target, power)
        spelled2 = spell2(target, power)
        return (spelled1, spelled2)
    return spelled

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def multiplied(target, power):
        multi = base_spell(target, power * multiplier)
        return multi
    return multiplied

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target, power):
        if condition(target, power):
            speller = spell(target, power)
            return speller
        else:
            return "Spell fizzled"
    return conditional

def spell_sequence(spells: list[Callable]) -> Callable:
    def all_spells(target, power):
        res_lst = []
        for spell in spells:
            res_lst.append(spell(target, power))
        return res_lst
    return all_spells

if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    combi_drag = combined("Dragon", 54)
    first_spell = combi_drag[0].split("for")
    second_spell = combi_drag[1].split("for")
    print(f"Combined spell result: "
          f"{first_spell[0].strip(" ")}, {second_spell[0]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    multi = mega_fireball("Dragon", 10)
    multi_formatter = multi.split(" ")
    fire = fireball("Dragon", 10)
    fire_formatter = fire.split(" ")
    print(f"Original: {fire_formatter[4]}, Amplified: {multi_formatter[4]}" )

    print("\nTesting conditional caster...")
    print("Should be successful...")
    caster = conditional_caster(condition_test, heal)
    conditional = caster("Dragon", 21)
    print(conditional)

    print("\nTesting conditional caster...")
    print("Should fail...")
    caster = conditional_caster(condition_test, heal)
    conditional = caster("Dragon", 19)
    print(conditional)

    print("\nTesting spell sequence...")
    seq = spell_sequence([fireball, heal, shield])
    lst = seq("Dragon", 32)
    counter = 0
    for el in lst:
        counter +=1
        print(f"{counter}. {el}")
