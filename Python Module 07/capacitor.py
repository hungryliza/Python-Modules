from ex1 import TransformCreatureFactory, HealingCreatureFactory

def healing_creature(factory):
    creature = factory.create_base()
    print(" base:")
    print(f"{creature.describe()}")
    print(f"{creature.attack()}")
    print(f"{creature.heal()}")
    print(" evolved:")
    evolved_creature = factory.create_evolved()
    print(f"{evolved_creature.describe()}")
    print(f"{evolved_creature.attack()}")
    print(f"{evolved_creature.heal()}")

def transform_creature(factory):
    print(" base:")
    creature = factory.create_base()
    print(f"{creature.describe()}")
    print(f"{creature.attack()}")
    print(f"{creature.transform()}")
    print(f"{creature.attack()}")
    print(f"{creature.revert()}")
    print(" evolved:")
    evolved_creature = factory.create_evolved()
    print(f"{evolved_creature.describe()}")
    print(f"{evolved_creature.attack()}")
    print(f"{evolved_creature.transform()}")
    print(f"{evolved_creature.attack()}")
    print(f"{evolved_creature.revert()}")


if __name__ == "__main__":
    print("Testing Creature with healing capability")
    sproutling = HealingCreatureFactory()
    shiftling = TransformCreatureFactory()
    healing_creature(sproutling)
    print("\nTesting Creature with transform capability")
    transform_creature(shiftling)
