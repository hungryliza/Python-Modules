class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", float(25), 30)
    rose.show()
    oak = Plant("Oak", float(200), 365)
    oak.show()
    cactus = Plant("Cactus", float(5), 90)
    cactus.show()
    sunflower = Plant("Sunflower", float(80), 45)
    sunflower.show()
    fern = Plant("Fern", float(15), 120)
    fern.show()
