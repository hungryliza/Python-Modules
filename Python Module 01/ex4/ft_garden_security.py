class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)

    def set_height(self, _height: float) -> None:
        if _height < 0:
            print(f"{self.name}: "
                  f"Error, height can't be negative\nHeight update rejected")
        else:
            self._height = _height

    def set_age(self, _age: int) -> None:
        if _age < 0:
            print(f"{self.name}: "
                  f"Error, age can't be negative\nAge update rejected\n")
        else:
            self._age = _age

    def show(self) -> None:
        print(f"Plant created: "
              f"{self.name}: {self._height}cm, {self._age} days old\n")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", float(15), 10)
    rose.show()
    rose.set_height(25)
    rose.set_age(30)
    newheight = rose.get_height()
    newage = rose.get_age()
    print(f"Height updated: {newheight}cm")
    print(f"Age updated: {newage} days\n")
    rose.set_height(-25)
    rose.set_age(-25)
    print(f"Current state: {rose.name}: {newheight}cm, {newage} days old")
