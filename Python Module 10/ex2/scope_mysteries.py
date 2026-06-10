from collections.abc import Callable


def mage_counter() -> Callable:
    counter = 0
    def call_counter():
        nonlocal counter
        counter +=1
        return counter
    return call_counter

def spell_accumulator(initial_power: int) -> Callable:
    def pow_overtime(add):
        nonlocal initial_power
        res = initial_power + add
        initial_power = res
        return initial_power
    return pow_overtime

def enchantment_factory(enchantment_type: str) -> Callable:
    def enchanted(item_name):
        nonlocal enchantment_type
        res = enchantment_type + ' ' + item_name
        return res
    return enchanted

def memory_vault() -> dict[str, Callable]:
    mem_dict = {}
    def store(key, value):
        mem_dict[key] = value
    def recall(key):
        if key in mem_dict:
            return mem_dict[key]
        else:
            return "Memory not found"
    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    mage_count = mage_counter()
    counter_a = mage_count()
    counter_b = mage_count()
    counter_c = mage_count()
    print(f"Number of calls: counter_a call 1: {counter_a}")
    print(f"Number of calls: counter_b call 2: {counter_b}")
    print(f"Number of calls: counter_c call 3: {counter_c}")

    print("\nTesting spell accumulator...")
    accumul = spell_accumulator(100)
    calc_a = accumul(20)
    print(f"Base: 100, add 20: {calc_a}")
    calc_b = accumul(30)
    print(f"Base: 100, add 30: {calc_b}")

    print("\nTesting enchantment factory...")
    enchants = enchantment_factory("Flaming")
    enchant_a = enchants("Sword")
    print(enchant_a)
    enchants = enchantment_factory("Frozen")
    enchant_b = enchants("Shield")
    print(enchant_b)

    print("Testing memory vault...")
    mem = memory_vault()
    stored = mem['store']
    stored('secret', 42)
    print(f"Store 'secret' = 42")
    recalled = mem['recall']
    recalled_data = recalled('secret')    
    print(f"Recall 'secret': {recalled_data}")
    stored('secret', 42)
    recalled = mem['recall']
    recalled_data = recalled('unknown')
    print(f"Recall 'unknown': {recalled_data}")
