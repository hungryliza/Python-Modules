class Plant:
    def __init__(self, name, height, initage):
        self.name = name
        self.height = height
        self.initialheight = height
        self.initage = initage

    def grow(self):
        self.height += 2.1

    def age(self):
        self.initage += 1

    def show(self):
        print(f"{self.name}: {float(round(self.height))}cm, {self.initage} days old")
        
class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self, bloomed):
        if bloomed is True:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def show(self):
        super().show()
        print(f" Color: {self.color}")

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter =  trunk_diameter

    def produce_shade(self):
        print("[asking the oak to produce shade]")
        print(f"Tree {self.name} now produces"
              f" a shade of {self.height}cm long and {self.trunk_diameter}cm wide.")

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")
    
    def grow(self):
        super().grow()
        self.nutritional_value += 1
    
    def age(self):
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
