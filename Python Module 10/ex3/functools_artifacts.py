from typing import Any, Callable
import functools
import operator


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} damages {target} for {power} HP"

def spell_reducer(spells: list[int], operation: str) -> int:
    op_dict = {"add" : operator.add, 
               "multiply" : operator.mul,
               "max" : lambda a, b: max(a, b), 
               "min" : lambda a, b: min(a, b)}

    if len(spells) == 0:
        return 0
    try:
        return functools.reduce(op_dict[operation], spells)
    except KeyError:
        return "Operation unknown"

def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    dict_el = {}
    fire = functools.partial(base_enchantment, power=50, element="fire")
    water = functools.partial(base_enchantment, power=50, element="water")
    air = functools.partial(base_enchantment, power=50, element="air")
    dict_el['fire'] = fire
    dict_el['water'] = water
    dict_el['air'] = air 
    return dict_el

@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatched(spell_type: Any) -> str:
        return "Unknwon spell type"

    @dispatched.register(int)
    def _(spell_type: int):
        return spell_type

    @dispatched.register(str)
    def _(spell_type: str):
        return spell_type

    @dispatched.register(list)
    def _(spell_type: list):
        return spell_type
    return dispatched


if __name__ == "__main__":
    print("Testing spell reducer...")
    spell_pow = [40, 5, 21, 19, 10, 3, 2]
    print(f"Sum: {spell_reducer(spell_pow, "add")}")
    print(f"Product: {spell_reducer(spell_pow, "multiply")}")
    print(f"Max: {spell_reducer(spell_pow, "max")}")

    print("\nTesting partial enchanter...")
    fire_test = partial_enchanter(base_enchantment)['fire']
    water_test = partial_enchanter(base_enchantment)['water']
    air_test = partial_enchanter(base_enchantment)['air']
    print(fire_test(target="Dragon"))
    print(water_test(target="Dragon"))
    print(air_test(target="Dragon"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    types = 42, "fireball", ["fireball", "heal", "shield"]
    for i in types:
        spell_type = i
        spelled = spell_dispatcher()
        dispatcher_spell = spelled(spell_type)
        if i == 42:
            print(f"Damage spell: {dispatcher_spell}")
        if i == "fireball":
            print(f"Enchantment: {dispatcher_spell}")
        if i == ["fireball", "heal", "shield"]:
            print(f"Multi-cast: {len(dispatcher_spell)} spells")

    spell_type = {"spell1" : "fireball", "spell2" : "heal"}
    spelled = spell_dispatcher()
    dispatcher_spell = spelled(spell_type)
    print(dispatcher_spell)
