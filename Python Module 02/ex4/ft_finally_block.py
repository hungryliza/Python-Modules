class GardenError(Exception):
    def __init__(self, message="Unknown plant error"):
        self.message = message

    def __str__(self):
        return self.message

class PlantError(GardenError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name} : [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

def test_watering_system():
    try:
        print(f"\nTesting valid plants...")
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
        print("Closing watering system\n")
    except PlantError as err:
        print(f"Caught PlantError: {err}")
    try:
        print(f"Testing invalid plants...")
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as err:
        print(f"Caught PlantError: {err}")
    finally:
        print(".. ending tests and returning to main")
        print("Closing watering system")
        print("\nCleanup always happens, even with errors!")

if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()