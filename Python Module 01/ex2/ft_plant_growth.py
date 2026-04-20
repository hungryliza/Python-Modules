class Plant:
    def __init__(self, name: str, height: int, initage: int) -> None:
        self.name = name
        self.height = height
        self.initialheight = height
        self.initage = initage
        self.growth = 0

    def grow(self) -> None:
        self.height += 1
        self.growth += 1

    def age(self) -> None:
        self.initage += 1

    def show(self) -> None:
        print(f"=== Day {i} ===")
        print(f"{self.name}: {self.height}cm, {self.initage} days old")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 30)
    for i in range(1, 8):
        rose.show()
        rose.grow()
        rose.age()
    print(f"Growth this week: {rose.height - rose.initialheight}cm\n")
    print("=== Garden Plant Growth ===")
    sunflower = Plant("Sunflower", 80, 45)
    for i in range(1, 8):
        sunflower.show()
        sunflower.grow()
        sunflower.age()
    print(f"Growth this week: "
          f"{sunflower.height - sunflower.initialheight}cm\n")
    print("=== Garden Plant Growth ===")
    cactus = Plant("Cactus", 15, 120)
    for i in range(1, 8):
        cactus.show()
        cactus.grow()
        cactus.age()
    print(f"Growth this week: {cactus.height - cactus.initialheight}cm")
