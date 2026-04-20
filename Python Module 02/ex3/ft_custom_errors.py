class GardenError(Exception):
    def __init__(self, message="Unknown plant error"):
        self.message = message

    def __str__(self):
        return self.message

class PlantError(GardenError):
    def __init__(self, message="The tomato plant is wilting!"):
        self.message = message

    def __str__(self):
        return self.message

class WaterError(GardenError):
    def __init__(self, message="Not enough water in the tank!"):
        self.message = message

    def __str__(self):
        return self.message

def garden_checker():
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError()
    except (GardenError) as err:
        print(f"Caught GardenError: {err}")
    try:
        raise WaterError()
    except (GardenError) as err:
        print(f"Caught GardenError: {err}")

def plant_checker():
    print("Testing PlantError...")
    try:
        raise PlantError()
    except PlantError as err:
        print(f"Caught PlantError: {err}")

def water_checker():
    print("\nTesting WaterError...")
    try:
        raise WaterError()
    except WaterError as err:
        print(f"Caught WaterError: {err}")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    plant_checker()
    water_checker()
    garden_checker()
    print("\nAll custom error types work correctly!")
