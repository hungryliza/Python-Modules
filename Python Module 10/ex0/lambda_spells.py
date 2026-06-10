def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact : artifact['power'], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return filter(lambda mages: mages['power'] >= min_power)

def spell_transformer(spells: list[str]) -> list[str]:
    return map(lambda spell: "* " + spell + " * ", spells)

def mage_stats(mages: list[dict]) -> dict:
    dict_mage = {}
    max_mage = max(mages, key=lambda mage_pow: mage_pow['power'])
    dict_mage['max_power'] = max_mage['power']
    min_mage = min(mages, key=lambda mage_pow: mage_pow['power'])
    dict_mage['min_power'] = min_mage['power']
    average = round(sum(map(lambda mage: mage['power'], mages)) / len(mages), 2)
    dict_mage['average'] = average
    return dict_mage

if __name__ == "__main__":
    print("Testing artifact sorter..")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
    ]

    spell_names = ["fireball", "heal", "shield"]

    mages = [
        {'name' : "Alex", 'power' : 65},
        {'name' : "Jordan", 'power' : 72},
        {'name' : "Riley", 'power' : 23},
        {'name' : "Casey", 'power' : 156}
    ]

    artifact_sorter(artifacts)
    first = artifacts[0]
    second = artifacts[1]
    print(f"{first['name']} ({first['power']} power) comes before "
          f"{second['name']} ({second['power']} power)")

    print("\nTesting spell transformer..")
    transformed = spell_transformer(spell_names)
    for spell in transformed:
        print(spell, end="")

    print()
    print("\nTesting mage stats..")
    stats = mage_stats(mages)
    print(f"Max Power : {stats['max_power']}, "
          f"Min Power : {stats['min_power']}, "
          f"Average Power : {stats['average']}")

