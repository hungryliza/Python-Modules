from ex0 import FlameFactory, AquaFactory

def creature_test(factory):
    creature = factory.create_base()
    print(f"{creature.describe()}")
    print(f"{creature.attack()}")
    evolved_creature = factory.create_evolved()
    print(f"{evolved_creature.describe()}")
    print(f"{evolved_creature.attack()}")

def fight(factory1, factory2):
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()
    print(f"{creature1.describe()}")
    print(" vs.")
    print(f"{creature2.describe()}")
    print(" fight!")
    print(f"{creature1.attack()}")
    print(f"{creature2.attack()}")

if __name__ == "__main__":
    print("Testing factory")
    flame = FlameFactory()
    aqua = AquaFactory()
    creature_test(flame)
    print("\nTesting factory")
    creature_test(aqua)
    print("\nTesting battle")
    fight(flame, aqua)
