from alchemy.potions import healing_potion as heal
from alchemy.potions import strength_potion

if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing heal alias: {heal()}")
