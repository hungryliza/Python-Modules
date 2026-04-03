class Plant:
    def __init__(self, name, height, initage):
        self.name = name
        self.height = height
        self.initialheight = height
        self.initage = initage
        self.stats = Plant.Stats(self.name)

    def grow(self):
        self.height += 8
        self.stats.set_nbr_grow()

    def age(self):
        self.initage += 1
        self.stats.set_nbr_age()

    @staticmethod
    def age_checker(year_age):
        if year_age > 365:
            print(f"Is {year_age} days more than a year? -> True\n")
        else:
            print(f"Is {year_age} days more than a year? -> False")

    @classmethod
    def anon_plants(cls):
        return(cls("Unknown plant", 0.0, 0))

    def show(self):
        print(f"{self.name}: {float(round(self.height))}cm, {self.initage} days old")
        self.stats.set_nbr_show()

    class Stats:
        def __init__(self, name):
            self._nbr_grow = 0
            self._nbr_age = 0
            self._nbr_show = 0
            self.name = name
        
        def get_nbr_grow(self):
            return (self._nbr_grow)

        def set_nbr_grow(self):
            self._nbr_grow += 1

        def get_nbr_age(self):
            return (self._nbr_age)

        def set_nbr_age(self):
            self._nbr_age += 1

        def get_nbr_show(self):
            return (self._nbr_show)

        def set_nbr_show(self):
            self._nbr_show += 1

        def display(self):
            print(f"[statistics for {self.name}]")
            print(f"Stats: {self.get_nbr_grow()} grow, {self.get_nbr_age()} age, {self.get_nbr_show()} show")

        
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

class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seed = 0

    def bloom(self, bloomed):
        super().bloom(bloomed)
        if bloomed is True:
            self.set_bloom()
        else:
            print(f"[make {self.name} grow, age and bloom]")

    def grow(self):
        self.height += 30
        self.stats.set_nbr_grow()

    def age(self):
        self.initage += 20
        self.stats.set_nbr_age()

    def set_bloom(self):
        self.seed = 42

    def get_bloom(self):
        return (self.seed)

    def show(self):
        super().show()
        print(f" Seeds: {self.get_bloom()}")

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.stats = Tree.Treestats(self.name)
        self.trunk_diameter =  trunk_diameter

    def produce_shade(self):
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces"
              f" a shade of {self.height}cm long and {self.trunk_diameter}cm wide.")
        self.stats.set_nbr_shades()

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}")

    class Treestats(Plant.Stats):
        def __init__(self, name):
            super().__init__(name)
            self.nbr_shade = 0

        def get_nbr_shades(self):
            return (self.nbr_shade)

        def set_nbr_shades(self):
            self.nbr_shade += 1

        def display(self):
            print(f"[statistics for {self.name}]")
            print(f"Stats: {self.get_nbr_grow()} grow, {self.get_nbr_age()} age, {self.get_nbr_show()} show")
            print(f"{self.get_nbr_shades()} shade")

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

def display(plant):
    plant.stats.display()

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.age_checker(30)
    Plant.age_checker(400)
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom(False)
    display(rose)
    print(f"[asking the rose to grow and bloom]")
    rose.grow()
    rose.show()
    rose.bloom(True)
    rose.stats.display()
    print("=== Tree")
    oak = Tree("Oak Tree", 200.0, 365, 5.0)
    oak.show()
    display(oak)
    oak.produce_shade()
    display(oak)
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    sunflower.bloom(False)
    sunflower.grow()
    sunflower.age()
    sunflower.bloom(True)
    sunflower.show()
    display(sunflower)
    print("=== Anonymous")
    anon = Plant.anon_plants()
    anon.show()
    display(anon)
