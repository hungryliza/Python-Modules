class Plant:
    def __init__(self, name: str, height: float, initage: int) -> None:
        self.name = name
        self.height = height
        self.initialheight = height
        self.initage = initage

    def grow(self) -> None:
        self.height += 2.1

    def age(self) -> None:
        self.initage += 1

    def show(self) -> None:
        print(f"{self.name}: "
              f"{float(round(self.height))}cm, {self.initage} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self, bloomed: bool) -> None:
        if bloomed is True:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print(f"Tree {self.name} now produces"
              f" a shade of {self.height}cm long "
              f"and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age(self) -> None:
        super().age()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom(False)
    print("[asking the rose to bloom]")
    rose.show()
    rose.bloom(True)
    print("=== Tree")
    oak = Tree("Oak Tree", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
